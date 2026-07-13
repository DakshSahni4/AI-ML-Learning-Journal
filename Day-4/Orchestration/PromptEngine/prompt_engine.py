import os
import json
import re

class PromptEngine:

    def __init__(self):
        self.base_path = os.path.join(os.path.dirname(__file__),"prompts")

    def loadPrompt(self,category,prompt_name):
        path = os.path.join(self.base_path,category,f"{prompt_name}.json")


        with open(path,"r") as file:
            return json.load(file)
    
    def validateVariables(self,template,variables):
        placeholders = re.findall(r"\{\{(.*?)\}\}",template)

        missing = [placeholder for placeholder in placeholders if placeholder not in variables]

        if missing:
            raise ValueError(
            f"Missing required template variables: {', '.join(missing)}"
        )
    
    def render(self,category,prompt_name,version,variables):

        prompt = self.loadPrompt(category,prompt_name)

        template = prompt[version]["template"]

        self.validateVariables(template,variables)

        for key,value in variables.items():
            template = template.replace("{{"+key+"}}",str(value))

        return template
    
    def addPrompt(self,category,version,prompt_name,template):

        category_path = os.path.join(self.base_path,category)
        os.makedirs(category_path,exist_ok = True)

        file_path = os.path.join(category_path,f"{prompt_name}.json")

        if os.path.exists(file_path):
            with open(file_path,'r') as file:
                data = json.load(file)
                if version in data:
                    raise ValueError(f"Version '{version}' already exists.")
        else:
            data ={}
        
        data[version] ={
            "template":template
        }

        with open(file_path,'w') as file:
            json.dump(data,file,indent=4)

        return f"Prompt '{prompt_name}' ({version}) added successfully."

    
        

