	Architect
=========

## Setup

    sudo apt-get install mongodb python-pip
    sudo pip install flask flask-script mongoengine flask_mongoengine

## Run

    python manage.py runserver

Go to [localhost:5000](http://localhost:5000) in your browser.

## Links

mongoengine inheritance

http://docs.mongoengine.org/en/latest/tutorial.html

create a blog

http://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/
https://github.com/rozza/flask-tumblelog

sql comparison

http://docs.mongodb.org/manual/reference/sql-comparison/

automatic versioning of documents - oh goodie!

https://github.com/thiloplanz/v7files/wiki/Vermongo
https://github.com/benjeffery/pycrud/blob/master/vermongo.py

pip install -r requirements.txt
pip freeze > stable-req.txt
http://codeinthehole.com/writing/using-pip-and-requirementstxt-to-install-from-the-head-of-a-github-branch/


all documents needs
* version
* scheme name - or maybe we apply this to the whole database (and history items)?! yes, this sound better
* 


## ApiResource

    ApiResource(Document):
    _id
    _versions
    _deleted
    
    # synthesized
    version
    latest_version = len(_versions)
    modified_by
    modified_at





## ApiAuthServer

    #login_log
    date
    user
    result
    
    #api_log
    date
    app
    user
    role
    result
    
    #sessions
    token
    user
    expiration
    
    #apps
    token
    name
    
    #app_roles
    app
    name
    type=all,black,white
    
    #role_list
    app_role
    user
    
    
    
    api -> authenticate()
