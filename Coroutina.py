
def echo(value=None):
     print("Execution starts when 'next()' is called for the first time.")
     try:
        while True:
             try:
                 value = (yield value)
             except Exception as e:
                value = e
     finally:
         print("Don't forget to clean up when 'close()' is called.")

generator = echo(1)
print(next(generator))

#Execution starts when 'next()' is called for the first time.

print(next(generator))

print(generator.send(2))

generator.throw(TypeError, "spam")

generator.close() # Завершает выполнение "функции" генератора до последней строки
#Don't forget to clean up when 'close()' is called.
