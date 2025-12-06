import pyWars

#
# The datasample contains a list. 
# Identify all of the items that are not decendants of a string object and remove it from the list. 
# Submit a list with only children of string objects or strings
# themselves in the order they appear in the original data.
#

d = pyWars.exercise("https://live.sec673.com:10000")
d.login('jrupp@acuity.com', 'xBogztGy7#$#BKcA')
input = d.data(51)
answer = []
for item in input:
    if isinstance(item, str):
        answer.append(item)


print(len(input),input)
print(len(answer), answer)
response = d.answer(answer)
print(response)
d.logout()
exit()