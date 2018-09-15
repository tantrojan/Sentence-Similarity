from nltk.corpus import stopwords 
import operator
import sys
stop_words = set(stopwords.words('english')) 



def abs_to_ext(complete, source, destination):

	fil = open(source,"r")
	sentences = fil.read().split("\n")
	most_similar = []

	for sent in sentences:
		filtered_word = []
		words = sent.split() 
		for r in words: 
		    if not r in stop_words: 
		    	filtered_word.append(r)

		sent_dict = {}

		fil = open(complete,"r")
		text = fil.read()
		lines=text.split(".")
		lines=[ i.replace('\n','') for i in lines]
		lines=[ i for i in lines if len(i)>15 ]

		max_count=0
		for i in lines:
			count = 0
			for j in filtered_word:
				if j.lower() in i.lower():
					count+=1
				max_count=max(max_count,count)
				sent_dict[i]=count

		for key,value in sent_dict.items():
			if value == max_count:
				most_similar.append(key)

		# print(filtered_word)
	f = open(destination, "w")
	for i in most_similar:
		f.write(i.lstrip() + "\n")

def main():
	comp = sys.argv[1]
	sour = sys.argv[2]
	dest = sys.argv[3]
	abs_to_ext(comp,sour,dest)


if __name__ == "__main__" :
	main()