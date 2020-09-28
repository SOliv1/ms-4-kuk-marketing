# KUK Marketing

#### Table Of Contents
* General Information
* Live Demo
* UX Introduction
* User stories
* Wireframe Mockups
* Website & Database
* Accessibility
* Features
* Deployment
* Testing
* Credits
* Conclusion

###  LIVE DEMO CAN BE FOUND AT HEROKU: https://kuk-milestone-4.herokuapp.com/

### README  Further information and alternative view via LINK HERE
  README.md https://1drv.ms/w/s!AgMQTPoqZgRAjBzcw6gYVD7gImdt?e=5XbCvm
  
## UX Introduction - Platform for B2B lead 
A website where consumers can purchase with a budget in mind either upgrading and / or investing in a website package.  
This website celebrates the user's ability to evaluate and purchase products and services with a view to capture an online audience and ultimately promote and retain loyalty.
Encourage and promote the user update / upgrade in order captivate a target audience on desktop, mobile, and tablet. 
Drive leads to promote business awareness via website online-packages; purchase branded and non branded products to target audience.
The website is a B2C emotion driven and appeals to the benefits of users by encouraging interaction and engagement via contact forms with requirements dropdown box.
Ideal additions to this website: a gallery; social-media; newsletters; Skype, Zoom and other live streaming for on-line interaction between consumers and marketeers.
Join a community that drives sales, marketing, and product innovation and trendsetters driving growth on the internet.  
Translate business growth into sales and loyalty.

#### Ideal Customer:
##### Target businesses:  
* 'Start-Up business' operates on a budget and wants strategic direction.
* 'Inspire An Audience' Those who want to invest in a fullstack premium package. 
* 'Budget Aware' - Those who would like to upgrade to a package without fully investing in premium package.
#### Visitors to this website are looking for:
* Ideas that can be transformed into success for their startup business or keep on trend with what is driving growth sales via the internet.
* This website is designed for those looking to translate their expertise into a viable proposition for their business and make it a reality.
* Visitors can contact the website to discuss their objectives whether it be to build brand awareness, generate leads, or drive website traffic. The website designer can provide the format that is the `best fit`.
1. A new customer who wants to discover more about and potentially buy the products on offer via the website to promote their business. A complete package for budget minded startup business.
1. As a new visitor to the website I want to be able to navigate quickly and easily via the search box and can look up products by category / price / rating / name of product.
1. As an interested visitor / customer I want to follow the activities of this website on social media.
1. As an engaged customers I want to return to the website and potentially purchase the products and find out what else  is new and driving business success.  A contact form and newsletter will be set up for this. 
1. Provide *User-stories adding to the website to encourage new and returning customers.


## User Stories:
* As a customer, I want to be able to quickly look up the best products and services with a view to purchasing a complete website and branding startup package, so that I can order via the website from the company. 
I want to experiement with my ideas and engage with the web-company to find what suits or as they say `the best fit`: 
I want to edit / delete / and update with my own requriements by filling out the form and have them contact me with further information and ultimately purchase a suitable package to suit my budget. 
**Happy Customer**

* I love the look and feel of the website. It is clean and aesthetically simple to view and to use.  I can find my requirements from **KUKMarketing** and look forward to letting my `business shine!`
  *Satisfied Client 
  
* I like the website packages available and the opportuntity to come up with my requriements for the `best fit` for improving my current website. 
 * **Looking to Shine**
 
* I like the idea of buying products and services directly from the website - gettting the quoted price and ordering the products and services I want.  I can use a simple form to convey my requirements which will then be evaluated and then open up dialogue between KUKmarketing and myself the (potential)client. 
  **Propspective Client**
  
## KUKMarketing = Wireframes and Mockups:

*Please follow the link below to view README.md /wireframes and / Mockups*:

