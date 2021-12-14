
from app_conf import app, db
from entity import *
from flask import request, render_template, redirect, url_for, flash
from sqlalchemy.databases import postgres


db.create_all()


@app.route('/')
def index():
    ##train = Train.query.filter_by(Number=2).first()
    ##print(train)
    ##return render_template("AHead.html", train=train)
    return render_template("AHead.html")


@app.route('/Station')
def station():
    station = Station.query.all()
    print(station)

    ##form = StationForm()
    ##return render_template("Station.html", stations=station, form=form)
    return render_template("Station.html", stations=station)


@app.route('/createStation', methods=['GET', 'POST'])
def createStation():
    station = Station.query.all()
    # form = StationForm(request.form if request.method == "POST" else None, obj=station)
    #
    # if form.button_delete.data:
    #     db.session.delete(station)
    #     db.session.commit()
    #     flash("Данные успешно изменены")
    #
    # if form.button_save.data and form.validate():
    #     form.populate_obj(station)
    #     db.session.add(station)
    #     db.session.commit()
    #     db.session.flush()
    #     flash("Данные успешно изменены")
    return render_template('createStation.html', stations=station)


@app.route('/Train')
def train():
    train = Train.query.all()
    print(train)
    ##tr = db.session.query(Train).all()
    return render_template("Train.html", trains=train)
    ##return render_template("Train.html",trains=tr)


@app.route('/TrainRout')
def trainRoute():
    trainRoute= TrainRout.query.all()
    print(trainRoute)
    return render_template("TrainRout.html", trainRoutes=trainRoute)


@app.route('/TrainWagon')
def trainWagon():
    trainWagon=TrainWagon.query.all()
    return render_template("TrainWagon.html", trainWagons=trainWagon)


@app.route('/Wagon')
def wagon():
    wagon = Wagon.query.all()
    print(wagon)
    return render_template("Wagon.html", wagons=wagon)


@app.route('/createWagon')
def createWagon():
    return render_template('createWagon.html')


if __name__ == '__main__':
    ##db.create_all()
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
