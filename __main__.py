from searchTree import SearchTree

if __name__ == "__main__":
    words = ["hello", "world", "how", "are", "you", "heck"]
    tree = SearchTree(words)
    tree += "heops"
    print(tree["h", 3]) #-> ['how', 'heck', 'hello']
    print("wo" in tree) #-> True because world is in the tree
    tree.display()
    print(tree)


