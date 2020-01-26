class Employee():
    employee_list=[]
    def __init__(self, employee_name,employee_surname,age,salary):
        self.employee_name=employee_name
        self.employee_surname=employee_surname
        self.age=age
        self.salary=salary
        self.e_mail=employee_name+employee_surname+"@pycoders.com"
        Employee.employee_list.append(self)

    def display(args):
        display_list=[]
        for each in args:
            display_list.append(each.employee_name + " " + each.employee_surname + " " + str(each.age) + " " + str(each.salary))
        print("\nThe Employee List\n")
        for each in display_list:
            print(each)

    def sort_by_name(args):
        name_list = []
        for each in Employee.employee_list:
            name_list.append(each.employee_name + " " + each.employee_surname + " " + str(each.age) + " " + str(each.salary))
        name_list.sort()
        print("\nSorted by Name\n")
        for each in name_list:
            print(each)

    def sort_by_surname(args):
        surname_list = []
        for each in Employee.employee_list:
            surname_list.append(
                each.employee_surname + " " + each.employee_name + " " + str(each.age) + " " + str(each.salary))
        surname_list.sort()
        print("\nSorted by Surname\n")
        for each in surname_list:
            print(each)

    def sort_by_age(args):
        age_list = []
        for each in Employee.employee_list:
            age_list.append(
                str(each.age) + " " + each.employee_name + " " + each.employee_surname + " " + str(each.salary))
        age_list.sort()
        print("\nSorted by Age\n")
        for each in age_list:
            print(each)

    def sort_by_salary(args):
        salary_list = []
        for each in Employee.employee_list:
            salary_list.append(str(each.salary) + " " + each.employee_name + " " + each.employee_surname + " " + str(each.age))
        salary_list.sort()
        print("\nSorted by Salary\n")
        for each in salary_list:
            print(each)
    def salary_increase(ratio):
        salary_list=[]
        for each in Employee.employee_list:
            salary_inc=0
            salary_inc=each.salary+((each.salary*ratio)/100)
            salary_list.append(each.employee_name+" "+each.employee_surname+" "+str(salary_inc))
        print("\nThe list after salary raise\n")
        for each in salary_list:
            print(each)
    def total_increase(ratio):
        total_inc=0
        for each in Employee.employee_list:
            total_inc+=(each.salary*ratio)/100
        return print("\nThe total cost after each salary raise",total_inc)

employee1=Employee("Fikret","Yıl",30,1000)
employee2=Employee("Hasan","Can",25,1300)
employee3=Employee("Murat","Sökmez",38,2000)
employee4=Employee("A.Rıza","Kerim",39,1800)
employee5=Employee("Ufuk","Doymaz",32,1700)
employee6=Employee("Fikri","Kaya",24,1250)
employee7=Employee("Frankie","Jong",21,900)
employee8=Employee("Ryan","Bergkamp",40,3300)
employee9=Employee("Ronald","Molenaar",45,4000)
employee10=Employee("Max","Sar",26,1750)
employee11=Employee("Bastian","Kruse",36,2700)
employee12=Employee("Manuel","Lahm",23,1250)
employee13=Employee("Fernando","Neuer",28,2000)
employee14=Employee("Hakan","Usta",35,2500)
employee15=Employee("Umut","Tekke",22,1300)
employee16=Employee("Ferdi","Kan",25,1300)
employee17=Employee("Johan","Kuyt",26,1900)
employee18=Employee("Lionel","Ronaldo",34,2300)
employee19=Employee("Marcelo","Messi",33,4000)
employee20=Employee("Fatih","Arslan",24,1250)
Employee.display(Employee.employee_list)
Employee.sort_by_name(Employee.employee_list)
Employee.sort_by_surname(Employee.employee_list)
Employee.sort_by_age(Employee.employee_list)
Employee.sort_by_salary(Employee.employee_list)
x=input("\nPlease enter the salary raise ratio\n")
x=int(x)
Employee.salary_increase(x)
Employee.total_increase(x)
