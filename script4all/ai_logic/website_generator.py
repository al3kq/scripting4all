import requests
from dotenv import load_dotenv
import os
import json
import datetime

def generate_index_html(description):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = "You are an AI that generates HTML code based on a provided description. Output only the HTML code. The result will be ran directly, no description or text. No Logos, links, or images. ONLY HTML here NO Javascript"
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

def generate_styles_css(description):
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
    system_prompt = "You are an AI that generates JavaScript code based on a provided description. ONLY output JavaScript code."
    user_prompt = f"Generate the JavaScript code for the following description:\n{description}"
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

def bring_it_togther(fix_file, all_code):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = """You are an AI that edits code and ensures it all works together. Look at the following code and ONLY make edits to the fix_file. No descriptions.
    Make sure the logic of the 3 files works together and this code will run correctly. Do Not output anything but the exact input format of edited code. No Logos, links, or images."""
    user_prompt = f"Ensure my code all works well together:\nAll Code: {all_code}\nFix File: {fix_file}"
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
    system_prompt = f"""You are an AI that ensures code can be used and is logically correct. Take a look at the index.html and script.js given.
    Suggest ONLY necessary edits to improve the user experience and fix bugs. We don't care about how the code looks or comments. No Logos, links, or images.
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
        "model": "gpt-4-turbo",
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

def iterate(code, suggestions):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = """You are an AI that edits code and ensures it all works together. Look at the following code and ONLY make edits. No descriptions.
    Consider and implement the suggestions given to you.
    Make sure the logic file works and this code will run correctly. Do Not output anything but the exact input format of edited code.
    """
    user_prompt = f"Help me fix my code:\nCode: {code}\nSuggestions: {suggestions}"
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
    You are an advanced AI system tasked with generating a basic single page website structure based on user input. The user will provide a detailed description of the website they want to create. Your job is to use this description to generate detailed assumptions and descriptions for the three main files of a website: index.html, styles.css, and script.js.
    NO IMAGES OR LINKS all single page.
    User Input:
    The user will provide a detailed description including:

    The purpose of the website (e.g., personal blog, e-commerce, portfolio).
    The target audience (e.g., young professionals, students, hobbyists).
    Main features and sections (e.g., homepage, about page, contact form, product listings).
    Any specific design preferences (e.g., color scheme, layout style).
    Your Task:

    Analyze the User Description: Understand the overall purpose, target audience, main features, and design preferences of the website.
    Generate Detailed Assumptions and Descriptions: Based on the user's input, provide a detailed description and assumptions for each of the three main files:
    index.html: Describe the structure and main sections of the HTML file.
    styles.css: Describe the design elements, including color schemes, typography, and layout styles.
    script.js: Describe the functionality and interactivity that will be included in the JavaScript file. If the website does not require a script.js just output BLANK STRING
            This description should go in depth on the nuances of complex reasoning if necessary. Think carefully though step by step.
    Output Format:
    Your output should be structured as follows:

    User Description Analysis:
    Title: {script_request.title}
    Description: {script_request.description}

    Detailed Assumptions and Descriptions:

    index.html:
    Description: Describe the HTML structure, including the main sections such as header, footer, main content areas, navigation menus, etc.

    styles.css:
    Description: Outline the color scheme, typography choices, and any specific design preferences mentioned by the user. 
    Describe the layout style, including any grid systems or responsive design elements.
    Detail the styling for different HTML elements and sections, such as buttons, headings, paragraphs, etc.

    script.js:
    Description: Describe the expected functionality and interactivity, such as form validations, animations, event handling, etc. Provide details on how the user will interact with the website, including any dynamic content or interactive features.



    Provide ONLY a JSON object with the following structure. Do not include any other fields.:
    {{
        "output_files": [
            {{
                "file_name": "index.html",
                "description": "<file_description>"
            }},
            {{
                "file_name": "styles.css",
                "description": "<file_description>"
            }},
            {{
                "file_name": "script.js",
                "description": "file_description>"
            }},
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
                    Be specific, make assumptions, only output json.
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
            elif file_name == "styles.css":
                style_code = generate_styles_css(description)
            elif file_name == "script.js":
                script_code = generate_script_js(description)
            else:
                continue
        response = {"index.html": html_code, "style.css": style_code, "script.js": script_code}
        response_copy = response.copy()
        for key in response:
            main_file_content = response[key]
            other_files = {k: v for k, v in response.items() if k != key}
            print(key)
            response[key] = bring_it_togther(main_file_content, other_files)
        # response_str = str(response)
        # response_str = bring_it_togther(response_str)
        # # print(response_str)
        # print(json.dumps(response_str))
        suggestions_str = logic_check(response["index.html"], response["script.js"])
        print(suggestions_str)
        try:
            suggestions_dict = eval(suggestions_str)
            print(suggestions_dict)
            index_suggestions = suggestions_dict['output_files'][0]['Suggestions']
            script_suggestions = suggestions_dict['output_files'][1]['Suggestions']
            response["index.html"] = iterate(response["index.html"], index_suggestions)
            response["script.js"] = iterate(response["script.js"], script_suggestions)
        except Exception as e:
            print("BAD")
            print(e)
            return json.dumps(response)

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