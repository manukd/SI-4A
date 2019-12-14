class Character:
    def __init__(self, nom, prenom, age, profession, boostMoral):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boostMoral = boostMoral

    def _get_Nom(self):
        return self.nom

    def _get_Prenom(self):
        return self.prenom

    def _get_Age(self):
        return  self.age

    def _get_Profession(self):
        return self.profession

    def _get_BoostMoral(self):
        return self.boostMoral

    def _set_Nom(self, nom):
        self.nom = nom

    def _set_Prenom(self, prenom):
        self.prenom = prenom

    def _set_Age(self, age):
        self.age = age

    def _set_Profession(self, profession):
        self.profession = profession

    def _set_BoostMoral(self, boostMoral):
        self.boostMoral = boostMoral


    def __str__(self):
        return self.nom + " " + self.prenom + " " + self.age + " " + self.profession + " " + self.boostMoral

if __name__ == '__main__':
    import csv
    with open('characters.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        line_count = 0
        characters_list = []
        i = 0
        for row in csvreader:
            characters_list.append(Character(row["name"], row["first name"], row["age"], row["profession"], row["morale value"]))
            i = i + 1
        print(characters_list[0])