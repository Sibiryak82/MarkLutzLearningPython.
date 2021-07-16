#!/usr/bin/python
"""
Файл certificate.py: сценарий на Python 2.X и 3.X
Генерирует простой сертификат об окончании чтения: выводит
и сохраняет в текстовом и HTML-файле, отображаемом в веб-браузере.
"""
import time, sys, webbrowser

if sys.version_info[0] == 2:
    input = raw_input
    import cgi
    htmlescape = cgi.escape
else:
    import html
    htmlescape = html.escape

maxline = 60
browser = True
saveto = 'Certificate.txt'
template = """
%s

===> ОФИЦИАЛЬНЫЙ СЕРТИФИКАТ <===

Date: %s

Этот сертификат подтверждает:
\t%s

что вы прочитали эту массивную книгу:

\t%s

и теперь имеете право на все его привилегии, в том числе
право перейти к изучению разработки веб-сайтов
сайты, графические интерфейсы пользователя, научные модели и
различные приложения,с возможным сопровождением последующих заявок
книги, такие как Programming Python (бесстыдный плагин).

--Марк Лутц, инструтор
(Примечание: сертификат недействителен, если он получен путем пропуска вперед.)

%s
"""

# Взаимодействие, настройка

for c in 'Configuration!'.upper():
    print(c, end=' ')
    sys.stdout.flush()
    time.sleep(0.02)
print()

date = time.asctime()
name = input('ВВЕДИТЕ ИМЯ: ').strip() or 'An unkown reader'
sept = '*' * maxline
book = 'Learning Python 5th Edition'

# Создание версии в текстовом файле

file = open(saveto, 'w')
text = template % (sept, date, name, book, sept)
print(text, file=file)
file.close()

# Создание версии в файле html

htmlto = saveto.replace('.txt', '.html')         # Вставка нескольких html-дескрипторов
file = open(htmlto, 'w')

tags = text.replace(sept,  '<hr>')
tags = tags.replace('===>', '<h1 align=center>')
tags = tags.replace('===>', '</h1>')

tags = tags.split('\n')                          # Построчный режим
tags = ['<p>' if line == ''
        else line for line in tags]
tags = ['<i>%s</i>' % htmlescape(line) if line[:1] == '\t'
        else line for line in tags]
tags = '\n'.join(tags)

link = '<i><a href="http://www.rmi.net/~lutz">Book support site</a></i>\n'
foot = '<table>\n<td><img src="ora-1p.jpg" hspace=5>\n<td>%s</table>n' % link
tags = '<html><body bgcolor=Aqua>' + tags + foot + '</body><html>'

print(tags, file=file)
file.close()

# Отображение результатов

print('[File: %s]' % saveto, end='')
print('/n' * 2, open(saveto).read())

if browser:
    webbrowser.open(saveto, new=True)
    webbrowser.open(htmlto, new=False)

if sys.platform.startswith('win'):
    input('[Press Enter]')                # Оставить окно открытым при щелчке в Windows
