class Employee:
    company_name = "TechCorpSolutions"
    total_employees = 0
    pf_percentage = 12.0
    MIN_SALARY = 15000
    MAX_SALARY = 500000
    def __init__(self,name,emp_id,department,salary,pan_number=""):
        self.name = name
        self._emp_id = emp_id
        self._department = department
        self._salary = salary
        self.__pan_number = pan_number
        Employee.total_employees += 1
    @property
    def emp_id(self,eid):
        self._emp_id = eid
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,sal):
        if not isinstance(sal,(int,float)):
           raise TypeError("Salary must be number")
        elif sal <= self.MIN_SALARY or sal >=self.MAX_SALARY :
            raise ValueError("Blocked: Salary must be between MIN_SALARY and MAX_SALARY, got",sal)
        self._salary = sal
    def apply_hike(self,percent):
        if(percent < 0 or percent>50):
            raise ValueError("Percent must be between 0 and 50")
        self._salary += (self._salary*percent)/100.0
        return self._salary
    def calculate_pf(self):
        return (self._salary*Employee.pf_percentage)/100
    def tranfer_department(self,new_dept):
        print(self.name,"moved from",self._department,"to",new_dept)
        return new_dept
    @classmethod
    def get_tottal_employee(cls):
        return cls.total_employees
    @staticmethod
    def is_valid_salary(amount):
        if amount < 15000 or amount > 500000:
            return False
        return True
    def __str__(self):
        return(f"Employee[{self._emp_id}] {self.name} | {self._department} | Rs.{self.salary}")
      