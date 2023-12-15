import re

init_strs = open("input.txt").readlines()[0].split(",")

def HASH(step):
    cv = 0
    step = re.sub('\n','',step)
    for c in step:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv

results = [HASH(step) for step in init_strs]

# solution
sum(results)

## PART 2
boxes = {i:{} for i in range(256)}

def HASHMAP(step):
    label, lens = re.split('[=-]',step)
    box = HASH(label)
    if lens == '': # <- 
        if label in boxes[box].keys():
            boxes[box].pop(label)
    else:
        boxes[box][label] = int(lens)
        
for step in init_strs:
    HASHMAP(step.rstrip("\n"))
    
# solution
sum([(1+i)*(1+p)*lens for i, (_, lenses) in enumerate(boxes.items()) for p, (_, lens) in enumerate(lenses.items())])