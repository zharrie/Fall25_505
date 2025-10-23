# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def find_ID(name, student_dict):
    if name in student_dict:
        return student_dict[name]
    else:
        raise StudentInfoError(f"Student ID not found for {name}")


def find_name(ID, student_dict):
    for name, student_id in student_dict.items():
        if student_id == ID:
            return name
    raise StudentInfoError(f"Student name not found for {ID}")


def main():
    # Example student dictionary
    student_dict = {
        'Reagan': 'rebradshaw835',
        'Ryley': 'rbarber894',
        'Peyton': 'pstott885',
        'Tyrese': 'tmayo945',
        'Caius': 'ccharlton329'
    }

    # Input
    choice = int(input())
    key = input()

    try:
        if choice == 0:
            result = find_ID(key, student_dict)
        elif choice == 1:
            result = find_name(key, student_dict)
        else:
            result = "Invalid choice"
        print(result)
    except StudentInfoError as e:
        print(e)


if __name__ == "__main__":
    main()
