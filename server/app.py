import json
import pymysql
from flask import Flask, render_template, request
from views.view import webui

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/allfilm', endpoint="allfilm")
def index():
    return render_template("allfilm.html")

@app.route('/type_area', endpoint="type_area")
def index():
    return render_template("type_area.html")

@app.route('/吸金导演', endpoint="吸金导演")
def index():
    return render_template("吸金导演.html")

@app.route('/电影统计', endpoint="电影统计")
def index():
    return render_template("电影统计.html")
@app.route('/地区特征', endpoint="地区特征")
def index():
    return render_template("地区特征.html")
@app.route('/年代特征', endpoint="年代特征")
def index():
    return render_template("年代特征.html")
@app.route('/演员热度', endpoint="演员热度")
def index():
    return render_template("演员热度.html")
@app.route('/电影年代', endpoint="电影年代")
def index():
    return render_template("电影年代.html")

@app.route('/电影类型', endpoint="电影类型")
def index():
    return render_template("电影类型.html")
@app.route('/handle10', endpoint="handle10", methods=["GET", "POST"])
def handle10():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='剧情' ORDER BY year"
    mycursor1.execute(sql)
    datas.append(mycursor1.fetchall())
    mycursor2 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='喜剧' ORDER BY year"
    mycursor2.execute(sql)
    datas.append(mycursor2.fetchall())
    mycursor3 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='爱情' ORDER BY year"
    mycursor3.execute(sql)
    datas.append(mycursor3.fetchall())
    mycursor4 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='动作' ORDER BY year"
    mycursor4.execute(sql)
    datas.append(mycursor4.fetchall())

    mycursor5 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='惊悚' ORDER BY year"
    mycursor5.execute(sql)
    datas.append(mycursor5.fetchall())
    mycursor6 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='动画' ORDER BY year"
    mycursor6.execute(sql)
    datas.append(mycursor6.fetchall())
    mycursor7 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='冒险' ORDER BY year"
    mycursor7.execute(sql)
    datas.append(mycursor7.fetchall())

    mycursor8 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='科幻' ORDER BY year"
    mycursor8.execute(sql)
    datas.append(mycursor8.fetchall())
    mycursor9 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='灾难' ORDER BY year"
    mycursor9.execute(sql)
    datas.append(mycursor9.fetchall())
    mycursor10 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='悬疑' ORDER BY year"
    mycursor10.execute(sql)
    datas.append(mycursor10.fetchall())
    mycursor11 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='文艺' ORDER BY year"
    mycursor11.execute(sql)
    datas.append(mycursor11.fetchall())
    mycursor12 = mydb.cursor()
    sql = "SELECT *FROM Rq3 where type='其他' ORDER BY year"
    mycursor12.execute(sql)
    datas.append(mycursor12.fetchall())

    data = []
    mycursor13 = mydb.cursor()
    sql = "SELECT *FROM Rq4 ORDER BY want"
    mycursor13.execute(sql)
    data.append(mycursor13.fetchall())
    results = []
    for i in datas:
        for j in range(0, 7):
            result = {}
            result["value"] = i[j][2]
            results.append(result)
    for i in data[0]:
        result = {}
        result["value"] = i[1]
        results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    mycursor2.close()
    mycursor3.close()
    mycursor4.close()
    mycursor5.close()
    mycursor6.close()
    mycursor7.close()
    mycursor8.close()
    mycursor9.close()
    mycursor10.close()
    mycursor11.close()
    mycursor12.close()
    mycursor13.close()
    # 发出返回数据
    return ret_json

