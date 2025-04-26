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
        }
    }
    return questions