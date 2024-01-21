'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.'''

def remove_duplicates(nums):
    # Manejar el caso del array vacío
    if not nums:
        return 0

    # Inicializar el puntero para la nueva longitud del array
    new_length = 1

    # Iterar sobre el array desde el segundo elemento
    for i in range(1, len(nums)):
        # Verificar si el elemento es diferente al anterior
        if nums[i] != nums[i - 1]:
            # Actualizar el array in-place y el puntero de la nueva longitud
            nums[new_length] = nums[i]
            new_length += 1

    return new_length

# Ejemplo de uso:
nums_example = [1, 1, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(nums_example)
print(length)  # Output: 5 (el array modificado es [1, 2, 3, 4, 5])


