"""
Module basics

The interactive Python interpreter provides the simplest way to run Python code. 
However, once the interpreter is closed, all defined variables, functions, and classes are lost. 
To preserve and reuse code, programmers usually write Python code in a file and pass that file to the interpreter. 
Such a file is called a script.

In practice, programmers often repeat the same functions across different scripts, or they end up with overly long, hard-to-maintain code. 
To address this, Python provides modules—files containing reusable Python code that can be imported into scripts, other modules, or the interpreter itself. 
Importing a module means executing its code and making its definitions available to the importing program.
A module file must have a .py extension for the interpreter to recognize it. 
The module name used in an import statement should match the filename without .py. 

For example, if the file is HTTPServer.py, the correct statement is import HTTPServer. 
Import statements are case-sensitive: import ABC and import aBc refer to different modules.
The interpreter also needs to know where to locate the module. The simplest approach is to place modules in the same directory as the running script, though Python can search the system more broadly. 
It is considered best practice to place all import statements at the top of a file. 
This makes dependencies—external modules a program relies on—easy for readers to identify.

Importing a module
When Python encounters an import statement, it follows this process:
- It checks whether the module has already been imported.
- If yes, the existing module object is reused.
- If not, a new module object is created and added to sys.modules.

The module’s code is executed within this new module object’s namespace.
The sys.modules dictionary, part of Python’s standard sys module, keeps track of all loaded modules. 
A module object is essentially a namespace containing all definitions from the module. 
If a module is already in sys.modules, the interpreter simply reuses it; otherwise, it executes the module code and stores the resulting namespace.
For example, executing import HTTPServer creates a new module object for HTTPServer and runs its code. 
If that code itself contains import webpage, Python checks whether webpage is already loaded. If not, a new module object is created, added to sys.modules, and its code is executed. 
Any definitions made inside webpage are stored in its namespace. Once webpage finishes loading, execution of HTTPServer continues, adding its own definitions. 
If the importing script later uses import webpage, Python will reuse the already-loaded module rather than executing it again.
"""

"""
How Python Finds and Imports Modules
When an import statement is executed, Python begins searching for the corresponding file. The search order is as follows:
- Built-in modules – Python first checks if the requested name matches a built-in module, which comes preinstalled (e.g., sys, time, math). 
If a match exists, the built-in module is loaded.
Caution: if you name your own module with the same name as a built-in one, the built-in takes precedence.
- Directories in sys.path – If no built-in match is found, Python searches the directories listed in sys.path, a variable defined in the sys module. 
By default, sys.path includes:
- The directory containing the executing script
- Directories specified in the environment variable PYTHONPATH
- The directory where Python itself is installed

For small programs, placing modules in the same directory as the script is sufficient. 
Larger projects often involve many modules or rely on third-party packages located elsewhere. 
In such cases, developers configure the PYTHONPATH environment variable so Python knows where to look. 
Environment variables are stored by the operating system and available to all programs. 
On Windows, for example, PYTHONPATH can be set permanently via the control panel or temporarily in a terminal with:
set PYTHONPATH="c:\dir1;c:\other\directory"
export MY_VARIABLE="value"

import module vs. from module import name
A normal import statement (e.g., import HTTPServer) loads the module and makes it accessible as a single object. 
Names are then accessed using dot notation, such as HTTPServer.address.

By contrast, the from form imports only specific items directly into the current namespace. For example:
from HTTPServer import address
print(address)
Here, only the variable address from HTTPServer is imported, and it can be used without prefixing it with the module name.

"""

"""
Running a Module as a Script
Normally, when you import a module, Python runs all of the code at the top level of that file. 
This includes things like print() statements or input() calls. Often, you don’t want those lines to run just because the module is imported — they should only run if the file is being executed directly as a program.
Python solves this problem with a special variable called __name__.

What is __name__?
Every Python file (script or module) gets a built-in variable named __name__.
If the file is being imported, __name__ is set to the module’s name (e.g., "WebSearch").
If the file is being run directly, __name__ is set to "__main__".

Using __name__ in Your Code
You can use an if statement to check whether a file is being run directly or imported:
if __name__ == "__main__":
    # Code in here runs only when the file is executed directly
    # It will NOT run when the file is imported

This allows you to separate:
Reusable definitions (functions, classes, constants) → always available when imported.
Executable code (tests, demos, user interface) → runs only if the file is executed directly.

Example
Let’s say you have a file WebSearch.py:
def search(query):
    return f"Results for {query}"

if __name__ == "__main__":
    # Only runs when WebSearch.py is executed directly
    results = search("python tutorial")
    print(results)

Running python WebSearch.py will execute the search and print the results.
Importing it in another file, e.g. import WebSearch, won’t trigger the search — it only makes the search() function available.
Now a second file, MultipleWebSearch.py, can safely import WebSearch without causing the initial search to run:
import WebSearch

print(WebSearch.search("flask tutorial"))
This pattern (if __name__ == "__main__":) is one of the most common Python idioms. 
It keeps your files flexible: they can act as standalone scripts or as reusable modules.
"""

