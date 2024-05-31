# your_module.py
import base64
import requests
import os
from dotenv import load_dotenv
from PIL import Image
from pdf2image import convert_from_path
import json

def encode_file(file_path):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    return encoded_string

def convert_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    image_path = pdf_path.replace('.pdf','.jpg')
    images[0].save(image_path, 'JPEG')
    return image_path

def get_user_details_response(script_request, file_content_type):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    # Access the uploaded file
    description_file = script_request.description_file
    if not description_file:
        raise ValueError("No file uploaded")

    file_path = description_file.path  # Get the file path

    if file_content_type == 'application/pdf':
        # Convert PDF to image
        file_path = convert_pdf_to_image(file_path)
        file_content_type = 'image/jpeg'

    # Encode the image content to base64
    base64_file = encode_file(file_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    if file_content_type == 'image/jpeg':
        data_url_prefix = "data:image/jpeg;base64,"
    else:
        raise ValueError("Unsupported file type")

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """Return all information about the application in a text form.
                            Be sure to include the following if present:
                            Contact_Details: <contact_details>
                            Work_Experience:
                                Company: <work_experience_company>
                                Title: <work_experience_title>
                                dates: <work_experience_date>
                                content: <work_experience_content>
                            Education:
                                School: <education_school>
                                Degree: <education_degree_type>
                                Year: <education_year>
                            Skills: <skills>
                            Other: <other>
                            """
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{data_url_prefix}{base64_file}"
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(response)

    if response.status_code == 200:
        # Process the response from the API
        response_data = response.json()
        generated_details = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
    else:
        raise Exception(f"Failed to generate code: {response.status_code} - {response.text}")

    return generated_details


def parse_user_details(user_str):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")
    system_prompt = "You are an AI that takes in a parsed string of a users resume. Your job is to output a list of relevant field names for this user. Ex (Work history, education, skills, projects, ...)"
    user_prompt = f"Generate the Field Names for the following user resume:\n{user_str}"
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
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

def generate_code(script_request, file_content_type):
    response_details = get_user_details_response(script_request, file_content_type)
    important = parse_user_details(response_details)
    print(important)
    return important
    