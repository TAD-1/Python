
print("Please Enter Assignment score:")
assign = int(input())
weighted_assign = assign * 0.1

print("Please Enter Attendance score:")
attend = int(input())
weighted_attend = attend * 0.1

print("Please Enter Short Quiz score:")
short = int(input())
weighted_short = short * 0.15

print("Please Enter Project score:")
project = int(input())
weighted_project = project * 0.15

print("Please Enter Long Quiz score:")
longQuiz = int(input())
weighted_longQuiz = longQuiz * 0.2

print("Please Enter Major Exam score:")
major = int(input())
weighted_major = major * 0.3

total = weighted_assign + weighted_attend + weighted_short + weighted_project + weighted_longQuiz + weighted_major

if (total <= 100 and total >= 90):
    grade = str('Very Good')

elif (total <= 89 and total >= 80):
    grade = str('Good')

elif (total <= 79 and total >= 70):
    grade = str('Fair')

elif (total <= 69 and total >= 60):
    grade = str('Poor')

elif (total >= 0 and total < 60):
    grade = str('Needs Improvement')

print("Total Weighted Score: " + str(total) + "%")

print("Rating: " + grade)

