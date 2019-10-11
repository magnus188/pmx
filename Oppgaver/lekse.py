# create list a and b
a = [2,6,'hello',5.0, 2.5, 2, 2]
b = [4,'nei',2,'magnus', 2.5, 'hello']

# create empty lists for unique and similar objects
uniqueA = []
uniqueB = []
similar = []

# for every item in list a:
# if in both list -> append to similar array
# if not -> append to uniqueA list
for data in a:
    if (data in b and data not in similar):
        # append to similar array
        similar.append(data)
    elif (data not in uniqueA):
        # append to uniqueA list
        uniqueA.append(data)

# for every item in list b:
# if in both list and not in uniqueB
# append to uniqueB
for data in b:
    if (data not in a and data not in uniqueB):
        # append to uniqueB
        uniqueB.append(data)

print('Unique for list A:', uniqueA)
print('Unique for list B:', uniqueB)
print('Similar in both list:', similar)

        