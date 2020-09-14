import requests
import json
import ANI
from PIL import Image


#put your api key in APIKEY.txt see read me for details

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
pageId = 0

z = 0

while True:
    c = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&list=random")
    query = json.loads(c.content.decode("utf-8"))
    query = query['query']['random'][0]['title']
    print("\033[H\033[J") 
    print("finding valid page",'.'*(z%3+1))
    z+=1
    if(":" not in str(query) and len(str(query)) <= 10 and isEnglish(str(query))):
        query = str(query).replace("Category:","")
        pageId = int(json.loads(c.content.decode("utf-8"))['query']['random'][0]["id"])
        break



a = ANI.searcher(query,"secret")
a.getImage()

phanumeric_filter = filter(str.isalnum, str(query))

query = ''.join(phanumeric_filter)


image = Image.open("secret.jpg")
image.show()
print("\033[H\033[J")
while True:
    z = input("guess anwser: ")
    if(z.lower() != str(query).lower().replace("_"," ")):
        print("you are wrong! ")
        x = input("continue? y/n: ")
        print("\033[H\033[J") 
        if(x != "n"):
            pass
        else:
            print("word is:",query, '\n' , f"page is: https://en.wikipedia.org/wiki/{query}")
            break
    else:
        print("gg you got it!")

input("Enter to exit")



