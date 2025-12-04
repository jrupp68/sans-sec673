import pyWars

d = pyWars.exercise("https://live.sec673.com:10000")
d.login('jrupp@acuity.com', 'xBogztGy7#$#BKcA')
input = d.data(47)

raw_bytes = input.encode('latin1')
utf_8 = raw_bytes.decode('utf-8')
print(utf_8)
response = d.answer(utf_8)
print(response)
d.logout()
exit()
