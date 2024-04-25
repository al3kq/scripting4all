import subprocess

def execute_python_script(script_path):
    # Create a Docker container and execute the Python script
    command = f"docker run -v {script_path}:/app/script.py python:3.9 python /app/script.py"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Decode the output and error messages
    output = stdout.decode('utf-8')
    error = stderr.decode('utf-8')

    return output, error