value = True
str_one = input()
if len(str_one) != 5:
    print('Error')
    exit()
else:
    if str_one[0] != '*' or str_one [1] == '*' \
    or str_one[2] == '*' or str_one[3] == '*' or str_one[4] != '*':
        value = False

str_one = input()
if len(str_one) != 5:
    print('Error')
    exit()
else:
    if str_one[0] != '*' or str_one[1] != '*' \
    or str_one[2] == '*' or str_one[3] != '*' or str_one[4] != '*':
        value = False

str_one = input()
if len(str_one) != 5:
    print('Error')
    exit()
else:
    if len(str_one) != 5 or str_one[0] != '*' or str_one[1] == '*' \
    or str_one[2] != '*' or str_one[3] == '*' or str_one[4] != '*':
        value = False
print(value)
