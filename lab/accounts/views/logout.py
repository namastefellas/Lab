from django.contrib.auth import authenticate, login, logout
from webapp.models import Basket
from django.shortcuts import render, redirect


def logout_view(request):
    basket = Basket.objects.all()
    logout(request)
    basket.delete()
    return redirect('webapp:index')