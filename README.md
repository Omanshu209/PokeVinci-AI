<div align = "center">
  <h1>
    <img src = "https://github.com/Omanshu209/PokeVinci/assets/114089324/77dca620-0daf-4153-b3d4-ced19028f7af" width = "40" />
    PokeVinci
    <img src = "https://github.com/Omanshu209/PokeVinci/assets/114089324/77dca620-0daf-4153-b3d4-ced19028f7af" width = "40" />
  </h1>
</div>

This is a Python-based application that allows users to `search for information about different Pokemons`. The app has three main screens:

**Search**: This screen allows users to search for a Pokemon by name or ID. When the user enters a valid query and clicks the search button, the app `loads the corresponding Pokemon's information`.
<img src = "https://github.com/Omanshu209/PokeVinci-AI/assets/114089324/060c97f2-dfd4-4441-abe3-15fb9caa1434" width = "500" align = "left"/>

**Stats**: This screen `displays the information about the Pokemon` selected by the user in the Pokemon Loader screen including its `image`, `name`, `ID`, `type(s)`, `height`, `weight`, `abilities`, and `stats` (HP, Attack, Defense, Special Attack, Special Defense, and Speed). The app shows the same information as in the previous screen but in a more detailed and organized way.
<img src = "https://github.com/Omanshu209/PokeVinci-AI/assets/114089324/63604fd5-b916-4ce5-a9a4-f9e4e533b4ce" width = "500" align = "right"/>

**AI**: The AI section of this app leverages `advanced image classification` techniques to `predict Pokemon` species from images. Capture the essence of your `surroundings`, and let the AI unveil the Pokemon that resides within your photos. The application's intuitive interface makes it easy for both Pokemon enthusiasts and AI enthusiasts to dive into a seamless and magical experience.
<img src = "https://github.com/Omanshu209/PokeVinci-AI/assets/114089324/980eaa00-c135-441d-ab94-de1a01529c86" width = "550" align = "left"/>

## Technologies Used
The app is built using the following technologies:

**Python 3.8**: The core programming language used to develop the app.

**Kivy**: A free and open-source Python framework for creating multi-touch applications with a natural user interface (NUI).

**KivyMD**: A collection of Material Design compliant widgets for Kivy, a Python framework for building multi-touch applications.

**PyTorch**:........

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
>
> `torch (v1.9.1)`
>
> `torchvision(v0.10.0)`
>
> `pillow`

You can install them by running the following command in your terminal:
```
pip install -r requirements.txt
```
**OR**
```
pip install kivy==2.0.0 kivymd==1.1.1 requests==2.28.2 torch==1.9.1 torchvision==0.10.0 pillow
```
## Usage
To run the app, you need to execute the `main.py` script located in the root directory of the project. You can do it by running the following command in your terminal:
```
python3 main.py
```
When you run the app, you will see the *Search* screen. `Enter` the name or ID of a Pokemon and click the `PokeSearch` button to `load` its information. If the Pokemon exists, you will see its name, image, and other details. `Click` the Pokemon icon to see more details about the selected Pokemon in the *Stats* screen.

In the *Stats* screen, you can see the same information as in the previous screen but in a more detailed and organized way.

## Credits
The app and AI were developed by **Omanshu**.
