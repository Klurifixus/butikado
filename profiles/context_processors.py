def loyalty_program_status(request):
    if request.user.is_authenticated:
        profile = request.user.userprofile
        return {
            'is_eligible_for_discount': profile.is_eligible_for_discount,
            'purchases_left_for_discount': 5 - profile.loyalty_purchase_count
        }
    return {}