content = open("index.html", "r").read()

content = content.replace(
    "background: transparent;\n      white-space: nowrap;",
    "background: transparent !important;\n      white-space: nowrap;"
)

content = content.replace(
    "width: 320px;\n      background: transparent;\n    }",
    "width: 320px;\n      background: transparent !important;\n    }\n\n    .footer-email-form input:-webkit-autofill,\n    .footer-email-form input:-webkit-autofill:hover,\n    .footer-email-form input:-webkit-autofill:focus {\n      -webkit-box-shadow: 0 0 0px 1000px transparent inset !important;\n      box-shadow: 0 0 0px 1000px transparent inset !important;\n      transition: background-color 5000s ease-in-out 0s;\n    }"
)

open("index.html", "w").write(content)
print("✅ Fixed!")
