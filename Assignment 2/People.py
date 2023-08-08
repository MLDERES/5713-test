# This module contains the People class, which is used to create a list of people and the different types of people in our system
# Create a class called Person which is the base class from which other classes will inherit
class Person:

    # Creating the properties of the Person class
    id = 0
    first_name = ""
    last_name = ""
    
    # A person has an ID, first name and last name 
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    # The id property is a unique identifier for each person
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        # Check if the id is a positive integer, if not raise an exception
        if id < 0:
            raise ValueError("ID must be a positive integer")
        self.id = id

    # The string representation of a person is their first name and last name
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

# Create a class called course
# A course is a class that a student can take and an instructor can teach
class Course:
    course_number = 0
    couse_name = ""
    description = ""
    department = ""
    credits = 0

    # A course has a course ID, course name, description, department and credits
    def __init__(self, course_number, course_name, description, department, credits):
        self.course_number = course_number
        self.course_name = course_name
        self.description = description
        self.department = department
        self.credits = credits

    # The course number is a unique identifier for each course which must be greater than 0
    def set_course_number(self, course_number):
        if course_number < 0:
            raise ValueError("Course number must be a positive integer")
        self.course_number = course_number
    
    # The course ID is a combination of the department and course number
    # It can't be set directly, but can be retrieved
    def course_id(self):
        return f'{self.department}{self.course_number}'
    
    # The string representation of a course is the ID and the course name
    def __str__(self):
        return f'{self.course_id()} {self.course_name}'

# Create a class called Instructor which inherits from the Person class
# An instructor is a person who teaches one or more courses
class Instructor(Person):
    courses_teaching = []

    # An instructor has an ID, first name, last name and a list of courses they are teaching
    def __init__(self, id, first_name, last_name, courses_teaching):
        # Initialize the Person class
        super().__init__(id, first_name, last_name)
        self.courses_teaching = courses_teaching

    # An instructor can teach a course
    def add_course(self, course):
        self.courses_teaching.append(course)

    # An instructor can stop teaching a course
    def remove_course(self, course):
        self.courses_teaching.remove(course)

    # An instructor can get a list of courses they are teaching
    def get_courses(self):
        return self.courses_teaching

# Create two courses ISYS1234 and ISYS5713
isys_1234 = Course(1234, "Introduction to Programming", "This course introduces students to programming", "ISYS", 3)
isys_5713 = Course(course_number=5713, 
                   course_name="Advanced Programming", 
                   description="This course introduces students to advanced programming", 
                   department="ISYS",
                   credits= 3)

# Create an instructor called John Smith who teaches ISYS1234
# Print out the instructor's details
# Print out the courses the instructor is teaching
# Add a new course for the instructor to teach
# Print out the courses the instructor is teaching
# Remove a course for the instructor to teach
# Print out the courses the instructor is teaching


# Part II
# Create a class called Student which inherits from the Person class
# A student is a person who is enrolled in one or more courses

# Create a student with your name.  The student id should be a positive number
# Print out the student's details
# Print out the courses the student is enrolled in
# Add a new course for the student to enroll in
# Print out the courses the student is enrolled in
# Remove a course for the student to enroll in
# Print out the courses the student is enrolled in
