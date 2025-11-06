VERSION = "2.0-C"
RULE = "Config-driven: 1 per €12; +3 bonus for new customers"

CONFIG = {
    "per_eur": 12,
    "new_customer_bonus": 3,
}

def calculate_points(total: float, is_new_customer: bool -> int:
    """
    C-rule (config driven)
    """
    per_eur = CONFIG.get("per_eur", 10)
    bonus_val = CONFIG.get("new_customer_bonus", 5)
    base = int(total // per_eur)
    bonus = bonus_val if is_new_customer else 0
    return base + bonus

def format_message(total: float, is_new_customer: bool) -> str:
    pts = calculate_points(total, is_new_customer)
    return f"[v{VERSION}] {pts} pts — {RULE}"

if __name__ == "__main__":
    print(format_message(100.0, False))