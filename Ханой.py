
l1 = [x + 1 for x in range(5)]
l2 = []
l3 = []

towers = [l1, l2, l3]

def move_disk(from_tower: int, to_tower: int):
    disk = towers[from_tower].pop(0)
    towers[to_tower].insert(0, disk)
    print(f'Move disk {disk} from {from_tower + 1} to {to_tower + 1}')


def hanoi(number_of_disks: int, from_tower: int, to_tower: int):
    print('Tower1',l1,'Tower2', l2,'Tower3', l3)
    if number_of_disks == 0:
        return
    tmp_tower = 3 - from_tower - to_tower
    hanoi(number_of_disks - 1, from_tower, tmp_tower)
    move_disk(from_tower, to_tower)
    hanoi(number_of_disks - 1, tmp_tower, to_tower)
    

hanoi(len(l1), 0, 1)
    
