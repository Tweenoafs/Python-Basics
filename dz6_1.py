with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    req_tuple = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for _ in req_tuple:
        print(*req_tuple, sep=',\n')

# Решение в стиле "убей ОЗУ"(начальный вариант):
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         req_tuple = (line.split()[0], line.split()[5][1:], line.split()[6])
#         print(req_tuple)
