from Stack import Stack

def brace_sequence_correct(s: str) -> bool:
    stack = Stack()

    for token in s:
        if not token in '[()]':  # Сразу пропускаем не-скобочные символы
            continue
        if token in '[(':       # Если скобка открывающая - добавляем в стек
            stack.push(token)
        else:
            assert token in '])', 'Ахтунг! Скобка должна быть закрывающей'
            left_brace = stack.pop()
            assert left_brace in '[(', 'Ахтунг! Скобка должна быть открывающей!'
            right_brace = ''
            if left_brace == '[':
                right_brace = ']'
            else:
                right_brace = ')'
            if not token == right_brace:
                return False
    return stack.is_empty()

import doctest
def _test():
    """
    >>> brace_sequence_correct('[[(())]] []')
    True
    >>> brace_sequence_correct('[(])')
    False
    >>> brace_sequence_correct('[')
    False
    >>> brace_sequence_correct('')
    True
    >>> brace_sequence_correct('[(456, 45), (34, 87), [(2323,1,32),(232,2,1,1)]]')
    True
    >>> brace_sequence_correct('(456+255)*(7098-98)/2')
    True
    >>> brace_sequence_correct('((878 + 9] * [979 - 78))')
    False
    """
    pass

doctest.testmod(verbose=True) # Запускает все тесты, находящиеся в док-строках всех функций



