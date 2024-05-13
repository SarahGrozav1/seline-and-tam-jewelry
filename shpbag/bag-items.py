from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    else:
        product = get_object_or_404(Product, pk=item_id)
        for size, quantity in item_data['items_by_size'].items():
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
            })

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
