# Twitter-Bot
Twitter Bot Using Web Scraping and Selenium Library

## What is Web Scraping?
Web scraping is an automated method used to extract large amounts of data from websites. The data on the websites are unstructured. Web scraping helps collect these unstructured data and store it in a structured form.

## What is Selenium?
Selenium is a powerful tool for controlling web browsers through programs and performing browser automation. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C#, etc, we will be working with Python.

## Other Modules I Used
-nltk
-requests
-fromstring

## What Has Been Made Step by Step
In this project, I take the famous lines from the Kurtlar Vadisi TV series and share them on a Twitter account at the time intervals I have determined.

# 1-Scraping
I have defined a function to scrape sentences. I pull out the sentences in random order by giving an appropriate xpath from the site I chose and return it as the response of the function.

![---](/images/1.png)

# 2-Login
I have defined another function for the login operation. This function finds the username and password fields on the Twitter login page on the given xpath and enters the information you specify. It then finds the login button in the same way and allows you to login.

![---](/images/2.png)

# 3-Sending Tweet
The function that I have defined for tweeting writes one of the sentences we have already scraped into the box by finding the box where we will write the content of the tweet with xpath after logging in. Then it allows us to tweet by finding the send button with xpath.

![---](/images/3.png)

# Note: You may need to make changes on the code depending on the change of xpath directories or the browser version on your system.

## Thank you for your interest, I hope it was useful.
