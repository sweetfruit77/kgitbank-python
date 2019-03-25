from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    import requests, bs4
    resp = requests.get('https://www.naver.com')
    if (resp.status_code == requests.codes.ok):
        html = resp.text
    bs = bs4.BeautifulSoup(html, 'html.parser')
    tags = bs.select('a.ah_a') # Top 뉴스
    ress=""
    for t in tags :
        ress= ress+t.getText()+"<br>"
    return ress


if  __name__ == '__main__':  
    app.run()
#  app.run(debug=True, host='0.0.0.0’ )  원격 컴퓨터에서 접속 가능한 설정 시작
#  app.debug=True
#   app.run(host='0.0.0.0‘, port = 80)
