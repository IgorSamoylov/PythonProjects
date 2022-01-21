

def speak(text):
    def whisper(t):
        result = t.lower() + "..."
        return result
    return whisper(text)

print(speak("Привет"))

# Напрямую вложенную функцию вызвать невозможно, поскольку она существует только
#в контексте внешней функции и может быть вызвана только ею

#whisper("Йоу")  wrong!

#speak.whisper("Йоу")  wrong!


# Данная функция возвращает одну из своих вложенных функций, но не вызывает её!
def speak(volume):
    def whisper(text):
        result = text.lower() + "..."
        return result
    def yell(text):
        result = text.upper() + "!!!"
        return result
    if volume < 0.5:
        return whisper
    else:
        return yell

print(speak(0.7) ('Привет!') ) # Вызов возвращенной функции осуществляется здесь 
    


# Здесь функции whisper и yell имеют лексическое замыкание в контексте внешней функции
def speak(volume, text):
    def whisper():
        result = text.lower() + "..."
        return result
    def yell():
        result = text.upper() + "!!!"
        return result
    if volume < 0.5:
        return whisper
    else:
        return yell

print(speak(0.1, 'Привет замыкание!') () ) # Здесь происходит вызов возвращенной функции ()
print(speak(0.9, 'Привет замыкание!') () )

# Фуекция возвращает вложенные функции-сумматоры, помнящие свой контекст при создании
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))
