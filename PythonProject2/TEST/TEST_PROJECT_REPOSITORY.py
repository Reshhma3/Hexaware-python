import unittest
import sqlite3

class ProjectManageSystem:
    def __init__(self, db_name=":memory:"):
        self.conn = sqlite3.connect(db_name)  # Use an in-memory DB
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Project (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            ProjectName TEXT NOT NULL,
            Description TEXT,
            Start_date DATE,
            Status TEXT CHECK (Status IN ('started','dev','build','test','deployed')) NOT NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            Designation TEXT,
            Gender TEXT,
            Salary DECIMAL(10,2),
            Project_id INTEGER,
            FOREIGN KEY(Project_id) REFERENCES Project(Id) ON DELETE SET NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Task (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            project_id INTEGER,
            employee_id INTEGER,
            Status TEXT CHECK (Status IN ('Assigned','Started','Completed')) NOT NULL,
            FOREIGN KEY(project_id) REFERENCES Project(Id) ON DELETE CASCADE,
            FOREIGN KEY(employee_id) REFERENCES Employee(id) ON DELETE SET NULL
        )''')

    def add_task(self, task_name, project_id, employee_id, status):
        try:
            self.cursor.execute('''INSERT INTO Task (task_name, project_id, employee_id, Status)
                                    VALUES (?, ?, ?, ?)''', (task_name, project_id, employee_id, status))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise Exception("Task creation failed, check constraints.")

    def search_projects_by_employee(self, employee_id):
        self.cursor.execute('''SELECT * FROM Project WHERE Id IN (
                                SELECT project_id FROM Employee WHERE id = ?)''', (employee_id,))
        return self.cursor.fetchall()


class TestProjectManageSystem(unittest.TestCase):
    def setUp(self):
        self.db = ProjectManageSystem()

        # Add sample data for tests
        self.db.cursor.execute('''INSERT INTO Project (ProjectName, Description, Start_date, Status)
                                  VALUES ('Test Project', 'Test Description', '2025-01-01', 'started')''')
        self.db.cursor.execute('''INSERT INTO Employee (name, Designation, Gender, Salary, Project_id)
                                  VALUES ('Test Employee', 'Developer', 'Male', 50000, 1)''')
        self.db.conn.commit()

    def test_task_creation(self):
        # Adding a task
        self.db.add_task("Test Task", 1, 1, "Assigned")

        # Verify task creation
        self.db.cursor.execute("SELECT * FROM Task WHERE task_name='Test Task'")
        task = self.db.cursor.fetchone()
        self.assertIsNotNone(task)
        self.assertEqual(task[1], "Test Task")

    def test_exceptions_on_task_creation(self):
        with self.assertRaises(Exception):
            self.db.add_task("Invalid Task", 9999, 9999, "Invalid Status")

    def test_search_projects_by_employee(self):
        projects = self.db.search_projects_by_employee(1)
        self.assertEqual(len(projects), 1)

    def tearDown(self):
        self.db.conn.close()

if __name__ == '__main__':
   unittest.main()