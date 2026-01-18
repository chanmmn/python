from abc import ABC, abstractmethod
from typing import List


# Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


# Concrete Strategy 1: Bubble Sort
class BubbleSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result


# Concrete Strategy 2: Quick Sort
class QuickSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        self._quick_sort(result, 0, len(result) - 1)
        return result
    
    def _quick_sort(self, arr: List[int], low: int, high: int):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)
    
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


# Concrete Strategy 3: Merge Sort
class MergeSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        self._merge_sort(result)
        return result
    
    def _merge_sort(self, arr: List[int]):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            self._merge_sort(left)
            self._merge_sort(right)
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1


# Context Class
class SortContext:
    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        """Change the sorting strategy at runtime"""
        self._strategy = strategy
    
    def execute_sort(self, data: List[int]) -> List[int]:
        """Execute the sorting using the current strategy"""
        if not self._strategy:
            raise ValueError("Strategy not set")
        return self._strategy.sort(data)


# Client Code
def main():
    # Sample data
    data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 33, 70]
    print(f"Original data: {data}\n")
    
    # Create context
    sorter = SortContext()
    
    # Use Bubble Sort
    print("Using Bubble Sort Strategy:")
    sorter.set_strategy(BubbleSort())
    result = sorter.execute_sort(data)
    print(f"Sorted: {result}\n")
    
    # Use Quick Sort
    print("Using Quick Sort Strategy:")
    sorter.set_strategy(QuickSort())
    result = sorter.execute_sort(data)
    print(f"Sorted: {result}\n")
    
    # Use Merge Sort
    print("Using Merge Sort Strategy:")
    sorter.set_strategy(MergeSort())
    result = sorter.execute_sort(data)
    print(f"Sorted: {result}\n")
    
    # Demonstrate changing strategy dynamically
    print("Demonstrating dynamic strategy change:")
    strategies = [
        ("Bubble Sort", BubbleSort()),
        ("Quick Sort", QuickSort()),
        ("Merge Sort", MergeSort())
    ]
    
    for name, strategy in strategies:
        sorter.set_strategy(strategy)
        test_data = [5, 2, 8, 1, 9]
        sorted_data = sorter.execute_sort(test_data)
        print(f"{name}: {test_data} -> {sorted_data}")


if __name__ == "__main__":
    main()
