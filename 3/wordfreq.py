sentence = "why do we fall? so that we can learn to pick ourselves up."

#the sentence contains question marks and full stop we need to remove it

import re
sentence = re.sub(r'[?.,\"\'\\{}!@#$%^&*()|]',' ',sentence)

# now splitting on basis of words

wordlist = sentence.split(' ')

#maintaining word frequency dictionary

wordcount={}
wordlist=[w for w in wordlist if w!='']

for word in wordlist:
	if word not in wordcount:
		wordcount[word]=1
	else:
		wordcount[word]+=1

print(wordcount)
