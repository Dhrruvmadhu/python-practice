print("Check student pass or fail in Exam")


English = int(input("Enter your marks for English: "))
Maths = int(input("Enter your marks for Maths: "))
Science = int(input("Enter your marks for Science: "))
Social_Studies = int(input("Enter your marks for Social Studies: "))
Hindi = int(input("Enter your marks for Hindi: "))
Gujarati = int(input("Enter your marks for Gujarati: "))

total_percentage = (English + Maths + Science + Social_Studies + Hindi + Gujarati) / 6 
print("your Total Percentage: ", total_percentage, "%")

if (total_percentage >= 40 and English >= 33 and Maths >= 33 and Science >= 33 and Social_Studies >= 33 and Hindi >= 33 and Gujarati >= 33):
    print("Congratulations! You passed the exam")
else:
    print("Sorry,You failed the exam! Better luck next time.")




