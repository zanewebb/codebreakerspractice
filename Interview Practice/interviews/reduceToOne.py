'''
input int

break down int to number 1 in least amount of steps possible

operations available,
    divide by 3
    divide by 2
    subtract by 1
    
step = 1 operations


input 3
output 1 --> 3 / 3 = 1

input 6 
out 2 --> 6 / 3 = 2 - 1 = 1


input 24    24
        8   12 
        4   4
        2   2
        1   1
        
input 33


input 10   10
       5   9
       4   3
       2   1
       1  

'''

# 10

# input - 1

# if can divide by 3
    # input / 3
    
# if can divide by 2
    # input / 2
    
# 9, x , 5

# cache [n+1]
# cache [0, 0 , 1, 1, 2]
         0  1   2  3  4
         
# 4/2 =cache[2] + 1
# 4-1 =cache[3] + 1
# answer = min()
def main(mainnum):
    # curnum : min steps
    tried = [0] * mainnum + 1
    #tried[0] = tried[1] = 0
    #tried[3] = tried[2] = 1
    # [n-1] = 
    # 
    # [0, 0, 1, 1, min(tried[4/2] + 1, tried[4-1] + 1), ] 
    
    
    for i in range(2, mainnum+1):
        div3 = 999999
        if i % 3 == 0:
            div3 = tried[i/3] + 1
        div2 = 999999
        if i % 2 == 0:
            div2 = tried[i/2] + 1
        sub1 = 999999
        if i - 1 >= 0:
            sub1 = tried[i-1] + 1
        
        tried[i] = min(sub1, div2, div3)
    
    return tried[mainnum]

    def investigate(num, steps):
        # base case
        if num == 1:
            return steps
        
        # recursive cases
        div3 = 99999999999
        if num % 3 == 0:
            div3 = min(investigate(num/3, steps + 1))
        
        div2 = 99999999999
        if num % 2 == 0:
            div2 = min(investigate(num/2, steps + 1))
        
        return min(investigate(num - 1, steps + 1), div3, div2)


    investigate(mainnum)
    
# 1 -> 0
# 2 -> 1
# 3 -> 1
    
    def investigate2(num):
        # 4
        # 4 / 2 
        
        []
        []
        []










