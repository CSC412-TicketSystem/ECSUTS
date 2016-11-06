#Documentation for Connecting Django with MySQL database (using Anaconda & MAMP/LAMP)

##Installing Dependencies
1. Install the latest-stable version of Python (https://www.python.org/downloads/)

2. Install Anaconda (https://www.continuum.io/downloads) (because you are using anaconda, you don't have to use virutalenv or virtualenvwrapper)

3. Install Django (https://docs.djangoproject.com/en/1.10/topics/install/#installing-official-release)

4. Install MySQL on Linux (http://dev.mysql.com/doc/refman/5.7/en/linux-installation.html)
  * Install MySQL on Mac (https://dev.mysql.com/doc/refman/5.6/en/osx-installation-pkg.html)
  
5. Install mysqlclient (https://github.com/PyMySQL/mysqlclient-python)
  
##Creating Anaconda Environment
1. Create Conda virtual environment: `create conda -n (name_of_virtual_environment) python=(version) anaconda`

2. To activate conda virtual environment: `source activate (name_of_virtual_environment)`

3. To deactivate conda virtual environment: `source deactivate (name_of_virtual_environment)`

##Launching Webserver via MAMP
1. Launch the MAMP application and click on start server

2. (keep this connection on for the next part) Click on Open Webstart page

3. At the top tool bar click tools and then phpmyAdmin and there you will see the databases in phpAdmin. 
  * You can alter database information as well as query using phpmyAdmin or use WYSIWYG like mysql workbench or sequel pro (for Mac)

##Editing settings.py in Django project
1. (while in conda environment) Create a Django project: `django-admin startproject projectname`

2. Go to your project's settings.py file which would be located in: `/projectname/projectname/settings.py`

3. Edit the `DATABASE` section of the settings.py so that it looks like this:

```python
DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': '', #input the name of your database
      'USER': '', #enter the username (in most cases, it will be root)
      'PASSWORD': '',   #enter the password (in most cases, it may be root as well)
      'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',   #if on linux system and using LAMP, exchange MAMP for LAMP
      'PORT': '', #port number of your mySQL database
      'OPTIONS': {
          'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
       },
    }
}  
```
4. Save and exit settings.py and go back to the level of the directory that has `manage.py projectname`

5. Type in the following: `python manage.py migrate` in order for Django to connect to the database that you have created

6. Now type in the command line; `python manage.py runserver`, if it runs successfully, then your Django project is connected to a database and you can then create your django application using `django-admin startapp app_name`

7. If you have issues, make sure your `DATABASE` field is correct in syntax and what each field is assigned to.  Furthermore, look at the above steps to see if you have reviewed them carefully
