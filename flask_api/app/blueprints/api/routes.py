from . import bp as api
from flask import jsonify, request, url_for, render_template, redirect
import requests
from .models import NationalPokemon, JohtoPokemon, KantoPokemon, SinnohPokemon, AlolaPokemon, UnovaPokemon, PokemonTypes, Items, ItemCategories

@api.route('/', methods=['GET'])
def api_page():
    return render_template('api/api.html')

# API Routes
@api.route('/items', methods=['GET', 'POST'])
def items():
    """
    [GET] /api/items
    """
    return jsonify([item.attributes_as_dictionary() for item in Items.query.all()])

@api.route('/item_categories', methods=['GET', 'POST'])
def item_categories():
    """
    [GET] /api/item_categories
    """
    return jsonify([category.attributes_as_dictionary() for category in ItemCategories.query.all()])

@api.route('/pokemon_types', methods=['GET', 'POST'])
def pokemon_types():
    """
    [GET] /api/pokemon_types
    """
    return jsonify([types.attributes_as_dictionary() for types in PokemonTypes.query.all()])

@api.route('/national_dex', methods=['GET', 'POST'])
def national_dex():
    """
    [GET] /api/national_dex
    """
    return jsonify([pokemon.attributes_as_dictionary() for pokemon in NationalPokemon.query.all()])

@api.route('/kanto_dex', methods=['GET', 'POST'])
def kanto_dex():
    """
    [GET] /api/kanto_dex
    """
    return jsonify([pokemon.attributes_as_dictionary() for pokemon in KantoPokemon.query.all()])

@api.route('/johto_dex', methods=['GET', 'POST'])
def johto_dex():
    """
    [GET] /api/johto_dex
    """
    return jsonify([pokemon.attributes_as_dictionary() for pokemon in JohtoPokemon.query.all()])

@api.route('/sinnoh_dex', methods=['GET', 'POST'])
def sinnoh_dex():
    """
    [GET] /api/sinnoh_dex
    """
    return jsonify([pokemon.attributes_as_dictionary() for pokemon in SinnohPokemon.query.all()])

@api.route('/unova_dex', methods=['GET', 'POST'])
def unova_dex():
    """
    [GET] /api/unova_dex
    """
    return jsonify([pokemon.attributes_as_dictionary() for pokemon in UnovaPokemon.query.all()])

@api.route('/alola_dex', methods=['GET', 'POST'])
def alola_dex():
    """
    [GET] /api/alola_dex
    """
    return jsonify([pokemon.attributes_as_dictionary() for pokemon in AlolaPokemon.query.all()])

# Database Population
@api.route('/populate_items')
def populate_items():
    # category_api = requests.get('https://pokeapi.co/api/v2/item-category').json()
    # for category in category_api['results']:
    #     new_category = ItemCategories()
    #     category_data = {
    #         'name' : category['name'] 
    #     }
    #     new_category.set_attributes(category_data)
    #     new_category.save_item()
    #     print(f"\n\n{category_data['name']}")
        
    #     content_api = requests.get(f"{category['url']}").json()
    #     for item in content_api['items']:
    #         new_item = Items()
    #         item_api = requests.get(f"{item['url']}").json()
    #         item_data = {
    #             'name' : item['name'],
    #             'category' : category_data['name'],
    #             'price' : item_api['cost']/10,
    #             'sprite' : item_api['sprites']['default']
    #         }
    #         print(item_data)
    #         new_item.set_attributes(item_data)
    #         new_item.save_item()

    return redirect(url_for('api.api_page'))

@api.route('/populate_types', methods=['GET', 'POST'])
def populate_types():
    # type_api = requests.get(f'https://pokeapi.co/api/v2/type').json()
    # for pokemon_type in type_api['results']:
    #     new_type = PokemonTypes()
    #     type_info = requests.get(f"{pokemon_type['url']}").json()
    #     type_data = {
    #         'name' : pokemon_type['name'],
    #         'defense_weakness' : ", ".join([x['name'] for x in type_info['damage_relations']['double_damage_from']]),
    #         'defense_strength' : ", ".join([x['name'] for x in type_info['damage_relations']['half_damage_from']]),
    #         'defense_immune' : ", ".join([x['name'] for x in type_info['damage_relations']['no_damage_from']]),
    #         'attack_strength' : ", ".join([x['name'] for x in type_info['damage_relations']['double_damage_to']]),
    #         'attack_weakness' : ", ".join([x['name'] for x in type_info['damage_relations']['half_damage_to']]),
    #         'attack_immune' : ", ".join([x['name'] for x in type_info['damage_relations']['no_damage_to']]),
    #     }
    #     new_type.set_attributes(type_data)
    #     new_type.save_item()
    #     print(new_type)
    return redirect(url_for('api.api_page'))


