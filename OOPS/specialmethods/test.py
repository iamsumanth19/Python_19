class Employee:
    company_name='wipro'
    company_location='bangolore'
    emp_count=0
    def __init__(self,en,eid,esal,edes):
        self.employee_name=en
        self.employee_id=eid
        self.employee_sal=esal
        self.edesignation=edes
        Employee.emp_count+=1

    def __del__(self):
        Employee.emp_count-=1
sumanth=Employee('sumanth',123,500000,'sde')
shiva=Employee('shiva',124,200000,'sde')
print(sumanth.emp_count)
del shiva
print(sumanth.emp_count)
        