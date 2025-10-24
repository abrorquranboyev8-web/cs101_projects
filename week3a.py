prices = {"24hour": 3.99,"48hour": 5.99,"weekly": 8.99 }
total = 0.0

while True:
    rental_period = input("Enter rental period: ").lower() 
    
    if rental_period == "done":
        break
    
    if rental_period in prices:
        price = prices[rental_period]  
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    else:
        print("Invalid rental period! Please enter 24hour, 48hour, or weekly.\n")
print("\n=== Rental Summary ===")
print(f"Subtotal: ${total:.2f}")
discount = 0.0
if total >= 25.00:
    discount = 3.50
    print(f"Binge Watcher Discount: -${discount:.2f}")
else:
    print("Binge Watcher Discount: $0.00")
final_total = total - discount

print("=== Streaming Movie Rental System ===")
print("Enter rental period: 24hour, 48hour, or weekly")
print("Type 'done' when finished selecting movies\n")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for your rental!")