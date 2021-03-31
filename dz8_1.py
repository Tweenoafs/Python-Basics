import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<user>([\w]+))@(?P<addr>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f'Некорректный почтовый адрес: {email_address}')
    print(re_email.match(email_address).groupdict())


try:
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
except ValueError as error:
    print(error)
