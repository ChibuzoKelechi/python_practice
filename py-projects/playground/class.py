#OOP in Python
class Nigerian:
    enemy = 'Sapa'
    acc_balance = 2000.0
    
    def debit(self, debit_amt):
        self.acc_balance -= debit_amt
        return self.acc_balance

kc = Nigerian()
kc.debit(2000)
print(f'{kc.acc_balance} NGN')
 
class Lang:
    def __init__(self, rank):
        self.__rank = rank
    
    def get_rank(self):
        rank = 1
        return self.__rank

#Inheritance
class Anime:
    def __init__(self, genre, mc):
        self.genre = genre
        self.mc = mc

class Kuroko(Anime):
    def __init__(self):
        super().__init__('sport', 'Kuroko' )
    
# Polymorphism       
# class Animal:
#     def __init__(self, legs):
#         self.legs = legs

# class Human(Animal):
#     def __init__(self):
#         super().__init__(2)
        
# me = Human()

class Language:
    def framework(self):
        print('Programming languages have frameworks/Libraries')
        
class Python(Language):
    def framework(self):
        frm_work = 'Django'
        print(f'Python uses libraries like {frm_work}')

class Java(Language):
    def framework(self):
        frm_work = 'Spring'
        print(f'Java uses {frm_work}')
        # return super().framework()

lang_list = [Language(), Python(), Java()]

for lang in lang_list:
    lang.framework()