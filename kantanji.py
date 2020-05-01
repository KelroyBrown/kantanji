#! python3
# kantanji.py - Kanji readings and stoke counts from a list with data

from kanjilist import *

num = 0

while num < len(kanji1):
    print(kanji1[num][0] + ' means ' + kanji1[num][1] + ' and has ' + kanji1[num][2] + ' stroke(s)\n' + 'Kun reading(s) ' + kanji1[num][3] + '\nOn reading(s) ' + kanji1[num][4])
    print('#Japanese #JLPT #日本語 #漢字')
    print('\n')
    num += 1
    if num == len(kanji1):
        print ('all ' + str(num) + ' Kanji printed')


##https://automatetheboringstuff.com/
##https://automatetheboringstuff.com/2e/chapter9/ - quiz idea base
##https://en.wikipedia.org/wiki/Ky%C5%8Diku_kanji#First_grade_(80_kanji)
##http://www.kanji-a-day.com/
##https://www.kanjireview.com/
##https://www.japandict.com/
##https://jisho.org/
