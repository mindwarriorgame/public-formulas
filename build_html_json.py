import os
import json
import markdown

directory = "letters"

content_dict = {}

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        name, lang_code = filename.rsplit('.', 2)[:2]

        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        if lang_code not in content_dict:
            content_dict[lang_code] = {}

        content_dict[lang_code][name] = markdown.markdown(content)

json_output = json.dumps(content_dict, ensure_ascii=False, indent=4)

print(json_output)