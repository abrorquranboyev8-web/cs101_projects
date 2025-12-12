def process_donations(pledge_list):
    result = {}

    for item in pledge_list:
        parts = item.split(",")
        name = parts[0]
        cause = parts[1]
        amount = parts[2]
        amount = int(amount)
        if cause not in result:
            result[cause] = []
        result[cause].append((name, amount))
    return result

def print_fund_totals(charity_dict):
    for cause, records in charity_dict.items():
        total = 0
        for donor, amount in records:
            total += amount
        print(f"{cause}: ${total} total")

pledge_list = [
    "Alice,Animals,50",
    "Bob,Environment,100",
    "Charlie,Animals,25",
    "David,Education,200",
    "Eve,Environment,50",
    "Frank,Education,75"
]
data = process_donations(pledge_list)
print_fund_totals(data)





