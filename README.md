# Overview

I was asked by a friend if I could create some code to send out text messages to a group of people.


I decded to use sql lite for this project, to play around with databases. This code will look at a
csv file and import it into a database. It also checks  to see if you have already added that person
or not too. 

I decided it was a great time to not only work on my objective code in python, but to also brush up on sql.

I have a link below of a demo for the project, and go into detail about the code.

[Software Demo Video](https://youtu.be/zdy7QwyBhfA)

# Relational Database

I use sql lite for this project. Which is a simple way to add SQL databases to a python project.

This SQL database is pretty simple, it's one table, with 
| primary_key | fname | lname | phone_number |   |
|-------------|-------|-------|--------------|---|
I didnt' think much more was needed, however in the future adding in a family table could be interesting.


# Development Environment

For the libraries I used.
* SQL Lite - for the sql databse
* Twilio - for the phone api
* Python-dotenv - for hidden values
* pandas - importing the csv
* tqdm - to show the progress bar


I wrote this code in python, using VScode. 

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Python](https://www.twilio.com/)
- [Twilio](https://www.python.org/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Adding in more tables
- Adding a way to remove people
- Linking people together, to send less texts