"""

Reloading Modules
Normally, when you import a module, Python executes it only once. 
If you later change the module’s source code, those changes won’t take effect in the current Python session unless you restart the program.
To avoid restarting, you can use the reload() function from the importlib standard library. This re-executes the module’s code and updates its definitions in place.
from importlib import reload
import send_gmail

# ... later in the program
reload(send_gmail)

Why Reload?
Imagine Johnny’s HotDogs has a script, send_coupons.py, that uses send_gmail.py to email thousands of customers. 
If the program is stopped and restarted just to update the email header, some customers might receive duplicate emails. 
Instead, Johnny can update send_gmail.py, and the running program can reload the module dynamically to pick up the new header text — without stopping the process.

Detecting Changes Automatically
You can even detect when a module’s file has changed.
Every module has a __file__ attribute that stores its path on disk. For example:
print(send_gmail.__file__)
# Output: C:\Users\Johnny\send_gmail.py

Using os.path.getmtime(), you can check the file’s last modified time.
send_coupons.py could store the modification time when it first imports send_gmail, then check at the end of each loop whether the file has changed. If so, it calls reload(send_gmail).

Important Notes
Reload updates the module in place. After reload(send_gmail), calls like send_gmail.send() will use the new version of the function.
Avoid from module import name with reload. If you import specific attributes (e.g., from send_gmail import send), reloading won’t update those references — only the module object itself is refreshed.
Reloading is useful for long-running programs. For example, a web server handling many clients can update one module without restarting and disconnecting everyone.
In short, reload() is a handy tool when you need to update code on the fly in long-running applications.
"""

"""
Packages

So far, we’ve looked at importing single modules. But in larger projects, related modules are usually grouped together inside a package.
A package is just a directory that contains modules (and possibly subdirectories of modules). To tell Python that a directory is a package, it must include a special file called __init__.py. This file can be empty, or it can include code — such as imports — that runs when the package is loaded.
Python searches for packages in the directories listed in sys.path, just like it does for modules.

Example Directory Structure
draw_scene.py          # Script that imports ASCIIArt package
ASCIIArt/              # Top-level package
    __init__.py
    canvas.py
    figures/           # Subpackage for figure art
        __init__.py
        man.py
        cow.py
    buildings/         # Subpackage for building art
        __init__.py
        barn.py
        house.py

Importing a Package
import ASCIIArt
This imports the package, making its modules accessible by full path.
For example:
import ASCIIArt.canvas

ASCIIArt.canvas.draw_canvas()
Here, you import canvas.py from the ASCIIArt package and call its draw_canvas() function by specifying the full path.

Using from with Packages
You can also import subpackages, modules, or even specific names directly into your namespace using the from form.
Importing a module from a subpackage:
from ASCIIArt.figures import cow
cow.draw()

Importing just one function from a module:
from ASCIIArt.figures.cow import draw
draw()
This way, you don’t need to keep writing the full package path.

Import Rules
With import x.y.z, the last item (z) must be a package or module.
With from x.y import z, the last item can also be a name defined inside y (like a function, class, or variable).

Why Packages Matter
Packages help organize large projects and avoid naming conflicts. For example:
ASCIIArt.canvas and 3DGraphics.canvas are two different modules, even though they share the same filename.
Packages are Python’s way of grouping related modules into clean, organized namespaces, keeping big projects manageable.

"""

"""
Standard library

By default, Python includes a collection of modules that can be imported into new programs. 
The Python standard library includes various utilities and tools for performing common program behaviors. 
Ex: The math module provides mathematical functions, the datetime module provides date and calendar capabilities, the random module can produce random numbers, the sqlite3 module can be used to connect to SQL databases, and so on. 
Before starting any new project, good practice is to research what is available in the standard library or on the internet to help complete the task. 
Methods to find more modules are discussed in another section.

Python standard library modules.
Module name	    Description	                                                                                Documentation link
datetime	    Functions for creating and editing of dates and times objects	                            https://docs.python.org/3/library/datetime.html
random	        Functions for working with random numbers	                                                https://docs.python.org/3/library/random.html
copy	        Functions that create complete copies of objects	                                        https://docs.python.org/3/library/copy.html
time	        Functions that get the current time, convert time zones, and sleep for a number of seconds	https://docs.python.org/3/library/time.html
math	        Mathematical functions	                                                                    https://docs.python.org/3/library/math.html
os	            Operating system informational and management helper functions	                            https://docs.python.org/3/library/os.html
sys	            System-specific environment or configuration helper functions	                            https://docs.python.org/3/library/sys.html
pdb	            The Python interactive debugger	                                                            https://docs.python.org/3/library/pdb.html
urllib	        URL handling functions, such as requesting web pages	                                    https://docs.python.org/3/library/urllib.html
"""
