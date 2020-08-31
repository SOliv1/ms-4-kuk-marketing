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
         
        pip3 install boto3
        pip3 install django-storages
   1.  
   1.  
   1.  
   1.  
   1.   `cp - r` means copy recursively
   1.   cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/*
## CREDits and  ACKNOWLEDGEMENTS  (Other website acknowledgemnts)       
1.  The whole website code was copied but from conception to completion and NOT cloned as a whole from the Code Institue Fullstack final e-commerce website.
    ACKNOWLEDGEMENTS and Credits go to ckz8780 Chris Zielinski who created the excellent Boutique Ado Website.
        Most of the products are taken from the C.I. dataset which originates from https://www.kaggle.com/  and modified to suit the purpose of this website.  
        I do not claim to make the code from this website my own. But I did build this website from conception to completion in an effort to understand the process more clearly.
        Any intention to pass off any code as my own is purely unintentional.
1.    Products and fixtures credits images 'Tailor Brands https://studio.tailorbrands.com/ : 
        *Brand-book-1_VvE5VhU.webp*, *Business-deck-1-1 (1).webp*, *Business-deck-1-1 (1).webp* 
        Also branding and marketing ideas are based the Tailor Brands website.
1.      New Products all credits go to: Cool wine accesories and branding image and copied text credits from https://www.igopromo.co.uk/
1.      New Products all credits go to: https://www.igopromo.co.uk/inspiration-pages/sustainable-products/bandana-rpet-multi-functional-scarf-all-over-printing/p4348-master
    
    
    
    ### font stories  
1.   
1.       
1.  
1.      

## Product app
1.     *Given to me by Kevin at C.I. tutor support* 
1.   The easiest fix would be to empty your DB on Heroku: https://stackoverflow.com/questions/4820549/how-to-empty-a-heroku-database
Then export the products from your local project to a fixtures file (Django can create the JSON files automatically for you):
python manage.py dumpdata products.product --indent 4              
1.      
1.      
1.                     
1.  
1.          
1.          
1.          
1.          