from django.shortcuts import render, get_object_or_404
from .models import Category, Headphone
from cart.forms import CartAddProductForm


def headphone_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    headphones = Headphone.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        headphones = headphones.filter(category=category)
    return render(request, 'headphones/headphone/list.html', {'category': category,
                                                      'categories': categories,
                                                      'headphones': headphones})


def headphone_detail(request, id, slug):
    headphone = get_object_or_404(Headphone, id=id, slug=slug, available=True)
    cart_headphone_form = CartAddProductForm()
    return render(request,
                  'headphones/headphone/detail.html',
                  {'headphone': headphone,
                  'cart_headphone_form': cart_headphone_form})

