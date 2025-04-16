class Project:
    def __init__(self, project_id=None, project_name=None, description=None, start_date=None, status=None):
        self.__project_id = project_id
        self.__project_name = project_name
        self.__description = description
        self.__start_date = start_date
        self.__status = status

    @property
    def project_id(self):
        return self.__project_id

    @project_id.setter
    def project_id(self, value):
        self.__project_id = value

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, value):
        self.__project_name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value