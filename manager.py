from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/index')
def index():
    return 'index'
#1
if __name__ == '__main__':
    manager.run()