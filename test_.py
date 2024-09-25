from searchTree import SearchTree


def test_find_and_breadth_first():
    words = ["hello", "world", "how", "are", "you", "heck"]
    tree = SearchTree(words)
    tree += "heops"
    assert tree["h", 3] == ['how', 'heck', 'hello']


def test_that_display_does_not_break():
    words = ["hello", "world", "how", "are", "you", "heck"]
    tree = SearchTree(words)
    tree += "heops"
    tree.display()


def test_in():
    words = ["hello", "world", "how", "are", "you", "heck"]
    tree = SearchTree(words)
    tree += "heops"
    assert "wo" in tree
    assert "h" in tree
    assert "ar" in tree

    assert not "po" in tree
