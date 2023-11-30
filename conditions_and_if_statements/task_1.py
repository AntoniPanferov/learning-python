# A company provides free shipping for orders with a total value of 200.00€ or more.
# For orders below 200.00€, a flat shipping fee of 5.50€ applies. Write an application
# that outputs the invoice amount depending on the order value

min_value_for_free_shipping = 200
shipping_fee = 5.5
order_value = float(input("Enter your order value: "))

order_value += shipping_fee if order_value < min_value_for_free_shipping else 0
print(f"You have to pay {order_value}€.")
