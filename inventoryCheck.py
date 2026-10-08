#Retail Warehouse Inventory Check
inventory = {
    "women's pants": {"price": 25.00, "quantity": 255},
    "men's pants": {"price": 25.00, "quantity": 190},
    "women's shirt": {"price": 15.50, "quantity": 390},
    "men's shirt": {"price": 15.50, "quantity": 260},
    "baby clothes": {"price": 10.43, "quantity": 120}
}
threshold = 250

def check_low_stock(inventory,threshold):
    for item, details in inventory.items():
        if details["quantity"] < threshold:
            quantityDifference = threshold - details["quantity"]
            print("Low stock for", item, ": $", details["price"], ", Quantity:", details["quantity"], 
                  "is below threshold of", threshold, "by", quantityDifference, "items.")

check_low_stock(inventory, threshold)
