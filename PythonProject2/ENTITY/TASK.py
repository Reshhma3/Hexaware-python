class Task:
    def __init__(self, task_id=None, task_name=None, project_id=None, employee_id=None, status=None):
        self.__task_id = task_id
        self.__task_name = task_name
        self.__project_id = project_id
        self.__employee_id = employee_id
        self.__status = status

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, value):
        self.__task_id = value

    @property
    def task_name(self):
        return self.__task_name

    @task_name.setter
    def task_name(self, value):
        self.__task_name = value

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, value):
        self.__project_id = value

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value