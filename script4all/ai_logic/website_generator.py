import requests
from dotenv import load_dotenv
import os
import json

def debug_print_request(api_url, headers, data):
    """
    Helper function to print debug info before the request is made.
    """
    print("\n[DEBUG] --- Preparing Request ---")
    print(f"API URL: {api_url}")
    print("HEADERS:")
    for k, v in headers.items():
        print(f"   {k}: {v}")
    print("DATA:")
    print(json.dumps(data, indent=2))

def debug_print_response(response):
    """
    Helper function to print debug info after the request is made.
    """
    print("\n[DEBUG] --- Response Info ---")
    print(f"Status Code: {response.status_code}")
    print("REASON:", response.reason)
    print("RESPONSE HEADERS:")
    for k, v in response.headers.items():
        print(f"   {k}: {v}")
    try:
        print("RESPONSE TEXT:", response.text)
    except Exception as e:
        print("Could not read response text due to error:", e)

def generate_index_html(description):
    """
    Generates the HTML code for index.html using a GPT-4 model, 
    returning the content from the 'html' field of the structured response schema.
    """
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    system_prompt = (
        "You are an AI that generates HTML code based on a provided description. "
        "Output only complete HTML code. A style.css and script.js will also be made; make sure to reference these. "
        "The result will be ran directly, no description or text. No Logos, links, or images. ONLY HTML here NO Javascript."
    )
    user_prompt = f"Generate the HTML code for the following description:\n{description}"

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "html_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "html": {
                            "description": "The generated HTML code based on the description",
                            "type": "string"
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
    }

    # Debug Print - request
    debug_print_request(api_url, headers, data)

    response = requests.post(api_url, headers=headers, json=data)

    # Debug Print - response
    debug_print_response(response)

    if response.status_code == 200:
        response_dict = response.json()
        # If the structured response is embedded in JSON, parse accordingly:
        return response_dict.get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        # Additional debug if needed
        print("[DEBUG] generate_index_html request failed.")
    return ""

def generate_style_css(description, index, user_descrption):
    """
    Generates the CSS code for style.css using a GPT-4 model, 
    returning the content from the 'css' field of the structured response schema.
    """
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    system_prompt = (
        "You are an AI that generates CSS code based on a provided description. Output only the CSS code. "
        "The result will be ran directly, no description or text.\n"
        "Below is the user description and index code. Make sure the logic for this file makes sense.\n\n"
        f"user description: {user_descrption}\n"
        f"index.html: {index}"
    )
    user_prompt = f"Generate the CSS code for the following description:\n{description}"

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "css_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "css": {
                            "description": "The generated CSS code based on the description",
                            "type": "string"
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
    }

    debug_print_request(api_url, headers, data)
    response = requests.post(api_url, headers=headers, json=data)
    debug_print_response(response)

    if response.status_code == 200:
        response_dict = response.json()
        return response_dict.get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        print("[DEBUG] generate_style_css request failed.")
    return ""

def generate_script_js(description, index, style, user_description):
    """
    Generates the JavaScript code for script.js using a GPT-4 model, 
    returning the content from the 'js' field of the structured response schema. 
    If `description == "BLANK STRING"`, returns an empty string.
    """
    if description == "BLANK STRING":
        return ""

    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    system_prompt = (
        "###Instruction### Your task is to generate JavaScript code based on a provided description. "
        "You MUST output ONLY JavaScript code.\n"
        "Make sure functions are only used AFTER their declaration.\n\n"
        "Below is the user description, index code, and style code. Make sure the logic for this file makes sense.\n\n"
        f"user description: {user_description}\n"
        f"index.html: {index}\n"
        f"style.css: {style}\n"
    )
    user_prompt = f"###Question### Generate the JavaScript code for the following description:\n{description}"

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "js_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "js": {
                            "description": "The generated JS code based on the description",
                            "type": "string"
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
    }

    debug_print_request(api_url, headers, data)
    response = requests.post(api_url, headers=headers, json=data)
    debug_print_response(response)

    if response.status_code == 200:
        response_dict = response.json()
        return response_dict.get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        print("[DEBUG] generate_script_js request failed.")
    return ""

