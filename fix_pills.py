content = open("index.html", "r").read()

content = content.replace(
    ".integrations {\n      background: #ffffff;",
    ".integrations {\n      background: #ffffff !important;"
)

content = content.replace(
    ".integration-pill {",
    ".integration-pill {\n      background: #ffffff !important;"
)

open("index.html", "w").write(content)
print("✅ Fixed!")
