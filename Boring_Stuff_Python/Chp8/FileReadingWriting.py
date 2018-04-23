helloFile = open(r'.\Chp8\hello.txt', 'r')
helloContent = helloFile.read()
print(helloContent)
helloFile.close()

sonnetFile = open(r'.\Chp8\sonnet29.txt')
list = sonnetFile.readlines()
print(list)
sonnetFile.close()


