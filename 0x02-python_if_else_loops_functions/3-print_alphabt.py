#!/usr/bin/python3
store = ''
for each in range(97, 123):
    a = chr(each)
    if a == 'q' or a == 'e':
        pass
    else:
        store = store + a
print(store)
