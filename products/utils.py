from products.models import Address,Order
import json
def fetch_product():
     # fetch all the address
    address=Address.objects.all()

    # based on address fetch the orders
    addr_order=Order.objects.filter(address__in=address)

    # makea  empty dict
    orders_dic={}
    for order in addr_order:
        if order.address_id not in orders_dic:
            orders_dic[order.address_id] = order.item_json

    # print(orders_dic)
    line_items = []

    for order_id, order_detail_json in orders_dic.items():
        order_detail = json.loads(order_detail_json)

        for item_id, item_info in order_detail.items():
            product_name, quantity, amount, image_url = item_info
            unit_amount = int(float(amount) * 100)  # Convert amount to cents

            line_item = {
                'price_data': {
                    'currency': 'PKR',
                    'product_data': {
                        'name': product_name,
                        'description': f'Quantity: {quantity}',
                        'images': [image_url],
                    },
                    'unit_amount': unit_amount,
                },
                'quantity': int(quantity),
            }

            line_items.append(line_item)
    return line_items
    

# print(fetch_product())