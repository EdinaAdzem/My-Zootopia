import json

def load_data(file_path):
    """Function to load the JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def display_animal_data(data):
    """Read and print the animal data contents"""
    output = ''
    for animal in data:
        if "name" in animal:
            output += '<li class="cards__item">'
            output += '<div class="card__title">'
            output += f"Name: {animal['name']}<br/>\n"
            output += '</div>'
            output += '<p class="card__text">'
            if "locations" in animal:
                first_location = animal['locations'][0]  # Get the location directly
                output += f"<strong>Location:</strong> {first_location}<br/>\n"
            if "characteristics" in animal:
                characteristics = animal["characteristics"]
                if "distinctive_feature" in characteristics:
                    output += f"<strong>Distinctive Features:</strong> {characteristics['distinctive_feature']}<br/>\n"
                if "temperament" in characteristics:
                    output += f"<strong>Temperament:</strong> {characteristics['temperament']}<br/>\n"
                if "lifespan" in characteristics:
                    output += f"<strong>Lifespan:</strong> {characteristics['lifespan']}<br/>\n"
                if "type" in characteristics:
                    output += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"
                if "diet" in characteristics:
                    output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"
            output += '</p>'
            output += '</li>'
    return output


def serialize_animal(animal_object):
    """changes to a single animal"""
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_object["name"]}</div>\n'
    output += '<p class="card__text">\n'

    if "locations" in animal_object:
        first_location = animal_object['locations'][0]
        output += f"<strong>Location:</strong> {first_location}<br/>\n"

    if "characteristics" in animal_object:
        characteristics = animal_object["characteristics"]
        if "group" in characteristics:
            output += f"<strong>Group:</strong> {characteristics['group']}<br/>\n"
        if "lifespan" in characteristics:
            output += f"<strong>Lifespan:</strong> {characteristics['lifespan']}<br/>\n"
        if "type" in characteristics:
            output += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"
        if "diet" in characteristics:
            output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"

    output += '</p>\n'
    output += '</li>\n'
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
