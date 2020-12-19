class TrieNode:
    def __init__(self,ch):
        self.ch=ch
        self.child=[None]*26
        self.word_end=False

    def addchild(self,substring):
        ch=substring[0]
        ascii_value=ord(ch)-ord('a')
        if self.child[ascii_value] is None:
            self.child[ascii_value]=TrieNode(ch)

        if len(substring[1:]) == 0:
            self.child[ascii_value].word_end = True
        else:
            self.child[ascii_value].addchild(substring[1:])

    def searchild(self,substring):
        if substring is None:
            return False
        ascii_value = ord(substring[0])-ord('a')
        if self.child[ascii_value] is None:
            return False
        if len(substring[1:]) >= 1:
            return self.child[ascii_value].searchild(substring[1:])
        if self.child[ascii_value].word_end:
            return True
        return False

    def printchild(self):
        for child in self.child:
            if child is not None:
                print(child.ch)
                child.printchild()
class Trie:
    def __init__(self):
        self.roots=[None]*26

    def add(self, word):
        first_char = word[0]
        ascii_value= ord(first_char)-ord('a')
        if self.roots[ascii_value] is None:
            self.roots[ascii_value]=TrieNode(first_char)
        self.roots[ascii_value].addchild(word[1:])

    def searchNode(self,word):
        if word is None:
            print("1")
            return False
        ascii_value = ord(word[0])-ord('a')
        if self.roots[ascii_value] is None:
            print("2")
            return False
        if len(word[1:]) >= 1:
            print("3")
            return self.roots[ascii_value].searchild(word[1:])
        return True

    def printNode(self):
        print(self.roots)
        for root in self.roots:
            if root is not None:
                print(root.ch)
                root.printchild()

if __name__ == '__main__':
    trie_new = Trie()
    words = ['me','men','mom']
    for word in words:
        trie_new.add(word)
    trie_new.printNode()
    print(trie_new.searchNode('tom'))

