# order.py

class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.status = "Pending"

    def get_order_id(self):
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_products(self):
        return self.products

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


# 创建客户
customer1 = Customer(1, "John Doe", "john@example.com")
customer2 = Customer(2, "Jane Smith", "jane@example.com")

# 创建产品
product1 = Product(1, "iPhone", 999)
product2 = Product(2, "MacBook Pro", 1999)

# 创建订单
order1 = Order(1, customer1, [product1])
order2 = Order(2, customer2, [product2])

# 输出订单信息
print("Order ID:", order1.get_order_id())
print("Customer:", order1.get_customer().get_name())
print("Products:")
for product in order1.get_products():
    print("- ", product.get_name())
print("Status:", order1.get_status())

print("Order ID:", order2.get_order_id())
print("Customer:", order2.get_customer().get_name())
print("Products:")
for product in order2.get_products():
    print("- ", product.get_name())
print("Status:", order2.get_status())

# 更新订单状态
order1.set_status("Shipped")
order2.set_status("Delivered")

# 输出更新后的订单状态
print("Updated Status:", order1.get_status())
print("Updated Status:", order2.get_status())
