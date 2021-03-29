from json import dump
from itertools import zip_longest

with open('users_more.csv', 'r', encoding='utf-8') as u:
    with open('hobby_less.csv', 'r', encoding='utf-8') as h:

        full_list = zip_longest((" ".join(i.split(",")) for i in u), h)
        req_dict = {str(el[0]).strip(): str(el[1]).strip() for el in full_list}

        with open('req_dict.json', 'w', encoding='utf-8') as f:
            if 'None' in req_dict:
                exit(1)
            else:
                dump(req_dict, f, ensure_ascii=False)
                print(req_dict)

# Вариант для тестирования, где количество строк в users меньше чем в hobby

# from json import dump
# from itertools import zip_longest
#
# with open('users_less.csv', 'r', encoding='utf-8') as u:
#     with open('hobby_more.csv', 'r', encoding='utf-8') as h:
#
#         full_list = zip_longest((" ".join(i.split(",")) for i in u), h)
#         req_dict = {str(el[0]).strip(): str(el[1]).strip() for el in full_list}
#
#         with open('req_dict.json', 'w', encoding='utf-8') as f:
#             if 'None' in req_dict:
#                 exit(1)
#             else:
#                 dump(req_dict, f, ensure_ascii=False)
#                 print(req_dict)
