import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
dogs = ['a', 'b', 'c', 'd']
shelfFile['cats'] = cats
shelfFile['dogs'] = dogs
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
cats = shelfFile['cats']
print(cats)
dogs = shelfFile['dogs']
print(dogs)
shelfFile.close()

shelfFile = shelve.open('mydata')
l1 = list(shelfFile.keys())
print(l1)
l2 = list(shelfFile.values())
print(l2)



