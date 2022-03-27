import random


def encoder(s: str) -> str:
    if len(s) < 2:
        return s
    if len(s) == 2:
        return "".join(random.sample(s, k=2))

    div = random.randint(0, len(s))
    a = s[:div]
    b = s[div:]
    result = [encoder(a), encoder(b)]
    random.shuffle(result)
    return "".join(result)

    

def is_encoded(test_str: str, enc_str: str) -> bool:
    if len(s) < 2:
        if test_str == enc_str:
            return True
        else:
            return False
    
    for i in range(len(s)):
        a = test_str[:i]
        b = test_str[i:]
        if all([])
        
        
    return False



for i in range(10):
    test_str = "".join([chr(random.randint(65, 90)) for x in range(random.randint(5, 15))])
    print("Test string: ", test_str)
    enc_str = encoder(test_str)
    print("Encoded string: ", enc_str)
    is_enc = is_encoded(test_str, enc_str)
    print("Is encoded" if is_enc else "Is not encoded")
