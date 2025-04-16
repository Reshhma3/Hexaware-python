import sqlite3
from DAO.IPROJECTREPOSITORY import IProjectRepository
from ENTITY.EMPLOYEE import Employee
from ENTITY.PROJECT import Project
from ENTITY.TASK import Task
from EXCEPTIONS.EMPLOYEENOTFOUND import EmployeeNotFoundException
from EXCEPTIONS.PROJECTNOTFOUND import ProjectNotFoundException
from UTIL.db_conn_util import DBConnUtil

class ProjectRepositoryImpl(IProjectRepository):
    def create_employee(self, emp: Employee, conn=None) -> bool:
        own_conn = False
        if conn is None:
            conn = DBConnUtil.get_connection()
            own_conn = True
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Employee (id, name, Designation, Gender, Salary, Project_id) VALUES (?, ?, ?, ?, ?, ?)",
                (emp.emp_id, emp.name, emp.designation, emp.gender, emp.salary, emp.project_id))
            if own_conn:
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            cursor.close()
            if own_conn:
                conn.close()

    def create_project(self, pj: Project) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Project (Id, ProjectName, Description, Start_date, Status) VALUES (?, ?, ?, ?, ?)",
                           (pj.project_id, pj.project_name, pj.description, pj.start_date, pj.status))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            cursor.close()
            conn.close()

    def create_task(self, task: Task) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Task (task_id, task_name, project_id, employee_id, Status) VALUES (?, ?, ?, ?, ?)",
                           (task.task_id, task.task_name, task.project_id, task.employee_id, task.status))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            cursor.close()
            conn.close()

    def assign_project_to_employee(self, project_id: int, employee_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Employee SET Project_id = ? WHERE id = ?", (project_id, employee_id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()

    def assign_task_in_project_to_employee(self, task_id: int, project_id: int, employee_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Task SET employee_id = ? WHERE task_id = ? AND project_id = ?", (employee_id, task_id, project_id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()

    def delete_employee(self, user_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Employee WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()

    def delete_project(self, project_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Project WHERE Id = ?", (project_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()

    def get_all_tasks(self, emp_id: int, project_id: int):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Task WHERE employee_id = ? AND project_id = ?", (emp_id, project_id))
            tasks = cursor.fetchall()
            return [Task(task_id=row[0], task_name=row[1], project_id=row[2], employee_id=row[3], status=row[4]) for row in tasks]
        finally:
            cursor.close()
            conn.close()