import unittest
from homework_17 import TeamLead

class TestTeamLeadAttributes(unittest.TestCase):
    
    def test_1_manager(self):
        team_lead = TeamLead("Test Test", 1000, "IT", "Python", 2)
        self.assertEqual(team_lead.name, "Test Test")
        self.assertEqual(team_lead.salary, 1000)
        self.assertEqual(team_lead.department, "IT")
        
    def test_2_developer(self):
        team_lead = TeamLead("Test Test", 1000, "IT", "Python", 2)
        self.assertEqual(team_lead.name, "Test Test")
        self.assertEqual(team_lead.salary, 1000)
        self.assertEqual(team_lead.programming_language, "Python")
        
    def test_3_team_lead(self):
        team_lead = TeamLead("Test Test", 1000, "IT", "Python", 2)
        self.assertEqual(team_lead.name, "Test Test")
        self.assertEqual(team_lead.salary, 1000)
        self.assertEqual(team_lead.department, "IT")
        self.assertEqual(team_lead.programming_language, "Python")
        self.assertEqual(team_lead.team_size, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)


