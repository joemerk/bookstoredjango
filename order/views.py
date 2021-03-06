from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
	cart = Cart(request)
	if request.user.is_authenticated():
		user_id = request.user.id
		current_user_object = User.objects.get(id=user_id)
		form = OrderCreateForm(request.POST)
			
		if form.is_valid():
			order = form.save(commit=False)
			order.user = current_user_object
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
                                         headphone=item['headphone'],
                                         price=item['price'],
                                         quantity=item['quantity'])
			cart.clear()
			return render (request, 'order/order/created.html',{'order':order})

		else:
			return render (request, 'order/order/create.html',{'form': form})			
	else:
		return render(request, 'order/order/create-login.html')