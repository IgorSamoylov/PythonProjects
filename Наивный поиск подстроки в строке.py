
def equal_strings(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if i == len(B) or A[i] != B[i]:
            return False
    return True

def search_substring(s: str, sub: str):
    if len(sub) > len(s):
        raise ValueError("Подстрока не должна быть длиннее строки!")
    for i in range(0, len(s) - len(sub) + 1):
        if equal_strings(s[i : i + len(sub)], sub):
            print("Индекс начала подстроки в строке: ", i)


search_substring("tertertertertberbterbert", "te")
