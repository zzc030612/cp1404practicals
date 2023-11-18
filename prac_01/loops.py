def determine_grade(score):
    if not (0 <= score <= 100):
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    try:
        score = float(input("Enter score: "))
        print(determine_grade(score))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()