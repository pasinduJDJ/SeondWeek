students = []

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    students.append({"name": name, "age": age})

def view_students():
    if not students:
        print("No Students")
        return 
    
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}")

def delete_student():
    name = input("Enter Student Name: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            break
    else:
        print("Student Not Found")

def save_file():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['marks']}\n")

def load_file():
    with open("students.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            students.append({"name": name, "marks": int(marks)})


while True:
    print("==== Menu ====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Save File")
    print("5. Load File")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        save_file()
    elif choice == 4:
        load_file()
    elif choice ==6:
        break
    else:
        print("Invalid Choice")
    