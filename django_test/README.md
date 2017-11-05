## Procedures before running:
1. create a python venv by yourself (I use python2.7.13)
2. pip install Django, mysqlclient
3. in the setting.py under mytestsite
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'DBproject',
          'USER': 'root',
          'PASSWORD': '123456',
      }
  }

change USER and PASSWORD to your own DB settings