@api.route('/populate_national', methods=['GET', 'POST'])
def populate_national():
    # dex_api = requests.get(f'https://pokeapi.co/api/v2/pokedex/1').json()
    # for entry in dex_api['pokemon_entries']:
    #     try:
    #         new_pokemon = NationalPokemon()
    #         pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{entry['pokemon_species']['name']}/").json()
    #         species_api = {}
    #         try:
    #             species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         except:
    #             species_api = requests.get("https://pokeapi.co/api/v2/pokemon-species/25/").json()
    #             print('Default Price Created')
    #         pokemon_price = round(255/(species_api['capture_rate'])*10,2)
    #         pokemon_data = {
    #             'name' : entry['pokemon_species']['name'],
    #             'dex_id' : entry['entry_number'],
    #             'type1' : pokemon_api['types'][0]['type']['name'],
    #             'type2' : None,
    #             'sprite' : pokemon_api['sprites']['front_default'],
    #             'height' : pokemon_api['height'],
    #             'weight' : pokemon_api['weight'],
    #             'price': pokemon_price
    #         }
    #         if len(pokemon_api['types']) > 1:
    #             pokemon_data['type2'] = pokemon_api['types'][1]['type']['name']
    #         else:
    #             pokemon_data['type2'] = None
    #         new_pokemon.set_attributes(pokemon_data)
    #         new_pokemon.save_item()
    #         pokemon_loaded += 1
    #         print(f'Pokemon Loaded: {pokemon_loaded}')
    #     except:
    #         print("failed")

    return redirect(url_for('api.api_page'))

@api.route('/populate_johto', methods=['GET', 'POST'])
def populate_johto():
    # dex_api = requests.get(f'https://pokeapi.co/api/v2/pokedex/original-johto').json()
    # for entry in dex_api['pokemon_entries']:
    #     try:
    #         new_pokemon = JohtoPokemon()
    #         pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{entry['pokemon_species']['name']}/").json()
    #         species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         # try:
    #         #     species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         # except:
    #         #     species_api = requests.get("https://pokeapi.co/api/v2/pokemon-species/25/").json()
    #         #     print('Default Price Created')
    #         pokemon_price = round(255/(species_api['capture_rate'])*10,2)
    #         pokemon_data = {
    #             'name' : entry['pokemon_species']['name'],
    #             'dex_id' : entry['entry_number'],
    #             'type1' : pokemon_api['types'][0]['type']['name'],
    #             'type2' : None,
    #             'sprite' : pokemon_api['sprites']['front_default'],
    #             'height' : pokemon_api['height'],
    #             'weight' : pokemon_api['weight'],
    #             'price': pokemon_price
    #         }
    #         if len(pokemon_api['types']) > 1:
    #             pokemon_data['type2'] = pokemon_api['types'][1]['type']['name']
    #         else:
    #             pokemon_data['type2'] = None
    #         new_pokemon.set_attributes(pokemon_data)
    #         new_pokemon.save_item()
    #         pokemon_loaded += 1
    #         print(f'Pokemon Loaded: {pokemon_loaded}')
    #     except:
    #         print("failed")

    return redirect(url_for('api.api_page'))

@api.route('/populate_kanto', methods=['GET', 'POST'])
def populate_kanto():
    # dex_api = requests.get(f'https://pokeapi.co/api/v2/pokedex/kanto').json()
    # pokemon_counter = 0
    # for entry in dex_api['pokemon_entries']:
    #     try:
    #         new_pokemon = KantoPokemon()
    #         pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{entry['pokemon_species']['name']}/").json()
    #         species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         pokemon_price = round(255/(species_api['capture_rate'])*10,2)
    #         pokemon_data = {
    #             'name' : entry['pokemon_species']['name'],
    #             'dex_id' : entry['entry_number'],
    #             'type1' : pokemon_api['types'][0]['type']['name'],
    #             'type2' : None,
    #             'sprite' : pokemon_api['sprites']['front_default'],
    #             'height' : pokemon_api['height'],
    #             'weight' : pokemon_api['weight'],
    #             'price': pokemon_price
    #         }
    #         if len(pokemon_api['types']) > 1:
    #             pokemon_data['type2'] = pokemon_api['types'][1]['type']['name']
    #         else:
    #             pokemon_data['type2'] = None
    #         new_pokemon.set_attributes(pokemon_data)
    #         new_pokemon.save_item()
    #         pokemon_loaded += 1
    #         print(f'Pokemon Loaded: {pokemon_loaded}')
    #     except:
    #         pokemon_counter +=1
    #         print(pokemon_counter)

    return redirect(url_for('api.api_page'))

