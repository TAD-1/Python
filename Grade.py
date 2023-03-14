print("Quizzes")

print("Please enter your quiz 1 score:")
a = float(input())

print("Please enter your quiz 2 score:")
b = float(input())

print("Please enter your quiz 3 score:")
c = float(input())

add = a + b + c
quizAvg = add/3
print(quizAvg)

weighted_Quiz = quizAvg * 0.3



print("\nProject")
print("Please enter your project 1 score:")
d = float(input())

print("Please enter your project 2 score:")
e = float(input())

print("Please enter your project 3 score:")
f = float(input())

add2 = d + e + f
projectAvg = add2 / 3
print(projectAvg)

weighted_Project = projectAvg * 0.2


print("\nFinal Exam Grade")
fExam = float(input())
weighted_fExam = fExam * 0.3

print("\nAssignment Grade")
aGrade = float(input())
weighted_aGrade = aGrade * 0.1

print("\nClass Standing")
cStanding = float(input())
weighted_cStanding = cStanding * 0.1

finalGrade = weighted_Quiz + weighted_Project + weighted_fExam + weighted_aGrade + weighted_cStanding

print("Your Final Grade:")
print(finalGrade)
