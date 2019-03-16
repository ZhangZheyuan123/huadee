from flask import Blueprint, render_template

webui = Blueprint('webui',__name__)

@webui.route('/index')
def index():
    return render_template("index.html")

# @app.route('/index', endpoint="index")
# def index():
#     return render_template("index.html")

# @app.route('/allfilm', endpoint="allfilm")
# def index():
#     return render_template("allfilm.html")
#
# @app.route('/type_area', endpoint="type_area")
# def index():
#     return render_template("type_area.html")
#
# @app.route('/吸金导演', endpoint="吸金导演")
# def index():
#     return render_template("吸金导演.html")
#
# @app.route('/国家票房', endpoint="国家票房")
# def index():
#     return render_template("电影统计.html")
# @app.route('/地区特征', endpoint="地区特征")
# def index():
#     return render_template("地区特征.html")
# @app.route('/年代特征', endpoint="年代特征")
# def index():
#     return render_template("年代特征.html")
# @app.route('/演员热度', endpoint="演员热度")
# def index():
#     return render_template("演员热度.html")
# @app.route('/电影年代', endpoint="电影年代")
# def index():
#     return render_template("电影年代.html")
#
# @app.route('/电影类型', endpoint="电影类型")
# def index():
#     return render_template("电影类型.html")

