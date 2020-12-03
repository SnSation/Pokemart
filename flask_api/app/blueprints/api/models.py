import requests
from app import db

# Database Models
# National Pokedex
class ItemCategories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'< Item Category | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    sprite = db.Column(db.String(200))

    def __repr__(self):
        return f'< Item | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'category', 'price', 'sprite']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'category':self.category,
            'price':self.price,
            'sprite':self.sprite
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class PokemonTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    defense_weakness = db.Column(db.String(100))
    defense_strength = db.Column(db.String(100))
    defense_immune = db.Column(db.String(100))
    attack_weakness = db.Column(db.String(100))
    attack_strength = db.Column(db.String(100))
    attack_immune = db.Column(db.String(100))

    def __repr__(self):
        return f'< Pokemon Type | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'defense_weakness', 'defense_strength', 'defense_immune', 'attack_weakness', 'attack_strength', 'attack_immune']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'defense_weakness':self.defense_weakness,
            'defense_strength':self.defense_strength,
            'defense_immune':self.defense_immune,
            'attack_weakness':self.defense_weakness,
            'attack_strength':self.defense_strength,
            'attack_immune':self.defense_immune,
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

class NationalPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dex_id = db.Column(db.Integer)
    type1 = db.Column(db.String(20))
    type2 = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sprite = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'< National Pokemon | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'dex_id', 'type1', 'type2', 'height', 'description', 'weight', 'sprite', 'price']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'dex_id':self.dex_id,
            'types':[self.type1, self.type2],
            'height':self.weight,
            'weight':self.weight,
            'sprite':self.sprite,
            'price':self.price
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

# Johto Pokedex
class JohtoPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dex_id = db.Column(db.Integer)
    type1 = db.Column(db.String(20))
    type2 = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sprite = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'< Johto Pokemon | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'dex_id', 'type1', 'type2', 'height', 'description', 'weight', 'sprite', 'price']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'dex_id':self.dex_id,
            'types':[self.type1, self.type2],
            'height':self.weight,
            'weight':self.weight,
            'sprite':self.sprite,
            'price':self.price
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

# Kanto Pokedex
class KantoPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dex_id = db.Column(db.Integer)
    type1 = db.Column(db.String(20))
    type2 = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sprite = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'< Kanto Pokemon | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'dex_id', 'type1', 'type2', 'height', 'description', 'weight', 'sprite', 'price']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'dex_id':self.dex_id,
            'types':[self.type1, self.type2],
            'height':self.weight,
            'weight':self.weight,
            'sprite':self.sprite,
            'price':self.price
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

# Sinnoh Pokedex
class SinnohPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dex_id = db.Column(db.Integer)
    type1 = db.Column(db.String(20))
    type2 = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sprite = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'< Sinnoh Pokemon | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'dex_id', 'type1', 'type2', 'height', 'description', 'weight', 'sprite', 'price']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'dex_id':self.dex_id,
            'types':[self.type1, self.type2],
            'height':self.weight,
            'weight':self.weight,
            'sprite':self.sprite,
            'price':self.price
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

# Alola Pokedex
class AlolaPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dex_id = db.Column(db.Integer)
    type1 = db.Column(db.String(20))
    type2 = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sprite = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'< Alola Pokemon | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'dex_id', 'type1', 'type2', 'height', 'description', 'weight', 'sprite', 'price']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'dex_id':self.dex_id,
            'types':[self.type1, self.type2],
            'height':self.weight,
            'weight':self.weight,
            'sprite':self.sprite,
            'price':self.price
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()

# Unova Pokedex
class UnovaPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    dex_id = db.Column(db.Integer)
    type1 = db.Column(db.String(20))
    type2 = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sprite = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'< Unova Pokemon | Name: {self.name} | ID: {self.id} >'

    def set_attributes(self, data):
        for attribute in ['name', 'dex_id', 'type1', 'type2', 'height', 'description', 'weight', 'sprite', 'price']:
            if attribute in data:
                setattr(self, attribute, data[attribute])

    def attributes_as_dictionary(self):
        dictionary = {
            'id':self.id,
            'name':self.name,
            'dex_id':self.dex_id,
            'types':[self.type1, self.type2],
            'height':self.weight,
            'weight':self.weight,
            'sprite':self.sprite,
            'price':self.price
        }
        return dictionary

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_item(self):
        db.session.delete(self)
        db.session.commit()

    def update_item(self):
        db.session.commit()