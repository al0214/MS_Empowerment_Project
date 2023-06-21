import gradio as gr
classifier = pipeline("sentiment-analysis",
                      model="sangrimlee/bert-base-multilingual-cased-nsmc")


def sentiment_analysis(text):
    result = classifier(text)
    label = result[0]['label']
    return label


demo = gr.Interface(fn=sentiment_analysis, inputs='text',
                    outputs='text', title='감정분석', description="텍스트를 입력하면 감정을 분석합니다.")
demo.launch()
