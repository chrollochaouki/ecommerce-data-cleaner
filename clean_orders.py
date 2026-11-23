import csv

def load(path):
    rows = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def clean(rows):
    cleaned = []
    seen = set()
    for row in rows:
        try:
            price = float(row["price"])
            quantity = int(row["quantity"])
        except ValueError:
            continue
        if price <= 0:
            continue
        if quantity <= 0:
            continue
        if row["customer_email"] == "":
            continue
        signature = (row["product"], row["price"], row["customer_email"])
        if signature in seen:
            continue
        seen.add(signature)
        cleaned.append(row)
    return cleaned

def save(rows, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "product", "price", "quantity", "customer_email"])
        writer.writeheader()
        for item in rows:
            writer.writerow(item)

rows = load("orders_raw.csv")
cleaned = clean(rows)
save(cleaned, "orders_clean.csv")
print(f"Rows read: {len(rows)}")
print(f"Rows kept: {len(cleaned)}")
print(f"Rows rejected: {len(rows) - len(cleaned)}")