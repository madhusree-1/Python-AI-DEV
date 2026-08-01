from Employee import *
def main():
    print("Company:" ,Employee.company_name)
    print("Employee before:",Employee.total_employees)
    e1 = Employee("Ravi Kumar",101,"Engineering",60000.00)
    print(Employee.__str__(e1))
    e2 = Employee("Anita Sharma",102,"Finance",75000.00)
    print(Employee.__str__(e2))
    print("Employee after:",Employee.total_employees)
    print("PF for e1:",Employee.calculate_pf(e1))
    e1.__pan_number ="ABCDE1234F"
    print("After 10 % hike:",Employee.apply_hike(e1,10))
    Employee.tranfer_department(e1,"Data Science")
    # Attempt	an	invalid	salary	and	catch	the	error
    # print("is_valid_salary(9000):",e1.is_valid_salary(9000))
    # e1.salary=5000
    # Attempt	to	write	to	emp_id	and	catch	the	error
    # e1.emp_id ="madhu"
    #Access	the	protected and private attributes from outside and print	what happens
    print("Protected :",e1._department)
    print("Private :",e1.__pan_number)
if __name__ == "__main__":
    main()