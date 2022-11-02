# Part 1 set up Flask app
"""OpenAQ Air Quality Dashboard with Flask."""
import openaq
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)

api = openaq.OpenAQ()


def get_results(city='Los Angeles', parameter='pm25'):
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    data = body['results']
    dates = []
    for a in data:
        for x, y in a.items():
            if x == 'date':
                dates.append(y)

    utc_datetime = []
    for b in dates:
        for m, n in b.items():
            if m == 'utc':
                utc_datetime.append(n)

    value = []
    for c in data:
        for q, p in c.items():
            if q == 'value':
                value.append(p)

    la_data_values = list(zip(utc_datetime, value))

    return la_data_values


@app.route('/')
def root():

    return str(Record.query.filter(Record.value >= 18).all())


class Record(DB.Model):
    # id (integer, primary key)
    id = DB.Column(DB.Integer, primary_key=True)
    # datetime (string)
    datetime = DB.Column(DB.String)
    # value (float, cannot be null)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f"<{self.id}: {self.datetime}, {self.value}>"


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    data = get_results(city='Los Angeles', parameter='pm25')
    index = 1
    for z in data:
        record = Record(id=index, datetime=z[0], value=z[1])
        index += 1
        DB.session.add(record)
    DB.session.commit()

    return 'Data refreshed!'


# @app.route('/greater_than_18')
# def greater_than_18():
#     over18 = Record.query.filter(Record.value >= 18).all()
#     return str(over18)
