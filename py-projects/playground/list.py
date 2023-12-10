import pprint
# import random
import pyperclip
interests = 'Nichijou BungouSD Jigokuraku Bleach:TYBW TomodachiGame Eminence'
watchlist = interests.split(' ')

for anime in watchlist:
    print(anime)
# print(watch_list[0])

# watch_list.append('Eminence in Shadow')
# print(watch_list[random.randint(0, len(watch_list) - 1)])

armed_agency = ['Dazai', 'Ranpo', 'Atsushi']
dazai, ranpo, tiger = armed_agency

print(ranpo)

kc = {
    'skill': 'Developer',
    'favshow': 'Anime',
    'lang': ['Javascript', 'Python']
}

for lang in kc['lang']:
    print(lang)
    
kc.setdefault('fav_color', 'black')

print(kc)
pprint.pprint(kc)

pyperclip.copy('Chizzy DG')
pyperclip.paste()