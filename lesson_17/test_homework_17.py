




import unittest
from homework_17 import TeamLead

class TestTeamLead(unittest.TestCase):
    def setUp(self):
        self.team_lead = TeamLead(name="Agent Smith", salary=120000, department="IT", programming_language="Python", team_size=5)

    def test_attributes_from_manager(self):
        self.assertEqual(self.team_lead.name, "Agent Smith", "Name attribute is incorrect")
        self.assertEqual(self.team_lead.salary, 120000, "Salary attribute is incorrect")
        self.assertEqual(self.team_lead.department, "IT", "Department attribute is incorrect")

    def test_attributes_from_developer(self):
        self.assertEqual(self.team_lead.programming_language, "Python", "Programming Language attribute is incorrect")

    def test_team_size_attribute(self):
        self.assertEqual(self.team_lead.team_size, 5, "Team Size attribute is incorrect")

if __name__ == '__main__':
    unittest.main()