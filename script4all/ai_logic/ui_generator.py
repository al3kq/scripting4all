def generate_ui_scaffolding(input_variables):
    ui_scaffolding = ""

    for variable in input_variables:
        if variable["type"] == "str":
            ui_scaffolding += f'{variable["name"]} = input("Enter {variable["description"]}: ")\n'
        elif variable["type"] == "int":
            ui_scaffolding += f'{variable["name"]} = int(input("Enter {variable["description"]}: "))\n'
        elif variable["type"] == "float":
            ui_scaffolding += f'{variable["name"]} = float(input("Enter {variable["description"]}: "))\n'
        # Add more cases for different data types as needed

    return ui_scaffolding