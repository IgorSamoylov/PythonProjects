

def levenstein(A: str, B: str) -> int:
    F = [[(i + j) if i*j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    print("Базовая таблица DP. Крайние случаи:"); print_DP(F)

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])

    print("Заполненная таблица DP:"); print_DP(F)
    return F[-1][-1]

    

def print_DP(F: list):
    for i in F:
        print(i)



dist = levenstein("молоко", "колокол")
print("Результат: ", dist)

dist = levenstein("паровоз", "синхрофазатрон")
print("Результат: ", dist)


