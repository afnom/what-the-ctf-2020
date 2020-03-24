# Web challenge


## Overview
Theme: web
Difficulty: easy

A simple web challenge that requires you to do some recon of a web app, find a default password and crash a flask web app to reset the app to default.

This challenge is kind of aimed at teaching common developer security pitfalls, like default passwords or not deleting sensitive git info, as well as not relying on client provided input without proper validation

## Setup

`python3 website/app.py`

## Solution

you are presented with a webpage that you can use to customise cat ascii art.

A bit of enumeration will show a /login form and a /flag, with permission denied.

Looking at the website source will reveal a git repo (https://github.com/supersecuredev/website) with the website source.

Looking at the source shows that the app will reset to load a default password if you manage to trigger an exception when generating cat art.

Looking back through the git history will reveal the default admin password.

Now going back to the web page, use a browser source editor (or some proxy like burp) to submit an illegal value for cat_type (3). This will cause an exception, which will reload the default password.

now you can log in as admin and browse to /flag to get the flag


## Techniques learnt

 - basic web recon either manual or automated (something like gobuster should find the /login page)

 - using open source intelligence to look at git and find weaknesses / source code

 - abusing lack of server side validation by editing form details

 - looking for default creds

## Tools needed

 - A web browser

[Optional] 

 - a web scanner to speed initial enumeration

 - a proxy like ZAP or BURP for conducting form modification (can be done with a browser)


## Account details

email:
supersecuredev@outlook.com
L3Kuh4QcArFRxUWn

github:
V3xWTyJrtefBfAJY