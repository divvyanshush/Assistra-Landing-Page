content = open("index.html", "r").read()

# Add outline none and force transparent on focus too
old = ".footer-email-form input {\n      font-family: 'Geist', sans-serif;\n      font-size: 16px;\n      font-weight: 400;\n      color: #141413;\n      border: 1.5px solid rgba(0,118,131,0.25);\n      border-radius: 999px;\n      padding: 10px 24px;\n      outline: none;\n      width: 320px;\n      background: transparent !important;\n    }"

new = ".footer-email-form input {\n      font-family: 'Geist', sans-serif;\n      font-size: 16px;\n      font-weight: 400;\n      color: #141413;\n      border: 1.5px solid rgba(0,118,131,0.25);\n      border-radius: 999px;\n      padding: 10px 24px;\n      outline: none;\n      width: 320px;\n      background: transparent;\n      -webkit-appearance: none;\n      appearance: none;\n      box-shadow: none;\n    }\n\n    .footer-email-form input:focus {\n      background: transparent;\n      outline: none;\n      box-shadow: none;\n    }"

content = content.replace(old, new)
open("index.html", "w").write(content)
print("✅ Input fixed!")
