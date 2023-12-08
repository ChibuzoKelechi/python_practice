nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fibonacci_output = []

def add_adj_nums():
    fs_value = nums[0] + nums[1]
    fibonacci_output.append(fs_value)

    
def fibonnaci():
    fibonacci_output.append(nums[1])
    while len(nums) > 1:
        add_adj_nums()
        del nums[0]
        
fibonnaci()

for fs_num in fibonacci_output:
        print(fs_num)