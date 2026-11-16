orders = []

def add_expense(item, cost):
    orders.append({"item": item, "cost": cost})
    print(f"Added: {item} - Rs. {cost}")

def total_expense():
    return sum(order["cost"] for order in orders)

if __name__ == "__main__":
    add_expense("Paneer Biryani", 250)
    add_expense("Garlic Naan", 60)
    print(f"Total Delivery Expense: Rs. {total_expense()}")
