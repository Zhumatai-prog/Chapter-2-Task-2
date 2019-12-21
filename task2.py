def students_apple(s, a):
	return (f"Every students take {a // s} apples. {a % s} in basket.")

students = int(input("Students number: "))
apples = int(input("How many apples: "))
print(students_apple(students, apples))