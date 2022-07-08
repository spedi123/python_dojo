class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print('# emp_1과 emp_2는 다른 메모리 주소값을 가진 별개의 오브젝트입니다.')
print(id(emp_1))
print(id(emp_2))
print()

print('# emp_1과 emp_2는 같은 클래스의 인스턴스인 것을 확인합니다.')
class_of_emp_1 = emp_1.__class__
class_of_emp_2 = emp_2.__class__
print(id(class_of_emp_1))
print(id(class_of_emp_2))