@app.route('/handle_index', endpoint="handle_index", methods=["GET", "POST"])
def handle_index():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '中国' ORDER BY year"
    mycursor1.execute(sql)
    datas.append(mycursor1.fetchall())
    mycursor2 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '美国' ORDER BY year"
    mycursor2.execute(sql)
    datas.append(mycursor2.fetchall())

    mycursor3 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '英国' ORDER BY year"
    mycursor3.execute(sql)
    datas.append(mycursor3.fetchall())
    mycursor4 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '法国' ORDER BY year"
    mycursor4.execute(sql)
    datas.append(mycursor4.fetchall())
    mycursor5 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '俄罗斯' ORDER BY year"
    mycursor5.execute(sql)
    datas.append(mycursor5.fetchall())
    mycursor6 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '日本' ORDER BY year"
    mycursor6.execute(sql)
    datas.append(mycursor6.fetchall())
    mycursor7 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '德国' ORDER BY year"
    mycursor7.execute(sql)
    datas.append(mycursor7.fetchall())
    mycursor8 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '印度' ORDER BY year"
    mycursor8.execute(sql)
    datas.append(mycursor8.fetchall())
    mycursor9 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '韩国' ORDER BY year"
    mycursor9.execute(sql)
    datas.append(mycursor9.fetchall())
    mycursor10 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '意大利' ORDER BY year"
    mycursor10.execute(sql)
    datas.append(mycursor10.fetchall())
    mycursor11 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '巴西' ORDER BY year"
    mycursor11.execute(sql)
    datas.append(mycursor11.fetchall())
    mycursor12 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '加拿大' ORDER BY year"
    mycursor12.execute(sql)
    datas.append(mycursor12.fetchall())
    mycursor13 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '澳大利亚' ORDER BY year"
    mycursor13.execute(sql)
    datas.append(mycursor13.fetchall())
    mycursor14 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '西班牙' ORDER BY year"
    mycursor14.execute(sql)
    datas.append(mycursor14.fetchall())
    mycursor15 = mydb.cursor()
    sql = "SELECT *FROM Rq7 where area = '墨西哥' ORDER BY year"
    mycursor15.execute(sql)
    datas.append(mycursor15.fetchall())
    results = []
    try:
        for i in datas:
            for j in range(0, 7):
                result = {}
                result["value"] = i[j][2]
                results.append(result)
    except Exception as e:
        print(e)
    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    mycursor2.close()
    mycursor3.close()
    mycursor4.close()
    mycursor5.close()
    mycursor6.close()
    mycursor7.close()
    mycursor8.close()
    mycursor9.close()
    mycursor10.close()
    mycursor11.close()
    mycursor12.close()
    mycursor13.close()
    mycursor14.close()
    mycursor15.close()
    # 发出返回数据
    return ret_json

@app.route('/handle_area', endpoint="handle_area", methods=["GET", "POST"])
def handle_area():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '中国' ORDER BY type"
    mycursor1.execute(sql)
    datas.append(mycursor1.fetchall())
    mycursor2 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '美国' ORDER BY type"
    mycursor2.execute(sql)
    datas.append(mycursor2.fetchall())
    mycursor3 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '英国' ORDER BY type"
    mycursor3.execute(sql)
    datas.append(mycursor3.fetchall())
    mycursor4 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '法国' ORDER BY type"
    mycursor4.execute(sql)
    datas.append(mycursor4.fetchall())
    mycursor5 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '俄罗斯' ORDER BY type"
    mycursor5.execute(sql)
    datas.append(mycursor5.fetchall())
    mycursor6 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '日本' ORDER BY type"
    mycursor6.execute(sql)
    datas.append(mycursor6.fetchall())
    mycursor7 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '德国' ORDER BY type"
    mycursor7.execute(sql)
    datas.append(mycursor7.fetchall())
    mycursor8 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '印度' ORDER BY type"
    mycursor8.execute(sql)
    datas.append(mycursor8.fetchall())
    mycursor9 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '韩国' ORDER BY type"
    mycursor9.execute(sql)
    datas.append(mycursor9.fetchall())
    mycursor10 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '意大利' ORDER BY type"
    mycursor10.execute(sql)
    datas.append(mycursor10.fetchall())
    mycursor11 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '巴西' ORDER BY type"
    mycursor11.execute(sql)
    datas.append(mycursor11.fetchall())
    mycursor12 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '加拿大' ORDER BY type"
    mycursor12.execute(sql)
    datas.append(mycursor12.fetchall())
    mycursor13 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '澳大利亚' ORDER BY type"
    mycursor13.execute(sql)
    datas.append(mycursor13.fetchall())
    mycursor14 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '西班牙' ORDER BY type"
    mycursor14.execute(sql)
    datas.append(mycursor14.fetchall())
    mycursor15 = mydb.cursor()
    sql = "SELECT *FROM Rq11 WHERE area = '墨西哥' ORDER BY type"
    mycursor15.execute(sql)
    datas.append(mycursor15.fetchall())
    results = []
    for i in datas:
        for j in range(0, 11):
            result = {}
            result["value"] = i[j][2]
            results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    mycursor2.close()
    mycursor3.close()
    mycursor4.close()
    mycursor5.close()
    mycursor6.close()
    mycursor7.close()
    mycursor8.close()
    mycursor9.close()
    mycursor10.close()
    mycursor11.close()
    mycursor12.close()
    mycursor13.close()
    mycursor14.close()
    mycursor15.close()
    # 发出返回数据
    return ret_json

