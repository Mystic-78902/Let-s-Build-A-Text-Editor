def simple_interest(p, r, t):
    return (p * r * t) / 100

def compound_interest(p, r, t, n=1):
    amount = p * (1 + r / (100 * n))**(n * t)
    return amount - p

def interest_calculator():
    print(" Interest Calculator")
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time (in years): "))
    
    interest_type = input("Type 's' for Simple Interest or 'c' for Compound Interest: ").lower()

    if interest_type == 's':
        interest = simple_interest(p, r, t)
        amount = p + interest
        print(f"Simple Interest = {interest:.2f}")
        print(f"Total Amount = {amount:.2f}")
    elif interest_type == 'c':
        n = int(input("Enter number of times interest applied per year (e.g. 1, 4, 12): "))
        interest = compound_interest(p, r, t, n)
        amount = p + interest
        print(f"Compound Interest = {interest:.2f}")
        print(f"Total Amount = {amount:.2f}")
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    interest_calculator()
