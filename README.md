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
            
            This copies or the allauth templates in the packages so we can style them at will.
1.  Getbootstrap.com > go to documentation and copy the starter template 
    
    ### font stories  
    *About Roboto
        Roboto has a dual nature. It has a mechanical skeleton and the forms are largely geometric. At the same time, the font features friendly and open curves. While some grotesks distort their letterforms to force a rigid rhythm, Roboto doesn’t compromise, allowing letters to be settled into their natural width. This makes for a more natural reading rhythm more commonly found in humanist and serif types.

        This is the regular family, which can be used alongside the Roboto Condensed family and the Roboto Slab family.
        <addr>font-family: 'Montserrat', sans-serif;</Addr>
        <Addr>-family: 'Roboto', sans-serif;</Addr>

        To contribute, see github.com/google/roboto*
1.  
1.      <addr>The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to design this typeface and rescue the beauty of urban typography that emerged in the first half of the twentieth century. As urban development changes that place, it will never return to its original form and loses forever the designs that are so special and unique. The letters that inspired this project have work, dedication, care, color, contrast, light and life, day and night! These are the types that make the city look so beautiful. The Montserrat Project began with the idea to rescue what is in Montserrat and set it free under a libre license, the SIL Open Font License.
            This is the normal family, and it has two sister families so far, Alternates and Subrayada. Many of the letterforms are special in the Alternates family, while 'Subrayada' means 'Underlined' in Spanish and celebrates a special style of underline that is integrated into the letterforms found in the Montserrat neighborhood. Updated November 2017: The family was redrawn by Jacques Le Bailly at Baron von Fonthausen over the summer, and the full set of weights were adjusted to make the Regular lighter and better for use in longer texts. In fall, Julieta Ulanovsky, Sol Matas, and Juan Pablo del Peral, led the development of Cyrillic support, with consultation with Carolina Giovagnoli, Maria Doreuli, and Alexei Vanyashin.

            The Montserrat project is led by Julieta Ulanovsky, a type designer based in Buenos Aires, Argentina. To contribute, see github.com/JulietaUla/Montserrat
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,400;1,100;1,200;1,300;1,600&family=Roboto:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
            CSS rules to specify families

            font-family: 'Montserrat', sans-serif;
            font-family: 'Roboto', sans-serif;</addr>

## Home app
1.      `python3 manage.py startapp home`
                mkdir -p home/templates/home
1.      add the home app : `python3 manage.py startapp home`
1.      then create a templates directory in the home app > mkdir -p to create parents as required.
                    `mkdir -p home/templates/home`
                        And then right-click the inner *home directory*, new file and create *index.html*

1.          *extend the base template with extends base.html
                And load the static tag with load static, so we can use static files as needed.
                Lastly, we just need a content block with some content in it. So let's start with block content.
                And inside that, I'll just add a simple h1 with class equals display-4 and text-success
                to ensure bootstrap is working.  And I'll add the text it works.*
1.          *view* to render this template so let's head into **views.py*
                        And define an index view.
                        Which will simply render the index template.
1.          copy our project-level urls.py
                        Create new file in the *home app*, called *urls.py*
                        And paste it in to use as a shell
                        take out 'include' here.
                        And add one empty path to indicate that this is the route URL.
                        to render views.index. With the name of 'home'
                        then 'import views' from the current directory here at the top.
                        save that.
1.          go back to the *project level URLs file* and include the *home URLs*
                        The very last thing we need to do is add the 'home app' to installed apps in 'settings.py'
                        And then wire up our template directories.
                                Add home to installed apps
                                And then add both the route templates directory.
                                And  custom allauth directory to the template dirs setting
                                With that finished save and test it out
                                start up the development server.
                                Open the project.
                                And we land on our home page with it works, rendered in the correct bootstrap styles.
                                Stop server and commit the changes "add home app and templates"
1.          set up the *products app* - load in some products.
                                start by copying in the collection of product images.
                                We pruned these from a data set at kaggle.com which is a great provider of
                                free sample data for use in all sorts of industries.
                                create the products app using python3 manage.py *startapp products^
                                *python3 manage.py startapp products*
                                add this app to installed apps in settings.py
                                make a folder called fixtures inside the products app
                                drag and drop a couple of JSON fixture files in here
                                one for categories and one for products
                python3 manage.py startapp products

1.          Add to installed apps in settings.py mkdir products/fixtures

                                Add categories and products json https://jsonformatter.org/ to validate

                                Go to models.py and add code There - python3 manage.py makemigrations --dry-r dry run

                                pip3 install pillow

                                dry run again...

                                python3 manage.py migrate --plan

                                python3 manage.py makemigrations

                                python3 manage.py migrate then... -python3 manage.py loaddata categories python3 manage.py loaddata products

                                check it out - python3 manage.py runserver - go to admin

                                products admin
                                mkdir -p products/templates/products

                                file = products.html

1.          we're creating that inner products directory to make
                                sure that django knows which app these templates belong to.
                                In case any of them end up having the same names as other templates.
                                And let's now create a products.html inside that directory.
                                And copy the content of the home template in as a shell.
                                The products template will still extend base.html
                                And will still require static files as well as the page header
                                python3 manage.py runserver                




[![Build Status](https://travis-ci.com/SOliv1/ms-4-kuk-marketing.svg?branch=master)](https://travis-ci.com/SOliv1/ms-4-kuk-marketing)