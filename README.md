  1.  pip3 install django
1.  django-admin startproject kuk_marketing .
1.  python3 manage.py migrate
1.  python3 manage.py runserver
1.  touch .gitignore
1.  python3 manage.py runserver
1.  python3 manage.py migrate
1.  python3 manage.py createsuperuser
1.  git remote -v (we are already linked to github)
1.  pip3 install django-allauth
1.  configure settings

    ```AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ]

    1.  Add site_id = 1  underneath the authentication backends.
   1.  configure urls
   1.  python3 manage.py migrate
   1.  python3 manage.py runserver
   1.  navigate to accounts/login and login and add superusers and test
   1.  logout and you should be redirected to home page
   1.  set up a base template with bootstrap
   1.   `cp - r` means copy recursively
   1.   cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/*
1.  
1.  
1.  
1.  
1.  
1.  
1.
1.  
1.  
1.  
s
