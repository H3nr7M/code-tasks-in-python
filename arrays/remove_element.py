'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.'''
def remove_element(nums, val):
    # Inicializar el puntero para la nueva longitud del array
    new_length = 0

    # Iterar sobre el array
    for num in nums:
        # Verificar si el elemento es diferente al valor a eliminar
        if num != val:
            # Actualizar el array in-place y el puntero de la nueva longitud
            nums[new_length] = num
            new_length += 1

    return new_length

# Ejemplo de uso:
nums_example = [3, 2, 2, 3]
val_example = 3
new_length = remove_element(nums_example, val_example)
print(new_length)  # Output: 2 (el array modificado es [2, 2])

