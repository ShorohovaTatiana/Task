from app_conf import db


class Station(db.Model):
    __tablename__ = 'Station'
    Number = db.Column('Number', db.INTEGER, primary_key=True, autoincrement=True)
    Type = db.Column('Type', db.String, nullable=True, unique=False)


class TrainWagon(db.Model):
    __tablename__ = 'TrainWagon'
    Wagon_number = db.Column(db.ForeignKey('Wagon.Number'), primary_key=True)
    Wagon = db.relationship('Wagon', lazy=True, cascade='all')
    Train_number = db.Column(db.ForeignKey('Train.Number'), primary_key=True)
    Train_number_Wagon_number = db.Column('Train_number_Wagon_number', db.INTEGER, nullable=True, unique=False)


class Train(db.Model):
    __tablename__ = 'Train'
    Number = db.Column('Number', db.INTEGER, primary_key=True, autoincrement=True)
    Type = db.Column('Type', db.String, nullable=True, unique=False)
    TrainWagons = db.relationship('TrainWagon', lazy=True, cascade='all', backref='Train')
    TrainRoutes = db.relationship('TrainRout', lazy=True, cascade='all', backref='Train',
                                  order_by="TrainRout.Train_number_Order_of_stations")

class TrainRout(db.Model):
    __tablename__ = 'TrainRoute'
    Train_number = db.Column(db.ForeignKey('Train.Number'), primary_key=True)
    Station_number = db.Column(db.ForeignKey('Station.Number'), primary_key=True)
    Station = db.relationship('Station', lazy=True, cascade='all')
    Train_number_Order_of_stations = db.Column('Train_number_Order_of_stations', db.INTEGER, nullable=False)
    __table_args__ = (
        db.UniqueConstraint('Train_number', 'Train_number_Order_of_stations'),
    )


class Wagon(db.Model):
    __tablename__ = 'Wagon'
    Number = db.Column('Number', db.INTEGER, primary_key=True, autoincrement=True)
    Capacity = db.Column('Capacity', db.INTEGER, nullable=True, unique=False)
    Type = db.Column('Type', db.String, nullable=True, unique=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
