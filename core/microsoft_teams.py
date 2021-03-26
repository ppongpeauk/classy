from bs4 import BeautifulSoup
import urllib.request, webbrowser
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
def open_url(**kwargs):
    #request = urllib.request.Request(kwargs["url"].replace("&suppressPrompt=true", ""), None, headers)
    #response = urllib.request.urlopen(request)
   # response = urllib.request.urlopen(kwargs["url"].replace("https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2F", ""))
    #source = response.read()
    #print(source)
    #soup = BeautifulSoup(source, "html.parser")
    #get_teams_launcher = soup.find_all("teamsLauncher")
    #print(get_teams_launcher)
    #if get_teams_launcher:
    #    #get_url_protocol = get_teams_launcher[0].get("src")
    #    webbrowser.open(get_url_protocol)
    #else:
    #    print("alt")
    #    #webbrowser.open(kwargs["url"].replace("&suppressPrompt=true", ""))
    webbrowser.open(kwargs["url"].replace("https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2F", "msteams:/l/"))
    
#open_url(url="https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Afaa76da75f00422d8c80a51cfcafbb38%40thread.tacv2%2F1599253574355%3Fcontext%3D%257b%2522Tid%2522%253a%2522313708a6-b7e9-492c-ac7a-f19734f3f702%2522%252c%2522Oid%2522%253a%252254db24e0-c5dd-42bf-9958-10fc7c23ac85%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=48db59a8-ddd8-444d-9262-e77c404ed37f&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")