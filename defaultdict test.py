from collections import defaultdict

def default_giver():
    return 777


dd = defaultdict(default_giver)

print(dd["CAT"])
print(dd)
