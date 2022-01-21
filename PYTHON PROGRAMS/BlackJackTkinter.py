import random
import time
from tkinter import *

root = Tk()

lab = Label(root, bg='black', fg='white', width=150)
but_y = Button(root, text="Взять")
but_n = Button(root, text="Отказаться")






def mainlooper() :
    random.seed()
    lab['text'] = 'Добро пожаловать в игру BLACK JACK '
    
    
        #deck = {'6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Валет' : 10, 'Дама' : 10, 'Король' : 10, 'Туз' : 11}
        #* {"♦","♥","♣","♠"}
    deck = [6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
       
        #for i in deck:
        #   print(i)
    count = 0
    croupier_count = 0
        # перемешали колоду
    random.shuffle(deck)
        # переменные для крупье
    croupier_current = deck.pop()
    croupier_count += croupier_current
    time.sleep(3)   
    lab['text'] ="У крупье {} очков".join(str(croupier_current)) 
        

    while True:

        choise = input('У вас {} очков, что бы взять карту нажмите y или n что бы остановиться: '.format(count))
        choise = choise.lower()

        if choise == 'y':
            current = deck.pop()
            print('Вам попалась карта достоинством {}'.format(current))
            count += current
            if count > 21:
                print('У вас перебор. Вы проиграли, набрав {} очков'.format(count))
                break
            elif count == 21:
                print('Вы выиграли. У вас 21 очко! Просто прекрасно!')
                break
            else:
                print('')
        else:
            print('У вас {} очков, крупье берет карту: '.format(count))
                # блок добора и сравнения карт крупье
            while True:
                time.sleep(3)
                croupier_current = deck.pop()
                croupier_count += croupier_current
                print('Крупье взял еще и ему выпало {}, у крупье {}'.format(croupier_current, croupier_count))
                if croupier_count > 21:
                    print('Вы выиграли, набрав {} очков. Просто прекрасно!'.format(count))
                    break
                elif count < croupier_count <= 21:
                    print('Вы проиграли!, у вас {} у крупье {}. Казино забирает вашу ставку'.format(count, croupier_count))
                    break
                   
            break    
            

#but.bind('<Button-1>', mainloop())

but_y.pack()
but_n.pack()
lab.pack()
mainlooper()
root.mainloop()
