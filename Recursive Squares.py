
import graphics as gr
import time

window = gr.GraphWin("Squares", 610, 610)
alpha = 0.11

def fractal_squares(A, B, C, D, deep=10):
    if deep < 1:
        return
    for P1, P2 in (A, B), (B, C), (C, D), (D, A):
        line = gr.Line(gr.Point(*P1), gr.Point(*P2))
        line.draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha) #A1x = Ax + (Bx - Ах)*alpha
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    time.sleep(0.1)
    fractal_squares(A1, B1, C1, D1, deep - 1)

fractal_squares((10, 10), (10, 600), (600, 600), (600, 10), 100)
  
    
