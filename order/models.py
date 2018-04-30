from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from headphones.models import Headphone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    card_number = models.CharField(max_length=16, help_text="Please enter the 16 digit number on the front of your card")
    cardholder_name = models.CharField(max_length=30, help_text="Please enter your name displayed on your card")
    expiry_date = models.CharField(max_length=7, help_text="Please enter the expiry date on your card")
    CVV_code = models.CharField(max_length=3, help_text="Please enter the 3 digit expiry code on the rear of your card.")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    headphone = models.ForeignKey(Headphone, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
