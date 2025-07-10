import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    #print(response)    just printing the object will show a status code
    
    if response.status_code == 200:
        pokemon_data = response.json()  #converts response to a key value pair format
        
        for key, value in pokemon_data.items():
            return pokemon_data
    else:
        print(f"Failed to retrieve data: {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

print(f"{pokemon_info["name"]}")
#print(f"{pokemon_info["abilities"]}")
#print(f"{pokemon_info["moves"]}")
#print(f"{pokemon_info["type"]}")
print(f"{pokemon_info["abilities"][0]["ability"]["url"]}")  #access using abilities key, access the first element(0), access using key "ability", access using the key "url"
#for key, value in pokemon_info["abilities"]:
#    pass

"""
Good question — let’s break this down with your **list of dictionaries**, where each element looks like this:

```python
{
  'ability': {
    'name': 'static',
    'url': 'https://pokeapi.co/api/v2/ability/9/'
  },
  'is_hidden': False,
  'slot': 1
}
```

---

### ✅ **How to access elements step by step**

Suppose your data is called `abilities`:

```python
abilities = [
    {'ability': {'name': 'static', 'url': 'https://pokeapi.co/api/v2/ability/9/'}, 'is_hidden': False, 'slot': 1},
    {'ability': {'name': 'lightning-rod', 'url': 'https://pokeapi.co/api/v2/ability/31/'}, 'is_hidden': True, 'slot': 3}
]
```

**Example: Get the name of the first ability**

```python
first_ability_name = abilities[0]['ability']['name']
print(first_ability_name)  # static
```

---

**Example: Get the URL of the second ability**

```python
second_ability_url = abilities[1]['ability']['url']
print(second_ability_url)
# https://pokeapi.co/api/v2/ability/31/
```

---

**Loop over all abilities and print names**

```python
for ability_info in abilities:
    ability_name = ability_info['ability']['name']
    print(ability_name)
```

**Output:**

```
static
lightning-rod
```

---

### ✅ **Key takeaway**

* You index into the **list**: `abilities[0]`, `abilities[1]`
* Then index into the **dictionary**: `['ability']`
* Then index into the **nested dictionary**: `['name']`

---

**If you want help turning this into a function**, let me know — I can write a snippet!

"""