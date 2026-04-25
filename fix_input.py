content = open("index.html", "r").read()

old = """    .footer-email-form input {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: #141413;
      border: 1.5px solid #007683;
      border-radius: 999px;
      padding: 10px 24px;
      outline: none;
      width: 320px;
      background: #F0FFF9;
    }"""

new = """    .footer-email-form input {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: #141413;
      border: 1.5px solid rgba(0,118,131,0.25);
      border-radius: 999px;
      padding: 10px 24px;
      outline: none;
      width: 320px;
      background: transparent;
    }"""

content = content.replace(old, new)
open("index.html", "w").write(content)
print("✅ Input fixed!")
