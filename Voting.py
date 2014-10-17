## ========== classes =============

class Candidate:
    def __init__(self,candi_name):
        self.name = candi_name
        self.ballot_list = []
        self.count = 0

    def is_elim(self):
        return (self.candi_name in list_of_elim_candis)
        

class Ballot():
    def __init__(self,ballot_list):
        self.ballot_list = ballot_list

    def next_choice(self):
        i = 0
        while True:
            yield ballot_list[i]
            i += 1 

# ==================== CODE =========================



def voting_solve (r, w) :
    num_ballots = 0
    list_of_current_candis = []
    list_of_elim_candis = []
    # number of cases following
    cases = r.readline()   
    blank = r.readline()

    l = r.readline()
    print(l)
    num_candis = int(l)

    dic_name_to_object = {}
    for i in range(num_candis):
        name = r.readlines()
        candi = Candidate(name)
        dic_name_to_object[name] = candi
        list_of_current_candis.append(candi)
        #print(candi)
    list_of_items = zip(range(1,num_candis + 1),list_of_current_candis)
    dic_ballot_to_candi = {k : v for k, v in list_of_items}

    # the remaining 
    list_of_ballots = r.readlines()

    for line in list_of_ballots:
        ballot = Ballot(line)
        ballot_iter = next_choice(ballot)
        first_choice = next(ballot_iter)
        candi_name = dic_ballot_to_candi[first_choice]
        candi_object = dic_name_to_object[candi_name]
        candi_object.ballot_list.append(ballot.ballot_list)
        candi_object.count += 1
        num_ballots += 1


    # first 2 terminating conditions
    cutoff = num_ballots // 2 + 1
    cutoff_tie = num_ballots / num_candis
    if type(cutoff_tie) is int:
        all_tied = True
        for candi in list_of_current_candis:
            if (candi.count != cutoff_tie):
                all_tied = False

    if (all_tied == True):
        print list_of_current_candis

    for candi in list_of_current_candis:
        if (candi.count >= cutoff):
            return candi.name

    # now go to cool part!
    

