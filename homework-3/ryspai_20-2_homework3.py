class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f"Memory: {self.memory}, Cpu: {self.cpu}"

    def make_computations(self):
        return self.__cpu + other.__memory

    def __mul__(self, other):
        return self.__cpu * other.__memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __eq__(self, other):
        return self.memory == other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call (self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - Beeline')

    def __str__(self):
        return f"Сим карты: {self.sim_cards_list}"


class Smartphone(Computer, Phone):
    def __init__(self, location, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.location = location

    def use_gps(self, location):
        self.location = location
        print(f"Вы проложили маршрут в {location}")

    def __str__(self):
        return super(Smartphone, self).__str__() + \
               f" Location: {self.location}, Sim_card: {self.sim_cards_list}"


my_comp = Computer(8, 5000)
print(my_comp)
print(my_comp * my_comp)
print(my_comp >= my_comp)
print(my_comp == my_comp)
print(my_comp > my_comp)
call = Phone('Beeline')
call.call(1, +996778286492)
print(call)
my_smartphone = Smartphone("Talas", 8, 5000, 'beeline')
my_smartphone2 = Smartphone("Ysyk-kol", 4, 256, 'beeline')
my_smartphone.use_gps("ГУМ")
print(my_smartphone)