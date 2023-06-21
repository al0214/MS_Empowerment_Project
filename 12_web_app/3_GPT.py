from transformers import pipeline

nlp = pipeline("text-generation")
result = nlp("In a World")
# print(result)
text = result[0]['generated_text']
print(text)
