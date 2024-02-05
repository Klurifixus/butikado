from django.contrib import admin

from .models import Category, Product, Size


class SizeInline(admin.TabularInline):
    model = Size
    extra = 1  # Number of empty forms to display


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
        "low_stock_warning",  # This is your custom method
    )

    inlines = [SizeInline]
    ordering = ("sku",)

    def low_stock_warning(self, obj):
        low_stock_sizes = obj.sizes.filter(quantity__lt=5)
        if low_stock_sizes.exists():
            return ", ".join(
                [f"{size.size} ({size.quantity})" for size in low_stock_sizes]
            )
        return "Sufficient Stock"

    low_stock_warning.short_description = "Low Stock Warning"


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
