#Question 2
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


#question 1


import re

# a
Data = {
    "Name": "OgunsanyaOluwaseun",
    "Course": "Computer Science",
    "Level": "200",
    "Gender": "Male"
}
pattern = r"a"
Matching_value = [key for key in Data.keys() if re.search(pattern, key)]
print(Matching_value)

# b
replaced_dict = {}
for key, value in Data.items():
    replaced_value = re.sub(pattern, "g", value)
    replaced_dict[key] = replaced_value
    print(replaced_dict)




