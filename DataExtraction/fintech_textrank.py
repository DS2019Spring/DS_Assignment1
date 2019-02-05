import textrank as pyt
import time

# in_file = open('final_data.txt', 'rt')

# text=in_file.read()

# in_file.close()

# give file path to store data  in variable
filename = 'noisy_text_data.txt'
file = open(filename, 'rt',encoding="UTF-8")
text = file.read()
file.close()

#source:https://machinelearningmastery.com/clean-text-machine-learning-python/
# split into words
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to upper case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]



new_txt = " ".join(word for word in words)

# print(new_txt)


start=time.time()
phrase,word=pyt.top_keywords_sentences(new_txt,phrase_limit=100)

# print('Keywords:',word)

import csv
with open('Fintech_textrank_words.csv', 'w',encoding="UTF-8") as csvFile:
    writer = csv.writer(csvFile, lineterminator=',')
    writer.writerow(w for w in word.replace(',','').split(' ')) 
    # csvFile.write(w for w in word.replace(',','').split(' '))
csvFile.close()


# print('Keywords:',text)
#print('Time Taken: ',time.time()-start)