NumberOfMissionaries = 3 # liczba misjonarzy
NumberOfCannibals = 3 # liczba kanibali
RaftCapacity = 2 # pojemność tratfy

class Stan:
    def __init__(self, State = None , oL = False, mOTL = 0, cOTL = 0, mOTR = 0, cOTR = 0,a = None):
        if State:
            self.onLeft = False
            self.missionariesOnTheLeft = NumberOfMissionaries
            self.cannibalsOnTheLeft = NumberOfCannibals
            self.missionariesOnTheRight = 0
            self.cannibalsOnTheRight = 0
            self.ancestor = None
        else:
            self.onLeft = oL
            self.missionariesOnTheLeft = mOTL #mOTL -> Misionaries On The Left
            self.cannibalsOnTheLeft = cOTL
            self.missionariesOnTheRight = mOTR
            self.cannibalsOnTheRight = cOTR
            self.ancestor = a

class Searching:
    def __init__(self):
        self.HistoryOfTheState = []
        self.QueueOfTheState = []
        stan = Stan(None, True, NumberOfMissionaries, NumberOfCannibals, 0, None)

    def serch(self):
        while True:
            stan = selectStateToExpansion()
            if stan == None:
                print("Brak rozwiązania")
                break
            if orResolved(stan):
                while True:
                    if stan is not None:
                        print("Kanibale po lewej" + str(stan.cOTL) + "\n" +
                              "Misjonarze po lewej" + str(stan.mOTL) + "\n" +
                              "Kanibale po prawej" + str(stan.cOTR) + "\n" +
                              "Misjonarze po prawej" + str(stan.mOTR) + "\n" +
                              "===========================================\n")
                        stan = stan.ancestor
                    else:
                        break
                break
            listExpandState = ExpandsState(stan)
            listExpandState = FiltredStates(listExpandState)
            UpdateList(listExpandState)

    def UpdateList(self, ls):
        for S in ls:
            self.QueueOfTheState.append(S)
            self.HistoryOfTheState.append(S)
    def FiltredStates(self, ls):
        okList = []
        for it in ls:
            if self.InRules(it) and self.IsNew(it):
                okList.append(it)
        return okList
    def InRules(self, s):
        pass
    def IsNew(self, s):
        pass
    def ExpandsState(self, s):
        NewStates = []
        if s.onLeft:
            for i in range(RaftCapacity+1):
                for j in range(RaftCapacity+1):
                    if i == 0 and j == 0 or i+j > RaftCapacity:
                        continue
                    elif


