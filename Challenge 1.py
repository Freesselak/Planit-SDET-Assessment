# Get the nth number in the Fibonacci sequence given n

# Get input from the user and set it to an integer
nterms = int(input("How many terms? "))

# Initalise the first two terms
n1 = 0
n2 = 1

count = 0

# Check if input is a positive number
if nterms <= 0:
    print("Please enter a positive number")
# Then generate the Fibonacci sequence
else:
    print("Fibonacci sequence up to ", nterms, ":")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
