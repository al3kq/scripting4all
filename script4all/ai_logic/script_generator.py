import requests
from dotenv import load_dotenv
import os
import json
import datetime

def generate_code(script_request):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    # Define the base prompt
    base_prompt = f"""
    Please analyze the following script request and identify the potential input variables.
    The ONLY possible input types are str, int, and float.
    Carefully consider how to give the user inputs which will return an intelligent response. 

    Title: {script_request.title}
    Description: {script_request.description}

    Provide a JSON object with the following structure:
    {{
        "input_variables": [
            {{
                "name": "<variable_name>",
                "type": "<data_type>",
                "description": "<variable_description>"
            }},
            ...
        ]
    }}
    """

    # Make API call to identify input variables
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4-turbo",
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": f"{base_prompt}"
            },
            {
                "role": "user",
                "content": f"""
                    Be specific, make assumptions, and do NOT add too many variables
                    """
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)

    # print(response.content)
    # print(response.json())

    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        # Extract the content JSON string from the response
        content_str = response_dict['choices'][0]['message']['content']

        content_data = json.loads(content_str)

        input_variables = content_data["input_variables"]

        # Generate UI scaffolding based on input variables
        ui_scaffolding = generate_ui_scaffolding(input_variables)

        # Generate code based on the script request and input variables
        code_prompt = f"""
        Please generate ONLY Python code for the following script request:

        Title: {script_request.title}
        Description: {script_request.description}

        Input Variables:
        {input_variables}

        Requirements:
        - Use Python 3.x syntax
        - Follow PEP 8 style guide for code formatting
        - Include necessary error handling and input validation
        - Provide meaningful variable names and code comments

        Code Template:
        ```python
        def main({', '.join(f"{var['name']}: {var['type']}" for var in input_variables)}):
            # Your code here
            pass

        if __name__ == "__main__":
            # Get user input for each variable
            {ui_scaffolding}

            main({', '.join(var['name'] for var in input_variables)})
        ```
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        data = {
            "model": "gpt-3.5-turbo-0125",
            # "response_format": {"type": "json_object"},
            "messages": [
                {
                    "role": "system",
                    "content": f"{code_prompt}"
                },
                {
                    "role": "user",
                    "content": "Only generate error free and executable Python code."
                }
            ]
        }
        code_response = requests.post(api_url, headers=headers, json=data)

        if code_response.status_code == 200:
            response_dict = json.loads(code_response.content.decode('utf-8'))
            content_str = response_dict['choices'][0]['message']['content']
            clean_code = ""
            if content_str.startswith("```python") and content_str.endswith("```"):
                print("YAY")
                clean_code = content_str[9:-3].strip()
            #generated_code = code_response.json()["code"]
    # Get the current working directory
            current_dir = os.getcwd()
            
            # Specify the folder name
            folder_name = "temp_output"
            
            # Create the folder path by joining the current directory and folder name
            folder_path = os.path.join(current_dir, folder_name)
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Specify the file name with timestamp
            file_name = f"gtp3_file_{timestamp}.py"

            # Create the file path by joining the folder path and file name
            file_path = os.path.join(folder_path, file_name)
            
            # Write the clean code to the file
            with open(file_path, "w") as file:
                file.write(clean_code)
            return clean_code
            
            return improve_on_code_gtp4(clean_code, script_request.description, input_variables)
        else:
            # Handle API error for code generation
            raise Exception("Code generation failed")
    else:
        # Handle API error for input variable identification
        raise Exception("Input variable identification failed")
    
def improve_on_code_gtp4(code_string, description, input_variables):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    api_url = "https://api.openai.com/v1/chat/completions"
    code_prompt = f"""
        Look at the code below, make sure it is error free.
        Consider the logic of the code and if it matches the users needs.
        {description}
        Make assumptions to fill in these input variables, do not prompt the user.
        {input_variables}
        ```python
        {code_string}
        ```
    """
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    data = {
        "model": "gpt-4-turbo",
        # "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": f"{code_prompt}"
            },
            {
                "role": "user",
                "content": "Only generate executable Python code."
            }
        ]
    }
    code_response = requests.post(api_url, headers=headers, json=data)
    print(code_response.content)
    if code_response.status_code == 200:
            response_dict = json.loads(code_response.content.decode('utf-8'))
            print(response_dict)
            content_str = response_dict['content']
            clean_code = ""
            if content_str.startswith("```python") and content_str.endswith("```"):
                clean_code = content_str[9:-3].strip()
            #generated_code = code_response.json()["code"]
            print(clean_code)
            current_dir = os.getcwd()
            
            # Specify the folder name
            folder_name = "temp_output"
            
            # Create the folder path by joining the current directory and folder name
            folder_path = os.path.join(current_dir, folder_name)
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Specify the file name with timestamp
            file_name = f"gtp4_file_{timestamp}.py"

            # Create the file path by joining the folder path and file name
            file_path = os.path.join(folder_path, file_name)
            
            # Write the clean code to the file
            with open(file_path, "w") as file:
                file.write(clean_code)
            return clean_code
    else:
        # Handle API error for code generation
        raise Exception("Code generation failed")


    
def generate_ui_scaffolding(input_variables):
    ui_scaffolding = ""

    for variable in input_variables:
        ui_scaffolding += f"{variable["name"]}: {variable["type"]} \n"
        # if variable["type"] == "str":
        #     ui_scaffolding += f'{variable["name"]} = input("Enter {variable["description"]}: ")\n'
        # elif variable["type"] == "int":
        #     ui_scaffolding += f'{variable["name"]} = int(input("Enter {variable["description"]}: "))\n'
        # elif variable["type"] == "float":
        #     ui_scaffolding += f'{variable["name"]} = float(input("Enter {variable["description"]}: "))\n'
        # Add more cases for different data types as needed
    print(ui_scaffolding)
    return ui_scaffolding