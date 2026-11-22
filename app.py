def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return round(price * (1 - discount_percent / 100), 2)

if __name__ == "__main__":
    print(f"Final price: ${calculate_discount(100.0, 20.0)}")

