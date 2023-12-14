def calculate_ticket_price(age):
    if age < 14:
        return 5.50
    elif age > 62:
        return 7.00
    else:
        return 9.00

def generate_ticket_price_message(name, age):
    price = calculate_ticket_price(age)
    if age < 14:
        return f"The price for {name} is ${price:.2f} because he/she is younger than 14"
    elif age > 62:
        return f"The price for {name} is ${price:.2f} because he/she is older than 62"
    else:
        return f"The price for {name} is ${price:.2f} Regular Price"

while True:
    print("The price for Under 14 is $5.50 - over 62 is $7.00 - Regular price $9.00")
    name = input("Enter the name: ")

    while True:
        age_input = input("Enter the age: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Please insert an integer for age.")

    message = generate_ticket_price_message(name, age)
    print(message)

    repeat = input("Do you want to repeat the program? (yes/no): ").lower()
    if repeat != 'yes':
        break
