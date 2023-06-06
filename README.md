# Intro
This is solution of tasks defined below, implemented in python and flask.

# Starting app
To be able to start application python 3 has to be install.
To start application download project, open console and go to project root folder: `python`

<pre>
python3 -m venv venv

source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

pip install -r requirements.txt

export FLASK_APP=flaskr/__init__.py  # On macOS/Linux
set FLASK_APP=flaskr/__init__.py     # On Windows

flask run  # To start app
pytest tests/ -v  # To run tests
</pre>

# Task 1
Write an REST endpoint that receives a POST request with the following JSON body:
<pre>
{
    "first_names": [
        ["&lt;first name&gt;", "&lt;ID number&gt;"],
        ...
    ],
    "last_names": [
        ["&lt;last name&gt;", "&lt;ID number&gt;"],
        ...
    ],
}
</pre>

API response is based on the information contained in the incoming request and should be formatted in
following way:

<pre>
{
    "full_names": [
        ["&lt;first name&gt;", "&lt;last name&gt;", "&lt;ID number&gt;"],
        ...
    ]
}
</pre>

## Example
Input:
<pre>
{
    "first_names": [
        ["Adam", "1234"],
        ["John", "4321"]
    ],
    "last_names": [
        ["Anderson", "4321"],
        ["Smith", "1234"]
    ],
}
</pre>


Expected output:
<pre>
{
    "full_names": [
        ["Adam", "Smith", "1234"],
        ["John", "Anderson", "4321"]
    ]
}
</pre>

Sort output entries by the ID number

Not all first_names will have last_names and vice versa. These should be output as "unpaired"

# Task 2
A REST endpoint receives a POST request with a text body containing three sorts of braces "()", "{}", "[]".
Write a program that will determine if the braces in the text are balanced.
* If they are balanced it should respond with status code 200 and text "Braces are balanced.”.
* If they are not balanced, it should respond with status code 400 and point to the first
unbalanced brace.

### Examples
Input:  
`
Python {is an easy to [learn]}, (powerful programming language. It) 
has efficient high-level[(data structures) and a simple but
effective approach to object-oriented programming]. Python's elegant
syntax and dynamic typing, together with its {interpreted nature,
make it an ideal language (for) scripting and rapid} application
development in many areas on most platforms.
`

Output:  
status code: 200  
response text: `Braces are balanced.`

Input:  
`
Python) {is easy to {learn]}.
`

Output:  
status code: 400  
response text: `Python) << brace is unbalanced.`

Input:  
`Python (language) {is easy to learn[}].`

Output:  
status code: 400  
response text:
`Python (language) {is easy to learn[ << brace is unbalanced.`

# Task 3
Write a decorator that stores the result of a function call and returns the cached version in
subsequent calls (with the same parameters) for 5 minutes, or ten times - whichever comes
first.