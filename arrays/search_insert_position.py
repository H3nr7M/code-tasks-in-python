'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2'''

def search_insert(nums, target):
    # Inicializar punteros para búsqueda binaria
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Verificar si el elemento en el medio es igual al objetivo
        if nums[mid] == target:
            return mid
        # Si el elemento en el medio es menor, buscar en la mitad derecha
        elif nums[mid] < target:
            left = mid + 1
        # Si el elemento en el medio es mayor, buscar en la mitad izquierda
        else:
            right = mid - 1

    # Si el objetivo no está presente, devolver el índice donde se insertaría
    return left

# Ejemplo de uso:
nums_example = [1, 3, 5, 6]
target_example = 5
result = search_insert(nums_example, target_example)
print(result)  # Output: 2
