from flask import render_template, url_for, request
from flaskblog import app, db
from flaskblog.models import Util

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/insert", methods=['GET','POST'])
def insert():
    if request.method == 'GET':
        print('get method')
        return render_template('insert.html')
    else:
        lineup_title = request.form['title']
        lineup_id = request.form['id']
        util_type = request.form['type']
        map = request.form['map']
        oneway = request.form['oneway']
        if oneway == 'True':
            oneway = True
        else:
            oneway = False
        attack_bool = request.form['attack']
        if attack_bool == 'True':
            attack_bool = True
        else:
            attack_bool = False
        new_note = request.form['note']
        utility_x = request.form['util_x']
        utility_y = request.form['util_y']
        pos_x = request.form['pos_x']
        pos_y = request.form['pos_y']
        util = Util(id = lineup_id,title = lineup_title,type = util_type,map = map,lineup_image = 'lu'+str(lineup_id)+'.png', util_image = 'u'+str(lineup_id)+'.png', pos_image = 'p'+str(lineup_id)+'.png', one_way = oneway, attack = attack_bool, player_x = pos_x, player_y = pos_y, util_x = utility_x, util_y = utility_y, note = new_note)
        print(lineup_title,lineup_id,util_type,map,oneway,attack_bool,new_note,utility_x,utility_y,pos_x,pos_y)
        lineup_exists = db.session.query(Util.id).filter_by(id=lineup_id).scalar() is not None
        print(lineup_exists)
        if lineup_exists:
            db.session.delete(Util.query.filter_by(id=lineup_id).first())
            db.session.commit()
            db.session.add(util)
            db.session.commit()
        else:
            db.session.add(util)
            db.session.commit()
        return render_template('insert.html')
        

@app.route("/bind")
def bind():
    utils = Util.query.all()
    return render_template('bind.html', title='Bind', map = 'static/maps/bind.png', utils=utils)

@app.route("/haven")
def haven():
    utils=Util.query.all()
    return render_template('haven.html', title='Haven', map = 'static/maps/haven.png', utils=utils)

@app.route("/split")
def split():
    utils=Util.query.all()
    return render_template('split.html', title='Split', map = 'static/maps/split.png', utils=utils)

@app.route("/ascent")
def ascent():
    utils=Util.query.all()
    return render_template('ascent.html', title='Ascent', map = 'static/maps/ascent.png', utils=utils)

@app.route("/icebox")
def icebox():
    utils=Util.query.all()
    return render_template('icebox.html', title='Icebox', map = 'static/maps/icebox.png', utils=utils)