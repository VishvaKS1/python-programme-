class NegativeAgeException(Exception):
    pass

def create_student_details():
    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
        if age < 0:
            raise NegativeAgeException("Age cannot be negative.")
    except ValueError:
        print("Invalid age. Please enter a valid integer.")
        return None
    except NegativeAgeException as e:
        print(str(e))
        return None

    subjects = {}
    for i in range(6):
        subject = input("Enter subject name: ")
        marks = float(input("Enter marks for {}: ".format(subject)))
        subjects[subject] = marks

    student_details = {
        "Name": name,
        "Age": age,
        "Subjects": subjects
    }
    return student_details

student_dict = create_student_details()
if student_dict:
    print("Student details:")
    print(student_dict)
