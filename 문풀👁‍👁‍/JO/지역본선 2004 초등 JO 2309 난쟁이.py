dwarves = [ int(input()) for i in range(9)]
height = sum(dwarves)-100
def dwarf():
    global dwarves
    for i in range(8):
        for j in range(i+1,9):
            if dwarves[i]+dwarves[j]==height:
                del dwarves[j], dwarves[i]
                return dwarves.sort()
dwarf()
[ print(dwarf) for dwarf in dwarves]
