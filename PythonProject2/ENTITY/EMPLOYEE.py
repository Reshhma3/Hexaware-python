class Employee:
    def __init__(self, emp_id=None, name=None, designation=None, gender=None, salary=None, project_id=None):
        self.__emp_id = emp_id
        self.__name = name
        self.__designation = designation
        self.__gender = gender
        self.__salary = salary
        self.__project_id = project_id

    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, value):
        self.__emp_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def designation(self):
        return self.__designation

    @designation.setter
    def designation(self, value):
        self.__designation = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, value):
        self.__project_id = value