import unittest
from homework_17 import TeamLead

class TestTeamLeadAttributes(unittest.TestCase):

    def test_teamlead_attributes(self):
        team_lead = TeamLead("Karyna", 120000, "Development", "Python", 10)
        # Перевірка атрибутів від Manager
        self.assertEqual(team_lead.name, "Karyna")
        self.assertEqual(team_lead.salary, 120000)
        self.assertEqual(team_lead.department, "Development")
        # Перевірка атрибутів від Developer
        self.assertEqual(team_lead.programming_language, "Python")
        # Перевірка власного атрибуту
        self.assertEqual(team_lead.team_size, 10)

if __name__ == "__main__":
    unittest.main()
