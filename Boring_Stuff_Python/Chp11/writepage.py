import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
# print(res.iter_content(100000))
for chunk in res.iter_content(100000):
    # print(chunk)
    print(playFile.write(chunk))
playFile.close()

