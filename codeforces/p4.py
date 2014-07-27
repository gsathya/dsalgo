ip = [int(i) for i in raw_input().split(' ')]

k = ip[0]
n1 = ip[1]
n2 = ip[2]
n3 = ip[3]
t1 = ip[4]
t2 = ip[5]
t3 = ip[6]

time = 0

washing = k
drying = 0
folding = 0

min_p = min([n1, n2, n3])
min_t = min([t1, t2, t3])

now_wash = 0
now_dry = 0 
now_fold = 0

while 1:
    while now_wash < n1:
        washing = washing - min_p
        now_wash += min_p
        time += min_t
        

    
