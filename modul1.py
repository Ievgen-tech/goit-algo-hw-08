# Завдання 1
# Алгоритм пошуку найменшого значення у двійковому дереві пошуку (BST)

from __future__ import annotations


class Node:
    """Вузол двійкового дерева пошуку."""

    def __init__(self, key: int):
        self.key = key
        self.left: Node | None = None   # лівий нащадок (менше за поточний)
        self.right: Node | None = None  # правий нащадок (більше або рівне поточному)


class BinarySearchTree:
    """Двійкове дерево пошуку з ітеративними операціями вставки та пошуку мінімуму."""

    def __init__(self):
        self.root: Node | None = None  # корінь дерева; None — дерево порожнє

    def insert(self, key: int):
        """Вставляє нове значення у дерево, зберігаючи властивість BST."""
        # Якщо дерево порожнє — новий вузол стає коренем
        if self.root is None:
            self.root = Node(key)
            return

        # Ітеративно шукаємо правильну позицію для нового ключа
        current = self.root
        while True:
            if key < current.key:
                # Рухаємось ліворуч, якщо ключ менший за поточний вузол
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                # Рухаємось праворуч, якщо ключ більший або рівний поточному
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def find_min(self) -> int:
        """Повертає найменше значення у дереві.

        У BST мінімальний елемент завжди знаходиться у крайньому лівому вузлі.
        Складність: O(h), де h — висота дерева.
        """
        if self.root is None:
            raise ValueError("Дерево порожнє")

        # Рухаємось вліво, доки не дійдемо до вузла без лівого нащадка
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key


def find_min_value(tree: BinarySearchTree) -> int:
    """Повертає найменше значення у переданому дереві."""
    return tree.find_min()


def print_tree(node: Node | None, prefix: str = "", is_left: bool = True):
    """Рекурсивно виводить дерево у вигляді повернутого дерева (праве гілля вгорі)."""
    if node is None:
        return
    # Спочатку виводимо праве піддерево (відображається зверху)
    print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
    # Потім ліве піддерево (відображається знизу)
    print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    bst = BinarySearchTree()

    # Вставляємо значення у дерево
    values = [15, 10, 20, 8, 12, 17, 25, 6]
    for value in values:
        bst.insert(value)

    print("Значення у дереві:", values)
    print("\nСтруктура дерева:")
    print_tree(bst.root, is_left=False)
    print("\nНайменше значення в дереві:", find_min_value(bst))  # очікується: 6
