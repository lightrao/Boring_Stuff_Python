spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)
spam.sort(key=str.lower) #sort the values in regular alphabetical order
print(spam)