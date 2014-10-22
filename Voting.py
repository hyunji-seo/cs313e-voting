## ========== classes =============

class Candidate:
    def __init__(self,candi_name):
        self.name = candi_name
        self.ballot_list = []
        self.count = 0

    def is_elim(self):
        return (self.name in list_of_elim_candis)
        

class Ballot:
    def __init__(self,ballot_list):
        self.ballot_list = ballot_list

    def next_choice(self):
        i = 0
        while True:
            yield ballot_list[i]
            i += 1 

def has_winner(cutoff, cutoff_tie, list_of_current_candis):
    if type(cutoff_tie) is int:
        all_tied = True
        for candi in list_of_current_candis:
            if (candi.count != cutoff_tie):
                all_tied = False
        if (all_tied == True):
            return True

    else:
        for candi in list_of_current_candis:
            if (candi.count >= cutoff):
                return True
            else:
                return False


# ==================== CODE =========================


def voting_solve (r, w) :
    num_ballots = 0
    list_of_current_candis = []
    list_of_elim_candis = []
    # number of cases following
    cases = r.readline()  
    for i in range(int(cases)):

        blank = r.readline()
        l = r.readline()
        num_candis = int(l)

        # dic_name_to_object {candidate:object}
        # dic_ballot_candi {#:candidate}
        dic_name_to_object = {}
        for i in range(num_candis):
            name = r.readlines()
            candi = Candidate(name)
            dic_name_to_object[str(name)] = candi
            list_of_current_candis.append(candi)
            #print(candi)
        list_of_items = zip(range(1,num_candis + 1),list_of_current_candis)
        dic_ballot_to_candi = {k : v for k, v in list_of_items}
        list_of_ballots = []    
        while (r.readline() != ""):
            line_list = r.readline().split()
            print (line_list)
            list_of_ballots.append(line_list)
        print ("list of Ballot")
        print (list_of_ballots)
        for line in list_of_ballots:
            ballot_list = line.split()
            ballot = Ballot(ballot_list)
            first_choice = ballot_list[0]
            candi_name = dic_ballot_to_candi[first_choice]
            print ("*************************")
            print(str(candi_name) + "___________")
            candi_object = dic_name_to_object[candi_name]
            candi_object.ballot_list.append(ballot.ballot_list)
            candi_object.count += 1
            num_ballots += 1
        # first 2 terminating conditions
        cutoff = num_ballots // 2 + 1
        while (has_winner(cutoff, (num_ballots / num_candis), list_of_current_candis) == False):
        # do the following    

            # last terminating condition
            # first find the least num of ballots and see if there is a tie
#            print(list_of_current_candis[0])
            least_ballot = list_of_current_candis[0].count
#            print (str(least_ballot) + "++++++++++")
#            print (list_of_current_candis)
            for candi in list_of_current_candis:
                if candi.count < least_ballot:
                    least_ballot = candi.count
                elif (candi.count == least_ballot):
                    list_of_elim_candis.append(candi)
                    list_of_current_candis.remove(candi)
#            print(num_candis)
            num_candis = len(list_of_current_candis)

            for candi in list_of_elim_candis:
                ballot_list = candi.ballot_list
                # go through each ballot in that 2d list(ballot_list)
                for ballot in ballot_list:
                    ballot_iter = iter(ballot)
                    first_choice = next(ballot_iter)
                    while True:
                        if (dic_ballot_to_candi[next(ballot_iter)] not in list_of_elim_candis):
                            candi_name = dic_ballot_to_candi[next(ballot_iter)]
                            candi = dic_name_to_object[candi_name]
                            candi.count += 1
                            candi.ballot_list.append(ballot)
                            break

        if (all_tied == True):
            print (list_of_current_candis)
        else:
            print (list_of_current_candis[0])







