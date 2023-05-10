import os

cwd = os.getcwd()

#for i in range(100):
#    os.mkdir(f'hello_{i}')

for i in range(100):
    os.system(f'cp hello/__init__.py hello/test_hello.py hello_{i}')
