- Install python 3.12
- Db used is sqlite3

1. Create virtual env `Python -m venv venv`
2. Activate env `source venv/bin/activate`
3. Go to project `cd <project folder>`
4. Install requirements `pip install -r requirements.txt`
5. migrate db `python manage.py migrate`
6. run tests `python manage.py test`
7. runserver `python manage.py runserver`
8. APIs - 
- for filter blogs `curl --location 'localhost:8000/blog/?auther=1&created=2024-07-09'`
- create blogs `curl --location 'localhost:8000/blog/' \
--header 'Content-Type: application/json' \
--data '{
        "title": "Some blog 3",
        "content": "hjbkdsdfvcdfvclsd",
        "auther": 2,
        "created": "2024-07-02"
}'`