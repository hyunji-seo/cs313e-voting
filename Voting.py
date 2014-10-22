## ========== classes =============

class Candidate:
    def __init__(self,candi_name):
        self.name = candi_name
        self.ballot_list = []
        self.count = 0


    def __str__(self):
        return self.name
        

class Ballot:
    def __init__(self,ballot_list):
        self.ballot_list = ballot_list

def has_winner(cutoff, cutoff_tie, list_of_current_candis,all_tied):
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

    # number of cases following
    cases = r.readline() 
    blank = r.readline()

    for i in range(int(cases)):
        case_index = i
        num_ballots = 0
        list_of_current_candis = []
        list_of_elim_candis = []
        l = r.readline()
        num_candis = int(l)
        # dic_name_to_object {candidate_name:object}
        # dic_ballot_to_candi {#:object}
        dic_name_to_object = {}
        for i in range(num_candis):
            name = r.readline().rstrip()
            candi = Candidate(name)
            dic_name_to_object[str(name)] = candi
            list_of_current_candis.append(candi)
               
        # so far so good 
        list_of_items = zip(range(1,num_candis + 1),list_of_current_candis)
        dic_ballot_to_candi = {k : v for k, v in list_of_items}
        list_of_ballots = [] 
        end = False   
        while (not end):
            line = r.readline().rstrip()
            if (line != ""):
                line_list = line.split()
                list_of_ballots.append(line_list)
            else:
                end = True
        # first round voting 
        for line in list_of_ballots:
            ballot = Ballot(line)

            first_choice = line[0]
            candi_object = dic_ballot_to_candi[int(first_choice)]
            candi_object.ballot_list.append(ballot.ballot_list)
            candi_object.count += 1
            num_ballots += 1

        

        # first 2 terminating conditions
        if (num_ballots % 2 == 0):
            cutoff = num_ballots / 2 
        else:
            cutoff = num_ballots //2 + 1

        all_tied = False
        while (has_winner(cutoff, (num_ballots / num_candis),list_of_current_candis,all_tied) == False):
        # do the following    
            current_candi_copy = list(list_of_current_candis)
            # last terminating condition
            # first find the least num of ballots and see if there is a tie
            least_ballot = list_of_current_candis[0].count
            for candi in list_of_current_candis:
                if (candi.count < least_ballot):
                    least_ballot = candi.count

        
            for candi in current_candi_copy:
                if (candi.count == least_ballot):
                    list_of_elim_candis.append(candi)
                    list_of_current_candis.remove(candi)


            num_candis = len(list_of_current_candis)

            #revote
            for candi in list_of_elim_candis:
                ballot_list = candi.ballot_list
                # go through each ballot in that 2d list(ballot_list)
                for ballot in ballot_list:
                    ballot_iter = iter(ballot)
                    first_choice = next(ballot_iter)
                    while True:
                        try:
                            candi_revote = dic_ballot_to_candi[int(next(ballot_iter))]

                            if (candi_revote not in list_of_elim_candis):
                                candi = candi_revote
                                candi.count += 1
                                candi.ballot_list.append(ballot)
                                break
                        except StopIteration:
                            break

        if (all_tied == True):
            print (list_of_current_candis)
        else:
            for candi in list_of_current_candis:
                print(candi,candi.count)
                if (candi.count > cutoff):
                    print (candi)
        if (case_index != int(cases) - 1):
            print()

                  








