new_list = []

for i in range(100):

    new_list.append(i)

    if i % 3 == 0 and i % 5 == 0:

        new_list[i] = 'FizzBuzz'

    elif i % 3 == 0 and i % 5 != 0:

        new_list[i] = 'Fizz'

    elif i % 5 == 0 and i % 3 != 0:

        new_list[i] = 'Buzz'


print(new_list)
