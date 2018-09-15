import re, math
from collections import Counter
from nltk.corpus import stopwords 
import nltk
import operator
import sys
stop_words = set(stopwords.words('english')) 
WORD = re.compile(r'\w+')

# COSINE SIMILARITY MODULES
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
###########################

def abs_to_ext(complete, source, destination):

    fil = open(source,"r")
    sentences = nltk.sent_tokenize(fil.read())
    fil.close()

    fil = open(complete,"r")
    text = fil.read()
    fil.close()
    text=text.replace('\n','')
    lines = nltk.sent_tokenize(text)


    f = open(destination, "w")
    for sent in sentences:
        sent_dict = {}
        vector1 = text_to_vector(sent)
        for i in lines:
            vector2 =text_to_vector(i)
            cosine = get_cosine(vector1, vector2)
            sent_dict[i] = cosine
        sent_dict = sorted(sent_dict.items(), key=operator.itemgetter(1))
        f.write(sent_dict[-1][0] + '\n')

def main():
    comp = sys.argv[1]
    sour = sys.argv[2]
    dest = sys.argv[3]
    abs_to_ext(comp,sour,dest)


if __name__ == "__main__" :
    main()