def showLetterGrade(percentage):
    # end="" avoids pointer going to new line.
    if percentage >=90:
        grade='A'
        print("The grade " + str(percentage) + " is ", grade)
    elif percentage >=80:
        grade='B'
        print("The grade " + str(percentage) + " is ", grade)
    elif percentage >=70:
        grade='C'
        print("The grade " + str(percentage) + " is ", grade)
    elif percentage >=60:
        grade='D'
        print("The grade " + str(percentage) + " is ", grade)
    else:
        grade='F'
        print("The grade " + str(percentage) + " is ", grade)
    # if-elif-else series goes here inside the function.

showLetterGrade(95)
showLetterGrade(72)
showLetterGrade(51)
