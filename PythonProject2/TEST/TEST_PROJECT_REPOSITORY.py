import sqlite3
import pytest


class ProjectManageSystem:
    def __init__(self, db_name=":memory:"):
        self.conn = sqlite3.connect(db_name)
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
                                SELECT Project_id FROM Employee WHERE id = ?)''', (employee_id,))
        return self.cursor.fetchall()

# ------------------------
# Test code
# ------------------------

@pytest.fixture
def db():
    system = ProjectManageSystem()

    # Insert test project & employee
    system.cursor.execute('''INSERT INTO Project (ProjectName, Description, Start_date, Status)
                             VALUES ('Test Project', 'Test Description', '2025-01-01', 'started')''')
    system.cursor.execute('''INSERT INTO Employee (name, Designation, Gender, Salary, Project_id)
                             VALUES ('Test Employee', 'Developer', 'Male', 50000, 1)''')
    system.conn.commit()

    yield system
    system.conn.close()

def test_task_creation(db):
    db.add_task("Test Task", 1, 1, "Assigned")
    db.cursor.execute("SELECT * FROM Task WHERE task_name = 'Test Task'")
    task = db.cursor.fetchone()
    assert task is not None
    assert task[1] == "Test Task"

def test_invalid_task_creation_raises_exception(db):
    with pytest.raises(Exception, match="Task creation failed"):
        db.add_task("Invalid Task", 9999, 9999, "Invalid Status")

def test_search_projects_by_employee(db):
    projects = db.search_projects_by_employee(1)
    assert len(projects) == 1
    assert projects[0][1] == "Test Project"
