import requests
from dotenv import load_dotenv
import os
import json
import datetime

def generate_index_html(description):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = "You are an AI that generates HTML code based on a provided description. Output only the HTML code, a style.css and script.js will also be made. The result will be ran directly, no description or text. No Logos, links, or images. ONLY HTML here NO Javascript"
    user_prompt = f"Generate the HTML code for the following description:\n{description}"
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt}"
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict['choices'][0]['message']['content']
    return ""

def generate_style_css(description):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = "You are an AI that generates CSS code based on a provided description. Output only the CSS code. The result will be ran directly, no description or text."
    user_prompt = f"Generate the CSS code for the following description:\n{description}"
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt}"
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict['choices'][0]['message']['content']
    return ""

# Function to generate script.js
def generate_script_js(description):
    if description == "BLANK STRING":
        return ""
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = "###Instruction### Your task is to generate JavaScript code based on a provided description. You MUST output ONLY JavaScript code."
    user_prompt = f"###Question### Generate the JavaScript code for the following description:\n{description}"
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt}"
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict['choices'][0]['message']['content']
    return ""

def bring_it_together(fix_file, all_code,description):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = """You are an AI that edits code to ensure compatibility and correctness. Follow these instructions:
    1. Only make necessary edits to the provided fix_file.
    2. Ensure the logic of all three files works together and the code runs correctly.
    3. Output only the edited code in the exact input format, without any additional descriptions, logos, links, or images.
    4. Take the generated description into account to ensure the code is meeting all needs.
    5. Only the edited Fix File should be outputted, this will keep all html, css, js separate."""

    user_prompt = f"Ensure my code all works well together:\nDescription: {description}\nAll Code: {all_code}\nFix File: {fix_file}"
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt}"
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict['choices'][0]['message']['content']
    return all_code

def logic_check(index_code, script_code):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = f"""You are an AI that ensures code can be used and is logically correct. Review the provided index.html and script.js files. Suggest ONLY necessary edits to improve user experience and fix bugs. Focus on functionality, not appearance or comments. No logos, links, or images.
    Your suggestions are ONLY text descriptions, never code.
    Output Format:
    Your output should be structured as follows:

    User Files:
    index.html: {index_code}
    script.js: {script_code}

    Detailed Suggestions:

    script.js
    Suggestions: Provide specific suggestions on ONLY necessary changes that should be made to this code in order to make it work with index.html and improve the user experience.
    Make sure all the logic of the functions works as you reasonably assume they intend to.
    

    index.html:
    Suggestions: Provide specific suggestions on ONLY necessary changes that should be made to this code in order to make it work with script.js and improve the user experience.

    Provide ONLY a JSON object with the following structure. Do not include any other fields.:
    {{
        "output_files": [
            {{
                "file_name": "script.js",
                "Suggestions": "file_suggestions>"
            }},
            {{
                "file_name": "index.html",
                "Suggestions": "<file_suggestions>"
            }},
        ]
    }}
    """
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4o",
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"""
                    Be specific, make assumptions, only output json.
                    """
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict['choices'][0]['message']['content']
    return ""

def iterate(code, suggestions, other_file):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = """You are an AI that edits code to ensure compatibility and correctness. The other file is included to ensure logic works together. DO NOT edit Other_File Follow these instructions:
    1. Only make necessary edits to the code provided.
    2. Implement all given suggestions.
    3. Ensure the logic file works and the code runs correctly.
    4. Output only the edited code in the exact input format, without any additional descriptions.
    """
    user_prompt = f"Help me fix my code:\nEdit_Code: {code}\nSuggestions: {suggestions}\nOther_File: {other_file}"
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt}"
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_dict = json.loads(response.content.decode('utf-8'))
        return response_dict['choices'][0]['message']['content']
    return code

