import sys
import unittest

from flask.cli import FlaskGroup
from cloudalbum import create_app
# from cloudalbum.database import create_table

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    # delete_table()
    # create_table()
    pass

@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('cloudalbum/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    # database.session.add(User(username='mario', email='super@mario.com', password='asdf'))
    # database.session.add(User(username='luigi', email='super@luigi.com', password='asdf'))
    # database.session.commit()


if __name__ == '__main__':
    cli()
