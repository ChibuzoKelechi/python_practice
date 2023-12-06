# Anime characters
anime = 'Eminence in Shadow'
xter = 'Cid'
xter += "/Lord Shadow"

manga = 'Jujutsu Kaisen'
jjk_mc = 'Itadori Yuji'

jjk_characters = {
    'strongest': 'Gojo Satoru',
    'strongest2': 'Sukuna'
}

users = ['Kc', 'Victor', 'Onyii', 'Chizzy', 'Daneasy']

i = 3
print(xter)
# print((3*2) / 2 + 3)

name = ''
total = 0
for num in range(101):
    total += num
    print(total)
print(f'The total is {total}')

def divide(num):
    return 9/num

try:
    print(divide(3))
    print(divide(0))
    print(divide(9))
except ZeroDivisionError:
    print('Zero gives an error')
     