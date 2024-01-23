'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].'''

def plus_one(digits):
    # Inicializar un acarreo para la suma
    carry = 1

    # Iterar sobre el array desde el final
    for i in range(len(digits) - 1, -1, -1):
        # Sumar el dígito actual y el acarreo
        total = digits[i] + carry

        # Calcular el nuevo dígito y acarreo
        digits[i] = total % 10
        carry = total // 10

    # Si hay un acarreo restante, agregarlo al principio del array
    if carry:
        digits.insert(0, carry)

    return digits

# Ejemplo de uso:
digits_example = [1, 2, 3]
result = plus_one(digits_example)
print(result)  # Output: [1, 2, 4]

