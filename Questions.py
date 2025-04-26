def Level_1():
    questions = {
        "What is the correct syntax for a Python function?": {
            "options": [
                "def function_name:",
                "function function_name():",
                "def function_name():",
                "function_name def():"
            ],
            "correct_answer": "def function_name():"
        },
        "Which of the following is used to create a list in Python?": {
            "options": [
                "[]",
                "{}",
                "()",
                "<>"
            ],
            "correct_answer": "[]"
        },
        "What will be the output of the following Python code?\nx = 'Hello'\nprint(x[1])": {
            "options": [
                "H",
                "e",
                "l",
                "o"
            ],
            "correct_answer": "e"
        },
        "Which of the following is the correct way to create a dictionary in Python?": {
            "options": [
                "dict = (key1: value1, key2: value2)",
                "dict = {key1: value1, key2: value2}",
                "dict = [key1: value1, key2: value2]",
                "dict = <key1: value1, key2: value2>"
            ],
            "correct_answer": "dict = {key1: value1, key2: value2}"
        },
        "What does the following code do?\nx = 10\nx += 5": {
            "options": [
                "Adds 5 to 10 and stores it in x",
                "Subtracts 5 from 10 and stores it in x",
                "Multiplies 10 by 5 and stores it in x",
                "Divides 10 by 5 and stores it in x"
            ],
            "correct_answer": "Adds 5 to 10 and stores it in x"
        },
        # Additional 10 Level 1 questions
        "Which of the following is a valid Python variable name?": {
            "options": [
                "1variable",
                "_variable",
                "variable-1",
                "variable name"
            ],
            "correct_answer": "_variable"
        },
        "Which symbol is used for comments in Python?": {
            "options": [
                "//",
                "#",
                "/* */",
                "<!-- -->"
            ],
            "correct_answer": "#"
        },
        "How do you print 'Hello World' in Python?": {
            "options": [
                "echo 'Hello World'",
                "print('Hello World')",
                "printf('Hello World')",
                "console.log('Hello World')"
            ],
            "correct_answer": "print('Hello World')"
        },
        "Which of these is a correct if statement in Python?": {
            "options": [
                "if x == 5:",
                "if (x == 5)",
                "if x = 5 then",
                "if x == 5 then:"
            ],
            "correct_answer": "if x == 5:"
        },
        "Which keyword is used to create a loop in Python?": {
            "options": [
                "loop",
                "for",
                "iterate",
                "repeat"
            ],
            "correct_answer": "for"
        },
        "Which operator is used to check if two values are equal in Python?": {
            "options": [
                "=",
                "==",
                "!=",
                "equals"
            ],
            "correct_answer": "=="
        },
        "Which data type is used to store True or False values?": {
            "options": [
                "int",
                "str",
                "bool",
                "float"
            ],
            "correct_answer": "bool"
        },
        "Which method is used to find the length of a string?": {
            "options": [
                "length()",
                "len()",
                "count()",
                "size()"
            ],
            "correct_answer": "len()"
        },
        "Which of these is a Python tuple?": {
            "options": [
                "[1, 2, 3]",
                "{1, 2, 3}",
                "(1, 2, 3)",
                "<1, 2, 3>"
            ],
            "correct_answer": "(1, 2, 3)"
        },
        "How do you insert COMMENTS in Python code?": {
            "options": [
                "//This is a comment",
                "#This is a comment",
                "<!--This is a comment-->",
                "**This is a comment**"
            ],
            "correct_answer": "#This is a comment"
        }
    }
    return questions


