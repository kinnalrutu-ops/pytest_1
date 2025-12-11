def emp_det(name, emp_id, emp_dept,salary):
   res=(f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Employee Department: {emp_dept}\n"
        f"Employee Salary: {salary}\n")
   return res
if __name__ == "__main__":
    name="alice"
    emp_id=101
    emp_dept="HR"
    salary=60000
    print(emp_det(name, emp_id, emp_dept,salary))