def bring_it_together(fix_file, all_code):
    """
    Edits code to ensure compatibility and correctness, returning only the edited fix_file.
    """
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    system_prompt = (
        "You are an AI that edits code to ensure compatibility and correctness. Follow these instructions:\n"
        "1. Only make necessary edits to the provided fix_file.\n"
        "2. Ensure the logic of all three files works together and that code runs correctly.\n"
        "3. Output only the edited code in the exact input format, without any additional descriptions.\n"
        "5. Only the edited Fix File should be outputted, this will keep all html, css, js separate."
    )
    user_prompt = f"Ensure my code all works well together:\nAll Code: {all_code}\nFix File: {fix_file}"

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    }

    debug_print_request(api_url, headers, data)
    response = requests.post(api_url, headers=headers, json=data)
    debug_print_response(response)

    if response.status_code == 200:
        response_dict = response.json()
        return response_dict.get("choices", [{}])[0].get("message", {}).get("content", fix_file)
    else:
        print("[DEBUG] bring_it_together request failed.")
    return all_code

def gen_suggestions(index_code, script_code, style_code, description):
    """
    Generates suggestions for improving user experience and code compatibility.
    Uses a JSON object response format, per your instructions.
    """
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    system_prompt = (
        "You are an AI that ensures code can be used and is logically correct. "
        "Review the provided index.html, script.js, and style.css files. "
        "Suggest ONLY necessary edits to improve user experience and fix bugs. "
        "Focus on functionality, not appearance or comments. No logos, links, or images.\n\n"
        "Your suggestions are ONLY text descriptions, never code. "
        "Do not just debug; also improve functionality based on the user-provided description. "
        "Provide step by step logic on how to implement each suggestion.\n\n"
        "Output Format:\n"
        "Your output should be structured as follows:\n\n"
        f"User Description:\n{description}\n\n"
        f"User Files:\nindex.html: {index_code}\nscript.js: {script_code}\nstyle.css: {style_code}\n\n"
        "Detailed Suggestions:\n\n"
        "script.js\n"
        "Suggestions: Provide specific suggestions on ONLY necessary changes that should be made to this code in order to make it work with index.html and improve the user experience. "
        "Provide step by step logic on how to implement each suggestion.\n\n"
        "index.html:\n"
        "Suggestions: Provide specific suggestions on ONLY necessary changes that should be made to this code in order to make it work with script.js and improve the user experience.\n\n"
        "style.css:\n"
        "Suggestions: Ensure all references in index.html have an appropriate style.\n\n"
        "Provide ONLY a JSON object with the following structure. Do not include any other fields:\n"
        "{\n"
        '    "output_files": [\n'
        '        {\n'
        '            "file_name": "script.js",\n'
        '            "Suggestions": "<file_suggestions>"\n'
        "        },\n"
        '        {\n'
        '            "file_name": "index.html",\n'
        '            "Suggestions": "<file_suggestions>"\n'
        "        },\n"
        '        {\n'
        '            "file_name": "style.css",\n'
        '            "Suggestions": "<file_suggestions>"\n'
        "        }\n"
        "    ]\n"
        "}"
    )

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "o1-2024-12-17",  # if you use a different model, keep it or unify
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": "Be specific, make assumptions, only output json."
            }
        ]
    }

    debug_print_request(api_url, headers, data)
    response = requests.post(api_url, headers=headers, json=data)
    debug_print_response(response)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        print("[DEBUG] gen_suggestions request failed.")
    return ""

def iterate(code, suggestions, other_file):
    """
    Edits code to implement suggestions, ensuring the logic works well with another file.
    Returns only the edited code.
    """
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    system_prompt = (
        "You are an AI that edits code to ensure compatibility and correctness. "
        "The other file is included to ensure logic works together. DO NOT edit Other_File.\n"
        "Follow these instructions:\n"
        "1. Only make necessary edits to the code provided.\n"
        "2. Implement all given suggestions if applicable.\n"
        "3. Ensure the logic file works and the code runs correctly.\n"
        "4. Output only the edited code in the exact input format, without any additional descriptions.\n"
    )
    user_prompt = (
        f"Help me fix my code:\nEdit_Code: {code}\nSuggestions: {suggestions}\nOther_File: {other_file}"
    )

    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    }

    debug_print_request(api_url, headers, data)
    response = requests.post(api_url, headers=headers, json=data)
    debug_print_response(response)

    if response.status_code == 200:
        response_dict = response.json()
        return response_dict.get("choices", [{}])[0].get("message", {}).get("content", code)
    else:
        print("[DEBUG] iterate request failed.")
    return code

