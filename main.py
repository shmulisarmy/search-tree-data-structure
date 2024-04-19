"""
code sample:
    words = ["hello", "world", "how", "are", "you", "heck"]
    tree = SearchTree(words)
    print(tree.firstNThatStartWith(3, "h")) -> ['how', 'heck', 'hello']
"""


from collections import defaultdict


def inifiniteDict() -> defaultdict:
    return defaultdict(inifiniteDict)

class SearchTree:
    """
    methods:\n
        insert(word)\n
        isWord(word)\n
        isPrefix(letters)\n
        firstNThatStartWith(n, letters)\n
    """
    def insert(self, word):
        node = self.root
        for letter in word:
            node = node[letter]
        node['word'] = word

    def __init__(self, initialWords=[]):
        """
        param: initialWords - (optional) list of words to load initially
        """
        self.root = inifiniteDict()
        for word in initialWords:
            self.insert(word)

    def isWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return 'word' in node
    
    def isPrefix(self, letters):
        """returns true if there is a letters that starts with param: letters"""
        node = self.root
        for letter in letters:
            if letter not in node:
                return False
            node = node[letter]
        return True
    
    def firstNThatStartWith(self, n: int, letters) -> list|bool:
        """
        param: n - the number of words you want to return\n

        
        code sample:\n
        print(tree.firstNThatStartWith(2, "h")) -> ['how', 'hey'] (gets shorter words first (breadth first search))\n
        """
        node = self.root
        for letter in letters:
            if letter not in node:
                return False
            node = node[letter]

        que = [node]
        wordsCollected = []

        while len(que) > 0:
            node = que.pop(0)
            if 'word' in node:
                wordsCollected.append(node['word'])
                if len(wordsCollected) >= n:
                    return wordsCollected
            for letter in node:
                if letter != 'word':
                    que.append(node[letter])

        return wordsCollected