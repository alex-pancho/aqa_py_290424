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
# my answer:
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
replaced_text = adwentures_of_tom_sawer.replace('\n', ' ')
print("1) replaced text:",replaced_text)

# task 02 ==
#""" Замініть .... на пробіл
#"""
# my answer:
replaced_text_1 = replaced_text.replace('....', ' ')
print("2) one more replaced text: ",replaced_text_1)

# task 03 ==
#""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
#"""
# my answer:
print("3) count of spaces before: ", len(replaced_text_1))
cleaned_text = replaced_text_1.replace("  ", "")
print("cleaned from extra spaces text: ", cleaned_text)
print("count of spaces after: ", len(cleaned_text))

# task 04
#""" Виведіть, скількі разів у тексті зустрічається літера "h"
#"""
# my answer
print("4) count of symbol \'h\': ", cleaned_text.count("h"))

# task 05
#""" Виведіть, скільки слів у тексті починається з Великої літери?
#"""
# my answer:
count = 0
for i in cleaned_text:
    if i.isupper():
        count += 1
print("5) count of upper symbols: ", count)

# task 06
#""" Виведіть позицію, на якій слово Tom зустрічається вдруге
#"""
# my answer:
start = cleaned_text.find("Tom")
print("6) second position of the word \"Tom\"",cleaned_text.find("Tom", start+1))

# task 07
#""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
#Збережіть результат у змінній adwentures_of_tom_sawer_sentences
#"""
# my answer:
adwentures_of_tom_sawer_sentences = None
splited_text = cleaned_text.split('. ')
adwentures_of_tom_sawer_sentences = splited_text
print("7)", adwentures_of_tom_sawer_sentences)

# task 08
#""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
#Перетворіть рядок у нижній регістр.
#"""
# my answer:
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
print("8)", fourth_sentence.lower())

# task 09
#""" Перевірте чи починається якесь речення з "By the time".
#"""
# my answer: 
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        print("9) Yes")

# task 10
#""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
#"""
# my answer:
last_sentence = adwentures_of_tom_sawer_sentences[-1]
print("10) Quantity of word in the last sentence: ", len(last_sentence.split()))
