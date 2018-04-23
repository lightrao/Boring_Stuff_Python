import os

e =  os.path.exists('C:\\Windows')
print(e)

e2 = os.path.exists('C:\\some_made_up_folder')
print(e2)

d1 = os.path.isdir('C:\\Windows\\System32')
print(d1)

f1 = os.path.isfile('C:\\Windows\\System32')
print(f1)

d2 = os.path.isdir('C:\\Windows\\System32\\calc.exe')
print(d2)

f2 = os.path.isfile('C:\\Windows\\System32\\calc.exe')
print(f2)
