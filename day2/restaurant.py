print('Welcome to our restaurant')
food_type = int(input('1.north 2.south. Your choice please: '))
match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:  # Multiple patterns can be combined with '|'
        print("Weekend")
    case _:
        print("Invalid day number")

