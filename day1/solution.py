input_data = open('input.txt').read().split('\n')[:-1] # remove last \n

nums = '0123456789'

## Part 1
cal_vals_p1 = []
for inpt in input_data:
    l_s = r_s = "empty"
    i = 0
    # continue until both nums found
    while l_s == "empty" or r_s == "empty":
        # only rewrite if empty
        if inpt[i] in nums and l_s == "empty": 
            l_s = inpt[i]
        
        if inpt[-i-1] in nums and r_s == "empty":
            r_s = inpt[-i-1]
        i +=1
    cal_vals_p1.append(int(l_s + r_s))

# solution
sum(cal_vals_p1)

## Part 2
cal_vals_p2 = []
num_strs = ['one','two','three','four','five','six','seven','eight','nine']

for inpt in input_data:
    l_s = r_s = "empty"
    i = 0
    # continue until both nums found
    while l_s == "empty" or r_s == "empty":
        # only rewrite if empty
        if l_s == "empty": 
            if inpt[i] in nums: # check first if numeric
                l_s = inpt[i]
            else:
                for j in range(len(num_strs)): # loop through num strings
                    if inpt[i:].startswith(num_strs[j]):
                        l_s = str(j+1) # num is index + 1
        
        if r_s == "empty":
            if inpt[-i-1] in nums:
                r_s = inpt[-i-1]
            else:
                for j in range(len(num_strs)): # loop through num strings
                    if inpt[-i-1:].startswith(num_strs[j]):
                        r_s = str(j+1) # num is index + 1
        i +=1
    cal_vals_p2.append(int(l_s + r_s))

sum(cal_vals_p2)