# Django Online Shop Website with Payment
This is a simple e-commerce website built with Django (Python) and BankGateWay is added as payment processor.

I've made this as a "Shop" website but you can make any website you like.


And if you like this project then ADD a STAR ⭐️  to this project 👆

## Features of this Project

### A. Admin Users Can
1. Manage Category (Add, Update, Filter and Delete)
2. Manage Products (Add, Update, Filter and Delete)
3. Manage Users (Update, Filter and Delete)
4. Manage Orders (View and Process)

### B. Non-Registered Users Can
1. View Products (Can filter based on category)
2. Explore Product Details and Related Products


### C. Registered Users Can 
1. Add to Cart
2. Update Profile 
3. Pay with PayPal or Debit/Credit Card and Order
4. See the Order Status
5. See Order History
6. Reset Password
7. Change Password


## Support Developer
1. Add a Star 🌟  to this 👆 Repository



## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/arminam3/Django-Shop.git
```

Then, Enter the project
```
$  cd django-shop
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (Admin)

Command for PC:
```
$  python manage.py createsuperuser
```

Command for MAC:
```
$  python3 manage.py createsuperuser
```
Then Add Email, Username and Password

