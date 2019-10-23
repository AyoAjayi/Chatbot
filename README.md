# About Ayo's Chatbot

##
I have a chat room that allows people to communicate to each other. I wanted a very light and happy theme. This theme can be seen in my color scheme and in the chatbot responses

##
I incorporated my theme into my project by using bright colors(blue ).
##
I struggled with sending the client and server messages. I solved this by looking at the button example and researching on events. I struggled with pushing to heroku, I fixed this updating my requirements file. I struggled getting the chat messages to show up in a sequential way. I also struggled woith react components and setting up my database. I fixed some of these issues by looking at the slides and doing some research.

##
My project right now has my yelp API response but I was not able to parse that data and send it to my client. Also, I have some tests set up but I have troubles with getting my tests to run with cricleCI.

##
I would improve this project making sure the name of the user is displayed alongside their text. I will also ensure that I incorporate my API and only allow the user to sign in after they logged in.

##


### Ayo's Chatbot  created by Ayomide Ajayi
 
This web app is a chatroom in development where students can log in using the Google API, communicate with each other, and view previous conversations. The theme of this chatbot is light and happy.
### Built With:

- Python
-	Flask
-	React
-	Used socket.io for long polling to occur between server and client
-	Deployed via [Heroku](http://infinite-beach-83396.herokuapp.com/)



### Functionality:


- When the user types !! help, they get a list of commands they can use to navigate through the chatroom. The chatbot is there to help them.
- A new user can log in to the chatroom and their username and profile picture are pulled from the Google API and displayed in the chatroom
- Many people can use the chat room at once
- Messages that is entered in the text area is stored in a a database and laoded up when someone visits the site.
- If a user enters a url, it is clickable through the chatbot.


### Known Problems:
I had some issues while working on the project that I fixed later. Some are:

* I struggled with implementing my yelp api and making an even further advanced chatbot. The yelp api would have allowed the user to see food places near them. I am currently working to resolve this.

* I struggled with getting my app running with heroku initially. However, I realized that I need to update my requirements.txt file. 

* I could have decorated and formatted my chatbot more nicely.


