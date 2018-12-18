import webbrowser

q_list = ["bts","아이유","블랙핑크","위너"]

url = "https://www.google.com/search?q="

for q in q_list:

    webbrowser.open(url+q)
    #"https://www.google.com/search?q=bts"
    #"https://www.google.com/search?q=아이유"
    #"https://www.google.com/search?q=브랙핑크"
    #"https://www.google.com/search?q=위너"