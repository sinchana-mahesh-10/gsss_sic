'''
accept a number from the user and find the next possible smallest number which is bigger than given number having all the digits of given number

67598
67895

'''

def next_bigger_number(n):
    digits = list(str(n))
    length = len(digits)

    # Step 1: Find the first digit from the end that is smaller than its next digit
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return "Not possible"

    # Step 2: Find the smallest digit on right side of i which is greater than digits[i]
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Step 3: Swap
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Sort the digits after index i
    digits[i + 1:] = sorted(digits[i + 1:])

    # Convert back to integer
    return int("".join(digits))


# --- Input from user ---
num = int(input("Enter a number: "))
result = next_bigger_number(num)
print("Next bigger number with same digits:", result)
