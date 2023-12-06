import re
# read in and strip newline
cards = [re.sub('\n','',x) for x in open('input.txt').readlines()]

# PART 1
points = []
for card in cards:
    w_nos = re.search('(?<=:)[\d\s]*(?=\|)',card).group().split()
    c_nos = re.search('(?<=\|)[\d\s]*',card).group().split()
    matches = sum(no in c_nos for no in w_nos)
    if matches > 0: points.append(2**(matches - 1)) 

# solution
sum(points)

# PART 2
points = {i:1 for i in range(len(cards))}
for i, card in enumerate(cards):
    w_nos = re.search('(?<=:)[\d\s]*(?=\|)',card).group().split()
    c_nos = re.search('(?<=\|)[\d\s]*',card).group().split()
    matches = sum(no in c_nos for no in w_nos)
    for k in range(matches):
        points[i+k+1] += points[i]
        

# solution
sum(points.values())