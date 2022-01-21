#incorrect = 1

try:
    print(incorrect)

except Exception as e:
    
    print("Ошибка!", type(e), e)

else:
    print("Всё норм!")

finally:
    print("Пока")