@api.route('/populate_sinnoh', methods=['GET', 'POST'])
def populate_sinnoh():
    # dex_api = requests.get(f'https://pokeapi.co/api/v2/pokedex/original-sinnoh').json()
    # pokemon_counter = 0
    # for entry in dex_api['pokemon_entries']:
    #     try:
    #         new_pokemon = SinnohPokemon()
    #         pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{entry['pokemon_species']['name']}/").json()
    #         species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         pokemon_price = round(255/(species_api['capture_rate'])*10,2)
    #         pokemon_data = {
    #             'name' : entry['pokemon_species']['name'],
    #             'dex_id' : entry['entry_number'],
    #             'type1' : pokemon_api['types'][0]['type']['name'],
    #             'type2' : None,
    #             'sprite' : pokemon_api['sprites']['front_default'],
    #             'height' : pokemon_api['height'],
    #             'weight' : pokemon_api['weight'],
    #             'price': pokemon_price
    #         }
    #         if len(pokemon_api['types']) > 1:
    #             pokemon_data['type2'] = pokemon_api['types'][1]['type']['name']
    #         else:
    #             pokemon_data['type2'] = None
    #         new_pokemon.set_attributes(pokemon_data)
    #         new_pokemon.save_item()
    #         pokemon_loaded += 1
    #         print(f'Pokemon Loaded: {pokemon_loaded}')
    #     except:
    #         pokemon_counter +=1
    #         print(pokemon_counter)

    return redirect(url_for('api.api_page'))

@api.route('/populate_alola', methods=['GET', 'POST'])
def populate_alola():
    # dex_api = requests.get(f'https://pokeapi.co/api/v2/pokedex/original-alola').json()
    # pokemon_counter = 0
    # for entry in dex_api['pokemon_entries']:
    #     try:
    #         new_pokemon = AlolaPokemon()
    #         pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{entry['pokemon_species']['name']}/").json()
    #         species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         pokemon_price = round(255/(species_api['capture_rate'])*10,2)
    #         pokemon_data = {
    #             'name' : entry['pokemon_species']['name'],
    #             'dex_id' : entry['entry_number'],
    #             'type1' : pokemon_api['types'][0]['type']['name'],
    #             'type2' : None,
    #             'sprite' : pokemon_api['sprites']['front_default'],
    #             'height' : pokemon_api['height'],
    #             'weight' : pokemon_api['weight'],
    #             'price': pokemon_price
    #         }
    #         if len(pokemon_api['types']) > 1:
    #             pokemon_data['type2'] = pokemon_api['types'][1]['type']['name']
    #         else:
    #             pokemon_data['type2'] = None
    #         new_pokemon.set_attributes(pokemon_data)
    #         new_pokemon.save_item()
    #         pokemon_loaded += 1
    #         print(f'Pokemon Loaded: {pokemon_loaded}')
    #     except:
    #         pokemon_counter +=1
    #         print(pokemon_counter)

    return redirect(url_for('api.api_page'))

@api.route('/populate_unova', methods=['GET', 'POST'])
def populate_unova():
    # dex_api = requests.get(f'https://pokeapi.co/api/v2/pokedex/original-unova').json()
    # pokemon_counter = 0
    # for entry in dex_api['pokemon_entries']:
    #     try:
    #         new_pokemon = UnovaPokemon()
    #         pokemon_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{entry['pokemon_species']['name']}/").json()
    #         species_api = requests.get(f"{entry['pokemon_species']['url']}").json()
    #         pokemon_price = round(255/(species_api['capture_rate'])*10,2)
    #         pokemon_data = {
    #             'name' : entry['pokemon_species']['name'],
    #             'dex_id' : entry['entry_number'],
    #             'type1' : pokemon_api['types'][0]['type']['name'],
    #             'type2' : None,
    #             'sprite' : pokemon_api['sprites']['front_default'],
    #             'height' : pokemon_api['height'],
    #             'weight' : pokemon_api['weight'],
    #             'price': pokemon_price
    #         }
    #         if len(pokemon_api['types']) > 1:
    #             pokemon_data['type2'] = pokemon_api['types'][1]['type']['name']
    #         else:
    #             pokemon_data['type2'] = None
    #         new_pokemon.set_attributes(pokemon_data)
    #         new_pokemon.save_item()
    #         pokemon_loaded += 1
    #         print(f'Pokemon Loaded: {pokemon_loaded}')
    #     except:
    #         pokemon_counter +=1
    #         print(pokemon_counter)

    return redirect(url_for('api.api_page'))