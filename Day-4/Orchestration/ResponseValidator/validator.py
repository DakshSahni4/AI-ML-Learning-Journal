from models import ValidationResult
import json

class ResponseValidator:
    def __init__(self):
        self.lengthLimit = 1000
        self.prohibited = ['hack','kill','murder']

    def validate(self,response,validate_json = False):
        errors = []

        errors.extend(self.validateEmpty(response))
        if errors:
            return ValidationResult(
                valid=False,
                errors=errors
            )
        errors.extend(self.validateLength(response))
        errors.extend(self.validateKeywords(response))

        if validate_json:
            errors.extend(self.validateJSON(response))
        
        return ValidationResult(
            valid = len(errors) == 0,
            errors = errors
        )


    def validateKeywords(self,response):
        errors =[]
        for word in self.prohibited:
            if word in response:
                errors.append(f"Contains prohibited keyword: {word}")
        return errors
    
    def validateEmpty(self,response):
        if response is None:
            return ["Response is None"]
        if isinstance(response,str) and response.strip() == "":
            return ["Response is empty"]
        return []

    def validateJSON(self,response):
        try:
            temp = json.load(response)

            return []

        except json.JSONDecodeError:
            return ["Invalid JSON"]



    def validateLength(self,response):
        if len(response) >self.lengthLimit:
            return  [f"Response exceeds {self.lengthLimit} characters "]
        
        return []

