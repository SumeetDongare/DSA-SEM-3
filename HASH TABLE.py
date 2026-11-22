#LINERA PROBING WITHOUT REPLACEMENT 
size = 10
table = [-1] * size

n = int(input("Enter number of keys: "))
keys = list(map(int, input("Enter keys: ").split()))

for key in keys:
    index = key % size

    while table[index] != -1:
        index = (index + 1) % size

    table[index] = key

print("Hash Table:")

for i in range(size):
    print(i, ":", table[i])


#LINER PROBING WITH REPLACEMENT 
size = 10
table = [-1] * size

n = int(input("Enter number of keys: "))
keys = list(map(int, input("Enter keys: ").split()))

for key in keys:
    index = key % size

    if table[index] == -1:
        table[index] = key

    elif table[index] % size != index:
        temp = table[index]
        table[index] = key
        key = temp

        index = (index + 1) % size

        while table[index] != -1:
            index = (index + 1) % size

        table[index] = key

    else:
        index = (index + 1) % size

        while table[index] != -1:
            index = (index + 1) % size

        table[index] = key

print("Hash Table:")

for i in range(size):
    print(i, ":", table[i])
