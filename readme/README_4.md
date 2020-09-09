  1.  `alt + up/down arrows` to move a line or block of code up or down
        `alt + click` to select multiple regions
1.      
1.   pip3 install django-crispy-forms 
     pip3 install django-crispy-forms

 ## Deploying to heroku
1.        pip3 install pip3 install whitenoise
           pip3 install gunicorn  

1. ` echo "env.py" >> .gitignore `
    ` nano .gitignore ` to check that the file is still there (then exit out) by pressing enter 
1.          `git status ` 
1.          
1.          
1. 
 # Needed to login by username in Django admin, regardless of `allauth`
    

    # `allauth` specific authentication methods, such as login by e-mail
    '
##  Deploying to heroku
    1.  
   1. 
   1.  To check heroku logs on the gitpod terminal:
       follow these steps f you quit the server with Ctrl+C then type
    1.  `heroku login -i`
    1.  `heroku config:set DISABLE_COLLECTSTATIC=1 --app kuk-milestone-4`
        and sign in, then run:
        heroku logs --tail -a kuk-milestone-4`
        Go to AWS login and create a bucket then the bucket policy and the user'
        S3 and then to IAM 
        pip3 install django dj-database-url
        pip3 install boto3
        pip3 install django-storages
   1.  
   1.  
### Bugs and Problems I encountered whilst building this website:

#### Merge isssues 

I had two websites going simultanously as I built this website mainly when one failed me I would go with the other one.  But I found out that perhaps this is not such a good idea as when it came to merging the websites
to the master, I encountered *merge issues*.  I have done this procedure on my past websites and have not had much of a problem with merging but this time I did.  This is probably due to the complexity of the 
website which I guess I shoud have realised.  I did try the following code to debug from the C. I. Troubleshooting tips:

>>If you’re stuck in an editor, don’t panic -
Less - “less” is a pager program that may automatically open on the command line whenever you ask to read a very long file or output (e.g. when using “git log” on a repository with lots of history).
You can use the arrow keys or the page up/down keys to scroll around in Less. You can also use the “/” key to search for a specific part of the text and the “n” key to go to the next match.
Use the “q” key to quit Less.
>

   1.  
   1.   `cp - r` means copy recursively
   1.   cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/*
#   CREDITS AND ACKNOWLEDGEMENTS

## CREDits and  ACKNOWLEDGEMENTS  (Other website acknowledgemnts)       
1.  The whole website code was copied from conception to completion and NOT Cloned( as a whole).   Each page was copied and modified to suit the purposes of my website, 
    from the *Code Institue(C. I.) Fullstack final e-commerce website*.
    Other ideas and layouts came from my previous milestones:-
     Cook Corner(3) 
     and 
     Procol Harum(1) which in turn were also based on the excellent C. I. mini projects and websites which I acknowledge in  my previous merits and acknowledgements.
     Thorin and Company and 
     Putting it altogether mini projects.

### ACKNOWLEDGEMENTS and all  Credits go to *ckz8780 Chris Zielinski* who created the excellent *Boutique Ado Website*.
1.      Most of the products are taken from the C.I. dataset which originates from https://www.kaggle.com/  and modified to suit the purpose of this website.  
        I do not claim to make the code from this website my own. But I did build this website from conception to completion in an effort to understand the process more clearly.
        Any intention to pass off any code as my own was and is purely unintentional.
1.      The Slack Community for any questions queries and for helping out whenever I need it.
1.      Products and fixtures credits images 'Tailor Brands https://studio.tailorbrands.com/ : 
        *Brand-book-1_VvE5VhU.webp*, *Business-deck-1-1 (1).webp*, *Business-deck-1-1 (1).webp* 
        Also branding and marketing ideas are based the Tailor Brands website.
1.      New Products all credits go to: Cool wine accesories and branding image and copied text credits from https://www.igopromo.co.uk/
1.      New Products all credits go to: https://www.igopromo.co.uk/inspiration-pages/sustainable-products/bandana-rpet-multi-functional-scarf-all-over-printing/p4348-master    
1.      Other website Ideas and inspiration - https://www.walkeragency.co.uk/workThan
1.      The fantastic tutors for their unvaluable assistance and 
1.      Student Care for being so encouraging when I felt like giving up at times.
1.      Finally my Family deserve a mention for supporting me whilst I did this course and for that I thank you for being there.       
1.  
1.    * Product app Tutor suggestions from support Tutor*
1.     *Given to me by Kevin at C.I. tutor support* 
1.   The easiest fix would be to empty your DB on Heroku: https://stackoverflow.com/questions/4820549/how-to-empty-a-heroku-database
Then export the products from your local project to a fixtures file (Django can create the JSON files automatically for you):
python manage.py dumpdata products.product --indent 4 
        Also django documentation:             
1.      django documentation: creating forms for the database:
        https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields
1.      
1.                     
1.  
1.          
1.          
1.          
1.          