# Django Meetup Page

> Status: Developing


### This repository is dedicated to the study of the Django framework. The main code is from the course of Django from <a href="https://www.youtube.com/watch?v=t7DrJqcUviA&list=PLzsAIfynJhXHvyjxUoNNkHyzEMn3vwqw_&index=2">Academind</a>, but some features are going to be added, it was used idea to build a web application where it's possible to list the meetups that a person has and see its description.  (<a href="https://django-meetup-heroku.herokuapp.com/meetups/">see the application</a>)


## The models of the project are:
+ Meetup
+ Location
+ Participant

## The main model of this project is Meetup and its fields are:
+ title
+ slug 
+ organizer_email
+ date
+ description
+ image
+ location
+ participants 

## The Locations model has the following fields:
+ name
+ address

## The Participant model has the following field:
+ email

## Completed features:
+ In the admin page it is possible to create meetups. 
+ It's possible to vizualise the image uploaded in each meetup.
+ It was created a database to store Meetups, Participants and Locations.
+ It's possible to view more details about a meetup, see the organizer's email and subscribe a new participant at the meetup by passing the participant's email.

## Features in developing:
+ Make a CRUD to the meetups.

## Technologies used:
<table>
  <tr>
    <td>Django</td>
    <td>Python</td>
    <td>HTML</td>
    <td>CSS</td>
  </tr>
  
  <tr>
    <td>3.2.8</td>
    <td>3.9.7</td>
    <td>5</td>
    <td>3</td>
  </tr>
</table>