def generate_code(script_request):
    """
    Orchestrates the generation of the 3 main files (index.html, style.css, script.js),
    obtains suggestions, and attempts to iterate/fix code based on those suggestions.
    """
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    base_prompt = (
        "###Instruction### Your task is to generate and ensure a cohesive single-page website structure based on user input. "
        "The user will provide a detailed description of the website they want to create. You MUST generate detailed assumptions "
        "and descriptions for the three main files of a website: index.html, style.css, and script.js. No images or links.\n\n"
        "1. Analyze the User Description.\n"
        "2. Generate Detailed Assumptions and Descriptions for each file in JSON.\n\n"
        "Output Format:\n"
        "Only output a JSON object with this structure:\n"
        "{\n"
        '    "output_files": [\n'
        '        {\n'
        '            "file_name": "index.html",\n'
        '            "description": "<file_description>"\n'
        "        },\n"
        '        {\n'
        '            "file_name": "style.css",\n'
        '            "description": "<file_description>"\n'
        "        },\n"
        '        {\n'
        '            "file_name": "script.js",\n'
        '            "description": "<file_description>"\n'
        "        }\n"
        "    ]\n"
        "}"
    )

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
                "content": base_prompt
            },
            {
                "role": "user",
                "content": (
                    f"User Description Analysis:\n"
                    f"    - Title: {script_request.title}\n"
                    f"    - Description: {script_request.description}\n"
                )
            }
        ]
    }

    debug_print_request(api_url, headers, data)
    response = requests.post(api_url, headers=headers, json=data)
    debug_print_response(response)

    if response.status_code != 200:
        print("[DEBUG] generate_code request failed.")
        print("Status code:", response.status_code)
        return json.dumps({"index.html": "error", "style.css": "error", "script.js": "error"})

    response_dict = response.json()
    content_str = response_dict.get("choices", [{}])[0].get("message", {}).get("content", "")

    # Safely parse the JSON structure
    try:
        parsed_output = json.loads(content_str)
    except json.JSONDecodeError:
        print("[DEBUG] Unable to parse the JSON response from generate_code.")
        return json.dumps({"index.html": "", "style.css": "", "script.js": ""})

    print("[DEBUG] Parsed output from generate_code:", parsed_output)

    # Extract descriptions for each file and pass them into your code-generation functions
    html_code, style_code, script_code = "", "", ""
    for file_info in parsed_output.get("output_files", []):
        file_name = file_info.get("file_name")
        file_desc = file_info.get("description", "")

        if file_name == "index.html":
            html_code = generate_index_html(file_desc)
        elif file_name == "style.css":
            style_code = generate_style_css(file_desc, html_code, script_request.description)
        elif file_name == "script.js":
            script_code = generate_script_js(file_desc, html_code, style_code, script_request.description)
        else:
            continue

    response_data = {
        "index.html": html_code,
        "style.css": style_code,
        "script.js": script_code
    }

    # Generate suggestions for improvements
    suggestions_str = gen_suggestions(
        response_data["index.html"],
        response_data["script.js"],
        response_data["style.css"],
        script_request.description
    )

    try:
        suggestions_dict = json.loads(suggestions_str)
        print("[DEBUG] Suggestions dictionary from gen_suggestions:", suggestions_dict)
    except json.JSONDecodeError as e:
        print("[DEBUG] Unable to parse suggestions JSON.")
        print(e)
        return json.dumps(response_data)

    # Extract suggestions
    script_suggestions = ""
    index_suggestions = ""
    style_suggestions = ""

    for item in suggestions_dict.get("output_files", []):
        if item.get("file_name") == "script.js":
            script_suggestions = item.get("Suggestions", "")
        elif item.get("file_name") == "index.html":
            index_suggestions = item.get("Suggestions", "")
        elif item.get("file_name") == "style.css":
            style_suggestions = item.get("Suggestions", "")

    # Apply the suggestions
    response_data["index.html"] = iterate(
        response_data["index.html"],
        index_suggestions,
        response_data["script.js"]
    )
    response_data["script.js"] = iterate(
        response_data["script.js"],
        script_suggestions,
        response_data["index.html"]
    )
    response_data["style.css"] = iterate(
        response_data["style.css"],
        style_suggestions,
        response_data["index.html"]
    )

    # Optionally unify each file with bring_it_together
    # for file_info in parsed_output.get("output_files", []):
    #     file_name = file_info.get("file_name")
    #     if file_name in response_data:
    #         main_file_content = response_data[file_name]
    #         other_files = {k: v for k, v in response_data.items() if k != file_name}
    #         response_data[file_name] = bring_it_together(main_file_content, other_files)

    return json.dumps(response_data)
