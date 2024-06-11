import json

def load_data(file_path):
    """Function to load the JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def display_animal_data(data):
    """read and print the animal_data contents"""
    output = ''
    for animal in data:
        if "name" in animal:
            output += f"Name: {animal['name']}"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}"
        if "locations" in animal:
            output += f"Location: {animal['locations'][0]}"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}"
        output += "<br/>\n"
    return output

def load_template(template_path):
    """Read and return the content of the HTML template"""
    with open(template_path, "r") as template_file:
        return template_file.read()

def replace_placeholder(template_content, animals_info):
    """Replace the placeholder in the template with the animals' data"""
    return template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

def write_html(content, output_path):
    """Write the new HTML content to a file"""
    with open(output_path, "w") as output_file:
        output_file.write(content)

if __name__ == "__main__":
    # Load the animal data
    animals_data = load_data("animals_data.json")

    # Load the template content
    template_new_content = load_template("animals_template.html")

    # Generate the animals information
    animals_info = display_animal_data(animals_data)

    # replace wtih animal info
    new_animal_info_content = replace_placeholder(template_new_content, animals_info)

    # Write the new content to the output file
    write_html(new_animal_info_content, "animals.html")