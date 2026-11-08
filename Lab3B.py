#Class:CSE 1321L
#Section:B10
#Term:Fall 2026
#Instructor:Lan Vu
#Name:Dyllan Brooks
#Lab:3B
hrs1 = int(input("Enter credit hours for course 1:"))
grade1 = int(input("Enter quality points for course 1:"))
hrs2 = int(input("Enter credit hours for course 2: "))
grade2 = int(input("Enter quality points for course 2: "))
hrs3 = int(input("Enter credit hours for course 3: "))
grade3 = int(input("Enter quality points for course 3: "))
hrs4 = int(input("Enter credit hours for course 4: "))
grade4 = int(input("Enter quality points for course 4: "))

totalhrs = hrs1 + hrs2 + hrs3 + hrs4
totalquality = hrs1 * grade1 + hrs2 * grade2 + hrs3 * grade3 + hrs4 * grade4
gpa = (totalquality / totalhrs)

print("Course 1 hours: " + str(hrs1))
print("Grade for course 1: " + str(grade1))
print("Course 1 hours: " + str(hrs2))
print("Grade for course 2: " + str(grade2))
print("Course 3 hours: " + str(hrs3))
print("Grade for course 3: " + str(grade3))
print("Course 4 hours: " + str(hrs4))
print("Grade for course 4: " + str(grade4))
print("Total hours: " + str(totalhrs))
print("Total quality points: " + str(totalquality))
print("GPA: " + str(round(gpa, 2)))



