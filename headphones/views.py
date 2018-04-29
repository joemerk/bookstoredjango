from django.shortcuts import render, get_object_or_404
from .models import ModelNo, Headphone
from cart.forms import CartAddProductForm


def headphone_list(request, modelno_slug=None):
    modelno = None
    modelnos = ModelNo.objects.all()
    headphones = Headphone.objects.filter(available=True)
    if modelno_slug:
        modelno = get_object_or_404(ModelNo, slug=modelno_slug)
        headphones = headphones.filter(modelno=modelno)
    return render(request, 'headphones/headphone/list.html', {'modelno': modelno,
                                                      'modelnos': modelnos,
                                                      'headphones': headphones})


def headphone_detail(request, id, slug):
    headphone = get_object_or_404(Headphone, id=id, slug=slug, available=True)
    cart_headphone_form = CartAddProductForm()
    return render(request,
                  'headphones/headphone/detail.html',
                  {'headphone': headphone,
                  'cart_headphone_form': cart_headphone_form})

