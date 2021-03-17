s = input()
if 'f' in s: 
    if s.find('f') != len(s) - 1 - s[::-1].find('f'):
        print(s.find('f'), len(s) - 1 - s[::-1].find('f'))
    else:
        print(s.find('f'))
