# My Zootopia Project
My Zootopia is an interactive Python-based project that allows users to explore information about 
various animals by fetching data from the API Ninjas Animals API. 
Users can enter the name of an animal, and the program retrieves detailed information about that animal,
which is then formatted and displayed in a user-friendly HTML file called animals.html.

# Features
* **User Input:** The program prompts the user to enter the name of an animal.
* **API Integration:** It integrates with the API Ninjas Animals API to fetch data about the specified animal. This data includes various characteristics such as the animal's distinctive features, temperament, lifespan, type, and diet.
* **Data Handling:** If the entered animal name does not exist in the database, the program gracefully handles this scenario by displaying a friendly message in the output HTML file.
* **HTML Generation:** The retrieved data is then used to generate an informative and structured HTML file, animals.html. This file is created using a template that includes placeholders for animal data, which are replaced with actual information fetched from the API.
* **Output:** The generated HTML file includes a well-formatted list of animal characteristics, making it easy for users to read and understand the information.
* 
# Workflow
* _User Input:_ The program begins by asking the user to enter the name of an animal.
* Fetching Data: Using the entered animal name, the program sends a request to the API Ninjas Animals API and retrieves the corresponding data.
* _Handling Non-Existent Animals:_ If the API does not return any data for the specified animal name, the program generates an HTML message indicating that the animal does not exist.
* Loading Template: The program loads an HTML template which contains placeholders for the animal data.
* _Replacing Placeholders:_ The fetched animal data is inserted into the template, replacing the placeholders with actual information.
* _Writing HTML File:_ The final HTML content is written to an output file named animals.html.
* Result: The animals.html file is created or updated, containing detailed information about the specified animal or an appropriate message if the animal does not exist.

# Example
If a user enters "Fox" as the animal name, the program will fetch and display detailed information about foxes. 
If the user enters a name like "goadohjasgfas" which does not correspond to any known animal, 
the program will inform the user that the animal does not exist in the database.

**My Zootopia** makes it simple and enjoyable to learn about different animals by combining API data retrieval with 
dynamic HTML generation. The project showcases the power of APIs and dynamic content generation, 
making it a great educational tool and a fun project to explore and expand upon.
