n = int(input(' Enter a number : '))

new_list = []
new_list_2 = []

i = 0

while i <= n:

    new_list.append(i)
    i += 1

for j in range(n):

    if j % 2 == 0:

        new_list_2.append(j)

print(new_list)
print(new_list_2)
