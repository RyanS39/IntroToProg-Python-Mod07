# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Ryan Seng, 5/25/2024, Assignment07
# ------------------------------------------------------------------------------------------ #

# Importing JSON library to get json functions
import json

# This is the MENU users will be selecting from
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

# This is the other constant, the file to load data from
FILE_NAME: str = "Enrollments.json"

# These are the variables
menu_choice: str = ""
students: list = []

# This class focuses on reading in data from files and writing data to files
class FileProcessor:
    """
    This function reads data in from the file in file_name and puts it into a list.

    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
        Ryan Seng, 5/25/2024, Updated Script for Assignment07 version update
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'r') as file:

                loaded_student_data = json.load(file)
                for student in loaded_student_data:
                    loaded_student = Student(first_name = student["First_Name"], last_name = student["Last_Name"], course = student["Course"])
                    student_data.append(loaded_student)
                
                print("File loaded")
        except FileNotFoundError as e:
            IO.output_error_messages("The text/json file could not be found when running this script", e)
        except ValueError as e:
            IO.output_error_messages("There are corruption issues in the file", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    """
    This function takes a file name and a list of student data and writes the student data into a file named in file_name

    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
        Ryan Seng, 5/25/2024, Updated Script for Assignment07 version update
    """
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            list_of_students: list = []
            for student in student_data:
                student_json: dict = {"First_Name": student.first_name, "Last_Name": student.last_name, "Course": student.course}
                list_of_students.append(student_json)
    
            file = open(file_name, "w")
            json.dump(list_of_students, file)
            print(f"The student list was saved in {FILE_NAME}")
            file.close()
        except TypeError as e:
            IO.output_error_messages("The data may not be in a valid format", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        finally:
            if file.closed == False:
                file.close()

# This class focuses on user inputs, user outputs, and error handling
class IO:
    """
    This function prints error messages out in a way that should be legible and understandable to 
    anyone working on this script.

    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    """
    This function prints out a set of text that usually should be a menu that gives users an idea 
    of what to input for the input_menu_choice() function

    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
    """
    @staticmethod
    def output_menu(menu: str):
        print(menu)
    
    """
    This function prompts the user to select an option. If they don't select 1, 2, 3, or 4, then 
    it prompts them to try to select one of those options again
    
    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
    """
    @staticmethod
    def input_menu_choice():
        try:
            user_choice = input("Please select an option: ")
            if user_choice not in ("1","2","3","4"):
                raise Exception("Please select only 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages("Unknown Error.",e.__str__())
        return user_choice

    """
    This function prints the current list of student data (including inputs from the user)
    
    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
        Ryan Seng, 5/25/2024, Updated Script for Assignment07 version update
    """
    @staticmethod
    def output_student_courses(student_data: list):
        print("The current list of students is:")
        print("Name \t\tLast Name \tCourse")
        for student in student_data:
            print(f"{student.first_name} \t\t {student.last_name} \t\t{student.course}")

    """
    This function takes in users' inputs for a student's first name, last name, and course, create a student object using those inputs,
    and adds that student to the list of student data

    Change Log: (Who, When, What)
        Ryan Seng, 5/19/2024, Created Assignment06
        Ryan Seng, 5/25/2024, Updated Script for Assignment07 version update
    """
    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or symbols")
            
            student_last_name = input("Please enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The first name and last name should not contain numbers or symbols")
            
            course_name = input("Please enter the course name: ")

            new_student = Student(first_name=student_first_name, last_name=student_last_name, course= course_name)

            student_data.append(new_student)
            print(f"{new_student.first_name} {new_student.last_name} in {new_student.course} has been added.")            
        except ValueError as e:
            IO.output_error_messages("There is a incorrect value.", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        return student_data

# This class is the parent object to the student class and is the baseline for objects in this program
class Person:

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("There are numbers or symbols in the first name!")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("There are numbers or symbols in the first name!")
        
    def __str__(self):
        return f"{self.first_name},{self.last_name}"

# This is a child class of the Person class. It builds off of the Person class 
# by taking courses that the person is taking
class Student(Person):

    def __init__(self, first_name: str, last_name: str, course: str):
        super().__init__(first_name = first_name, last_name= last_name)
        self.course = course
    
    @property
    def course(self):
        return self.__course
    
    @course.setter
    def course(self, value: str):
        self.__course = value

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course}"

# Actual program begins here
if __name__ == "__main__":

    # Reading in the file
    students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

    # A While loop that facilitates the Menu and according actions
    while True:
        IO.output_menu(MENU)
        
        menu_choice = IO.input_menu_choice()

        match menu_choice:
            case "1":
                students = IO.input_student_data(student_data = students)
            case "2":
                IO.output_student_courses(student_data = students)
            case "3":
                FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
            case "4":
                print("The program has ended.")
                exit()