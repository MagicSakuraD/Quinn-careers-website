from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': '数据分析师',
  'location': '上海, 中国',
  'salary': '11,000￥'
},{
  'id': 2,
  'title': '数据科学家',
  'location': '上海, 中国',
  'salary': '20,000￥'
},{
  'id': 3,
  'title': '前端开发',
  'location': '杭州, 中国',
  'salary': '15,000￥'
},{
  'id': 4,
  'title': '后端开发',
  'location': '南京, 中国',
  'salary': '25,000￥'
},{
  'id': 5,
  'title': '网络安全工程师',
  'location': '深圳, 中国',
},]

@app.route("/")
def hello_Quinn():
    return render_template('home.html', jobs = JOBS, company_name = "Quinn")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)