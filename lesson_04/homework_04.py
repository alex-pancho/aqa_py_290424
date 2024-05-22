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
print("Task 1:")
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
print('', "Task 2:", sep="\n")
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
# task 03 ==
print('', "Task 3:", sep="\n")
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
probil_count = adwentures_of_tom_sawer.find("  ")
i = 10
if probil_count != (-1):
    while i > 1:
        probil = (" "*i)
        #print(probil)
        i = i-1
        adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(probil, " ")
print(adwentures_of_tom_sawer)

# task 04
print('', "Task 4:", sep="\n")
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Літера h в тексті зустрічається ", adwentures_of_tom_sawer.count("h"), " разів")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('', "Task 5:", sep="\n")
a = 0
for i in adwentures_of_tom_sawer:
    if i.isupper():
        a += 1
print("З великої букви починається ", a," слів")


# task 06
print('', "Task 6:", sep="\n")
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
start = adwentures_of_tom_sawer.find("Tom")
print("Слово Tom зустрічається вдруге на", adwentures_of_tom_sawer.find("Tom", start+1), "позиції")


# task 07
print('', "Task 7:", sep="\n")
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences =adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
print('', "Task 8:", sep="\n")
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
#adwentures_of_tom_sawer_sentences[3] = adwentures_of_tom_sawer_sentences[3].lower()
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
print('', "Task 9:", sep="\n")
""" Перевірте чи починається якесь речення з "By the time".
"""
cout_test = 0
for test in adwentures_of_tom_sawer_sentences:
    test = test.startswith('By the time')
    if test: cout_test += 1

if cout_test >=1:
    print("Якесь речення починається з By the time")
else:
    print("Жодне з речень не починається з By the time")

# task 10
print('', "Task 10:", sep="\n")
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
#print(adwentures_of_tom_sawer_sentences[-1])
last_line = adwentures_of_tom_sawer_sentences[-1]
last_line = last_line.replace(",", "")
last_line = last_line.replace(".", "")
last_line = last_line.split(" ")
print("Кількість слів останнього речення з adwentures_of_tom_sawer_sentences:", len(last_line))
