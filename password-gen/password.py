import random 

char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklknopqrstuvwxyz123457865890!@#$"

char_list = list(char_set)

key_len = int(input("Preffered key length? "))
def pass_gen(len):
    randomword = [random.choice(char_list) for f in range(len)]
    print("".join(randomword))
    
pass_gen(key_len)