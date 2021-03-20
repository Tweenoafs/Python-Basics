duration = 1000000000
# duration = 53
# duration = 153
# duration = 4153
# duration = 400153
seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 3600 % 24
days = duration // 86400 % 7
weeks = duration // 604800 % 4
months = duration // 2629743 % 12
years = duration // 31556926

print(years, 'г', months, 'мес', weeks, 'нед', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
