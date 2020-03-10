#%% Income-Bottom
def income_bottom(x):
    if x<=2:
        return 1
    elif x>=5:
        return 0
    else:
        return ((5-x) / (5-2))        


#%% Income-Middle
def income_middle(x):
    if x < 3 or x > 20:
        return 0
    elif x >= 3  and x <= 6:
        return (x-3) / (6-3)
    elif x >= 10 and x<= 20 :
        return ((20-x) / (20-10))
    else :
        return 1


#%% Income-High
def income_high(x):
    if x<5:
        return 0
    elif x > 15:
        return 1
    else:
        return ((x-5) / (15-5)) 
    return 0


#%% Input
x = float(input())
u_bottom = income_bottom(x)
u_middle = income_middle(x)
u_high = income_high(x)
print("%1.4f,%1.4f,%1.4f" % (u_bottom, u_middle, u_high))
