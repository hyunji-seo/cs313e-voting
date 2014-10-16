## ========== classes =============

class Candidate:
    list_of_current_candis = []
    list_of_elim_candis = []
    def __init__(self,candi_name):
        self.name = candi_name
        self.ballot_list = []

    def is_elim(self):
        return (self.candi_name in list_of_elim_candis)
        

class Ballot():
    def __init__(self,ballot_list):
        self.ballot = ballot_list

    def next_choice(self):
        i = 0
        while True:
            yield ballot_list[i]
            i += 1 

# ==================== CODE =========================



def voting_solve (r, w) :
    # number of cases following
    cases = r.readline()   
    blank = r.readline()

    l = r.readline()
#    l = l.split()
    print(l)
    num_candis = int(l)

    for i in range(num_candis):
        name = r.readlines()

    #    name = line.split("\n")
        candi = Candidate(name)
        print(candi)

    list_of_lines = r.readlines()

    for line in list_of_lines:
        ballot = Ballot(line)


