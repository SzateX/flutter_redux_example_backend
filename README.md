# flutter_redux_example_backend

This project is an example backend for: https://github.com/SzateX/flutter_redux_example, which is part of an article on Asseco Technology Blog: https://pl.asseco.com/kariera/blog/

## DO NOT USE THIS CODE IN PRODUCTION!

## How to run
1. Install required packages
```bash
pip install -r requirements.txt
```

2. Apply migrations to the database (sqlite)
```bash
python manage.py migrate
```

3. Seed the database with some data
```bash
python manage.py seed
```

4. Run the server
```bash
python manage.py runserver
```