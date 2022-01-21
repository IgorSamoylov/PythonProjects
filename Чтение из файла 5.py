
with open("input_6_2_4.txt", "r") as f:
    big_str = f.read()

rev_big_str = big_str[::-1]

with open("result.txt", "w") as f:
    f.write(rev_big_str)
