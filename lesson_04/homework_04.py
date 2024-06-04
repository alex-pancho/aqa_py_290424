adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adwentures_of_tom_sawer)

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

#task 01. Вирішення
replacing_var = adwentures_of_tom_sawer.replace('\n', ' ')
print(replacing_var)

# task 02 ==
""" Замініть .... на пробіл

"""

#task 02. Вирішення
repl_dots = adwentures_of_tom_sawer.replace('....', ' ')
print(repl_dots)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

#task 03. Вирішення
one_space = repl_dots.split()
print(' '.join(one_space))

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
#task 04. Вирішення
print(f"Літера 'h' зустрічається {adwentures_of_tom_sawer.count('h')} разів.")



# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
#task 05. Вирішення
#Вирішення 1
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = 0
for i in adwentures_of_tom_sawer:
    if i in alphabet:
        counter = counter + 1
print(f"З Великої літери у тексті починається {counter} слів")

#Вирішення 2
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
word_list = adwentures_of_tom_sawer.split()
counter = 0
for i in word_list:
    word = i.strip('"')
    if word[0] == word[0].upper():
        counter = counter + 1
print(f"З Великої літери у тексті починається {counter} слів")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
#task 06. Вирішення
position = adwentures_of_tom_sawer.find("Tom")
print(f"Слово 'Tom' на {adwentures_of_tom_sawer.find('Tom', position+1)} позиції.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#task 07. Вирішення
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
#task 08. Вирішення
print(adwentures_of_tom_sawer_sentences[3].lower())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
#task 09. Вирішення
print(f"Речення починається з 'By the time'? {adwentures_of_tom_sawer.startswith('By the time')}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
#task 10. Вирішення
print(f"В останньому реченні {len(adwentures_of_tom_sawer_sentences[-2].split())} слів")

