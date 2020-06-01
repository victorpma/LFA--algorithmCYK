from re import findall
from math import floor, ceil

grammar = dict()


def main():

    def readGrammar():
        with open('grammar.txt', 'r') as file:
            terminals = []
            no_terminals = []

            for row in file.readlines():
                left, right = row.split(" => ")

                right = right[:-1].split(" | ")

                for item in right:
                    if(str.islower(item)):
                        terminals.append([left, item])
                    else:
                        no_terminals.append([left, item])

            return no_terminals, terminals

    def getPair(value1, value2):
        res = set()
        if value1 == set() or value2 == set():
            return set()
        for f in value1:
            for s in value2:
                res.add(f+s)
        return res

    def runCYK(no_terminals, terminals, word):

        length = len(word)
        var0 = [va[0] for va in no_terminals]
        var1 = [va[1] for va in no_terminals]

        table = [[set() for _ in range(length-i)] for i in range(length)]

        for i in range(length):
            for te in terminals:
                if word[i] == te[1]:
                    table[0][i].add(te[0])

        for i in range(1, length):
            for j in range(length - i):
                for k in range(i):
                    row = getPair(table[k][j], table[i-k-1][j+k+1])
                    for ro in row:
                        if ro in var1:
                            table[i][j].add(var0[var1.index(ro)])

        for c in word:
            print("\t{}".format(c), end="\t")
        print()

        for i in range(len(word)):
            print(i+1, end="")
            for c in table[i]:
                if c == set():
                    print("\t{}".format("_"), end="\t")
                else:
                    print("\t{}".format(c), end=" ")
        print()

        if 'S' in table[len(word)-1][0]:
            print("Essa palavra faz parte da gramática!")
        else:
            print("Essa palavra não faz parte da gramática!")

    while True:
        print("----------------- MENU -----------------")
        print("\n1- Testar Palavra\n2- Finalizar")

        optionInput = int(input("\nEscolha uma opção acima:"))

        if optionInput == 1:
            word = input("\n Informe uma palavra para testar a gramática:")
            no_terminals, terminals = readGrammar()
            runCYK(no_terminals, terminals, word)
        else:
            print("Opção inválida, tente novamente!")
            break


if __name__ == "__main__":
    main()
