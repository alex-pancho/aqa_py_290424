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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# print(adwentures_of_tom_sawer)
replaced_space = adwentures_of_tom_sawer.replace('\n', ' ')
print(replaced_space)

# task 02 ==
""" Замініть .... на пробіл
"""
replaced_space_dot = replaced_space.replace('....', ' ')
print(replaced_space_dot)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
replaced_one_space_dot = replaced_space_dot.replace('   ', ' ')
print(replaced_one_space_dot)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = 0
for i in replaced_one_space_dot:
    if i == 'h':
        count_h += 1

print(f'\nLetter \'h\' in a string: {count_h}')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_upper_letter = 0
for i in replaced_one_space_dot:
    if i.isupper():
        count_upper_letter += 1

print(f'\nWords start with a capital letter: {count_upper_letter} in a string')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
find_tom_second_place = replaced_one_space_dot.find('Tom', replaced_one_space_dot.find('Tom') + 1)
print(f'\nWord \'Tom\' meets on a position {find_tom_second_place} after first meeting\n')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = replaced_one_space_dot.split('. ')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith('By the time'):
        print('\nThere is a sentence in a string which start with words \'By the time\'')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
count_words_in_last_sentence = len(last_sentence.split())
print(f'\nThere are {count_words_in_last_sentence} words in a last sentence of a string')
