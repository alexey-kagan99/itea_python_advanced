def bank(dep, years, percent):

    result = dep*(1+percent/100) ** years

    return result

sum_dep = int(input(' Enter start sum please : '))
percents = int(input(' Enter percents please : '))
time = int(input(' Enter amount of years please : '))


print(bank(sum_dep, percents, time))
