# Pokemon Scraping API
<img src="https://raw.githubusercontent.com/MicaelliMedeiros/micaellimedeiros/master/image/computer-illustration.png" min-width="400px" max-width="400px" width="400px" align="right" alt="Computador iuriCode">

<p align="left"> 
   Hi, this is a simple collector of pokemon data from the web and turning it into an API.
</p>

<p align="left">
  :space_invader: Languages: <strong>Python</strong>
</p>

<p align="left">
  💼 Libs and Tools: <strong>Flask, Flask-RESTful, Selenium, Beautiful Soup</strong>
</p>
</br>  
<p align="center">
   
Initial Purpose
---------------
   The initial proposal was to develop a <strong>web scraping</strong> that would collect data from the web and transform it into an api. 
The site from which the information was taken wouldn't make much difference to me, so I decided to look for something fun to work with. Between sports  sites, anime, music and games I ended up deciding on the (https://pokemondb.net/) site. 
What I really wanted was to test my skills and learn new technologies.

The Challengers  
---------------
   Well, among all the challenges I encountered making this little app was how would I get all that information from each of the pokemons on that site. Researching a little, I found a combination of libraries very efficient in this regard, <strong>Selenium</strong> and <strong>Beaultiful</strong> Soup helped me to collect each of the information I wanted with immense practicality.
Another small challenge was how I would create an api quickly with all that information collected, for that <strong>Flask-RESTful</strong> fit like a glove, when I least imagined my api was already in the air and working perfectly.

Conclusion
----------
      
The truth is that I had a lot of fun developing this application, in addition to learning how to quickly scrape a website, it's always good to be exploring new content and putting new ideas into practice. The application can be enhanced with new pokemon data, such as attributes, moves, etc. things I want to implement in the future, along with a special face for her.   

Getting Started
---------------
- Cloning this repository    
   open the terminal and type the commands

      git clone https://github.com/DsAlex-lnx/PokemonScrapingAPI.git
      cd PokemonScrapingAPI/

- Installing the requirements 
   
      pip install -r requirements.txt

- Running the Flask server   
 
      flask run

- The API contains a listing endpoint for all pokemons
      
      http://127.0.0.1:5000/api/v1/pokemon/
   
- However, you can only query the data of a single pokemon, passing its Pokedex ID in the endpoint, as in the example below:
      
      http://127.0.0.1:5000/api/v1/pokemon/1
