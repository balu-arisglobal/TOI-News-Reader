# TOI-News-Reader
A news reader REST python application where it invokes the TOI API to fetch the news and display the same onto desktop screen at regular interval of time


<h3>Method Description</h3> 

<h4>invoke_toi</h4>
REST Invocation to TOI happens where it takes the top headlines along with apiKey which is obtained by signing in


<h4>notifier</h4>
Parameters
> timeInMinutes - configurable time </br>
Notifier takes the user input time in minutes and converts it into milliseconds
it fetches the news from above invoke_toi and pops up to desktop at the mentioned intervals of time untill the news list is iterated fully.


<h4>accept_configurable_time</h4>
First invocation happens where user enters the configurable time in minutes, there by it sends the same to notifier



<h3>Note</h3>
> Prefered code for Ubuntu(any version) </br>
> Windows not at all preferred for execution </br>
> install python-dbus for hardware GUI changes to enable desktop notifications </br>
> install all the packages in requirement.txt (pip install -r requirements.txt) </br>
> Project structure looks like Flask but Please run only app.py from command line and nothing else as it is not required.
