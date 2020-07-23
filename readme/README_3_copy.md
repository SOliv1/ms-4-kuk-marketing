 ## Toasts 
    https://getbootstrap.com/docs/4.5/components/toasts/
    
 1.         Inside the main templates/includes folder let's add an additional subfolder to contain all the toasts
                    These toasts will be small HTML snippets that will pop up when a user performs an action
                    such as adding something to their shopping bag.
                    success toast inside a file called toast success.html.
                    structure for this comes from the bootstrap documentation.
                    start by just pasting it in from the completed project.
                    Almost everything here is straight from bootstrap. With the exception of our custom toast class.
                    -two divs at the top will just add a little extra visual touch to the top of the notification.
                    -toast is organized into a header and a body.
                    -header has a heading on the left and a close button on the right.
                    - data auto-hide and data dismiss attributes are required
                            to prevent auto-hiding the notification after a few seconds.
                            And instead, give the user the ability to dismiss it on their own.
                    -In the body of the toast is the message template variable.  going to be included in the message container in the base template.
                        - first copy this code and create a similar one
                        -for errors warnings and info using the standard bootstrap classes.
                        -copy the exact same code into three appropriately named files.
                        -And change the relevant classes.
                        -one toast error. And it will use the bootstrap danger class to make it red
                        -this one toasts info.  use the info class.
                        -this one toast warning. Which will use the warning class.
                        -save and head to base.html.
                        - find the message container toward the bottom of the page.
                        -inside  message container, we'll want to iterate through any messages
                        -sent back form the server and render one of these includes.
                        -(to demonstrate just include includes/toasts/toasts_success.html
                            and then go to the add to bag view in the bag app)
    1.  import the product model and also the messages framework
                        from Django.contrib here at the top.
                        - to demonstrate how these messages will work.
                        - first get the product at the top of the view here.
                        - then use the messages dot success function.
                        -to add a message to the request object.
                        -and use some string formatting to let the user know they've added this product to their bag.
                        - next piece of the puzzle is to use the bootstrap JavaScript to show the toast.
                        -which can be done in the post loadjs block of base.html.
                        -all have to be done is add a little JavaScript. To call the toast method from bootstrap. With an option of show.
                        -on any elements with the toast class.
                        -by putting this in the base HTML template will ensure that every page that loads
                            will immediately call the show option on all toasts that have been rendered in the messages container
                        -this also explains why for all this time we've been including block dot super in
                            our templates when overriding the post loadjs block.  we ensure that any JavaScript we've written in the templates that extend this one
                        -this will ensure it won't overwrite this call to show all the toasts.
                        -last - add one more setting to *settings.py* to tell it to store messages in the session this is
                                often not a required step because there is a default which falls back to this
                                storage method but *NOTE - due to the use of git pod in these recordings it's required
                                for us*
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
   1.  
   1.  
   1.  
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
1.  
1.          
1.          
1.          
1.          