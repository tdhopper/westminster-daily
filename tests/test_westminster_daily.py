import datetime as dt

from flask_application import app


def test_daily_westminster_pages_exist():
    start_date = dt.date(2015, 01, 01)

    with app.test_client() as c:
        for days in range(365):
            date = start_date + dt.timedelta(days=days)
            month, day = date.month, date.day
            response = c.get('/{month:02d}/{day:02d}/'.format(month=month, day=day))
            assert response.status_code == 200


def test_daily_westminster_bad_days():
    with app.test_client() as c:
        response = c.get('/01/32/')
        assert response.status_code == 404
        response = c.get('/02/30/')
        assert response.status_code == 404
        response = c.get('/04/31/')
        assert response.status_code == 404


def test_daily_leap_day():
    with app.test_client() as c:
        response = c.get('/02/29/')
        assert response.status_code == 200