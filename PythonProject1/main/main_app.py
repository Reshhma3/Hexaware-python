

from dao.customer_dao import CustomerDAO
from dao.product_dao import ProductDAO
from entity.customer import Customer
from entity.product import Product

from datetime import date
from entity.order import Order
from entity.order_detail import OrderDetail
from dao.order_dao import OrderDAO
from entity.inventory import Inventory
from dao.inventory_dao import InventoryDAO

inventory = Inventory()

def menu():
    while True:
        print("\nTechShop Menu")
        print("1. Register Customer")
        print("2. Add Product")
        print("3. Update Product")
        print("4. View Products")
        print("5. Delete Product")
        print("6. Place Order Simulate")
        print("7. Exit")
        ch = input("Choice: ")

        if ch == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            customer = Customer(0, first, last, email, phone, address)
            CustomerDAO.register_customer(customer)

        elif ch == '2':
            name = input("Product Name: ")
            desc = input("Description: ")
            price = float(input("Price: "))
            product = Product(0, name, desc, price)
            ProductDAO.add_product(product)

        elif ch == '3':
            pid = int(input("Enter Product ID to update: "))
            desc = input("New Description: ")
            price = float(input("New Price: "))
            product = Product(pid, "", desc, price)
            ProductDAO.update_product_info(product)

        elif ch == '4':
            products = ProductDAO.get_all_products()
            print("\nProduct Catalog:")
            for p in products:
                print(f"ID: {p[0]}, Name: {p[1]}, Desc: {p[2]}, Price: ₹{p[3]}")

        elif ch == '5':
            pid = int(input("Enter Product ID to delete: "))
            ProductDAO.delete_product(pid)
            print("Product deleted.")

        elif ch == '6':
            print("\n📦 Simulate Order Placement")
            customer_id = int(input("Enter Customer ID: "))
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Product Price: "))
            total = quantity * price

            order = Order(0, Customer(customer_id, '', '', '', '', ''), date.today())
            order_detail = OrderDetail(0, order, Product(product_id, '', '', price), quantity)
            order.order_details.append(order_detail)

            '''OrderDAO.create_order(customer_id, order._Order__order_date, total)'''
            OrderDAO.create_order(customer_id, order._Order__order_date, total, order.order_details)

            print("Order placed with total amount: ₹", total)

        elif ch == '7':
            break

if __name__ == "__main__":
    menu()



