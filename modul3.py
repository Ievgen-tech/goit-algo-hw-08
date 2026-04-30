# Завдання 3
# Мінімальні витрати на об'єднання кабелів за допомогою купи (min-heap)

import heapq


def min_cost_connect_cables(cables: list[int]) -> int:
    """Обчислює мінімальні витрати на послідовне об'єднання всіх кабелів.

    Алгоритм (жадібний + min-heap):
      1. Помістити всі кабелі у мінімальну купу.
      2. Поки в купі більше одного кабелю:
         - Витягти два найкоротших кабелі.
         - З'єднати їх: витрати = сума їхніх довжин.
         - Додати новий кабель назад у купу.
         - Накопичити витрати.
      3. Повернути загальні витрати.

    Складність: O(n log n), де n — кількість кабелів.
    """
    if len(cables) <= 1:
        return 0  # порожній список або один кабель — з'єднувати нічого

    # Будуємо мінімальну купу з усіх кабелів
    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        # Витягуємо два найкоротших кабелі
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        # Витрати на з'єднання = сума їхніх довжин
        cost = first + second
        total_cost += cost

        # Новий об'єднаний кабель повертаємо у купу
        heapq.heappush(heap, cost)

    return total_cost


def _print_steps(cables: list[int]) -> None:
    """Демонструє покроковий порядок з'єднань кабелів."""
    heap = cables[:]
    heapq.heapify(heap)
    step = 1
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        print(f"  Крок {step}: {first} + {second} = {cost}")
        heapq.heappush(heap, cost)
        step += 1


if __name__ == "__main__":
    def main():
        input_cables = [4, 3, 2, 6]

        print("Довжини кабелів:", input_cables)
        print("Порядок з'єднань (від найменших до найбільших):")
        _print_steps(input_cables)

        result = min_cost_connect_cables(input_cables)
        print(f"\nМінімальні загальні витрати: {result}")

    main()
