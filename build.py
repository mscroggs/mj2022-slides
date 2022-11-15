import os
import json
from markup import to_html


def make_slide(page, settings):
    return to_html(page), settings


if os.path.isdir("build"):
    os.system("rm -r build")

os.system("mkdir build")
os.system("cp -r _static build/_static")

slides = []
i = 0
while os.path.isfile(f"slides/{i}.html"):
    settings = {"style": "default"}
    page = ""
    with open(f"slides/{i}.html") as f:
        for line in f:
            if line[0] == "!":
                key, value = line[1:].split("=", 1)
                settings[key.strip()] = value.strip()
            elif line.strip() == "<newslide>":
                slides.append(make_slide(page, settings))
                page = ""
            else:
                page += line
        slides.append(make_slide(page, settings))
    i += 1

with open("_template.html") as f:
    t = f.read()

with open("_template.js") as f:
    js = f.read()
js = js.replace("{slides}", json.dumps(slides))

t = t.replace("{slide}", slides[0][0])
t = t.replace("{js}", js)

with open("build/index.html", "w") as f:
    f.write(t)
