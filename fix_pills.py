content = open("index.html", "r").read()

content = content.replace(
    ".integration-pill {",
    ".integration-pill {\n      background-color: #ffffff !important;"
)

open("index.html", "w").write(content)
print("✅ Pills fixed!")
