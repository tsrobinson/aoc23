import re

sequences = [re.sub('\n','', x).split() for x in open('input.txt').readlines()]

# PART 1

new_numbers = []
for seq in sequences:
    seq_list = [[int(x) for x in seq]]
    while(set(seq_list[-1]) != {0}):
        seq_list.append([seq_list[-1][i+1]-seq_list[-1][i] for i in range(len(seq_list[-1])-1)])

    for i in range(len(seq_list)-2,-1, -1):
        seq_list[i].append(seq_list[i][-1] + seq_list[i+1][-1])
    new_numbers.append(seq_list[0][-1])

# solution
sum(new_numbers)

# PART 2
new_numbers = []
for seq in sequences:
    seq_list = [[int(x) for x in seq]]
    while(set(seq_list[-1]) != {0}):
        seq_list.append([seq_list[-1][i+1]-seq_list[-1][i] for i in range(len(seq_list[-1])-1)])

    for i in range(len(seq_list)-2,-1, -1):
        seq_list[i].insert(0,seq_list[i][0] - seq_list[i+1][0])
    new_numbers.append(seq_list[0][0])

# solution
sum(new_numbers)