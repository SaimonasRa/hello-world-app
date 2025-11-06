# Loyalty engine
VERSION = "2.0-A"
RULE = "1 point per €5; +10 bonus for new customers"

def calc_points(total: float, is_new_customer: bool) -> int:
    """
    A-rule:
      - floor(total / 5)
      - +10 if new customer
    """
    base = int(total // 5)
    bonus = 10 if is_new_customer else 0
    return base + bonus

def format_message(total: float, is_new_customer: bool) -> str:
    pts = calc_points(total, is_new_customer)  # NOTE: renamed function
    return f"[v{VERSION}] {pts} pts — {RULE}"

if __name__ == "__main__":
    print(format_message(100.0, False))