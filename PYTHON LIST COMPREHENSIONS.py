# Comprehension style

result = [x for x in range(100) if x % 2 == 0]
print(result)


# Lambda style

result = [x for x in range(100)]
result = filter((lambda x : x if x % 2 == 0 else None), result)
print(*result)



