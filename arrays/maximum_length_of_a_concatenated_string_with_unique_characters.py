'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
'''
def max_length(arr):
    def is_unique(string):
        return len(set(string)) == len(string)

    def backtrack(start, path):
        nonlocal max_len

        # Verificar si la combinación actual tiene caracteres únicos
        if is_unique(path):
            max_len = max(max_len, len(path))

        # Recorrer el array y realizar la búsqueda
        for i in range(start, len(arr)):
            backtrack(i + 1, path + arr[i])

    max_len = 0
    backtrack(0, "")
    return max_len

# Ejemplo de uso:
arr_example_1 = ["un", "iq", "ue"]
result_1 = max_length(arr_example_1)
print(result_1)  # Output: 4

arr_example_2 = ["cha", "r", "act", "ers"]
result_2 = max_length(arr_example_2)
print(result_2)  # Output: 6
