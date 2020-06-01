from algorithm_cyk import AlgorithmCYK

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

    while True:
        print("----------------- MENU -----------------")
        print("\n1- Testar Palavra\n2- Finalizar")

        optionInput = int(input("\nEscolha uma opção acima:"))

        if optionInput == 1:
            word = input("\n Informe uma palavra para testar a gramática:")
            noTerminals, terminals = readGrammar()
            newAlgorithmCYK = AlgorithmCYK(noTerminals, terminals, word)
            newAlgorithmCYK.runCYK()
        else:
            print("Opção inválida, tente novamente!")
            break


if __name__ == "__main__":
    main()
