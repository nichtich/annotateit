from setuptools import setup, find_packages

setup(
    name = 'annotateit',
    version = '2.2.0',
    packages = find_packages(),

    install_requires = [
        'annotator==0.9.0',
        'Flask==0.9',
        'Flask-Mail==0.6.1',
        'Flask-SQLAlchemy==0.15',
        'Flask-WTF==0.5.4',
        'SQLAlchemy==0.7.5',
        'sqlalchemy-migrate==0.7.2',
        'itsdangerous==0.12',
        'decorator==3.3.2',
        'iso8601==0.1.4',
        'negotiate==0.0.1'
    ],
)
