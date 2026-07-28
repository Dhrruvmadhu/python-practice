print("Welcome to the age checker program!")

a = int(input("Enter your age: "))

if(a < 0):
    print("Invalid age. Age cannot be negative.")
elif(a == 0):
    print("You are not entering a valid age.")
elif(a < 18):
    print("You are a minor.")
elif(a == 18):
    print("You are exactly 18 years old.")
elif(a > 18 and a < 65):
    print("You are an adult.")
else:
    print("You are a senior citizen.")


print("Thank you for using the age checker program!")
