invest_start = int(input("How much is your base investissement?" ))  
apr = int(input("How much is Apr?"))
duration = int(input("How many day?"))
coumpound_routine = str(input("How often do you coumpound? Dayly(d), weekly(w), monthly(m), yearly(y)"))
a=-1

if coumpound_routine == "d":
    coumpound_routine_a = 365
elif coumpound_routine == "w":
    coumpound_routine_a = 56
elif coumpound_routine == "m":
    coumpound_routine_a = 12
elif coumpound_routine == "y":
    coumpound_routine_a = 1
else:
    print("Please only write:\"Dayly(d), weekly(w), monthly(m), yearly(y)\"")
    
    
    

roi_dayly = 1+apr/365/100
inv = invest_start 
dayly_compound = invest_start*apr/coumpound_routine_a/100

for n in range(0,duration):
    inv*=roi_dayly
    if n%30==0:
        a+=1
        if a==0:
            continue
        print("Au bout de "+str(a)+" mois"+", on a "+str(inv))
    inv+=dayly_compound-0.05
    

print("L'apy est de "+str(inv*100/invest_start))
    
