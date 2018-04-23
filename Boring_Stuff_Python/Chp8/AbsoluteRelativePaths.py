import os

j = os.path.abspath(r'.\a')
print(j)

j = os.path.isabs(r'c:\hello') 
print(j)

x =  os.path.relpath(r'c:\hello', r'.')
print(x)

j = os.path.isabs(os.path.abspath('.'))
print(j)

print(os.getcwd())

path = 'C:\\Windows\\System32\\calc.exe'
b = os.path.basename(path)
print(b)
d = os.path.dirname(path)
print(d)

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
s = os.path.split(calcFilePath)
print(s)
s2 = (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
print(s2)

print(os.path.sep)

l = calcFilePath.split(os.path.sep)
print(l)
