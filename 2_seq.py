def seq(pos):
    if pos%2 == 0:
        return (pos**2 - 1)
    else:
        return (pos**2 + 1)
print(seq(7))