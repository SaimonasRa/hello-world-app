# Loyalty engine
VERSION = "2.0-B"
RULE = "~1 point per €8 (rounded); +5 bonus; cap 50"

def calculate_points(total: float, is_new_customer: bool, campaign: str | None = None) -> int:
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