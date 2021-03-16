from requests import get, utils

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(unicode):
    string = response.split('Valute ID=')
    for el in string:
        if unicode.upper() in el:
            return float(el.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print('***Работа из файла***\n')
    print(type(currency_rates('USD')))
    print(currency_rates('uSd'))
    print(currency_rates('eur'))
    print(currency_rates('GbP'))
    print(currency_rates('Dog'))
else:
    print('***Работа через подключаемый модуль***\n')