def Level_2():
    questions = {
        "What is the output of this Python code?\nx = [1, 2, 3]\nprint(x[2])": {
            "options": [
                "1",
                "2",
                "3",
                "IndexError"
            ],
            "correct_answer": "3"
        },
        "Which of the following is used to define a class in Python?": {
            "options": [
                "class ClassName:",
                "def ClassName:",
                "create ClassName:",
                "class = ClassName"
            ],
            "correct_answer": "class ClassName:"
        },
        "What will be the result of the following Python code?\nstr = 'Python'\nstr[0] = 'p'": {
            "options": [
                "python",
                "Python",
                "Error",
                "None"
            ],
            "correct_answer": "Error"
        },
        "Which of the following methods is used to add an element to a list in Python?": {
            "options": [
                "list.add()",
                "list.append()",
                "list.insert()",
                "list.push()"
            ],
            "correct_answer": "list.append()"
        },
        "What is the keyword used to define an exception block in Python?": {
            "options": [
                "try",
                "catch",
                "except",
                "throw"
            ],
            "correct_answer": "except"
        },
        # Additional 10 Level 2 questions
        "Which of these is a mutable data type in Python?": {
            "options": [
                "list",
                "tuple",
                "str",
                "int"
            ],
            "correct_answer": "list"
        },
        "Which method can be used to remove an element from a list?": {
            "options": [
                "remove()",
                "delete()",
                "discard()",
                "erase()"
            ],
            "correct_answer": "remove()"
        },
        "What does the 'pass' statement do in Python?": {
            "options": [
                "Skips an iteration",
                "Does nothing",
                "Exits the loop",
                "Raises an error"
            ],
            "correct_answer": "Does nothing"
        },
        "What is the output?\nprint(type([]))": {
            "options": [
                "<class 'list'>",
                "<class 'tuple'>",
                "<class 'dict'>",
                "<class 'set'>"
            ],
            "correct_answer": "<class 'list'>"
        },
        "Which is NOT a Python keyword?": {
            "options": [
                "elif",
                "assert",
                "local",
                "finally"
            ],
            "correct_answer": "local"
        },
        "Which module is used to work with dates in Python?": {
            "options": [
                "datetime",
                "time",
                "calendar",
                "dates"
            ],
            "correct_answer": "datetime"
        },
        "Which statement is used to handle exceptions in Python?": {
            "options": [
                "handle",
                "except",
                "catch",
                "error"
            ],
            "correct_answer": "except"
        },
        "What is the output?\nprint(2 ** 3)": {
            "options": [
                "6",
                "8",
                "9",
                "5"
            ],
            "correct_answer": "8"
        },
        "Which keyword is used to create an object in Python?": {
            "options": [
                "new",
                "class",
                "def",
                "None of these"
            ],
            "correct_answer": "None of these"
        },
        "Which operator is used for logical AND in Python?": {
            "options": [
                "&&",
                "and",
                "&",
                "AND"
            ],
            "correct_answer": "and"
        }
    }
    return questions


def Level_3():
    questions = {
        "What will be the output of the following Python code?\nx = 2\nx = x ** 3\nprint(x)": {
            "options": [
                "6",
                "8",
                "4",
                "64"
            ],
            "correct_answer": "8"
        },
        "Which of the following is used to remove an element from a set in Python?": {
            "options": [
                "set.remove()",
                "set.delete()",
                "set.pop()",
                "set.clear()"
            ],
            "correct_answer": "set.remove()"
        },
        "Which method can be used to convert a string to lowercase in Python?": {
            "options": [
                "string.lower()",
                "string.toLower()",
                "string.lowercase()",
                "string.Lower()"
            ],
            "correct_answer": "string.lower()"
        },
        "Which of the following is NOT a valid variable name in Python?": {
            "options": [
                "var_name",
                "_varName",
                "var-name",
                "var123"
            ],
            "correct_answer": "var-name"
        },
        "What is the result of this Python code?\nlist = [1, 2, 3]\nlist[1] = 5\nprint(list)": {
            "options": [
                "[1, 2, 3]",
                "[1, 5, 3]",
                "[5, 2, 3]",
                "[1, 2, 5]"
            ],
            "correct_answer": "[1, 5, 3]"
        },
        # Additional 10 Level 3 questions
        "What is the output of the following?\nprint(bool('False'))": {
            "options": [
                "False",
                "True",
                "None",
                "Error"
            ],
            "correct_answer": "True"
        },
        "Which of the following functions returns the largest item in an iterable?": {
            "options": [
                "largest()",
                "max()",
                "biggest()",
                "maximum()"
            ],
            "correct_answer": "max()"
        },
        "What is the result of the expression 3*1**3?": {
            "options": [
                "27",
                "3",
                "1",
                "9"
            ],
            "correct_answer": "3"
        },
        "Which function is used to sort a list in ascending order?": {
            "options": [
                "sort()",
                "sorted()",
                "order()",
                "arrange()"
            ],
            "correct_answer": "sort()"
        },
        "What is the output of this?\nprint('5' + '6')": {
            "options": [
                "56",
                "11",
                "5 6",
                "Error"
            ],
            "correct_answer": "56"
        },
        "What is a correct syntax to output the type of a variable?": {
            "options": [
                "print(typeof(x))",
                "print(type(x))",
                "print(typeof x)",
                "print(typeOf(x))"
            ],
            "correct_answer": "print(type(x))"
        },
        "Which method can be used to replace parts of a string?": {
            "options": [
                "replace()",
                "switch()",
                "change()",
                "alter()"
            ],
            "correct_answer": "replace()"
        },
        "Which operator is overloaded by the __add__() method?": {
            "options": [
                "+",
                "-",
                "*",
                "/"
            ],
            "correct_answer": "+"
        },
        "Which keyword is used for function in Python?": {
            "options": [
                "func",
                "define",
                "def",
                "function"
            ],
            "correct_answer": "def"
        },
        "What is the output?\nprint(len({1: 'a', 2: 'b'}))": {
            "options": [
                "2",
                "1",
                "0",
                "Error"
            ],
            "correct_answer": "2"
        }
    }
    return questions
