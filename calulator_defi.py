print("Create by @familybubu#2154")
invest_start = int(input("How much is your base investissement?"))
apr = int(input("How much is Apr?"))
duration = int(input("How many day?"))
compound_routine = str(input("How often do you coumpound? Dayly(d), weekly(w), monthly(m), yearly(y)"))
if compound_routine == "d":
    coumpound_routine_a = 365
elif compound_routine == "w":
    coumpound_routine_a = 48
elif compound_routine == "m":
    coumpound_routine_a = 12
elif compound_routine == "y":
    coumpound_routine_a = 1
else:
    print("Please only write:\"Dayly(d), weekly(w), monthly(m), yearly(y)\"")

transaction_fee = float(input("How much are fees for transaction?"))
token_price_change = int(input("How much do you think the token price will change? +xx or -xx(in %) "))
apr_change_by_month = int(input("How much will APR decrease by month?"))

a = -1
fee_total = 0

roi_dayly =  apr / 365 / 100
inv = invest_start
percent_compound = apr / coumpound_routine_a / 100
dayly_compound = invest_start * percent_compound
gain=0
for n in range(0, duration):
    gain += inv * apr / 365 / 100
    if n % 30 == 0:
        a += 1
        if a == 0:
            aaaaaa=3

        else:
            if apr>0:
                apr -= apr_change_by_month
            roi_dayly = 1 + apr / 365 / 100
            print("The " + str(a) + " month" + ", we have " + str(round(inv, 2))+" lock and a gain of "+str(gain))
    if compound_routine == "d":
        inv += gain
        fee_total += transaction_fee
        gain=0
    elif compound_routine == "w":
        if n % 7 == 0 and n != 0:
            inv += gain
            fee_total += transaction_fee
            gain = 0
    elif compound_routine == "m":
        if n % 30 == 0 and n != 0:
            inv += gain
            fee_total += transaction_fee
            gain = 0
    elif compound_routine == "y":
        if n % 365 == 0 and n != 0:
            inv += gain
            fee_total += transaction_fee
            gain = 0
inv+=gain
print("At the end of the select period you will have " + str(round(inv, 2)) + ",minus " + str(
    round(fee_total, 2)) + " transaction fee,so a benefic of " + str(round(inv - invest_start - fee_total, 2)))
print("L'apy est de " + str(round(inv * 100 / invest_start-100, 2)))
aaa = inv - invest_start - fee_total
if token_price_change < 0:
    aaaa = aaa * (100 + token_price_change) / 100
else:
    token_price_change = str(token_price_change)
    token_price_change = token_price_change.replace("+", "")
    token_price_change = int(token_price_change)
    aaaa = aaa * (100 + token_price_change) / 100
print("With the token price change,your benefic will be " + str(round(aaaa, 2)))

