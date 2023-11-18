# Get sales from the user
sales = float(input("Enter sales: $"))

# Check if sales is greater than or equal to 0
while sales >= 0:
    # Calculate bonus based on sales
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15

    # Print the bonus
    print(f"Your bonus is: ${bonus:.2f}")

    # Get the next sales value
    sales = float(input("Enter sales: $"))

# End of program
print("Thank you for using the sales bonus calculator.")