import data_fetcher

def display_animal_data(data,animal_name):
    #Read and print the animal data contents
    #milestone 3 if the animal is not there
    if not data:
        return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    output = ''
    for animal in data:
        if "name" in animal:
            output += '<li class="cards__item">'
            output += '<div class="card__title">'
            output += f"Name: {animal['name']}<br/>\n"
            output += '</div>'
            output += '<p class="card__text">'
            if "locations" in animal:
                first_location = animal['locations'][0]
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
        else:
            print("The animal ""goadohjasgfas" "doesn't exist.")
    return output

def serialize_animal(animal_object):
    """Changes to a single animal"""
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

def main():
    # Define the animal name
    animal_name = input("Please enter the name of the animal:")

    # Load the animal data from the API
    animals_data = data_fetcher.fetch_data(animal_name)

    for animal in animals_data:
        print(f"{animal['name']} ({animal['locations']})")

    #generate the animals info
    animals_info = display_animal_data(animals_data, animal_name)

    #templ
    template_new_content = load_template("animals_template.html")

    # Replace with animals content into inputed by the user
    new_animal_info_content = replace_placeholder(template_new_content, animals_info)

    #to the  output file
    write_html(new_animal_info_content, "animals.html")


if __name__ == "__main__":
    main()
