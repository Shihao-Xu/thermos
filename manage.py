from __init__ import app, db
from models import User
from flask_script import Manager, prompt_bool


manager = Manager(app)


@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username='reindert', email='reinder@wef.com', password='test'))
	db.session.add(User(username='reinrt', email='reiner@wef.com', password='test'))
	db.session.commit()
	print 'Iinitialized the database'


@manager.command
def dropdb():
	if prompt_bool(
		"Are you sure you want to lose all your data"):
		db.drop_all()
		print 'Dropped the database'

if __name__ == '__main__':
	manager.run()