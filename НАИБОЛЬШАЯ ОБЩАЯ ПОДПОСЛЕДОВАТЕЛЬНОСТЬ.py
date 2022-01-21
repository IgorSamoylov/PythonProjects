"""Leetcode 1143. Longest Common Subsequence"""
import random

A = [random.randint(0, 100) for m in range(100)]
B = [random.randint(0, 100) for n in range(100)]

print(A)
print(B)

def lcs(A: list, B: list):
    """Возвращает длину наибольшей общей подпоследовательности"""
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    print(F)
    restore_answer(A, B, F)
    return F[-1][-1]

def restore_answer(A, B, F: list):
    """По массиву динамического программирования восстанавливает искомую последовательность"""
    Ans = []
    i = len(A)
    j = len(B)
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            Ans.append(A[i - 1])
            i -= 1
            j -= 1
        elif F[i - 1][j] == F[i][j]:
            i -= 1 
        else: 
            j -= 1 
    Ans = Ans[::-1]
    print(Ans)


print(lcs(A, B))
