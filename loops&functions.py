from cisc108 import assert_equal

def process_sale(amount: str) -> float:
    without_dollar = amount[1:]
    return float(without_dollar)

def process_sales(amounts: [str]) -> [float]:
    result = []
    for amount in amounts:
        result.append(process_sale(amount))
    return result

def remove_bad_sales(commands: [str]) -> [str]:
    result = []
    for command in commands:
        if "?" not in command:
            result.append(command)
    return result

def get_first_year(commands: [str]) -> [str]:
    result = []
    taking = True
    for command in commands:
        if command == "Happy new year!":
            taking = False
        elif taking:
            result.append(command)
    return result

def average(amounts: [float]) -> float:
    if not amounts:
        return None
    total = 0
    count = 0
    for amount in amounts:
        total += amount
        count += 1
    return total/count

def average_sales(commands: str) -> float:
    commands = commands.split(",")
    commands = get_first_year(commands)
    commands = remove_bad_sales(commands)
    amounts = process_sales(commands)
    return average(amounts)

assert_equal(average_sales("$2.50,$4.50,$3.50"), 3.50)
assert_equal(average_sales("$2.00"), 2.00)
assert_equal(average_sales("$2.50,error?,$4.50,$3.50"), 3.50)
assert_equal(average_sales("$2.00,$4.00,Happy new year!,$5.00"), 3.00)
assert_equal(average_sales("what?,$2.00,$4.00,Happy new year!,$5.00"), 3.00)
assert_equal(average_sales("what?,error?,Happy new year!,$5.00"), None)
assert_equal(average_sales("Happy new year!,$5.00"), None)