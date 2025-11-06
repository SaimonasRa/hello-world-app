VERSION = "1.0"
RULE = "1 point per €10; +5 bonus for new customers"

def calculate_points(total: float, is_new_customer: bool) -> int:
    """
    Base rule:
      - floor(total / 10)
      - +5 if new customer
    """
    base = int(total // 10)
    bonus = 5 if is_new_customer else 0
    return base + bonus

def format_message(total: float, is_new_customer: bool) -> str:
    pts = calculate_points(total, is_new_customer)
    return f"[v{VERSION}] {pts} pts — {RULE}"

if __name__ == "__main__":
    print(format_message(100.0, False))