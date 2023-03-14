class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class HourlyEmployee(Employee):
    def __init__(self,name,id):
        super().__init__(name,id)
    def calculate_payroll(self):
        payroll=5000
        print("Name=",self.name)
        print("id=",self.id)
        print("hourly payroll=",payroll)
class SalaryEmployee(Employee):
    def __init__(self,name,id):
        super().__init__(name,id)
    def calculate_payroll(self):
        print("monthly salary=",payroll)
payroll=50000*30
class CommissionEmployee(SalaryEmployee):
    def calculate_payroll(self):
        commission=0.01*payroll
        print("payroll after commission=",commission+payroll)
salary1=HourlyEmployee("James","1239087")
salary2=SalaryEmployee("James","1239087")
salary=CommissionEmployee("James","1239087")
salary1.calculate_payroll()
salary2.calculate_payroll()
salary.calculate_payroll()