"""
code sample:
    words = ["hello", "world", "how", "are", "you", "heck"]
    tree = SearchTree(words)
    print(tree.firstNThatStartWith(3, "h")) -> ['how', 'heck', 'hello']
    github link: https://github.com/shmulisarmy/search-tree-data-structure
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
    def __init__(self, initialWords=[]):
        """
        param: initialWords - (optional) list of words to load initially
        """
        self.root = inifiniteDict()
        for word in initialWords:
            self.__iadd__(word)

    def __iadd__(self, word):
        node = self.root
        for letter in word:
            node = node[letter]
        node['word'] = word
        return self

    

    def isWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return 'word' in node
    
    def __contains__(self, letters):
        """returns true if there is a letters that starts with param: letters"""
        node = self.root
        for letter in letters:
            if letter not in node:
                return False
            node = node[letter]
        return True
    
    def __getitem__(self, args) -> list:
        try:
            searchString, maxResults = args
        except:
            raise TypeError("expected 2 arguments, search string and the max number of results")
        """        
        code sample:\n
        does a a breadth first search starting from where ever the search string takes us into the tree\n
        print(tree.__getitem__(2, "h")) -> ['how', 'hey'] (gets shorter words first (breadth first search))\n
        """
        node = self.root
        for letter in searchString:
            if letter not in node:
                return False
            node = node[letter]

        que = [node]
        wordsCollected = []

        while len(que) > 0:
            node = que.pop(0)
            if 'word' in node:
                wordsCollected.append(node['word'])
                if len(wordsCollected) >= maxResults:
                    return wordsCollected
            for letter in node:
                if letter != 'word':
                    que.append(node[letter])

        return wordsCollected
    

    def getAllWords(self):
        node = self.root
        que = [node]
        wordsCollected = []

        while len(que) > 0:
            node = que.pop(0)
            if 'word' in node:
                wordsCollected.append(node['word'])
            for letter in node:
                if letter != 'word':
                    que.append(node[letter])

        return wordsCollected
    

    def __repr__(self): 
        return f"""
                this is a search tree that contains 
                {len(self.getAllWords())} words all of wich can be displayed 
                with .display() or queried for with [] syntax 
                (eg tree['h', 3] -> ['how', 'heck', 'hello'])
                """

    def display(self):
        node = self.root
        que = [node]
        wordsCollected = []

        while len(que) > 0:
            node = que.pop(0)
            if 'word' in node:
                wordsCollected.append(node['word'])
            for letter in node:
                if letter != 'word':
                    que.append(node[letter])

        print("************Search Tree************")
        print("words: ", len(wordsCollected))
        print(*wordsCollected, sep=", ")
  