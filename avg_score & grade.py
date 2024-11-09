Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:/Users/kssiv/OneDrive/Documents/fibonacci sequence.py ===========
enter the number of terms:6
0,1,1,2,3,5

============ RESTART: C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py ===========

============ RESTART: C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py ===========
enter the student's name:sivani
enter the number of subject:3
enter the subject:maths
enter the score of maths:80
enter the subject:cs
enter the score of cs:90
enter the subject:statistics
enter the score of statistics:70
Traceback (most recent call last):
  File "C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py", line 31, in <module>
    main()
  File "C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py", line 23, in main
    avg_score=sum(subject.values())/len(subject)
AttributeError: 'str' object has no attribute 'values'

============ RESTART: C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py ===========
enter the student's name:sivani
enter the number of subject:3
enter the subject:maths
enter the score of maths:80
Traceback (most recent call last):
  File "C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py", line 32, in <module>
    main()
  File "C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py", line 22, in main
    subject[subject]=score
TypeError: 'str' object does not support item assignment

============ RESTART: C:/Users/kssiv/OneDrive/Documents/avg_score & grade.py ===========
enter the student's name:sivani
enter the number of subject:3
enter the subject:maths
enter the score of maths:70
enter the subject:stati
enter the score of stati:60
enter the subject:cs
enter the score of cs:90

student:sivani
scores: {'maths': 70.0, 'stati': 60.0, 'cs': 90.0}
average score:110.00
grade:A

============ RESTART: C:/Users/kssiv/OneDrive/Documents/unique character.py ============

============ RESTART: C:/Users/kssiv/OneDrive/Documents/unique character.py ============
enter the string:hello
True

============ RESTART: C:/Users/kssiv/OneDrive/Documents/unique character.py ============
enter the string:hello
Traceback (most recent call last):
  File "C:/Users/kssiv/OneDrive/Documents/unique character.py", line 12, in <module>
    print(unique_character(string))
  File "C:/Users/kssiv/OneDrive/Documents/unique character.py", line 8, in unique_character
    seen_char.add(char)
NameError: name 'seen_char' is not defined. Did you mean: 'set_char'?

============ RESTART: C:/Users/kssiv/OneDrive/Documents/unique character.py ============
enter the string:hello
False

============== RESTART: C:/Users/kssiv/OneDrive/Documents/word_counter.py ==============
enter the paragraph:hello besties, how are you doing, i say you yesterday and i said hello to you, but you didnt said hello to me back
Traceback (most recent call last):
  File "C:/Users/kssiv/OneDrive/Documents/word_counter.py", line 19, in <module>
    word_counter(text)
  File "C:/Users/kssiv/OneDrive/Documents/word_counter.py", line 5, in word_counter
    paragraph=paragraph.translate(str.maketrans(",",string.punctuation))
ValueError: the first two maketrans arguments must have equal length

============== RESTART: C:/Users/kssiv/OneDrive/Documents/word_counter.py ==============
enter the paragraph:hello besties, how are you doing, i say you yesterday and i said hello to you, but you didnt said hello to me back
Traceback (most recent call last):
  File "C:/Users/kssiv/OneDrive/Documents/word_counter.py", line 19, in <module>
    word_counter(text)
  File "C:/Users/kssiv/OneDrive/Documents/word_counter.py", line 5, in word_counter
    paragraph=paragraph.translate(str.maketrans(",",string.punctuation))
ValueError: the first two maketrans arguments must have equal length
>>> 
============== RESTART: C:/Users/kssiv/OneDrive/Documents/word_counter.py ==============
enter the paragraph:hello besties, how are you doing, i say you yesterday and i said hello to you, but you didnt said hello to me back
hello:3
besties:1
how:1
are:1
you:4
doing:1
i:2
say:1
yesterday:1
and:1
said:2
to:2
but:1
didnt:1
me:1
back:1
>>> hello besties, how are you doing, i saw you yesterday and i said hello to you, but you didnt said hello to me back
SyntaxError: invalid syntax
>>> 
============== RESTART: C:/Users/kssiv/OneDrive/Documents/word_counter.py ==============
enter the paragraph:hello besties, how are you doing, i saw you yesterday and i said hello to you, but you didnt said hello to me back
hello:3
besties:1
how:1
are:1
you:4
doing:1
i:2
saw:1
yesterday:1
and:1
said:2
to:2
but:1
didnt:1
me:1
back:1
