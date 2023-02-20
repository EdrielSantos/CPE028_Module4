import Student
import Grades

p1 = Student.Student("Edriel SB. Santos", 21)
p1_Grades = Grades.Grades("CPE028", 4, 30)

print(p1)
print("Name: ", p1.name)
print("Age: ", p1.age)

print(p1_Grades)
print("Course Code: ", p1_Grades.Course_Code)
print("Course Units: ", p1_Grades.Course_Units)
print("Course Grade: ", p1_Grades.Course_Grade)