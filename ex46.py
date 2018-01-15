#namespace: Both can implement a function named random and there won’t be any
#problems knowing which one you want to use because you always have to tell python
#exactly which module’s random function you’re referring to. In computer science
#lingo we say that each module has its own namespace.

#modules: The module name is always the name of the file itself, and defines a
#namespace. So the statement from mymodule import foo will bring the function foo
#out of the namespace of mymodule and bring it into your current namespace. That is,
#assuming Python can find the module file mymodule.py that defines foo.

#packages: Everything you install via conda or pip is a package. A package is just
#a bunch of nested module files, inside a directory structure with some small extra
#details thrown in. Packages let you have more complex namespaces with multiple levels of depth.
#->  __init__.py files are doing in the directory structure. In order for Python
#to be able to identify directories that should be treated as part of the namespace(s)
#of a package, you always need to put an empty file named __init__.py inside each
#directory that should be included in the namespace.

#when setting up a new project: copy of template directory, change name of root folder to
#name of project, rename with mv the name directory to be name of project -> there you put all modules,
#edit setup.py with metadata of project
#rename NAME_tests.py with proejct name for NAME
#running nostetests again to see if everything still works fine
#scripts inside bin directory when starting to code
#bin folder: a standard place to put scripts that are run on the command line -> NOT a place to put modules
