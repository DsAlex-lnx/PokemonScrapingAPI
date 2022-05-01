from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://pokemondb.net/pokedex/national'

option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)
driver.get(url)

main_table = driver.find_element_by_id('main')
html_content = main_table.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
pokemon_generations = soup.find_all('div', {'class':'infocard'})

pokemon_types = []

def pokemons_infos():
    pokemon_infos = []

    for pokemon in pokemon_generations:
        pokedex_id = pokemon.find('small').text
        pokemon_name = pokemon.find('a', {'ent-name'}).text
        pokemon_type = pokemon.find_all('a', {'itype'})
        
        types = []   
        
        types.append(pokemon_type[0].text)
        if len(pokemon_type) > 1:
            types.append(pokemon_type[1].text)
        
        pokemon_type = types

        image_url = pokemon.find('span', {'class':'img-fixed img-sprite'})
        if image_url is not None:
            pokemon_image = image_url['data-src']
        else:
            pokemon_image = pokemon.find('img')['src']

        data_dict = {
            'pokedex_id' : pokedex_id,
            'pokemon_name' : pokemon_name,
            'pokemon_type': pokemon_type,
            'pokemon_image': pokemon_image
        }

        pokemon_infos.append(data_dict)
    
    return pokemon_infos

def searching_pokemon(pokedex_id):
    pokemon_info = pokemons_infos()
        
    pokemon = next((pokemon for pokemon in pokemon_info if pokemon['pokedex_id'] == pokedex_id), None)
    return pokemon 

def catching_by_id(pokedex_id):
    pokedex_id = int(pokedex_id)
    if pokedex_id < 10:
        pokedex_id = '#00'+str(pokedex_id)
        return searching_pokemon(pokedex_id)
   
    elif pokedex_id < 100:
        pokedex_id = '#0'+str(pokedex_id)
        return searching_pokemon(pokedex_id)
    
    else: 
        pokedex_id = '#'+str(pokedex_id)
        return searching_pokemon(pokedex_id)

driver.quit()