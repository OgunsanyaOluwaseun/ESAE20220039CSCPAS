def remove_number(string):
    numbers = "0123456789"
    for num in numbers:
        string = string.replace(num, "")
    return string


# This is to reverse the string

def reverse_string(str1):
    reversed_str = str1[::-1]
    return reversed_str


myString = "Oluwaseun004"

print(reverse_string(remove_number(myString)))



