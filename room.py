class StudentSystem:
    def __init__(self):
        self.students = set()  # store student IDs
        self.enrollments = {}  # {student_id: set of courses}
        self.attendance = {}   # {(student_id, course): attendance_count}
        self.grades = {}       # {(student_id, course): grade}

    # Add Student
    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.add(student_id)
            self.enrollments[student_id] = set()
            print("Student added successfully.")
        else:
            print("Student already exists.")

    # Enroll in Course
    def enroll_course(self, student_id, course):
        if student_id in self.students:
            self.enrollments[student_id].add(course)
            print("Enrolled in course successfully.")
        else:
            print("Student not found.")

    # Mark Attendance
    def mark_attendance(self, student_id, course):
        if student_id in self.students and course in self.enrollments[student_id]:
            key = (student_id, course)
            self.attendance[key] = self.attendance.get(key, 0) + 1
            print("Attendance marked.")
        else:
            print("Student or course not found.")

    # Assign Grade
    def assign_grade(self, student_id, course, grade):
        if student_id in self.students and course in self.enrollments[student_id]:
            self.grades[(student_id, course)] = grade
            print("Grade assigned.")
        else:
            print("Student or course not found.")

    # View Student Report
    def view_student_report(self, student_id):
        if student_id in self.students:
            print("\nStudent Report")
            print("Student ID:", student_id)
            for course in self.enrollments[student_id]:
                att = self.attendance.get((student_id, course), 0)
                grade = self.grades.get((student_id, course), "Not Assigned")
                print("Course:", course)
                print(" Attendance:", att)
                print(" Grade:", grade)
                print("------------------")
        else:
            print("Student not found.")

    # Course-wise Report
    def course_report(self, course):
        print("\nCourse-wise Report:", course)
        for student_id in self.students:
            if course in self.enrollments[student_id]:
                att = self.attendance.get((student_id, course), 0)
                grade = self.grades.get((student_id, course), "Not Assigned")
                print("Student ID:", student_id)
                print(" Attendance:", att)
                print(" Grade:", grade)
                print("------------------")


# -------- Menu --------

system = StudentSystem()

while True:
    print("\n1. Add Student")
    print("2. Enroll in Course")
    print("3. Mark Attendance")
    print("4. Assign Grade")
    print("5. View Student Report")
    print("6. Course-wise Report")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        system.add_student(sid)

    elif choice == "2":
        sid = input("Enter Student ID: ")
        course = input("Enter Course Name: ")
        system.enroll_course(sid, course)

    elif choice == "3":
        sid = input("Enter Student ID: ")
        course = input("Enter Course Name: ")
        system.mark_attendance(sid, course)

    elif choice == "4":
        sid = input("Enter Student ID: ")
        course = input("Enter Course Name: ")
        grade = input("Enter Grade: ")
        system.assign_grade(sid, course, grade)

    elif choice == "5":
        sid = input("Enter Student ID: ")
        system.view_student_report(sid)

    elif choice == "6":
        course = input("Enter Course Name: ")
        system.course_report(course)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
