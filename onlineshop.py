
# Accept order amount and membership status
amount = float(input("Enter order amount: "))
member = input("Are you a member? (yes/no): ").lower()

# Check whether order amount is valid
if amount < 0 or amount > 100000:
    print("Invalid order amount")

# Apply discount rules
elif amount >= 5000:
    discount = amount * 15 / 100
    print("Eligible for 15% discount")

elif member == "yes" and amount >= 2000:
    discount = amount * 10 / 100
    print("Eligible for 10% discount")

else:
    discount = 0
    print("No discount available")

# Display final amount
if amount >= 0 and amount <= 100000:
    print("Order Amount: ₹", amount)
    print("Discount: ₹", discount)
    print("Final Amount: ₹", amount - discount)
