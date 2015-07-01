# Flexible  Arguments

def arguments(*asd):
    total=0
    for a in asd:
        total+=a
    print(total)

arguments(3)
arguments(3,4,5,4,8)