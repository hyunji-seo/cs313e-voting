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
        self.index = 1
    
    def get_next(self,i):
        j = i
        i += 1
        self.index += 1
        return self.ballot_list[j]

    def revote(self,list_of_current_candis,list_of_elim_candis,ballot,dic_ballot_to_candi):
        assert type(list_of_current_candis) is list
        while True:
            candi_revote = dic_ballot_to_candi[int(self.get_next(self.index))]
            try:
                if ( candi_revote in list_of_current_candis):
                    candi = candi_revote
                    candi.count += 1
                    candi.ballot_list.append(ballot)
                    break
            except StopIteration:
                break
    



def has_winner(cutoff, cutoff_tie, list_of_current_candis):
    assert type(list_of_current_candis) is list
    assert cutoff >= 0
    all_tied = True
    max_v = 0
    min_v = 2 * cutoff
    for candi in list_of_current_candis:
        if (candi.count > max_v):
            max_v = candi.count
        if(candi.count < min_v):
            min_v = candi.count

    assert max_v >= 0
    assert min_v >= 0
    # if (all_tied == True):
    #     return True
    # else:
    #     return False
    if(max_v >= cutoff):
        return True
    elif(max_v == min_v):
        return True

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
        assert num_candis >= 0
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
            candi_object.ballot_list.append(ballot)
            candi_object.count += 1
            num_ballots += 1

        # first 2 terminating conditions
        if (num_ballots == 1):
            cutoff = 1

        elif (num_ballots % 2 == 0):
            cutoff = num_ballots / 2 + 1 
        else:
            cutoff = num_ballots //2 + 1

        assert cutoff >= 0

        while (has_winner(cutoff, (num_ballots / num_candis),list_of_current_candis) == False):
        # do the following
            list_of_elim_candis = []
            current_candi_copy = list(list_of_current_candis)
            # last terminating condition
            # first find the least num of ballots and see if there is a tie
            for candi in list_of_current_candis:
                if (candi.count == 0):
                    least_ballot = 0
                else:
                    least_ballot = list_of_current_candis[0].count
                    for candi in list_of_current_candis:
                        if (candi.count < least_ballot):
                            least_ballot = candi.count

        
            for candi in current_candi_copy:
                if (candi.count == least_ballot):
                    list_of_elim_candis.append(candi)
                    list_of_current_candis.remove(candi)

            # list_of_elim_candis is right
            
            for candi in list_of_elim_candis:
                ballot_list = candi.ballot_list
                # go through each ballot in that 2d list(ballot_list)

                for ballot in ballot_list:
                    ballot.revote(list_of_current_candis,list_of_elim_candis,ballot,dic_ballot_to_candi)
                    #ballot_genertor = ballot.get_next(0)
                    
            num_candis = len(list_of_current_candis)
            assert num_candis >= 0
        
            
        all_tied = True
        for candi in list_of_current_candis:
            if (candi.count != num_ballots / num_candis):
                all_tied = False
                break

        if (all_tied == True):
            for candi in list_of_current_candis:
                print (candi)
        else:
            for candi in list_of_current_candis:
                if (candi.count >= cutoff):
                    print (candi)
        if (case_index != int(cases) - 1):
            print()

                  







