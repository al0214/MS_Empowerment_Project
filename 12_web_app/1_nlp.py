# !pip install transformers # Transformers 패키지를 설치합니다. 이 패키지는 자연어 처리에 사용되는 트랜스포머 모델과 관련된 기능을 제공합니다.
# !pip install torch # Torch 패키지를 설치합니다. 이 패키지는 파이토치(PyTorch)라고도 불리며, 텐서(Tensor) 계산을 위한 딥러닝 라이브러리입니다.
# !pip install pipeline # Pipeline 패키지를 설치합니다. 이 패키지는 Hugging Face 라이브러리에서 제공하는 자연어 처리 파이프라인 기능을 사용할 수 있게 해줍니다.
# !pip install gradio # Gradio 패키지를 설치하는 명령어입니다. Gradio는 간단하게 웹 기반 인터페이스를 만들어 모델을 시연하고 상호 작용할 수 있는 패키지입니다.
from transformers import pipeline

nlp = pipeline("sentiment-analysis")
result = nlp("I LOVE This Movie")
print(result)
