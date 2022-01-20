# Week01 Setup Python

Slide:https://docs.google.com/presentation/d/1y8Ut-GZqvsao0TxrjEA4sHc_xElQa4drYnUeylggiGM/edit#slide=id.g5137d70e84_0_472

Video:https://www.youtube.com/watch?v=jd2yPPRdsEM&list=PLK7HqNsOnqjYrwd6E7C86cVAd2_nenybk&index=8&t=2s 


# Week01

1. Check present working directory
    1. macOS ou Linux: ```$ pwd``` -- /home/wasit/github
    2. Windows: ```$ cd``` -- C:/Users/wasit/Desktop```
2. Create a new directory for the class “dsi202_2021”
    1. macOS ou Linux: ```$ mkdir dsi202_2021```
    2. Windows: ```$ mkdir dsi202_2021```
3. Enter to the directory with command “cd dsi202_2021” the check current directory
    1. macOS ou Linux: ```$ pwd``` -- /home/wasit/github/dsi202_2021```
    2. Windows: ```$ cd``` C:/Users/wasit/Desktop/dsi202_2021```
4. Create a new directory for week01 “week01”
    1. macOS ou Linux: ```$ mkdir week01```
    2. Windows: ```$ mkdir week01```
5. Change Directory to week01 as working directory
6. Create a new Python virtual environment and install Django web framework
    1. ```$ conda create -n dsi202_2022 python=3.6```
    2. ```$ conda activate dsi202_2022```
    3. ```$ conda install django=2.2```
7. Create Django project called “myproject” and runserver
    1. ```$ django-admin startproject myproject```
    2. ```$ cd myproject```
    3. ```$ python manage.py runserver 127.0.0.1:8008```
8. Go to browser and enter url
    1. http://127.0.0.1:8008/
    2. http://localhost:8008/
9. Terminate server by pressing Ctrl+c
10. Create a super user account
    1. ```$ python manage.py makemigrations```
    2. ```$ python manage.py migrate```
    3. ```$ python manage.py createsuperuser```


# Assignment
1. Create Django Project
2. Save homepage screen (rocket landing page)
3. Create admin account using "admin"
4. In admin page, create your account with your first name and capture the screen