def generate_code(script_request):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    # Define the base prompt
    base_prompt = f"""
###Instruction### Your task is to generate and ensure a cohesive single-page website structure based on user input. The user will provide a detailed description of the website they want to create. You MUST generate detailed assumptions and descriptions for the three main files of a website: index.html, style.css, and script.js. No images or links, all single-page.

###Example### User Input:
The user will provide a detailed description including:
- The purpose of the website (e.g., personal blog, e-commerce, portfolio).
- The target audience (e.g., young professionals, students, hobbyists).
- Main features and sections (e.g., homepage, about page, contact form, product listings).
- Any specific design preferences (e.g., color scheme, layout style).

###Instruction### Your task:
1. Analyze the User Description: Understand the overall purpose, target audience, main features, and design preferences of the website.
2. Generate Detailed Assumptions and Descriptions: Based on the user's input, provide a detailed description and assumptions for each of the three main files:
    - index.html: Describe the structure and main sections of the HTML file. Ensure all necessary elements are included, such as dynamically generated grids and keyboards.
    - style.css: Describe the design elements, including color schemes, typography, and layout styles. Ensure all referenced class names and styles are defined.
    - script.js: Describe the functionality and interactivity that will be included in the JavaScript file. Ensure that all necessary elements are dynamically generated and that all functionality, such as keyboard input and game reset, is implemented. If the website does not require a script.js, output a blank string. Provide in-depth details on the nuances of complex reasoning if necessary.

###Example### Output Format:
Your output should be structured as follows:

User Description Analysis:
- Title: {script_request.title}
- Description: {script_request.description}

Detailed Assumptions and Descriptions:
- index.html:
  Description: Describe the HTML structure, including the main sections such as header, footer, main content areas, navigation menus, etc. Ensure that necessary elements such as the word grid and virtual keyboard are dynamically generated.
- style.css:
  Description: Outline the color scheme, typography choices, and any specific design preferences mentioned by the user. Describe the layout style, including any grid systems or responsive design elements. Detail the styling for different HTML elements and sections, such as buttons, headings, paragraphs, etc. If the style is not specified, go for a modern look. Ensure all class names referenced in script.js are defined.
- script.js:
  Description: Describe the expected functionality and interactivity, such as form validations, animations, event handling, etc. Provide details on how the user will interact with the website, including any dynamic content or interactive features. Ensure all referenced class names and functionality, such as dynamic generation of elements and game reset, are implemented.

Provide ONLY a JSON object with the following structure. Do not include any other fields:
{{
    "output_files": [
        {{
            "file_name": "index.html",
            "description": "<file_description>"
        }},
        {{
            "file_name": "style.css",
            "description": "<file_description>"
        }},
        {{
            "file_name": "script.js",
            "description": "<file_description>"
        }}
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
                    User Description Analysis:
                        - Title: {script_request.title}
                        - Description: {script_request.description}
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
        response_dict = eval(content_str)
        print(response_dict)
        html_code, style_code, script_code = "", "", ""
        for file in response_dict['output_files']:
            file_name = file['file_name']
            description = file['description']
            
            if file_name == "index.html":
                html_code = generate_index_html(description)
            elif file_name == "style.css":
                style_code = generate_style_css(description)
            elif file_name == "script.js":
                script_code = generate_script_js(description)
            else:
                continue
        output_dir = 'temp_output'
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "index1.html"), 'w') as file:
            file.write(html_code)
        with open(os.path.join(output_dir, "style1.css"), 'w') as file:
            file.write(style_code)
        with open(os.path.join(output_dir, "script1.js"), 'w') as file:
            file.write(script_code)
        response = {"index.html": html_code, "style.css": style_code, "script.js": script_code}
        response_copy = response.copy()
        # response_str = str(response)
        # response_str = bring_it_togther(response_str)
        # # print(response_str)
        # print(json.dumps(response_str))
        suggestions_str = logic_check(response["index.html"], response["script.js"])
        print(suggestions_str)
        try:
            suggestions_dict = eval(suggestions_str)
            index_suggestions = suggestions_dict['output_files'][1]['Suggestions']
            script_suggestions = suggestions_dict['output_files'][0]['Suggestions']
            response["index.html"] = iterate(response["index.html"], index_suggestions, response["script.js"])
            response["script.js"] = iterate(response["script.js"], script_suggestions, response["index.html"])
        except Exception as e:
            print("BAD")
            print(e)
            return json.dumps(response)
        with open(os.path.join(output_dir, "index2.html"), 'w') as file:
            file.write(response["index.html"])
        with open(os.path.join(output_dir, "style2.css"), 'w') as file:
            file.write(response["style.css"])
        with open(os.path.join(output_dir, "script2.js"), 'w') as file:
            file.write(response["script.js"])

        for file in response_dict['output_files']:
            file_name = file['file_name']
            description = file['description']
            
            main_file_content = response[file_name]
            other_files = {k: v for k, v in response.items() if k != file_name}
            
            print(file_name)
            response[file_name] = bring_it_together(main_file_content, other_files, description)
        # for key in response:
        #     main_file_content = response[key]
        #     other_files = {k: v for k, v in response.items() if k != key}
        #     print(key)
        #     response[key] = bring_it_togther(main_file_content, other_files)

        with open(os.path.join(output_dir, "index3.html"), 'w') as file:
            file.write(response["index.html"])
        with open(os.path.join(output_dir, "style3.css"), 'w') as file:
            file.write(response["style.css"])
        with open(os.path.join(output_dir, "script3.js"), 'w') as file:
            file.write(response["script.js"])
        return json.dumps(response)

        content_data = json.loads(response)

        input_variables = content_data["input_variables"]

        # Generate UI scaffolding based on input variables
        # ui_scaffolding = generate_ui_scaffolding(input_variables)

        # Generate code based on the script request and input variables
        code_prompt = f"""
        Please analyze the following request and identify the potential input variables.
        This user needs help writing Python code for a project! Think indepth what knowledge this question needs for a robust answer.
        Non technical user. Use assumptions. Think logically of the most likely interpretation of the description.
        Import packages as necessary. Do NOT need to pip install anything.
        Please generate ONLY Python code for the following script request:

        Title: {script_request.title}
        Description: {script_request.description}

        Input Variables:
        {input_variables}

        Requirements:
        - Use Python 3.x syntax
        - Follow PEP 8 style guide for code formatting
        - Include necessary error handling and input validation

        Code Template:
        ```python
            Your code here
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
                    "content": "Only generate error free and executable Python code."
                }
            ]
        }
        code_response = requests.post(api_url, headers=headers, json=data)

        if code_response.status_code == 200:
            response_dict = json.loads(code_response.content.decode('utf-8'))
            content_str = response_dict['choices'][0]['message']['content']
            print(content_str)
        return "boobs"