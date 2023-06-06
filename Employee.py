#creating a class
class Employee:

    #create a class attribute/variable
    vacation_days = 15

#creating object/inctance from the class
Mariya = Employee()
Jane = Employee()
Bob = Employee()

print(f'Mary vacation available days {Mariya.vacation_days}')
print(f'Jane vacation available days {Jane.vacation_days}')
print(f'Bob vacation available days {Bob.vacation_days}')

# Change object atrebute value
Jane.vacation_days = 10
Jane.is_manager = True

print(Jane.is_manager)


# change class attribute value
Employee.vacation_days = 12

print(f'Mary vacation available days {Mariya.vacation_days}')
print(f'Jane vacation available days {Jane.vacation_days}')
print(f'Bob vacation available days {Bob.vacation_days}')

print(id(Employee.Mariya.vacation_days))

# print(Mariya)
# print(type(Mariya))
# print(isinstance(Mariya, Employee))
# print(isinstance('test',str))
# print(isinstance(1000))
