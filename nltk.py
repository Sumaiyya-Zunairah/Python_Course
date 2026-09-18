
import nltk
nltk.download("maxent_ne_chunker_tab")
nltk.download("words")

from nltk import word_tokenize, pos_tag, ne_chunk

text = "Sundar Pichai is the CEO of Google"
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
ner_tree = ne_chunk(pos_tags)

print(ner_tree)


text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasnt "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)
# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
