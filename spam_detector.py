p1 = "Make a lot of money"
p2 = "buy now"
p3 = "click here"
p4 = "subscribe now"

type = input("Enter your message: ")
message = type.lower()


if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This is a spam message")
else:
    print("This is not a spam message")
