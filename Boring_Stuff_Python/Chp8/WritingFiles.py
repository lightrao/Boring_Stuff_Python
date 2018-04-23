baconFile = open(r'.\Chp8\bacon.txt', 'w')
baconFile.write('Hello world!\n')

baconFile.close()
baconFile = open(r'.\Chp8\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open(r'.\Chp8\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
