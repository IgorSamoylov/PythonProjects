
def moveTower(height,fromPole, toPole, withPole):
    if height > 0:
        moveTower(height-1,fromPole,withPole,toPole)
        print("moving disk from",fromPole,"to",toPole)
        moveTower(height-1,withPole,toPole,fromPole)
    #print(withPole)

moveTower(3,"A","B","C")
