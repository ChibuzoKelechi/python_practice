# Initial variables
field = input('What field are you venturing into?:  ')
libraries = {
    "AI/ML": ['PyTorch', 'TensorFlow', 'SciKitLearn', 'Keras'],
    "web": ['Django', 'Flask', 'FastAPI'],
    "data": ['NumPy', 'Matplotlib', 'Pandas']
}

others = ['Pyscript', 'Pygame', 'etc']

libs = []

# Checking field of development and assigning/outputting recommended libraries 
if field == 'AI/ML':
    libs = libraries['AI/ML']
elif field == 'data':
    libs = libraries['data']
elif field == 'web':
    libs = libraries['web']
else: 
    libs = others 

req_libs = ', '.join(str(x) for x in libs)

# Function that prints out suggested python libraries based on previous condition
def suggest_libs():
    if libs == others:
        print('Check out other awesome Python libraries like ' + req_libs)
    else:
        print('You will need the following libraries: ' + req_libs)


# suggest_libs()


# Function that prints out text file  
py_text = open('py-projects/playground/me.txt')
print(type(py_text))

myfile = 'py-projects/playground/me.txt'
with open(myfile, 'r') as file:
    content = file.read()

print(content)