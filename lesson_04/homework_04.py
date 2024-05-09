adventures_of_tom_sawyer = """\
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawyer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")
print(adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")
print(adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("  ", " ")
print(adventures_of_tom_sawyer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(adventures_of_tom_sawyer.count("h"))  # case-sensitive

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitalized_words = adventures_of_tom_sawyer.split()
capitalized_words_count = sum(1 for word in capitalized_words if word[0].isupper())
print(capitalized_words_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
start = adventures_of_tom_sawyer.find("Tom")
print(adventures_of_tom_sawyer.find("Tom", start+1))

# task 07
""" Розділіть змінну adventures_of_tom_sawyer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawyer_sentences
"""
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split(".")
print(adventures_of_tom_sawyer_sentences)

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawyer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentence_4 = adventures_of_tom_sawyer_sentences[3]
print(sentence_4)
print(sentence_4.lower())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adventures_of_tom_sawyer_sentences:
    print(sentence.strip().startswith("By the time")) # checking all sentences



# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawyer_sentences.
"""
print(len(adventures_of_tom_sawyer_sentences[-1]))  # we have an empty sentence at the end
