# Finger exercise: Add to Grades a generator that meets the
# specification
#     def get_students_above(self, grade):
#     """Return the students a mean grade > g one at a time"""

import statistics

class Grades(object):
    def __init__(self):
        """Create an empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self._students:
            raise ValueError("Duplicate student")
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: a grade is a float
           Add a grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')
        
    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')
        
    def get_students(self):
        """Return a sorted list of the students in the grade book"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s

    def get_students_above(self, grade):
        """Return the students a mean grade > g one at a time"""
        for s in self._students:
            try:
                if statistics.mean(self.get_grades(s)) > grade:
                    yield s
            except:
                pass
