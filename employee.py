import sys

def get_employee_info(name, emp_id, department, salary):
  
    return (
        f"Employee Name:{name},"
        f"Employee ID:{emp_id},"
        f"Department:{department},"
        f"Salary:{salary:.2f}"
    )
if _name_ == "_main_":
    print("=== Employee details ===")
    print(get_employee_info("John Doe","E101","IT",55000))
