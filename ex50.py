#framework -> a bunch of modules that make it easier for you to do something
#you need it to make a certain kind of application

#what's happening with http://localhost:5000/
#   browser makes putgoing network to own computer, request doesn't go far and is immediately received, localhost = own computer, port 5000
#   HTTP request afterwards, asking for root/URL, first URL of any website
#   bin/app.py bunch of functions paired to URLs, one we have is routing of / to hello_world(), whenever going to / flask will use hello_world
#   flask found routing to certain URL -> run that function, returns string for what Flask should send back to browser
#   flask finished request, sends response to browser -> seeing hello world
# -> base of world wide web

#fixing errors: NameError = greeting is not defined for example

#create basic templates:
#Hello World no good HTML file, -> needs properly formatted responses with HTML tags

#template other than normal HTML
#{{ greet }} is a placeholder for a variable you’ll pass to the template that customizes its contents.

#how does a template work
#   new variable render, stores results of render_template as string
#   render_template looks for template named index.HTML
#   browser hits root URL, flask runs hello world function, render_template gives string containing HTML markups
#   {% if greet %} -> if else with power to HTML, statement checks if greet exists, if it does -> renders the following, if not -> else
#   occurrences in your template of {{ greet }} are replaced by the value you passed into the template from your Python code
