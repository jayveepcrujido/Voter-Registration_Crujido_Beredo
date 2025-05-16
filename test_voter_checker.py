import unittest


from voter_checker import is_eligible_to_vote


class TestVoterEligibility(unittest.TestCase):

    def test_valid_voter(self):
        result = self.is_eligible_to_vote(18)
        self.assertTrue(result)

    def test_underage_voter(self):
        result = self.is_eligible_to_vote(17)
        self.assertFalse(result)

    def test_non_citizen_voter(self):
        result = self.is_eligible_to_vote(is_citizen) = False
        self.assertFalse(result)

    def test_underage_non_citizen(self):
        result = self.is_eligible_to_vote(18) \
            and is_eligible_to_vote(is_citizen=False)
        self.assertFalse(result)

    def test_negative_age(self):
        result = self.is_eligible_to_vote(-1)
        self.assertEqual(result, "Age cannot be negative")
