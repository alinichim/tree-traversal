import tree


class TestTree:
    def test_find(self):
        t_tree = tree.Tree()
        t_tree.add(10)
        t_tree.add(8)
        t_tree.add(9)
        t_tree.add(16)

        assert t_tree._find(5, t_tree.root) is None

        node = t_tree._find(9, t_tree.root)
        assert node is not None
        assert node.data == 9
