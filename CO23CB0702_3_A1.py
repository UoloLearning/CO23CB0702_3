# Ask the user to input a number
num = int(input("Enter a number: "))

# Create a nested loop to generate the multiplication table
for i in range(1, 11):
    for j in range(1, num+1):
        print(j, "x", i, "=", i*j)
    print("\n")
