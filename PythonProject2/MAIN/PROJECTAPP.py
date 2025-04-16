from DAO.PROJECTREPOSITORYIMPL import ProjectRepositoryImpl
from ENTITY.EMPLOYEE import Employee
from ENTITY.PROJECT import Project
from ENTITY.TASK import Task
from EXCEPTIONS.EMPLOYEENOTFOUND import EmployeeNotFoundException
from EXCEPTIONS.PROJECTNOTFOUND import ProjectNotFoundException

def main():
    repo = ProjectRepositoryImpl()

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Add Project")
        print("3. Add Task")
        print("4. Assign Project to Employee")
        print("5. Assign Task to Employee")
        print("6. Delete Employee")
        print("7. Delete Project")
        print("8. List All Tasks for Employee in Project")
        print("9. Exit")

        choice = int(input("Choose an operation: "))

        if choice == 1:
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            designation = input("Enter Designation: ")
            gender = input("Enter Gender: ")
            salary = float(input("Enter Salary: "))
            project_id = int(input("Enter Project ID (or 0 if none): "))
            employee = Employee(emp_id, name, designation, gender, salary, project_id)
            if repo.create_employee(employee):
                print("Employee added successfully.")
            else:
                print("Failed to add employee.")

        elif choice == 2:
            project_id = int(input("Enter Project ID: "))
            project_name = input("Enter Project Name: ")
            description = input("Enter Description: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            status = input("Enter Status (started/dev/build/test/deployed): ")
            project = Project(project_id, project_name, description, start_date, status)
            if repo.create_project(project):
                print("Project added successfully.")
            else:
                print("Failed to add project.")

        elif choice == 3:
            task_id = int(input("Enter Task ID: "))
            task_name = input("Enter Task Name: ")
            project_id = int(input("Enter Project ID: "))
            employee_id = int(input("Enter Employee ID (or 0 if none): "))
            status = input("Enter Status (Assigned/Started/Completed): ")
            task = Task(task_id,task_name, project_id, employee_id, status)
            if repo.create_task(task):
                print("Task added successfully.")
            else:
                print("Failed to add task.")

        elif choice == 4:
            project_id = int(input("Enter Project ID: "))
            employee_id = int(input("Enter Employee ID: "))
            if repo.assign_project_to_employee(project_id, employee_id):
                print("Project assigned to employee successfully.")
            else:
                print("Failed to assign project. Employee or project may not exist.")

        elif choice == 5:
            task_id = int(input("Enter Task ID: "))
            project_id = int(input("Enter Project ID: "))
            employee_id = int(input("Enter Employee ID: "))
            if repo.assign_task_in_project_to_employee(task_id, project_id, employee_id):
                print("Task assigned to employee successfully.")
            else:
                print("Failed to assign task. Task or project may not exist.")

        elif choice == 6:
            user_id = int(input("Enter Employee ID to delete: "))
            if repo.delete_employee(user_id):
                print("Employee deleted successfully.")
            else:
                print("Failed to delete employee. Employee may not exist.")

        elif choice == 7:
            project_id = int(input("Enter Project ID to delete: "))
            if repo.delete_project(project_id):
                print("Project deleted successfully.")
            else:
                print("Failed to delete project. Project may not exist.")

        elif choice == 8:
            emp_id = int(input("Enter Employee ID: "))
            project_id = int(input("Enter Project ID: "))
            try:
                tasks = repo.get_all_tasks(emp_id, project_id)
                if tasks:
                    print("Tasks assigned to employee in project:")
                    for task in tasks:
                        print(f"Task ID: {task.task_id}, Task Name: {task.task_name}, Status: {task.status}")
                else:
                    print("No tasks found for this employee in the specified project.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        elif choice == 9:
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
