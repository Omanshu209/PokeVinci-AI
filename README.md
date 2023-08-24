# PokeVinci
This is a Python-based application that allows users to `search for information about different Pokemons`. The app has two main screens:

**Pokemon Loader**: This screen allows users to search for a Pokemon by name or ID. When the user enters a valid query and clicks the search button, the app `loads the corresponding Pokemon's information`.
![Screenshot_2023-03-18-17-42-57-384](https://user-images.githubusercontent.com/114089324/226105428-7a23fb54-cd81-47b9-ae36-5f6589e305a6.jpeg)

**Pokemon Details**: This screen `displays the information about the Pokemon` selected by the user in the Pokemon Loader screen including its `image`, `name`, `ID`, `type(s)`, `height`, `weight`, `abilities`, and `stats` (HP, Attack, Defense, Special Attack, Special Defense, and Speed). The app shows the same information as in the previous screen but in a more detailed and organized way.
![Screenshot_2023-08-24-19-21-56-376](https://github.com/Omanshu209/PokeVinci/assets/114089324/aa7cdf20-7dcd-40e7-983c-80ee893f1010)

## Technologies Used
The app is built using the following technologies:

**Python 3.8**: The core programming language used to develop the app.

**Kivy**: A free and open-source Python framework for creating multi-touch applications with a natural user interface (NUI).

**KivyMD**: A collection of Material Design compliant widgets for Kivy, a Python framework for building multi-touch applications.

**PokeAPI**: A RESTful API that provides access to data about Pokemon creatures from the Pokemon video game franchise.

## Requirements
To run the app, you need to have the following software installed on your computer:
> `Python 3`

You also need to install the following Python packages:

> `kivy (v2.0.0)`
>
> `kivymd (v1.1.1)`
>
> `requests (v2.28.2)`

You can install them by running the following command in your terminal:
```
pip install -r requirements.txt
```
**OR**
```
pip install kivy==2.0.0 kivymd==1.1.1 requests==2.28.2
```
## Usage
To run the app, you need to execute the `main.py` script located in the root directory of the project. You can do it by running the following command in your terminal:
```
python3 main.py
```
When you run the app, you will see the Pokemon Loader screen. `Enter` the name or ID of a Pokemon and click the `search` button to `load` its information. If the Pokemon exists, you will see its name, image, and other details. `Click` the Pokemon button to see more details about the selected Pokemon in the Pokemon Details screen.

In the Pokemon Details screen, you can see the same information as in the previous screen but in a more detailed and organized way. Click the back button to return to the Pokemon Loader screen and search for another Pokemon.

## Credits
This app was developed by **Omanshu**.
