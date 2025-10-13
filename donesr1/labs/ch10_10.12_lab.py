# Define custom exception
class StudentInfoError(Exception):

    def __init__(self, message):
        self.message = message  # Initialize the exception message
    def __str__(self):
        return self.message  

def find_ID(name, info):
     if name in info:
        return info[name]
    else:
        raise StudentInfoError("Student name not found")
    
    
def find_name(ID, info):
     for name, student_id in info.items():
        if student_id == ID:
            return name
    raise StudentInfoError("Student ID not found")


if __name__ == "__main__":
    # Dictionary of student names and IDs
    student_info = {
        "Reagan": "rebradshaw835",
        "Ryley": "rbarber894",
        "Peyton": "pstott885",
        "Tyrese": "tmayo945",
        "Caius": "ccharlton329",
    }

    userChoice = (
        input())  # Read search option from user. 0: find_ID(), 1: find_name()

    # FIXME: find_ID() and find_name() may raise an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
      try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as e:
        print(e)