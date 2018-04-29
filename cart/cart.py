from decimal import Decimal
from django.conf import settings
from headphones.models import Headphone


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        headphone_ids = self.cart.keys()
        headphones = Headphone.objects.filter(id__in = headphone_ids)
        for headphone in headphones:
            self.cart[str(headphone.id)]['headphone'] = headphone

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, headphone, quantity=1, update_quantity=False):
        headphone_id = str(headphone.id)
        if headphone_id not in self.cart:
            self.cart[headphone_id] = {'quantity': 0,
                                      'price': str(headphone.price)}
        if update_quantity:
            self.cart[headphone_id]['quantity'] = quantity
        else:
            self.cart[headphone_id]['quantity'] += quantity
        self.save()

    def remove(self, headphone):
        headphone_id = str(headphone.id)
        if headphone_id in self.cart:
            del self.cart[headphone_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
