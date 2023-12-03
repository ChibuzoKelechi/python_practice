bucket_list = []

def add_item(item):
    bucket_list.append(item)

def take_item(num): 
    for x in range(num):
        list_item = input("You want? ")
        add_item(list_item)
    
    

# if __name__ == '__main__':
def list_func():
    list_len = int(input("List length? "))
    take_item(list_len)
    for item in bucket_list:
        print(item)

list_func()