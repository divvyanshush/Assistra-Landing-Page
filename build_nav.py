html = open("index.html", "w")
html.write(open("/dev/stdin").read())
html.close()