[cookCorner](http://github.com/SOliv1/ms-4-kuk-marketing/tree/master/readme)

			
## This Website & Database is heavily based on the Boutique-Ado e-commerce fullstack project.
I chose **postgres** for my project, to use and demonstrate as a powerful fullstack database together with AWS bucket S3 and IAM users.  This is recommended by **C.I.** in the course. It features the excellent Boutique-Ado online project which I have copied directly and modified to suit the purposes of my own fullstack website project.
I figured the ideas on this website were so excellent, how can one improve! I therefore have copied most if not all except 'Services App' which is my owm but once again inspired from other projects on the course;(see credits and acknowledgements at bottom of this page) from the Boutique Ado Fullstack full-functioning website,
which I found most interesting.  The challenge for me is to be able to build the website exactly as it is done in the videos.  It is tricky but satisfying once I finally completed it.  I then repeated this website for my own purposes, building at each stage from conception to complettion.
My website Database consists of *Pages (to meet CRUD requirements via the Product / bag and Checkout apps - Create Read Update Delete) in a database*. A highly scalable server which stores data in a non-relational format.


#### Add products via backend admin(‘Create’, 'Read', 'Update', 'Delete')
This is how admin-users add products to the database. It contains a simple HTML form to collect the field attributes we intend to store. 
The product collections are all categorised and stored in a json format and transferred to the database via STATIC and MEDIA files where it is stored remotely in a bucket at AWS SERVICES. The code is add . / commit -m "" / and push/ to GitHub and then channelled to Heroku which has been set up so that it automatically connects and should deploy automatically.  I set up my deployment fairly early in the build process in order to give my self
less pressure and more peace of mind and watch more clearly the build process.


## Accessibility 
The pages are asscesible via buttons on the *Home page* and a menu accross the top with dropdown navigational menus.  The website is mobile friendly as well as compatible across ipad through to full-desktop.
The about page can be accessed on the top right corner of the menu(home-page).  The contact page can be accessed via the 'Our Services' heading on the drop-down menu.

## Features
The main feature I am showcasing in this website is the CRUD FUNCTIONALITY.  The pages consist of the following:
* 
* 
* 
* List of products and services page **(‘Read’)*
* These pages display the products in the database. ( this being on home page Product Management Section*).  Accessed via a superuser with staff status given credetials from the IAM users at AWS where username/ emails and passwords are verified.  
  This is also accessed via the Users page on the built in django-backend admin-page.
* The *add_product* *(Add a product)* page which displays the form allows the user to add a new product and service to the database together with an image field and category and sku for identification purposes. 
* The *edit_product* page *(‘Update’)* page enables the user to update the text and the image field on the database.
* A page to edit an existing and update existing products. This looks exactly the same as the *add recipe* page, except this time, the form is pre-populated with values belonging to the product or service being edited.

Each Product or Service listed on the `home` page has an *edit button* that links to the `home` page.
Delete link for each product *(‘Delete’)*
Each product form (on the Product-Management link accessed via dropdown on the home page) has a *delete_recipe* button that links to the `delete view`*.

_*Please note :- In the *insert_product* function I have copied and tried to modify the *insert_product* imagefield 'custom-clearable' in order to insert and upload the images from an external computor.  Unfortunaley, I have not had much success as some images work on the uploading image section and others do not. I consulted tutors and they suggested I revisit the AWS section of the course. Please note this issue only occurs on the deployed heroku site. Add the products and the image fields.//

-----///---
        
    @app.route("/insert_recipe", methods=["POST"])
    def insert_recipe():
        recipes = mongo.db.recipes
        form_request = request.form.to_dict()

        ingredients_list = form_request["ingredients"].split("\n")
        instructions_list = form_request["instructions"].split("\n")

        the_recipe = recipes.insert_one(
            {
            "category_name": form_request["category_name"],
            "recipe_name": form_request["recipe_name"],
            "image_link": form_request["image_link"],
            "description": form_request["description"],
            "recipe_ingredients": ingredients_list,
            "recipe_instructions": instructions_list
            }
        )

        return redirect(url_for("view_recipe",
                                recipe_id=the_recipe.inserted_id))

I have attributed this in the credits section below.*_

## Deployment

#### Deployment to Github
* make sure the branch or folder as a publishing source exists in the repository. Example, before  publishing project site from the /docs folder on the master branch of that repository, 
  collaborator must create a /docs folder on the *master* branch of that repository.
* On GitHub, navigate to site's repository.
* Under repository name, click  Settings.
* Under "GitHub Pages", use Source drop-down menu and select a publishing source.
* More information found on Github:
  https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-    source-for-your-github-pages-site

#### Cloning a repository to GitHub Desktop
I clone one of my Flask mini projects to deploy locally on GitHub desktop. 
On GitHub, I navigate to the main page of the repository.
Under my repository name, I click to clone my repository in Desktop. I follow the prompts in GitHub Desktop to complete the clone.  

###  Basic set up for my project
*(see *CRUD functionality notes further down page*)
pip3 install flask
pip3 install flask_pymongo
pip3 install PyMongo
pip3 install dnspython
pip3 freeze > requirement.txt
python3 app.py to run the server and test

#### Deployment to Heroku
Kindly given to me via Anna Greaves(tutor)as I had trouble logging in with previous commands.

#### First we:
 npm install -g heroku

Then, to login, use the command:
heroku login -i * 

#### Clone the repository
Use Git to clone ms-cook-corner's source code to your local machine.
(e.g. GitHub Pages or Heroku).
When trying to deploy my project to Heroku I hit a bug *- AttributeError
AttributeError: 'NoneType' object has no attribute 'categories'*
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

To resolve this I ...
Different values for environment variables (Heroku Config Vars)?
Different configuration files?

$ heroku git:clone 
Deploy changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

#### Deploy changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am ""
$ git push heroku master

**Flask** I add all html pages so they can be rendered in *Flask to the Folder Name "templates"*.  Eventually we will be able to deploy this website on Heroku.  More on this later.
I have rendered the home, about and contact pages using flask and basic jinga template language to make it easier to type the paths and render each of the templates.
for example: we add inside the
 *"@href put {{ url_for('index') }}"*. We also do the same for *"about: {{ url_for('about') }}" and "contact: {{ url_for('contact') }} pages*. 
Essentially, Flask looks up our index() and about() views and injects the URL for it into the href.  All works as expected.
Another handy feature of Flask is the ability to detect any errors we might make such as *writing the url for 'home' instead of the url for 'index'*.  Home does not exist but index does and so indicates this error.

**Template Inheritance** Inherits code from other templates, creating a *base template and using {% extends 'base.html' %} in a child template*.

**Passing Data from View to Template**  A very useful feature of using frameworks to actually set data on the server side and get it coming through to the client.
Benefits of using frameworks is the fact that we can actually get server-side code to provide the frontend with data. 
Example:- Go to *app.py*. Then add argument page_title="About"
to return serverside code to the frontend.
@app.route('/about')
def about():
    return render_template("about.html", page_title="About")

**Reducing repetition**  using the *{% %} notation* template tags for statements (not for expressions).
allowing us to use a *for loop* inside our HTML.  Standard Python *for loop* for number in list_of_numbers.
and then need to supply an {%end for%} so that the templating language knows where the *for loop* stops.
Example:- 
{% for number in list_of_numbers %}
    <p>{{ number }}</p> 
{% endfor %}

**The if template tag**
I use `if` statements inside my template. By using the example here:
 {% if some_condition %} tag and the closing {% endif %} tag. 
See this in action by going to *About* section of website.

**Getting Themes**  I have chosen the **Start bootstrap theme *Clean Blog* as featured in *CI lessons on Flask Framework*, for a multi-page website. 
I download the theme by copying the link then go to terminal and mkdir, then cd into it and wget the https://startbootstrap.com/themes/clean-blog/
I then style accordingly.   Unzip package with the *unzip gh-pages.zip* command.

## Existing Features - C.R.U.D. - allows users to add a recipe to store in database, by having them fill out the form.
*CREATE - Add the recipe by following the instructions.  Whole sections can be inserted by following the recipe page setup.
	  add recipe category, description, ingredinents, instructions.  MDB Atlas cleverly preserves the layout of the recipes     	    that are being populated on the database.

READ -    Read through and view all the recipes as a collection or view each recipe individually by clicking buttons. 

EDIT &
UPDATE -  Click the button to edit the page and follow the instructions there.  Then click the UPDATE button 															to save changes.  Then return to 	   Home page to add another recipe by clicking the CREATE BUTTON again.

DELETE	  Press the delete button to undo changes.  


## Existing Features  - An Example
### Feature 1 - allows users X to achieve Y, by having them fill out Z
Below is an example of a user friendly feature for user(X) to achieve(Y)a recipe collection by filling out their favourite recipe/s and sharing on a user friendly website(Z). 
*Please see modified code example below under the heading:-*
at **Further Inspiration and insert recipe idea from following CI Student website**
_Further Inspiration from following CI Student website:_
https://github.com/3PU/cook-book-milestone-project
*code snippets - *modified code in my project app.py - copied from **cook book** (app.py).*  
_*Please note this is also attributed in the credits section.*_

I want to achieve a seemless userfriendly experience whereby a user can easily copy and paste recipes with a minimum of fuss 
and without having to style the recipes in order to save time.  *Editing and updating*  can be done if and when needed in the users own time.
I tried using semi colons and commas to achieve the seemless new line effects in my insert_recipe function, but these did not work well for me so I copied the idea of newline "(/n)" which suits my purposes to easily *insert recipes* and I think to the satisfaction of the end-user.    
					
### Features Left to Implement:
			* Search box to search recipes.
			* Sort code to sort through recipes and categories
			* Login form with password so users sign in securely using the password to access the database.	
			* More links to other companies specialising in Mason Cash and other British products. 						* Links to other specialised recipe sites appropriate to this website.
			* Contact Form to sign up for newsletters.
			* Another possible  feature to be incorporated is to be able to *vote* for favourite recipes and rate			          a specific recipe.
			* Social media and blogs
			* Chat page / Forum

#### Technologies - a possible sample code to use in future:
>  *login snippet* - copied from https://github.com/joanms/recipe->database/blob/master/app.py:
>	if login_user:
            ### If the username is in the database, hash the password entered in the form and 								compare it with the hashed password in the database for that user
            		if bcrypt.hashpw(request.form['password'].encode('utf-8'), 			 			>login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        		### The user sees this message if the username and/or password are invalid
        				flash('Invalid username/password combination.')
    							return render_template('login.html')
#### Libraries / requirements:

		*dnspython==1.16.0
		*Flask==1.1.1
		*itsdangerous==1.1.0
		*pymongo==3.10.1
		*Werkzeug==1.0.0
		*bison==0.1.2
		*click==7.1.1
		*Flask==1.1.1
		*Flask-PyMongo==2.3.0


#### Links to libraries
	
*	https://pypi.org/project/Flask-Bootstrap4/

*	https://www.fullstackpython.com/flask.html

*	https://flask.palletsprojects.com/en/1.1.x/

*	https://www.mongodb.com/cloud/atlas

*	https://www.python.org/


### For CRUD FUNCTIONALITY 
Install flask: pip3 install flask
Create a python file: app.py
Install pynthon: pip3 dnspython

create instance of flask:   import os

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### JQuery
The project uses JQuery to simplify DOM manipulation.

##Testing
* https://validator.w3.org/nu/#l118c6 - There is further testing wihich needs addressing. 
127.0.0.1 - - [20/Mar/2020 12:05:52] "GET /get_categories HTTP/1.1" 500 -
Encountered:
* 505 error indicates a temporary problem, and sometimes that problem is very temporary. A site might be getting overwhelmed with traffic, for example. So, refreshing the page is always worth a shot. Most browsers use the F5 key to refresh, and also provide a Refresh button somewhere on the address bar. It doesn’t fix the problem very often, but it takes just a second to try.
* Firefox / Chrome / Edge / - All appear to be working as so are the links.

#### Cloning a repository to GitHub Desktop
I clone one of my Flask mini projects to deploy locally on GitHub desktop. 
On GitHub, I navigate to the main page of the repository.
Under my repository name, I click to clone my repository in Desktop. I follow the prompts in GitHub Desktop to complete the clone.  

(e.g. GitHub Pages or Heroku).
When trying to deploy my project to Heroku I hit a bug *- AttributeError
AttributeError: 'NoneType' object has no attribute 'categories'*
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

To resolve this I ...
Different values for environment variables (Heroku Config Vars)?
Different configuration files?

#### Bugs
While I was trying to connect sensitive info from my flask app into a env.py file, I got the following error:

Traceback (most recent call last):
  File "/workspace/qc-metrics-analyser-4/app.py", line 7, in <module>
    import env
  File "/workspace/qc-metrics-analyser-4/env.py", line 6, in <module>
    os.environ.get["MONGO_URI"] = "mongodb+srv://seqMetRoot:dbconnection"
TypeError: 'method' object does not support item assignment

I managed to fix my problem with my env.py file. I was incorrectly using the get method. os.environ.get["MONGO_URI"] should have been os.environ["MONGO_URI"] .

Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Slack community - *various borrowed code snippets* See below credits. I often change them
                     when some of the code did not work for me.  However it did
                     lead me on to thinking again about seeing a line of code highlighted in an error I had been seeing, and checking at the bottom of my jinga codes for these errors.
                     This experience gives me more confidence to debug code.

 #### Dashboard - based on:- 
 https://github.com/PrettyPrinted/building_user_login_system/blob/master/start/templates/dashboard.html

#### Recipes Manager - is based on the basic CRUD functionaity putting it altogether mini project featured in Code Institute DataCentric Module
with recipes made up by me as an example. T This feature is a basic functioning recipe website.  New features can easily be added to improve the user experience and functionality.

#### Technologies use and Atlas MongoDB on recommendation by Code Institute for educational purposes.  A good grounding to build upon.
Create recipes by 
Adding categories 
Adding recipes
Editing recipes
Updating recipes
Deleting recipes
Adding category
Editing category
Updating category
Deleting category


#### Excellent project guide by Code Institute Mentor Brian Machira - thank you for his guidance and support.
https://docs.google.com/document/u/0/?authuser=0&usp=docs_web

#### Further Inspiration and ideas from following CI Student website:
insert_recipe code copied and modified from this code below:-

'''
    @app.route("/insert_recipe", methods=["POST"])
    def insert_recipe():
    recipes = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = form_data["ingredients"].split("\n")
    instructions_list = form_data["instructions"].split("\n")

    the_recipe = recipes.insert_one(
        {
         "category_name": form_data["category_name"],
         "recipe_name": form_data["recipe_name"],
         "image_link": form_data["image_link"],
         "description": form_data["description"],
         "ingredients": ingredients_list,
         "instructions": instructions_list
        }
    )

    return redirect(url_for("view_recipe",
                            recipe_id=the_recipe.inserted_id))
'''                            
`https://github.com/3PU/cook-book-milestone-project`




#### The text for section "About" *history* was copied from the Wikipedia article https://en.wikipedia.org/wiki/Mason_Cash

#### Media
The photos and credits obtained and used in this site were obtained from *Mason Cash ...*
e.g. media - https://www.masoncash.co.uk/media/bannerslider/a/m/amazon-2.jpg

#### Acknowledgements
I received inspiration for this project from:- 

- "*Mason Cash - Buy British*
-   Brian Machira - *CI Mentor*
-   Anthony Herbet-*Pretty Printed, Flask Extensions videos'

- Slack community - *various borrowed code snippets* which I then modify to suit my purposes, although
                     some of the code did not work for me I had to rethink how to improve this.  However it did
                     lead me on to thinking again about seeing a line of code highlighted in an error that i had been    			     		      seeing, and checking at the bottom of my jinja codes for the errors.
                     It also gives me extra confidence to debug code.  


#### Family Hub - more ideas from this website created by Anna Greaves
https://github.com/AJGreaves/familyhub/blob/master/config.py    
Layout ideas / organisation for my website e.g. config.py, pages for my templates.
####README.md inspiration Anna Greaves - Family Portrait.
```

		     
## Conclusion	     
Overall I feel satisfied with my project and enjoyed creating it despite some issues along the way.  It was certainly challenging but I think the effort was worth it.
