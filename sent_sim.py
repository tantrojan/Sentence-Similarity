from nltk.corpus import stopwords 
import nltk
import operator
import sys
import re, math
from collections import Counter
WORD = re.compile(r'\w+')

stop_words = set(stopwords.words('english')) 


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

# SENTENCE WHOSE SIMILARITY IS TO BE FOUND
sent="Morris Dees is a co-founder and leader of the Southern Poverty Law Center, located in Montgomery, Alabama."
vector1 = text_to_vector(sent)
#########################################

# LOADING THE DATASET
fil = open("dataset_601.txt","r")
text = fil.read()
text=text.replace('\n','')
lines = nltk.sent_tokenize(text)
#####################

# LOOPING THROUGH THE LINES OF THE DATASET
sent_dict = {}

for i in lines:
	vector2 = text_to_vector(i)
	cosine = get_cosine(vector1, vector2)
	sent_dict[i] = cosine

sent_dict = sorted(sent_dict.items(), key=operator.itemgetter(1))
#########################################


print("SENTENCE : " + sent)
print("MOST SIMILAR SENTENCE : " + sent_dict[-1][0])
