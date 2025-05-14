#### Sensitive Sentence Checker
A python package that checks whether the sentence you have provided or you want to run that in code contains sensitive information like APIKEY, PASSWORD, CARD DETAILS or CVV etc.

#### Features
As an initial setup to check it can detects only following information as of now but anytime we can add some other sensitive information.
- Detects whether the text file has API_KEY or tokens
- Detects whether the text file contains some PASSWORD
- Detects whether the text file contains CARD CVV


#### Sample test cases has been provided which been run through pytest using assert and assert not functions
- Test Cases 1,2,3 has sensitive info so assert function has been used.
- Test Cases 4 and 5 doesn't have sensitive info so assert not function been used.

#### Used
- [Python](https://www.python.org/) - Programming Language
- [Black](https://github.com/psf/black) - Code Formatting
- [isort](https://pycqa.github.io/isort/) - Import Sorting
- [pytest](https://docs.pytest.org/) - Testing Framework


Made with ❤️ by [Sanket Kabra](https://github.com/sanketdv)
