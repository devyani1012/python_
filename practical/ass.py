
orders = [
    {
        'id': 101,
        'customer': 'devyani',
        'status': 'DELIVERED',
        'items': [('keyboard', 2, 1499.0),
                  ('mouse', 1, 599.0)]
    },
    {
        'id': 102,
        'customer': 'kasturi',
        'status': 'CANCELLED',
        'items': [('monitor', 1, 10999.0)]
    },
    {
        'id': 103,
        'customer': 'shreya',
        'status': 'DELIVERED',
        'items': [('cable', 5, 199.0)]
    },
    {
        'id': 104,
        'customer': 'shruti',
        'status': 'SHIPPED',
        'items': [('keyboard', 1, 1499.0),
                  ('monitor', 1, 10999.0)]
    },
    {
        'id': 105,
        'customer': 'Ravi',
        'status': 'DELIVERED',
        'items': [('mouse', 3, 599.0)]
    }
]


def analyse(orders):

    revenue = {}
    products = {}
    customer_status = {}

    for order in orders:

        name = order['customer']
        status = order['status']

        if name not in customer_status:
            customer_status[name] = True

        if status != 'DELIVERED':
            customer_status[name] = False

        if status == 'CANCELLED':
            continue

        if name not in revenue:
            revenue[name] = 0

        for item, qty, price in order['items']:

            revenue[name] += qty * price

            if item not in products:
                products[item] = 0

            products[item] += qty

    top_products = sorted(
        products.items(),
        key=lambda x: (-x[1], x[0])
    )[:2]

    fully_delivered = sorted(
        [name for name in customer_status
         if customer_status[name]]
    )

    return {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }


result = analyse(orders)
print(result)
