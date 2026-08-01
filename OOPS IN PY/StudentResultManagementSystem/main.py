from Student import *
def main():
    print("College:",Student.college_name)
    s1 = Student(101,"Ravi Kumar","CSE")
    s2 = Student(102,"Anit Sharma","ECE")
    print("Total Students:",Student.total_students)
    Student.add_marks(s1,"Maths",92)
    Student.add_marks(s1,"Physics",88)
    Student.add_marks(s1,"Chemistry",76)
    Student.add_marks(s2,"Maths",37.50)
    Student.add_marks(s2,"Physics",37.50)
    print(s1)
    print(s2)
    print("Private:",Student.get_marks(s1))
    print("s1 passed:",Student.has_passed(s1))
    Student.add_marks(s2,"Chemistry",0)
    print("s2 passed:",Student.has_passed(s2))
    print(Student.change_branch(s1,"IT"))
    print("is_valid_mark(105):",Student.is_valid_mark(105))
    #Blocked(mark 150):Mark must be between 0	and	100,got	150
    # print(Student.add_marks(s2,"Chemistry",150))
    #AttributeError: property 'average' of 'Student' object has no setter
    # s1.average = 99
    # AttributeError: property 'roll_number' of 'Student' object has no setter
    # s1.roll_number = 103
    print("Protected:",s1._branch)
    print("Private:",Student.get_marks(s1))

if __name__ == "__main__":
    main()