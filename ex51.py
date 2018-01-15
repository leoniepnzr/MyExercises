#how the web works

#type in url to browser, sends request to computers network interface (software/hardware responsible for data packages over network)
#request in global network, eventually routed to remote computer, where another server receives request
#once request data is received and accepted, gets digested by external web application and Python code rund function for url that was requested
#response comes out of Python, when returning it at end of function and gets send out again
#network interface of server packages up response, sends it over internet
#response routed to computer, network interface unpacks data, gives back to browser

#browser = software that you’re using every day to request and view web sites, for taking URLs, sending out to server,coming back file = response
#address = normally URL, http=protocol, language used=HTTP (also FTP), www.....com = hostname, IP address=indentifies computer, /.../ = trailing path
#connection = port neccessary, connects to port, browser is reading and writing from a data line connecting your computer to a remote server
#request = connection resource with address you gave, asks for resource(file), /book/-> you want resource behind /book/, request message -> should look like files
#server = computer at other end of line with pieces of software, Flask ->  knows how to take requests, and how to return resources that you craft using Python
#response = outcome, what's sent back from browser, files have to be sent back wrapped in a special HTTP “header” so that the browser can know what it’s getting back and decode the incoming data appropriately

#request.args.get -> to get user data sent from the browser
#request is a global variable, object containing  request message sent from browser to server
#args is dictionary containing all user data contained in the URL query string (everything after ?)
#name will then be set with name (can also be greet=Hola, as many as you want)
#request import!!!!!!!

#creating HTML forms
#using URL string for input is not the handiest way
#solution: POST form (HTML file with <form> tag in it, for creating user input fields)
#when using POST -> no query string
#terminal: two requests, GET and POST
#-> working because of <form action=”/hello” method=”POST”> -> collect data from user with form fields, send them to server with POST (hides from string), sends all to /hello URL (in action=”/hello”)
#two functions: one for GET, one for POST -> which runs which: chosen by @app.route
#@app.route has two arguments, methods=takes list of strings with all requests

#new application:
#browser hits application with GET, uses hello_get function for GET requests with going to /hello -> runs and returns rendered hello_form.html as response
#fill out form, <form> sends data to server as POST
#hello_post runs for new request

#templates into reusable layouts
#with inheritance which allows you to make a master HTML layout file that can be extended by other files, only filling in the parts that need to be unique
#two new commands in template (layout) -> block and endblock define a named block of code that can be replaced by templates that extend this one
#{% extends "layout.html" %} tells the template system that these files will extend layout.html, allowing you to use that file as a master layout and fill in its block definitions as you see fit

#testing forms
#treating app.py like a module, importing whole Flask application object
#calling test_client() method -> create a testing client object for me to use (fake web browser)
#two methods for test client client.get(path=’/’, headers=None) or client.post(path=’/’, data=None, headers=None)
#data argument = dictionary of name:value pairs will be passed to your app
#works without actually running an active web server, so you can run your automated tests while simultaneously using your browser to test a running server
#to validate responses: assert_response utility function, signature: ---assert_response(resp, contains=None, matches=None, headers=None, status=200, mime=None)
#after checking responses for get and post other arguments you can check
#status parameter for check for specific status code
#here: checking 404, /hello works with get and post
