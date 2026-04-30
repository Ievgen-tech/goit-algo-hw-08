# Завдання 1 (варіант AVL)
# Алгоритм пошуку найменшого значення у AVL-дереві

from __future__ import annotations


class AVLNode:
    """Вузол AVL-дерева."""

    def __init__(self, key: int):
        self.key = key
        self.left: AVLNode | None = None   # лівий нащадок
        self.right: AVLNode | None = None  # правий нащадок
        self.height: int = 1            # висота піддерева з коренем у цьому вузлі


class AVLTree:
    """AVL-дерево — самобалансуюче двійкове дерево пошуку.

    Після кожної вставки автоматично відновлює баланс за допомогою поворотів,
    гарантуючи висоту O(log n) і часову складність O(log n) для всіх операцій.
    """

    def __init__(self):
        self.root: AVLNode | None = None

    # ------------------------------------------------------------------ #
    #  Допоміжні методи                                                    #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _height(node: AVLNode | None) -> int:
        """Повертає висоту вузла (0 для None)."""
        return node.height if node else 0

    @staticmethod
    def _balance_factor(node: AVLNode) -> int:
        """Різниця висот лівого і правого піддерев (баланс-фактор)."""
        left_h = node.left.height if node.left else 0
        right_h = node.right.height if node.right else 0
        return left_h - right_h

    def _update_height(self, node: AVLNode):
        """Перераховує висоту вузла на основі висот його нащадків."""
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # ------------------------------------------------------------------ #
    #  Повороти для відновлення балансу                                    #
    # ------------------------------------------------------------------ #

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """Правий поворот навколо вузла y."""
        x = y.left
        assert x is not None
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """Лівий поворот навколо вузла x."""
        y = x.right
        assert y is not None
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """Відновлює баланс вузла, якщо потрібно, та повертає новий корінь піддерева."""
        self._update_height(node)
        bf = self._balance_factor(node)

        # Ліво-ліво
        if bf > 1 and node.left and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)

        # Ліво-право
        if bf > 1 and node.left and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Право-право
        if bf < -1 and node.right and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)

        # Право-ліво
        if bf < -1 and node.right and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # ------------------------------------------------------------------ #
    #  Публічний інтерфейс                                                 #
    # ------------------------------------------------------------------ #

    def insert(self, key: int):
        """Вставляє новий ключ у AVL-дерево зі збереженням балансу."""
        self.root = self._insert(self.root, key)

    def _insert(self, node: AVLNode | None, key: int) -> AVLNode:
        """Рекурсивна вставка з подальшим балансуванням."""
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return self._rebalance(node)

    def find_min(self) -> int:
        """Повертає найменше значення у дереві.

        Як і в звичайному BST, мінімум знаходиться у крайньому лівому вузлі.
        Завдяки балансуванню AVL висота гарантовано O(log n).
        """
        if self.root is None:
            raise ValueError("Дерево порожнє")

        # Рухаємось вліво до кінця
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key


def find_min_value(tree: AVLTree) -> int:
    """Повертає найменше значення у переданому AVL-дереві."""
    return tree.find_min()


def print_tree(node: AVLNode | None, prefix: str = "", is_left: bool = True):
    """Рекурсивно виводить дерево у вигляді повернутого дерева (праве гілля вгорі)."""
    if node is None:
        return
    print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
    print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    avl = AVLTree()

    # Вставляємо значення у дерево
    values = [15, 10, 20, 8, 12, 17, 25, 6]
    for value in values:
        avl.insert(value)

    print("Значення у дереві:", values)
    print("\nСтруктура AVL-дерева (збалансованого):")
    print_tree(avl.root, is_left=False)
    print("\nНайменше значення в дереві:", find_min_value(avl))  # очікується: 6
