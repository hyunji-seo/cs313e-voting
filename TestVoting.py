from io import StringIO
from unittest import main,TestCase
from Voting import voting_solve,has_winner,Candidate,Ballot

class TestVoting(TestCase):
#    def test_Candidate_class1(self):
#        p = Candidate("a")
#        self.assertEqual(p.name, "a")
    # below are test for ballot class
#    def test_Ballot_class1(self):
    # below are tests for has_winner
    def test_has_winner_1(self):
    	candi = Candidate("candi")
    	candi_2 = Candidate("candi_2")
    	list_1 = [candi, candi_2]
    	a = has_winner(3, 2.5, list_1)
    	self.assertEqual(a, True)
    def test_has_winner_2(self):
    	a = has_winner(1, .25, ["Red", "Green", "Blue", "Orange"])
    	self.assertEqual(a, True)
    def test_has_winner_3(self):
    	a = has_winner(9, 2, ["C1", "C2", "C3", "C4"])
    	self.assertEqual(a, True)
    def test_has_winner_4(self):
    	a = has_winner(5, 2, ["1", "2", "3"])
    	self.assertEqual(a, False)
    # below are test cases for voting solve
#    def test_voting_solve1(self):
main()