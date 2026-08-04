print("=======Student Information System =======")
name=input("Enter your name: ")
rollno=int(input("Enter your roll number: "))
age=int(input("Enter your age: "))
department=input("Enter your department: ")
python_marks=float(input("Enter your python marks: "))
java_marks=float(input("Enter your java marks: "))
ai_marks=float(input("Enter your AI marks: "))


# processing
total_marks=python_marks+java_marks+ai_marks
print(f"Total marks: {total_marks}")
print(f"Average marks: {total_marks/3}")
print(f"Student name is {name}, roll number is {rollno}, age is {age}, department is {department}, python marks is {python_marks}, java marks is {java_marks}, AI marks is {ai_marks}") 
print("=======End of Student Information System =======")
