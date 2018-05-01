import zipfile, os

exampleZip = zipfile.ZipFile('example.zip')
nl = exampleZip.namelist()
print(nl)
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
s = 'Compressed file is %sx smaller!' %(round(spamInfo.file_size/spamInfo.compress_size, 2))
print(s)

