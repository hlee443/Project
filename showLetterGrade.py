def showLetterGrade(percentage):
    # end="" avoids pointer going to new line.
    if percentage >= 90:
        grade = 'A'
        print("The grade " + str(percentage) + " is ", grade)
    elif percentage >= 80:
        grade = 'B'
        print("The grade " + str(percentage) + " is ", grade)
    elif percentage >= 70:
        grade = 'C'
        print("The grade " + str(percentage) + " is ", grade)
    elif percentage >= 60:
        grade = 'D'
        print("The grade " + str(percentage) + " is ", grade)
    else:
        grade = 'F'
        print("The grade " + str(percentage) + " is ", grade)
    # if-elif-else series goes here inside the function.


while True:
    print("Menue")
    inputGrade = input('Type your grade: ')
    if inputGrade == "break":
        print("Good Bye")
        break
    elif int(inputGrade) < 0 or int(inputGrade) > 100:
        print('Please type your grade between 0 and 100')

    else:
        percentage = int(inputGrade)
        showLetterGrade(percentage)
