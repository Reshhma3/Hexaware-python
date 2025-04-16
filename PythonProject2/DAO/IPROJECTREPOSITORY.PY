from abc import ABC, abstractmethod

class IProjectRepository(ABC):
    @abstractmethod
    def create_employee(self, emp):
        pass

    @abstractmethod
    def create_project(self, pj):
        pass

    @abstractmethod
    def create_task(self, task):
        pass

    @abstractmethod
    def assign_project_to_employee(self, project_id, employee_id):
        pass

    @abstractmethod
    def assign_task_in_project_to_employee(self, task_id, project_id, employee_id):
        pass

    @abstractmethod
    def delete_employee(self, user_id):
        pass

    @abstractmethod
    def delete_project(self, project_id):
        pass

    @abstractmethod
    def get_all_tasks(self, emp_id, project_id):
        pass