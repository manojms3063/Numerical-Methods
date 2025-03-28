def f(x):
    return 4.905*x**2-15*x+5

interval1 = 0
for u in range(-5,5):
    for v in range(-5,5):
        if f(u)*f(v) < 0 and abs(v-u) ==1:
            print(f"the interval is:{u,v}")
            interval1 = 1
            break
    if interval1:
        break       
a=u
b=v