@app.route('/handle_area1', endpoint="handle_area1", methods=["GET", "POST"])
def handle_area1():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '中国' ORDER BY type"
    mycursor1.execute(sql)
    datas.append(mycursor1.fetchall())
    mycursor2 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '美国' ORDER BY type"
    mycursor2.execute(sql)
    datas.append(mycursor2.fetchall())
    mycursor3 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '英国' ORDER BY type"
    mycursor3.execute(sql)
    datas.append(mycursor3.fetchall())
    mycursor4 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '法国' ORDER BY type"
    mycursor4.execute(sql)
    datas.append(mycursor4.fetchall())
    mycursor5 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '俄罗斯' ORDER BY type"
    mycursor5.execute(sql)
    datas.append(mycursor5.fetchall())
    mycursor6 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '日本' ORDER BY type"
    mycursor6.execute(sql)
    datas.append(mycursor6.fetchall())
    mycursor7 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '德国' ORDER BY type"
    mycursor7.execute(sql)
    datas.append(mycursor7.fetchall())
    mycursor8 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '印度' ORDER BY type"
    mycursor8.execute(sql)
    datas.append(mycursor8.fetchall())
    mycursor9 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '韩国' ORDER BY type"
    mycursor9.execute(sql)
    datas.append(mycursor9.fetchall())
    mycursor10 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '意大利' ORDER BY type"
    mycursor10.execute(sql)
    datas.append(mycursor10.fetchall())
    mycursor11 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '巴西' ORDER BY type"
    mycursor11.execute(sql)
    datas.append(mycursor11.fetchall())
    mycursor12 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '加拿大' ORDER BY type"
    mycursor12.execute(sql)
    datas.append(mycursor12.fetchall())
    mycursor13 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '澳大利亚' ORDER BY type"
    mycursor13.execute(sql)
    datas.append(mycursor13.fetchall())
    mycursor14 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '西班牙' ORDER BY type"
    mycursor14.execute(sql)
    datas.append(mycursor14.fetchall())
    mycursor15 = mydb.cursor()
    sql = "SELECT *FROM Rq12 WHERE area = '墨西哥' ORDER BY type"
    mycursor15.execute(sql)
    datas.append(mycursor15.fetchall())
    results = []
    for i in datas:
        for j in range(0, 11):
            result = {}
            result["value"] = i[j][2]
            results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    mycursor2.close()
    mycursor3.close()
    mycursor4.close()
    mycursor5.close()
    mycursor6.close()
    mycursor7.close()
    mycursor8.close()
    mycursor9.close()
    mycursor10.close()
    mycursor11.close()
    mycursor12.close()
    mycursor13.close()
    mycursor14.close()
    mycursor15.close()
    # 发出返回数据
    return ret_json

@app.route('/handle_year', endpoint="handle_year", methods=["GET", "POST"])
def handle_year():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '中国' ORDER BY year"
    mycursor1.execute(sql)
    datas.append(mycursor1.fetchall())
    mycursor2 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '美国' ORDER BY year"
    mycursor2.execute(sql)
    datas.append(mycursor2.fetchall())

    mycursor3 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '英国' ORDER BY year"
    mycursor3.execute(sql)
    datas.append(mycursor3.fetchall())

    mycursor4 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '法国' ORDER BY year"
    mycursor4.execute(sql)
    datas.append(mycursor4.fetchall())
    mycursor5 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '俄罗斯' ORDER BY year"
    mycursor5.execute(sql)
    datas.append(mycursor5.fetchall())
    mycursor6 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '日本' ORDER BY year"
    mycursor6.execute(sql)
    datas.append(mycursor6.fetchall())
    mycursor7 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '德国' ORDER BY year"
    mycursor7.execute(sql)
    datas.append(mycursor7.fetchall())
    mycursor8 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '印度' ORDER BY year"
    mycursor8.execute(sql)
    datas.append(mycursor8.fetchall())
    mycursor9 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '韩国' ORDER BY year"
    mycursor9.execute(sql)
    datas.append(mycursor9.fetchall())
    mycursor10 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '意大利' ORDER BY year"
    mycursor10.execute(sql)
    datas.append(mycursor10.fetchall())
    mycursor11 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '巴西' ORDER BY year"
    mycursor11.execute(sql)
    datas.append(mycursor11.fetchall())
    mycursor12 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '加拿大' ORDER BY year"
    mycursor12.execute(sql)
    datas.append(mycursor12.fetchall())
    mycursor13 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '澳大利亚' ORDER BY year"
    mycursor13.execute(sql)
    datas.append(mycursor13.fetchall())
    mycursor14 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '西班牙' ORDER BY year"
    mycursor14.execute(sql)
    datas.append(mycursor14.fetchall())
    mycursor15 = mydb.cursor()
    sql = "SELECT *FROM Rq10 where area = '墨西哥' ORDER BY year"
    mycursor15.execute(sql)
    datas.append(mycursor15.fetchall())
    results = []
    for i in datas:
        for j in range(0, 7):
            result = {}
            result["value"] = i[j][2]
            results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    mycursor2.close()
    mycursor3.close()
    mycursor4.close()
    mycursor5.close()
    mycursor6.close()
    mycursor7.close()
    mycursor8.close()
    mycursor9.close()
    mycursor10.close()
    mycursor11.close()
    mycursor12.close()
    mycursor13.close()
    mycursor14.close()
    mycursor15.close()
    # 发出返回数据
    return ret_json

