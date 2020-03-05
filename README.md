# Blackboard Course Auto Opener
Python Selenium script to automatically and easily open the Blackboard page of the desired course.

## Getting Started
### Requirements
* Python3
* Selenium (PyPI)

## Configuration
Change **values.py** file according to your personal data, and you can also add as much courses as you'd like:

```
USERNAME = "YOUR_USERNAME_HERE"
PASSWORD = "YOUR_PASSWORD_HERE"

LOADING_TIME = 2                            # --- if your internet is fast, put 1 (it's in seconds)
                                            # --- if it's slooooooow, put something high like 20

UC_SHORT = []
UC_FULL_NAME = []
UC_PAGE = []

UC_SHORT.append('YOUR_UC1_SHORTNAME')          # --- ex: "aer"
UC_FULL_NAME.append('YOUR_UC1_FULLNAME')       # --- ex: "Arquiteturas Emergentes de Rede"
UC_PAGE.append('YOUR_UC1_CONTENT_PAGE_NAME')   # --- ex "Conteúdo"

UC_SHORT.append('YOUR_UC2_SHORTNAME')
UC_FULL_NAME.append('YOUR_UC2_FULLNAME')
UC_PAGE.append('YOUR_UC2_CONTENT_PAGE_NAME')

UC_SHORT.append('YOUR_UC3_SHORTNAME')
UC_FULL_NAME.append('YOUR_UC3_FULLNAME')
UC_PAGE.append('YOUR_UC3_CONTENT_PAGE_NAME')

```

## Usage
``` 
$ python3 login_blackboard.py <<UCx_SHORT>>
```

## Contacts
* [pmatarodrigues.com](https://pmatarodrigues.com)
* [Linkedin](https://linkedin.com/in/pmatarodrigues)
* This Github
