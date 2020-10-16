class Cat:

    def __init__(self, name, age, bread):
        self.name = name
        self.age = age
        self.bread = bread
        self.skills = []

    @property
    def knowledge_level(self):
        return len(self.skills)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            return True
        else:
            return False

    def forget_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            return True
        else:
            return False


class Robot:
    # sale_country = ('China', 'USA', 'Europe')
    start_id = 0
    @property
    def serial_number(self):
        return str(self.region).lower() + '_' + str(self.id)

    def save_ability(self, skill):
        if isinstance(self, RoboCat):
            self.add_skill(skill)
            self.abilities.add(skill)
            return True
        else:
            return False

    def remove_ability(self, skill):
        if isinstance(self, RoboCat) and skill in self.skills and skill in self.abilities:
            self.forget_skill(skill)
            self.abilities.remove(skill)
            return True
        else:
            return False


class RoboCat(Cat, Robot):
    bread_region = {"Bambino": "USA", "Dragon Li": "China", "Aegean": "Europe"}
    all_robocats = []
    def __init__(self, name, age, bread):
        super().__init__(name, age, bread)
        self.abilities = set()
        self.region = self.bread_region[bread]
        self.__class__.start_id += 1
        self.id = self.start_id
        self.__class__.all_robocats.append(self)

    def add_skill(self, skill):
        if super().add_skill(skill):
            print('Recived skill "{}"'.format(skill))
            self.save_ability(skill)
            return True
        else:
            return False

    def remove_skill(self, skill):
        if self.forget_skill(skill):
            print('Recived skill "{}" for deleting'.format(skill))
            self.remove_ability(skill)
            return True
        else:
            return False

    @classmethod
    def sync(cls):
        print('Sync all abilities over network')
        all_abilities = set()
        for cat in cls.all_robocats:
            all_abilities.update(cat.abilities)
        for cat in cls.all_robocats:
            cat.abilities.update(all_abilities)
        return True





# Mike = Cat(name="Mike", age=1, bread="Aegean")
#
# print(Mike.__dict__)
# print(Mike.knowledge_level)
# print(Mike.add_skill('bark'))
# print(Mike.add_skill('bark'))
# print(Mike.forget_skill('bark'))


Tom = RoboCat(name="Tom", age=1, bread="Bambino")
Mike = RoboCat(name="Mike", age=1, bread="Aegean")
Barsik = RoboCat(name="Barsik", age=1, bread="Aegean")

# print(Tom.__dict__)
print(Tom.serial_number)
print(Mike.serial_number)

# print(Mike.__dict__)
# print(Mike.remove_ability("kill"))
# print(Mike.remove_ability("sleep"))
print(Mike.add_skill('bark'))
print(Tom.add_skill('sleep'))
print(Tom.add_skill('eat'))
print(Mike.save_ability("kill"))
# print(Mike.forget_skill('kill'))
print(Mike.remove_skill('kill'))
print(RoboCat.sync())
print(Barsik.abilities)

# Garbage collector
# import gc
# for obj in gc.get_objects():
#     if isinstance(obj, RoboCat):
#         print(obj.name)