@app.route('/handle_year_feature', endpoint="handle_year_feature", methods=["GET", "POST"])
def handle_year_feature():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq5 ORDER BY year"
    mycursor1.execute(sql)
    datas.append(mycursor1.fetchall())
    results = []
    for i in datas:
        for j in range(0, 7):
            result = {}
            result["value"] = i[j][1]
            results.append(result)
    for i in datas:
        for j in range(0, 7):
            result = {}
            result["value"] = i[j][2]
            results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    return ret_json

@app.route('/handle_data_sum', endpoint="handle_data_sum", methods=["GET", "POST"])
def handle_data_sum():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    results = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '中国'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '美国'"
    mycursor1.execute(sql)
    datas = {}
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '英国'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '法国'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '俄罗斯'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '日本'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '德国'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '印度'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '韩国'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '意大利'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '巴西'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '加拿大'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '澳大利亚'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '西班牙'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq6 WHERE area = '墨西哥'"
    datas = {}
    mycursor1.execute(sql)
    result = mycursor1.fetchall()
    datas["value"] = result[0][1]
    results.append(datas)

    ret_json = json.dumps(results, ensure_ascii=False)
    mydb.close()
    mycursor1.close()
    return ret_json

@app.route('/handle_index_box', endpoint="handle_index_box", methods=["GET", "POST"])
def handle_index_box():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq2 ORDER BY box desc"
    mycursor1.execute(sql)
    datas = mycursor1.fetchall()
    results = []
    for i in datas:
        result = {}
        result["name"] = i[0]
        result["box"] = i[1]
        results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mycursor1.close()
    mydb.close()
    return ret_json

@app.route('/handle_allfilm', endpoint="handle_allfilm", methods=["GET", "POST"])
def handle_allfilm():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq1 ORDER BY type"
    mycursor1.execute(sql)
    datas = mycursor1.fetchall()
    results = []
    for i in datas:
        result = {}
        result["name"] = i[0]
        result["box"] = i[2]
        results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mycursor1.close()
    mydb.close()
    return ret_json

@app.route('/handle_dir', endpoint="handle_dir", methods=["GET", "POST"])
def handle_dir():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq8 ORDER BY box desc LIMIT 100"
    mycursor1.execute(sql)
    datas = mycursor1.fetchall()
    results = []
    for i in datas:
        result = {}
        result["name"] = i[0]
        result["box"] = i[1]
        results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mycursor1.close()
    mydb.close()
    return ret_json

@app.route('/handle_act', endpoint="handle_act", methods=["GET", "POST"])
def handle_act():
    mydb = pymysql.connect("192.168.111.130", "root", "z123456", "huadee")
    datas = []
    mycursor1 = mydb.cursor()
    sql = "SELECT *FROM Rq9 ORDER BY box desc LIMIT 100"
    mycursor1.execute(sql)
    datas = mycursor1.fetchall()
    results = []
    for i in datas:
        result = {}
        result["name"] = i[0]
        result["box"] = i[1]
        results.append(result)
    ret_json = json.dumps(results, ensure_ascii=False)
    mycursor1.close()
    mydb.close()
    return ret_json

if __name__ == '__main__':
    app.run()
