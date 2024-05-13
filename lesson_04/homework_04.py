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
adventures_of_tom_sawyer = adwentures_of_tom_sawer.replace("\n", " ")
print(adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")
print(adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawyer = " ".join(adventures_of_tom_sawyer.split())
print(adventures_of_tom_sawyer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adventures_of_tom_sawyer.count("h")
print("Літера 'h' зустрічається у тексті:", count_h, "разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adventures_of_tom_sawyer.split()
count_title_words = 0
for word in words:
    if word.startswith(tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        count_title_words += 1
print("Кількість слів, що починаються з великої літери:", count_title_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_time = adventures_of_tom_sawyer.find("Tom")
second_time = adventures_of_tom_sawyer.find("Tom", first_time + 1)
print("Позиція, на якій слово Tom зустрачається вдруге:", second_time)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split('. ')
print(adventures_of_tom_sawyer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adventures_of_tom_sawyer_sentences[3].lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.startswith("By the time"):
        print("Речення, яке починається з 'By the time':", sentence)
        break
else:
    print("Жодне речення не починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
words_in_last_sentence = adventures_of_tom_sawyer_sentences[-1].split()
word_count_in_last_sentence = len(words_in_last_sentence)
print("Кількість слів останнього речення:", word_count_in_last_sentence)