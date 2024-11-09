import string

def word_counter(paragraph):
    paragraph=paragraph.lower()
    paragraph=paragraph.translate(str.maketrans(' ',' ',string.punctuation))
    words=paragraph.split()

    word_count={}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word,count in word_count.items():
        print(f"{word}:{count}")

text=input("enter the paragraph:")
word_counter(text)
