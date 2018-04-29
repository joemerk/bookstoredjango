from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from headphones.models import Headphone
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, headphone_id):
    cart = Cart(request)
    headphone = get_object_or_404(Headphone, id=headphone_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(headphone=headphone,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, headphone_id):
    cart = Cart(request)
    headphone = get_object_or_404(Headphone, id=headphone_id)
    cart.remove(headphone)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
