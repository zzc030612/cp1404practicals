def calculate_total_price(num_items):
    total_price = 0

    for _ in range(num_items):
        while True:
            try:
                item_price = float(input("Price of item: "))
                if item_price < 0:
                    raise ValueError("Price cannot be negative")
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid price.")

        total_price += item_price

    return total_price


def main():
    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                raise ValueError("Invalid number of items!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number of items.")

    total_price = calculate_total_price(num_items)

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {num_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()