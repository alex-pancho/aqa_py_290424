class Employee():
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: float, department: str, programming_language: str, team_size: int):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
        return (f"TeamLead: {self.name}, Salary: {self.salary}, Department: {self.department}, "
                f"Programming Language: {self.programming_language}, Team Size: {self.team_size}")