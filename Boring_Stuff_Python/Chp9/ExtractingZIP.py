
import zipfile, os

exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall('exampleExtra')
exampleZip.extract('spam.txt', '.\\spamTxt')
exampleZip.close()

