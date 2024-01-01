import re

input_data = [x.rstrip('\n') for x in open("input.txt").readlines()]

workflows = {}
parts= []
for x in input_data:
    if re.match("^[a-z]",x):
        wf_name = re.sub("\{.*\}$","",x)
        workflows[wf_name] = re.findall('(?<=\{).+(?=\})',x)[0].split(",")
    elif re.match("^\{",x):
        parts.append(re.findall("[0-9]+",x))
        
CATS = {'x':0,'m':1,'a':2,'s':3}

def is_cond(cond):
    return(len(re.findall(":",cond)) > 0)

# evaluate single condition
def evaluate(cond_str, part):
    if not is_cond(cond_str):
        return cond_str
    
    cond = re.sub(":[a-zA-Z]*","", cond_str)
    ans = re.sub(".*:","", cond_str)
    
    cond_d = part[CATS[cond[0]]]
    cond_c = cond[1:]
    
    answer = eval(cond_d + cond_c)
    
    if answer:
        return ans
    else:
        return False
  
# evaluate entire workflow until new condition found  
def eval_workflow(workflow, part):
    i = 0
    answer = False
    while not answer and i < len(workflow):
        answer = evaluate(workflow[i], part)
        i += 1
    return answer
        
# main loop        
accepted = []
for p in parts:
    answer = 'in'
    while answer not in ['A','R']:
        answer = eval_workflow(workflows[answer], p)    
    
    if answer == 'A':
        accepted.append(p)
        
# solution
sum([int(y) for x in accepted for y in x])