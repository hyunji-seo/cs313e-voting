class Candidate:
    list_of_current_candis = []
    list_of_elim_candis = []
    def __init__(self,candi_name):
        self.name = candi_name
        self.ballot_list = []

    def is_elim(self):
        return (self.candi_name is in list_of_elim_candis)
        
















class Ballot():
    def __init__(self,ballot_list):
        self.ballot = ballot_list

    def next_choice(self):
        i = 0
        while True:
            yield ballot_list[i]
            i += 1 






def voting_solve(r,w):
    r.readline()
    r.readline()
    line = r.readline()
    l = line.split()
    num_candis = int(l[0])
    list_of_lines = r.readlines()
    for line in list_of_lines[]:
        name = line.split()
        candi = Candidate(name)





    for line in 