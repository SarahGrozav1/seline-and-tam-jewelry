from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def usercheckout(request):
    shpbag = request.session.get('shpbag', {})
    if not shpbag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)