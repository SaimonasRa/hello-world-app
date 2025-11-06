# Loyalty engine
VERSION = "2.0-B"
RULE = "~1 point per €8 (rounded); +5 bonus; cap 50"

def calculate_points(total: float, is_new_customer: bool, campaign: str | None = None) -> int:
    """
    B-rule:
      - round(total / 8)
      - +5 if new customer
      - cap at 50
    """
    base = round(total / 8)
    bonus = 5 if is_new_customer else 0
    points = base + bonus
    return min(points, 50)

def format_message(total: float, is_new_customer: bool) -> str:
    pts = calculate_points(total, is_new_customer, campaign="BLACKFRIDAY")  # NOTE: extra arg
    return f"[v{VERSION}] {pts} pts — {RULE}"

if __name__ == "__main__":
    print(format_message(100.0, False))