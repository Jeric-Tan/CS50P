def main():
    cost = dollars_to_float(input("How much was the meal? "))
    percentage = percentage_to_float(input("What percentage would you like to tip? "))
    tip = cost * percentage
    print(f"Leave ${tip:.2f}")

def dollars_to_float(cost):
    x = cost.replace('$','')
    return float(x)
def percentage_to_float(tip):
    y = float(tip.replace('%',''))
    return (y/100)

main()