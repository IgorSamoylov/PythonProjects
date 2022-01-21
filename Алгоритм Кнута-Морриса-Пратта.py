

def prefix_function(s: str) -> list:
    """ Вычисляет DP массив - префикс функцию переданной строки"""
    pi = [0] * len(s)
    for i in range(1, len(s)):
        prefix_length = pi[i - 1]

        while prefix_length > 0 and s[i] != s[prefix_length]:
            prefix_length = pi[prefix_length - 1]

        if s[i] == s[prefix_length]:
            pi[i] = prefix_length + 1
        else:
            pi[i] = prefix_length

    return pi

def find_substring(s: str, sub: str):
    """Находит все включения подстроки в строку, используя префикс-функцию"""
    pi = prefix_function(sub + '#' + s)
    size = len(sub)
    for i in range(0, len(s)):
        if pi[size + 1 + i] == size:
            begin_index = i - size + 1
            end_index = i
            print(f'Подстрока найдена в s[{begin_index}..{end_index}]')
