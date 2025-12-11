# faculty.py
from typing import List, Optional # <-- ADDED List and Optional imports
from student import Student
from study_field import StudyField

class Faculty:
    """
    Represents a Faculty that manages its associated students.
    """

    def __init__(self, name: str, abbreviation: str, study_field: StudyField):
        """Initializes a new Faculty with empty student lists."""
        self.name = name
        self.abbreviation = abbreviation
        self.study_field = study_field
        
        # Composition: List of currently enrolled students.
        self._students_enrolled: List[Student] = []
        self._students_graduated: List[Student] = []

    def __str__(self):
        """Provides a simple string representation for the faculty."""
        # This is where we need to ensure the attribute names are correct
        return (f"Faculty: {self.name} ({self.abbreviation}) | "
                f"Field: {self.study_field.value} | "
                f"Enrolled: {len(self._students_enrolled)} | " # CHECKED
                f"Graduates: {len(self._students_graduated)}") # CHECKED

    # --- Faculty Operations ---
    
    def enroll_student(self, student: Student) -> bool:
        if self.find_student_by_email(student.email):
            print(f"Error: Student with email '{student.email}' is already in this faculty.")
            return False
        
        student.is_graduated = False
        self._students_enrolled.append(student)
        return True

    def graduate_student(self, email: str) -> Optional[Student]:
        student_to_graduate = self.find_enrolled_student_by_email(email)

        if student_to_graduate:
            self._students_enrolled.remove(student_to_graduate)
            student_to_graduate.graduate()
            self._students_graduated.append(student_to_graduate)
            return student_to_graduate
        
        return None

    def find_enrolled_student_by_email(self, email: str) -> Optional[Student]:
        return next((s for s in self._students_enrolled if s.email == email), None)

    def find_student_by_email(self, email: str) -> Optional[Student]:
        """Checks both enrolled and graduated lists."""
        student = self.find_enrolled_student_by_email(email)
        return student if student else next((s for s in self._students_graduated if s.email == email), None)
        
    def display_enrolled_students(self):
        if not self._students_enrolled:
            print(f"[{self.abbreviation}] Currently no students are enrolled.")
            return

        print(f"[{self.abbreviation}] Currently Enrolled Students:")
        for student in self._students_enrolled:
            print(f"  - {student}")

    def display_graduates(self):
        if not self._students_graduated:
            print(f"[{self.abbreviation}] Currently no students have graduated.")
            return

        print(f"[{self.abbreviation}] Graduates:")
        for student in self._students_graduated:
            print(f"  - {student}")
            
    def get_study_field_name(self) -> str:
        return self.study_field.name
