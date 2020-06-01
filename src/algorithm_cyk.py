class AlgorithmCYK:
    def __init__(self, noTerminals, terminals, word):
        self.__noTerminals = noTerminals
        self.__terminals = terminals
        self.__word = word

    def __getPair(self, value1, value2):
        res = set()
        if value1 == set() or value2 == set():
            return set()
        for f in value1:
            for s in value2:
                res.add(f+s)
        return res

    def runCYK(self):
        length = len(self.__word)
        var0 = [va[0] for va in self.__noTerminals]
        var1 = [va[1] for va in self.__noTerminals]

        table = [[set() for _ in range(length-i)] for i in range(length)]

        for i in range(length):
            for te in self.__terminals:
                if self.__word[i] == te[1]:
                    table[0][i].add(te[0])

        for i in range(1, length):
            for j in range(length - i):
                for k in range(i):
                    row = self.__getPair(table[k][j], table[i-k-1][j+k+1])
                    for ro in row:
                        if ro in var1:
                            table[i][j].add(var0[var1.index(ro)])

        for c in self.__word:
            print("\t{}".format(c), end="\t")
        print()

        for i in range(len(self.__word)):
            print(i+1, end="")
            for c in table[i]:
                if c == set():
                    print("\t{}".format("_"), end="\t")
                else:
                    print("\t{}".format(c), end=" ")
        print()

        if 'S' in table[len(self.__word)-1][0]:
            print("Essa palavra faz parte da gramática!")
        else:
            print("Essa palavra não faz parte da gramática!")
