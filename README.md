# TOI-News-Reader
A news reader REST python application where it invokes the TOI API to fetch the news and display the same onto desktop screen at regular interval of time


#Method Description 

#invoke_toi
REST Invocation to TOI happens where it takes the top headlines along with apiKey which is obtained by signing in


#notifier
Arguements
> timeInMinutes - configurable time 

Notifier takes the user input time in minutes and converts it into milliseconds
it fetches the news from above invoke_toi and pops up to desktop at the mentioned intervals of time untill the news list is iterated fully.


#accept_configurable_time
#First invocation happens where user enters the configurable time in minutes, there by it sends the same to notifier
