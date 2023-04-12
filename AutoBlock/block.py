#!/usr/bin/python3.6

import hashlib


class Block:
    def __init__(self, timestamp, car, id):
        # Initialisation des attributs du bloc
        self.timestamp = timestamp
        self.car = car
        self.id = id
         # Les éléments suivants sont déterminés par un mineur
        self.nonce = 0
        self.previous_hash = ""
        self.hash = ""

    def increment_nonce(self, number):
        #Incrémente la valeur du nonce d'un certain nombre.
        self.nonce += number

    def get_block_obj(self, add_hash=False):
        """Renvoie le bloc sous forme de dictionnaire.

        :param add_hash: Booléen pour indiquer si le hachage du bloc doit être inclus ou non.
        :type add_hash: bool
        :return: Dictionnaire représentant le bloc.
        :rtype: dict
        """
        ret = {
            "timestamp": str(self.timestamp),
            "car": str(self.car),
            "id": str(self.id),
            "previous_hash": self.previous_hash,
            "nonce": str(self.nonce)
        }
        if add_hash:
            ret.update({"hash": self.hash})
        return ret

    def to_string(self):
        """Renvoie l'objet bloc (dictionnaire) y compris son hachage sous forme de chaîne de caractères

        :rtype: string
        """
        return str(self.get_block_obj())

    def to_string_add_hash(self):
        """Returns the block object (dict) including
        its hash in a string format.

        :rtype: string
        """
        b = self.get_block_obj()
        b["hash"] = self.hash
        return str(b)

    def get_hash(self):
        """Calcule le hachage du bloc.


        :return: Le hachage du bloc.
        :rtype: str
        """
        return hashlib.sha224(self.to_string().encode()).hexdigest()

    def is_block_valid(self):
        """Vérifie la validité du bloc.

        Un bloc est considéré comme valide si : TODO

        :return: True si le bloc est valide, sinon False.
        :rtype: bool
        """
        # Vérification si le hachage a été calculé correctement
        if self.hash != self.get_hash():
            return False
        # Vérification de l'intégrité et de la validité des données
        # TODO

        return True
