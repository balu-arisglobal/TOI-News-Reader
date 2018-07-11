from flask import Flask
import requests
import time
import notify2

app = Flask(__name__)

# dummy flask method
@app.route('/')
def hello_world():
    return 'Hello World!'

# In this method REST Invocation to TOI happens where it takes the top headlines along with apiKey which is obtained by signing in
def invoke_toi():
    URL = "https://newsapi.org/v2/top-headlines"
    PARAMS = {'sources':'the-times-of-india','apiKey': '5cfa12cd997646debc1a1ad1bcc75833',}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    result_set = []
    # Data will be in the format of {'status:'ok', ..... articles[{'title' : 'This is the title','description':'This is the description'}]}
    if data['status'] == 'ok':
        result_set = [dict({'title':articles['title'], 'description':articles['description']}) for articles in data['articles']]
        #print(result_set)
    else:
        print('Error invoking the News API')
    return result_set



# Notifier takes the user input time in minutes and converts it into milliseconds
# it fetches the news from above invoke_toi and pops up to desktop at the mentioned intervals of time untill the news list is iterated fully.
def notifier(timeInMinutes):
    timeInMilliseconds = timeInMinutes*1000
    ICON_PATH = "./TOI_logo.jpg"
    newsitems = invoke_toi()

    if len(newsitems) > 0:
        notify2.init("News Notifier")
        n = notify2.Notification(None, icon=ICON_PATH)
        n.set_urgency(notify2.URGENCY_NORMAL)
        #n.set_timeout(timeInMilliseconds if timeInMilliseconds < 5000 else 5000)

        for newsitem in newsitems:
            n.update(newsitem['title'], newsitem['description'])
            n.show()
            time.sleep(timeInMilliseconds)

# First invocation happens where user enters the configurable time in minutes, there by it sends the same to notifier
def accept_configurable_time():
    timeInMinutes = input("Please enter time duration(in minutes) at which interval you want to see the notifications: ")
    notifier(timeInMinutes)

if __name__ == '__main__':
    #app.run()
    accept_configurable_time()
