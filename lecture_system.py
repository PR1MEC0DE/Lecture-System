# lecture_system.py

class Lecture:
    def __init__(self, topic, duration, lecturer_name, room_number):
        self.topic = topic
        self.duration = duration
        self.lecturer_name = lecturer_name
        self.room_number = room_number
        self.attendees = []

    def start_lecture(self):
        print(f"Lecture '{self.topic}' started in {self.room_number}.")

    def end_lecture(self):
        print(f"Lecture '{self.topic}' has ended.")

    def add_attendee(self, student):
        self.attendees.append(student)
        print(f"{student.name} joined the lecture '{self.topic}'.")

    def display_details(self):
        print(f"Topic: {self.topic}, Lecturer: {self.lecturer_name}, Duration: {self.duration} minutes")


class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.lectures = []

    def add_lecture(self, lecture):
        self.lectures.append(lecture)
        print(f"Lecture '{lecture.topic}' added to course '{self.name}'.")


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def attend_lecture(self, lecture):
        lecture.add_attendee(self)
        print(f"{self.name} is attending {lecture.topic}.")


class Classroom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity

    def open_room(self):
        print(f"Classroom {self.room_number} is now open.")


# Simple example run
if __name__ == "__main__":
    # Objects
    room = Classroom("B201", 40)
    lecture = Lecture("Object-Oriented Programming", 90, "Mr. Dominic Flocea", room.room_number)
    course = Course("Software Engineering", "SE101")
    student1 = Student("Igor Boltunov", 1)

    # Interactions
    room.open_room()
    course.add_lecture(lecture)
    lecture.start_lecture()
    student1.attend_lecture(lecture)
    lecture.display_details()
    lecture.end_lecture()
