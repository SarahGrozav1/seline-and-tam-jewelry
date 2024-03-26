

def bag_contents(request):
    
    bag_items = []
    total = 0
    product_count = 0
    
    contexts = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    
    return contexts