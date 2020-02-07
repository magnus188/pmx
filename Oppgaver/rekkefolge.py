names = ['anders', 'bjørn', 'charles', 'david', 'erik', 'fredrik', 'georg']
i = step = 2
while len(names) > 0:
    if i >= len(names): i -= len(names)
    else:
        print(names.pop(i).capitalize() + ' removed')
        i += step

while names:
    for i in range(step):
        names.append(names.pop(0))
    print(names.pop(0))