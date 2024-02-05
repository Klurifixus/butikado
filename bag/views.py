from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)

from products.models import Product

# Create your views here.


def view_bag(request):
    """A view that renders the bag contents page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]["items_by_size"].keys():
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f"Updated size {size.upper()} {product.name} quantity to "
                    f'{bag[item_id]["items_by_size"][size]}',
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request, f"Added size {
                        size.upper()} {product.name} to your bag"
                )
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request, f"Added size {
                    size.upper()} {product.name} to your bag"
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"].setdefault(size, 0)
            bag[item_id]["items_by_size"][size] = quantity
            success_message = (
                f"Updated size {size.upper()} {product.name} "
                f'quantity to {bag[item_id]["items_by_size"][size]}'
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            success_message = (
                f"Removed size {size.upper()} {product.name} from your bag"
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            success_message = f"Updated {
                product.name} quantity to {bag[item_id]}"
        else:
            bag.pop(item_id)
            success_message = f"Removed {product.name} from your bag"

    request.session["bag"] = bag
    request.session.modified = True  # Ensure the session is saved

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        # Handle AJAX request: return JSON response
        return JsonResponse(
            {
                "success": True,
                "message": success_message,
                # Add any additional data needed for frontend updates here
            }
        )
    else:
        # Handle non-AJAX request: set message and redirect
        messages.success(request, success_message)
        return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request, f"Removed size {
                    size.upper()} {product.name} from your bag"
            )
        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
