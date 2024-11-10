# --------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files,
# and exception handling
# Change Log: (Who, When, What)
#   Jeremy Peters, 11/05/2024, Initial file creation
#   Jeremy Peters, 11/07/2024, Code updates for assignment
#   Jeremy Peters, 11/10/2024, Post-office hours adjustments
# --------------------------------------------------------------------------- #
import os

# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"
MENU: str = """
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""

# Define the Data Variables
student_first_name: str = str()
student_last_name: str = str()
course_name: str = str()
csv_data: str = str()
file = None
menu_choice: str = str()
student_data: dict = dict()
students: list = list()

# Define and initiate text color variables
husky_menu: str = "\033[1;35m{}"
husky_purple: str = "\033[35m{}"
# print(husky_purple.format("husky_purple"))
husky_gold: str = "\033[93m{}"
# print(husky_gold.format("husky_gold"))
warning_color: str = "\033[96m{}"
# print(warning_color.format("warning_color"))
reset_color: str = "\033[0m"
# print(reset_color.format("colors reset"))
error_color: str = "\033[31m{}"
# print(error_color.format("error_color"))

# Custom message variables
file_exists: str = f"File {FILE_NAME} already exists. Skipping file creation."
prompt_firstname: str = f"Please enter the student's first name: "
prompt_lastname: str = f"Please enter the student's last name: "
no_data: str = f"You have not entered any data.\n" \
               f"Try starting with starting option 1."
alpha_only: str = f"Student name should only contain alphabetic characters."
ascii_only: str = f"Course name should only contain ascii characters."

# Open and reset the CSV file back to a base value for this scenario
# These two lines can be commented out if there's an existing file with data
try:
    print(f"Checking for existing file {FILE_NAME}...")
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
        raise FileExistsError(warning_color.format(file_exists))
    with open(FILE_NAME, "w") as file:
        print(f"No existing file {FILE_NAME} found. File will be created.")
        file.write("")
except FileExistsError as e:
    # print(error_color.format("File already exists and has content.\n"))
    # print(error_color.format("-- Error Message -- "))
    print(error_color.format(e, e.__doc__, type(e), sep="\n"))
finally:
    if file in locals() and not None and not file.closed:
        file.close()

# Open and iterate through the CSV file
# Data present is added to the students list variable
try:
    with open(FILE_NAME, "r") as file:
        for each_row in file.readlines():
            # Transform the data from the file
            student_data = each_row.strip().split(",")
            student_data = {"FirstName": student_data[0],
                            "LastName": student_data[1],
                            "CourseName": student_data[2]}
            students.append(student_data)

    # print(students)
    # Present menu options, display and save data to file
    while True:
        # Present the menu of choices
        print(husky_menu.format(MENU))
        menu_choice = input("What would you like to do: ")

        # Input user data
        if menu_choice == "1":
            try:
                while True:
                    try:
                        student_first_name = input(husky_purple.format(
                            prompt_firstname))
                        if not student_first_name.isalpha():
                            raise ValueError(
                                warning_color.format(f"{alpha_only}"))
                        student_first_name = student_first_name.title().strip()
                        break
                    except ValueError as e:
                        print(error_color.format("-- Error -- "))
                        # print(error_color.format(e.__doc__))
                        print(error_color.format(e))
                while True:
                    try:
                        student_last_name = input(
                            husky_purple.format(prompt_lastname))
                        if not student_last_name.isalpha():
                            raise ValueError(
                                warning_color.format(f"{alpha_only}"))
                        student_last_name = student_last_name.title().strip()
                        break
                    except ValueError as e:
                        print(error_color.format("-- Error -- "))
                        # print(error_color.format(e.__doc__))
                        print(error_color.format(e))
                while True:
                    try:
                        course_name = input(husky_purple.format(
                            "Please enter the course name: "))
                        if not course_name.isascii():
                            raise ValueError(
                                warning_color.format(f"{ascii_only}"))
                        course_name = course_name.title().strip()
                        break
                    except ValueError as e:
                        print(error_color.format("-- Error -- "))
                        # print(error_color.format(e.__doc__))
                        print(error_color.format(e))
                student_data = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
                students.append(student_data)
                print(husky_gold.format(
                    f"You have added {student_first_name} "
                    f"{student_last_name} for course {course_name} to the "
                    f"registration list."))
            except Exception as e:
                print(error_color.format("-- Error Message -- "))
                print(error_color.format(e, e.__doc__, type(e), sep="\n"))
                print(error_color.format("There was a non-specific error!\n"))

        # Present the current data
        elif menu_choice == "2":
            try:
                # print(students)
                if student_first_name == str():
                    raise ValueError(warning_color.format(no_data))
                else:
                    print(husky_gold.format(
                        f"The following students are registered:"))
                    for student in students:
                        print(husky_purple.format(
                            f"{student["FirstName"]},{student["LastName"]} is "
                            f"enrolled in {student["CourseName"]}"))
            except ValueError as e:
                print(error_color.format("-- Error -- "))
                # print(error_color.format(e.__doc__))
                print(error_color.format(e))

        # Save the data to a file
        elif menu_choice == "3":
            try:
                if student_first_name == str():
                    raise ValueError(warning_color.format(no_data))
                else:
                    print(
                        husky_gold.format(f"The following was saved to file:"))
                    with open(FILE_NAME, "w") as file:
                        for student in students:
                            csv_data += (
                                f"{student["FirstName"]},{student["LastName"]}"
                                f",{student["CourseName"]}\n")
                            print(husky_purple.format(f"{student["FirstName"]}\
 {student["LastName"]} is enrolled in {student["CourseName"]}"))
                        file.write(csv_data)
            except ValueError as e:
                print(error_color.format("-- Error -- "))
                # print(error_color.format(e.__doc__))
                print(error_color.format(e))
            except Exception as e:
                print(error_color.format("-- Error Message -- "))
                print(error_color.format(e, e.__doc__, type(e), sep="\n"))
                print(error_color.format("There was a non-specific error!\n"))
        # Stop the loop and exit the program
        elif menu_choice == "4":
            print(reset_color.format("Program closed successfully"))
            exit()
except FileNotFoundError as e:
    print(error_color.format("-- Error Message -- "))
    print(error_color.format(e.__doc__))
    print(error_color.format(e))
    print(f"Exiting program with error(s)")
except Exception as e:
    print(error_color.format("There was a non-specific error!\n"))
    print(error_color.format("-- Error Message -- "))
    print(error_color.format(e, e.__doc__, type(e), sep="\n"))
finally:
    if file is not None and file.closed == False:
        file.close()
    exit()
