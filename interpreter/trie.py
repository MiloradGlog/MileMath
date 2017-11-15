class Trie(object):
    def __init__(self, value, letter):
        self.children = dict()
        self.value = value
        self.letter = letter

    def __str__(self):
        print("Sad sam u Node: " + self.letter)
        print("Deca su: \n" + self.children.__str__())
        print("Value mi je: " + str(self.value))
        print("Letter mi je: " + str(self.letter))
        print("Is final? " + self.isLeaf().__str__())
        print("------------------------------------------------------------------")

    # Dodaje rec u recnik
    def addWord(self, word, value):
        if (len(word) <= 0):
            return
        if (len(word) > 1):
            if word[0:1] not in self.children:
                self.children[word[0:1]] = Trie(";", word[0:1])

            self.children.get(word[0:1]).addWord(word[1:], value)

        if (len(word) == 1):
            if word in self.children:
                print("ne mozes da dodas, vec postoji")
                return
            self.children[word] = Trie(value, word)

            # Vraca vrednost neke reci

    def getWord(self, word):
        if (not self.hasChild(word[0:1])):
            print("Nemam to dete, ne postoji ta rec")
            return

        child = self.children[word[0:1]]

        if (len(word) == 1):
            if (child.letter == word):
                return child.value
            else:
                print("Ta rec ne postoji")
                return

        return child.getWord(word[1:])

    # Vraca true ili false ako trenutni node ima, ili nema odredjeno dete(slovo)
    def hasChild(self, letter):
        if letter in self.children:
            return True
        else:
            return False

    def isLeaf(self):
        return not bool(self.children)

    # Ispisuje stablo od trenutnog node-a
    def printTrie(self):
        self.__str__()
        for key in self.children:
            self.children.__getitem__(key).printTrie()