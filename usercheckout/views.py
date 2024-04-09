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
        'stripe_public_key': 'pk_test_51P3YZk05JlxbpV1PqAPAbKSF7JKg4ic9iktWh9y3NdFyb9NmDCcwDtA0utFL1A7lkl0XBKKzT0UZL4Qd7jV2SBQN00nMjtfrfH',
    }

    return render(request, template, context)