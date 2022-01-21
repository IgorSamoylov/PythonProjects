
notes0 = {'C':131,'D':148,'E':165,'F':175,'G':196,'A':220,'B':247} 
notes = {'C':262,'D':294,'E':330,'F':349,'G':392,'A':440,'B':494}
notes2 = {'C':523}
registr = {0:notes0, 1:notes, 2:notes2}
length = {'S':350, 'L':700, 'X':1400}


import numpy as np
import simpleaudio as sa

def play_note(frequency, length):
    #frequency = 440  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 1 #length / 1000  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, length, int(length * fs / 1000), False)

    # Generate a sine wave with frequency
    note = np.sin(frequency * t * 2 * np.pi / 1000)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()



def play(st):
    reg = 1
    leng = 'S'
    for note in st:
        print(note)
        if note == '0':
            reg = 0
        elif note == '1':
            reg = 1
        elif note == '2':
            reg = 2
        elif note == 'L':
            leng = 'L'
        elif note == 'S':
            leng = 'S'
        elif note == 'X':
            leng = 'X'
        else:
            play_note(registr[reg][note],length[leng])
    
import threading


def melody():
    while True:
        play('LGSEELGSEEGFEDXC')
        play('LA2SC1ALGSEELGFEXC')
        play('LA2SC1ALGSEELGFEXC')

def accomp():
    while True:
        play('0XCCCCCCCCC')
        play('0XCCCCCCCCC')
        play('0XGGGGGGGGG')
        
threading.Thread(target=melody).start()
threading.Thread(target=accomp).start()



#winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
