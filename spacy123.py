# import spacy
# nlp = spacy.load("en_core_web_sm")
# text ="This is an example sentence for creating n-grams."
# n=3
# tokens = [token.text for token in nlp(text)]
# ngrams = [tokens[i : i + n] for i in range(len(tokens) - n + 1)]
# print(ngrams)
# print(tokens)

# import spacy
 
# nlp = spacy.load("en_core_web_sm")
 
# text = "This is a simple example to demonstrate stop word removal using spaCy."
 
# doc = nlp(text)
 
# filtered_tokens = [
#     token.text
#     for token in doc
#     if not token.is_stop
# ]
 
# print(filtered_tokens)

#import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
