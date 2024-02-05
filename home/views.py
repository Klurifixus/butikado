from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def terms_of_usage(request):
    return render(request, "home/terms_of_usage.html")


def data_handling_policy(request):
    return render(request, "home/data_handling_policy.html")
