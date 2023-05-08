from flask import Flask

app = Flask(__name__)


@app.route('/')
def about_flask():
    return f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>플라스크의 특징</h1>
    <h2>간결하다</h2>
    <p>파일 하나로 구성된 짧은 코드만으로도 완벽하게 동작하는 프로그램을 만들 수 있다.</p>
    <h2>확장성</h2>
    <p>개발자가 직접 필요한 확장 모듈을 포함해가며 개발이 가능하다</p>
    <h2>유연함</h2>
    <p>최소한의 규칙만 있어서 자유도가 다른 프레임 워크보다 높다</p>
  </body>
</html>
'''


if __name__ == '__main__':
    app.run(port=8000)
