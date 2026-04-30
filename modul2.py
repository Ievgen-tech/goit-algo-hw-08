# Завдання 2
# Алгоритм пошуку суми всіх значень у двійковому дереві пошуку (BST)

from __future__ import annotations


class Node:
    """Вузол двійкового дерева пошуку."""

    def __init__(self, key: int):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    """Двійкове дерево пошуку з операціями вставки та підрахунку суми."""

    def __init__(self):
        self.root: Node | None = None

    def insert(self, key: int):
        """Вставляє значення у BST, зберігаючи властивість дерева пошуку."""
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def sum_values(self) -> int:
        """Повертає суму всіх значень у дереві."""
        return self._sum_subtree(self.root)

    def _sum_subtree(self, node: Node | None) -> int:
        """Рекурсивно обчислює суму значень піддерева з коренем у node."""
        if node is None:
            return 0
        return node.key + self._sum_subtree(node.left) + self._sum_subtree(node.right)


def sum_tree_values(tree: BinarySearchTree) -> int:
    """Повертає суму всіх значень у переданому дереві."""
    return tree.sum_values()


def print_tree(node: Node | None, prefix: str = "", is_left: bool = True):
    """Рекурсивно виводить дерево у вигляді повернутого дерева (праве гілля вгорі)."""
    if node is None:
        return
    print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
    print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [15, 10, 20, 8, 12, 17, 25, 6]

    for value in values:
        bst.insert(value)

    print("Значення у дереві:", values)
    print("\nСтруктура дерева:")
    print_tree(bst.root, is_left=False)
    print("Сума всіх значень у дереві:", sum_tree_values(bst))  # очікується: 113
