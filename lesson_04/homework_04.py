import re

print("\n", "Task 01")
adwentures_of_tom_sawer = '"Tom gave up the brush with reluctance in his .... face but alacrityin his heart."\n'\
    '"And while the late steamer "Big Missouri" worked .... and sweated in the sun,"\n'\
    '"the retired artist sat on a barrel in the .... shade close by, dangled his legs,"\n'\
    '"munched his apple, and planned the slaughter of more innocents."\n'\
    '"There was no lack of material; boys happened along every little while;"\n'\
    '"they came to jeer, but .... remained to whitewash. ...."\n'\
    '"By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for"\n'\
    '"a kite, in good repair; and when he played out, Johnny Miller bought"\n'\
    '"in for a dead rat and a string to swing it with—and so on, and so on,"\n'\
    '"hour after hour. And when the middle of the afternoon came, from being a"\n'\
    '"poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."\n'\
    
  
##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print(adwentures_of_tom_sawer.replace("\n", " "))


# task 02 ==
""" Замініть .... на пробіл
"""

print("\n", "Task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
print(adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print("\n", "Task 03")
print(adwentures_of_tom_sawer.replace("  ", ""))


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print("\n", "Task 04")
count_h = adwentures_of_tom_sawer.count('h')

print("The letter 'h' occurs", count_h, "times in the text.")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print("\n", "Task 05")
words = re.findall(r'\b[A-Z]\w*\b', adwentures_of_tom_sawer)
print("Number of words starting with a capital letter -", len(words))


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

print("\n", "Task 06")
position_1 = adwentures_of_tom_sawer.find("Tom")
position_2 = adwentures_of_tom_sawer.find("Tom", position_1 + 1)
print("Answer: the position at which the word Tom occurs a second time", position_2)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("\n", "Task 07")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print("\n", "Task 08")

sentence_4 = adwentures_of_tom_sawer_sentences[3].lower()
print(sentence_4)



# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

print("\n", "Task 09")
start = adwentures_of_tom_sawer.find("By the time")
print("Answer:", start)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\n", "Task 10")
sentence_5 = adwentures_of_tom_sawer_sentences[4].lower()
words_in_last_sentence = sentence_5.split()
words_in_sentence_5 = len(words_in_last_sentence)
print("Answer: the number of words in the last sentence:", words_in_sentence_5)

