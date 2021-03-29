from sys import argv

with open('sell.csv', 'a', encoding='utf-8') as sell_a:
    with open('sell.csv', 'r', encoding='utf-8') as sell_r:
        if len(argv) > 1 and [el for el in argv[1:] if el.replace('.', '').isdigit()]:
            if len(argv) == 3:
                print(*sell_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep='\n')
            if ',' in argv[1] or '.' in argv[1]:
                sell_r.read()
                print(argv[1], file=sell_a)
            else:
                print(*sell_r.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(sell_r.read())
