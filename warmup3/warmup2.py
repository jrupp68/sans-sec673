#!/home/student/python-env/63/bin/python
import pyWars
d = pyWars.exercise("https://live.sec673.com:10000")
d.login('jrupp@acuity.com', 'xBogztGy7#$#BKcA')
d.question(2)
d.data(2)

def rev1half(astring):
    end = int(len(astring)/2)
    half = astring[:end]
    rev = half[::-1]
    return rev+astring[end:]

answer = rev1half('sandwich')



d.answer(rev1half(d.data(2)))