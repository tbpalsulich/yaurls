# yaurls
Yet another URL shortener: http://tspurls.herokuapp.com/RmtodQ

This is a simple Python 3 Flask application used to shorten URLs. The app uses a single Postgresql table to store a map from random hashes to URLs. You can run this locally or easily deploy to Heroku.

## Install and run locally
1. `git clone git@github.com:tpalsulich/yaurls.git`
2. `cd yaurls`
3. `virtualenv venv && . venv/bin/activate`
4. `pip install -r requirements.txt`
5. Create a Postgresql database named `yaurls`
   1. `sudo -i -u postgres`
   2. `createdb yaurls`
   3. `exit`
6. `python`
7. `from yaurls import db`
8. `db.create_all()`
9. `exit()`
10. `foreman start`

## Heroku
1. `heroku create`
2. `heroku addons:create heroku-postgresql:hobby-dev`
3. `git push heroku master`
4. `heroku run python`
5. `from yaurls import db`
6. `db.create_all()`
7. `exit()`
8. `heroku open`
