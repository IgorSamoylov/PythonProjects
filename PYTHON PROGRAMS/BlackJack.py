import random
import time
random.seed()

while True:
    start = input('Нажмите Enter что бы начать, для выхода введите Exit \n')
    start = start.lower()
    if start != 'exit':
        deck = {'6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Валет' : 10, 'Дама' : 10, 'Король' : 10, 'Туз' : 11}
        #* {"♦","♥","♣","♠"}
       
        for i in deck:
            print(i)
        count = 0
        croupier_count = 0
        # перемешали колоду
        random.shuffle(deck)
        # переменные для крупье
        croupier_current = deck.pop()
        croupier_count += croupier_current
        print('Добро пожаловать в игру BLACK JACK ')
        print('У крупье {} очков'.format(croupier_current))
        

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
            
    else:
        break
    print('___следующий_раунд___')
