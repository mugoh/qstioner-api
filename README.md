

# qstioner-api
Questioner api is an api version 1 of the qstioner web application. It allows the user to send htttp requests to application and persists in data structures

Questioner is a platform where human beings can ask questions about meetups and vote present questions.

### What it can do
- Users can create an account and log in.
- Admin user can create a Meetup
- Users can post questions to meetups.
- Users can upvote posted questions.
- Users can downvote posted questions.
- Users can delete the questions they post.
- Users can post comments to a question.
- Users can view the comments to questions.


## API
### Installation
- Clone the repository
```shell
$ git clone https://github.com/hogum/qstioner-api.git
```
- Switch to the stackS directory
```shell
$ cd qstioner-api
```
- Depending on your os open your virtual enviroment
- Install the project requirements
```shell
$ pip install -r requirements.txt
```

### Running the application
```shell 
$ export FLASK_APP=app
```
or
```shell
$ set FLASK_APP=app
```
on Windows OS
##### Start the server
``` shell
$ flask run
```

### Project Dependencies
- [Flask](http://flask.pocoo.org/)

### Endpoints

##### Authorization Endpoints

Method | Endpoint | Functionality
--- | --- |---
POST | `api/v1/auth/register` | Register new User
POST | `api/v1/auth/login` | Login registered User
PUT | `api/v1/auth/users/user_id` | Update user details
DELETE | `api/v1/auth/users/user_id` | Delete a user account
GET | `api/v1/auth/users` | Get all registered users
GET | `api/v1/auth/users/user_id` | Get a single user


##### Meetup Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/meetups/` | Add a meetup
GET | `/api/v1/meetups/upcoming` | Lists all meetups 
GET | `/api/v1/meetups/meetup_id` | Retrieve a meetup 
PUT | `/api/v1/meetups/meetup_id` | Edit a meetup of a logged in user
DELETE | `/api/v1/meetups/question_id` | Delete a request of a logged in user

##### Questions Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question
GET | `/api/v1/questions` | Lists all questions 
GET | `/api/v1/questions/question_id` | Retrieve a question 
PUT | `/api/v1/questions/question_id` | Edit a question of a logged in user
DELETE | `/api/v1/questions/question_id` | Delete a request of a logged in user


##### Vote Endpoints

Method | Endpoint | Functionality
--- | --- | ---
PATCH | `/api/v1/question_id/upvote` | Upvote a Question
PATCH | `/api/v1/question_id/downvote` | Downvote a Question


##### Comment Endpoints


Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/question_id/comment` | Add an comment
GET | `/api/v1/questions/question_id/comment` | Lists all comments 
GET | `/api/v1/questions/question_id/comments/commentID` | Retrieve an comment 
PUT | `/api/v1/questions/question_id/comment/commentID` | Edit an comment 
DELETE | `/api/v1/questions/question_id/comment/commentID` | Delete an comment


##### Author

[Mugoh](https://github.com/hogum)
