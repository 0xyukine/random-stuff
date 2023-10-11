import markovify
import time
import nltk
import re

nltk.download('averaged_perceptron_tagger')
file_a = ""
file_b = ""

class POSifiedText(markovify.NewlineText):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words
    
    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


with open(file_a) as f:
    text = f.read()

with open(file_b) as f:
    text2 = f.read()

start = time.time()
text_model = POSifiedText(text)
text_model2 = POSifiedText(text2)
fin = time.time()
print(fin - start)

model_combo = markovify.combine([text_model, text_model2],[1,1])

for i in range(20):
    print(model_combo.make_sentence())
