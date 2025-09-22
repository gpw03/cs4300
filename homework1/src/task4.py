# Taking in a price and discount and returning discounted price
def calculate_discount(price: int, discount: float) -> int:
    cost_precent = 1 - (discount / 100) # Pulling out cost percentage

    cost = price * cost_precent # Multiplying cost precentage by origional price
    rounded_cost = round(cost, 2) # Rounding to 2 deicmals because its money
    return rounded_cost

if __name__ == "__main__":
    discount = calculate_discount(100, 20)
    print(f"$100 with a 20% discount is: {discount}")