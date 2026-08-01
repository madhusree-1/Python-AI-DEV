class Student:
    college_name = "Aditya Institute of Technology"
    total_students = 0
    PASS_MARK = 35
    MAX_SUBJECTS = 5
    def __init__(self,roll_number,name,branch):
        self.name = name
        self._roll_number = roll_number
        self._branch = branch
        self.__marks = {}
        Student.total_students += 1
    @property 
    def roll_number(self):
        return self._roll_number
    @property
    def average(self):
        if not self.__marks:
            return 0.0
        return sum(self.__marks.values())/len(self.__marks)
    @property
    def grade(self):
        if not self.has_passed():
            return "F"
        avg = self.average
        if avg >= 90:
            return "A+"
        elif avg >=75 and avg <= 89.99:
            return "A"
        elif avg >=60 and avg<=74.99:
            return "B"
        elif avg >= 35 and avg<= 59.99:
            return "C"
        else:
            return "F"
    def add_marks(self,subject,marks):
        if subject not in self.__marks and len(self.__marks) >= Student.MAX_SUBJECTS:
            raise ValueError("Subjects are Limited!")
        if not Student.is_valid_mark(marks):
            raise ValueError(f"Invalid mark:{marks}. Must be a number between 1 and 100")
        self.__marks[subject] = marks
    def get_marks(self):
        return dict(self.__marks)
    def has_passed(self):
        if not self.__marks:
            return False
        return all(marks >= Student.PASS_MARK for marks in self.__marks.values())
    def change_branch(self,new_branch):
        old_branch = self._branch
        self._branch = new_branch
        return f"{self.name} moved from {old_branch} to {new_branch}."
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    @staticmethod
    def is_valid_mark(mark):
        return isinstance(mark,(int,float)) and (0 <= mark <= 100)
    def __str__(self):
        return (f"Student[{self._roll_number}] {self.name} | {self._branch} | Average: {self.average:.2f} | Grade: {self.grade}")
    
         

