from transformers import pipeline

nlp = pipeline("question-answering")
result = nlp(question='What is my name?', context='My name is John')

answer = result['answer']
score = result['score']
print(f'answer = {answer}\nscore = {score}')
