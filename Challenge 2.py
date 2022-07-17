# Find the character with the highest occurances in a given string

input_str = input("Input a string to get the highest occuring letter:").lower()

print("The original string is: ", input_str)

# Create a dictionary to count the occurance of each character from the given string
all_freq = {}

# Loop through the string and count each occurance
for i in input_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

occurance = max(all_freq, key=all_freq.get)

print("The max of all characters in ", input_str, " is:", str(occurance))
