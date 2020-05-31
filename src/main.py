from re import findall
from algorithmCYK import AlgorithmCYK


grammar = dict()


def main():

    def readGrammar():

        with open('grammer.txt', 'r') as file:
            for row in file.readlines():
                left = findall(r'[a-zA-Z]+\s\=\>', row)[0]
                key = left.replace('=>', '').strip()
                production = row.replace(left, '').strip().split('|')
                grammar[key] = production

            return grammar

    while True:
        print("----------------- MENU -----------------")
        print("\n1- Testar Palavra\n2- Finalizar")

        optionInput = int(input("\nEscolha uma opção acima:"))

        if optionInput == 1:
            word = input("\n Informe uma palavra para testar a gramática:")

            AlgorithmCYK.validateWord(word, readGrammar())
        else:
            print("Opção inválida, tente novamente!")
            break


if __name__ == "__main__":
    main()
