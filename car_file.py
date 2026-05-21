import random
import gc
import math

vehicles = []

class Car:

    id_used = 1

    def __init__(self, model):
        #Number of the id will be assign by incrementing the id_used and alocating to the new car
        self.id = Car.id_used
        Car.id_used += 1
        self.model = model
        
        self.coordonate_x = random.randint (1,1000)
        self.coordonate_y = random.randint (1, 1000) 
        self.event = []
        self.speed = 0
        self.direction = 0 #if on axes x or y is moving, 0 means no moving, x=1, y=2

    def get_event(self,event):
        #Add event to a specific car
        self.event.append([event,self.coordonate_x, self.coordonate_y])
        return f"The events of the car {self.model} with the ID ({self.id}) has this event list: {self.event}"

    def get_speed(self,speed, direction):
        #Add speed to a specific car
        self.speed = speed
        self.direction = direction
        return f"The speed of the car {self.model} with the ID ({self.id}) : {self.speed}"
    
    def get_the_nearest_car(self):
        #Here is the calculation of the nearest car
        list_of_all_distances = []

        for vehicle in vehicles:
            #Calculate with euclidian distance
            euclidian_distance =math.sqrt((vehicle.coordonate_x - self.coordonate_x) ** 2 + (vehicle.coordonate_y - self.coordonate_y) ** 2)
            if vehicle.id != self.id:
                list_of_all_distances.append([euclidian_distance,vehicle.id, vehicle.model])
        the_nearest=10000
        the_nearest_id = self.id
        the_nearest_model=self.model
        for element in list_of_all_distances:
            if element[0] < the_nearest:
                the_nearest = element[0]
                the_nearest_id = element[1]
                the_nearest_model = element[2]
        return f"The nearest from {self.model} with the ID ({self.id}) is the car model {the_nearest_model} with the ID ({the_nearest_id}) "

    def read_the_data_about_car(self):
        #Read information about one car
        return f"---Detailed information about car with id {self.id}---\nThe model        = {self.model}\nThe events       = {self.event}\nThe coordonate x = {self.coordonate_x}\nThe coordonate y = {self.coordonate_y}\nThe speed = {self.speed}"

    @classmethod
    def add_time(cls):
        #Add time
        for vehicle in vehicles:
            if vehicle.speed != 0:
                #car can move on coordonate x or y and the speed is added only on one of them
                if vehicle.direction == 1:
                    vehicle.coordonate_x += vehicle.speed
                if vehicle.direction == 2:
                    vehicle.coordonate_y += vehicle.speed
            if vehicle.event != []:
                for single_event in vehicle.event:
                    #delete the event if passes 100
                    if vehicle.coordonate_x - single_event[1] > 100:
                        vehicle.event.remove(single_event)
                    if vehicle.coordonate_y - single_event[2] > 100:
                        vehicle.event.remove(single_event)

# Example of how to use all the atributes and methods
# car1 = Car("Volvo")
# car2 = Car("Audi")
# car3 = Car("BMW")
# print(car1.id)
# print(car1.model)
# print(car1.coordonate_x)
# print(car1.coordonate_y)
# print(car1.event)
# print(car1.get_speed(110,1))
# for obj in gc.get_objects():
#             if isinstance(obj, Car):
#                 vehicles.append(obj)
# print(car1.get_event("The car motor broke"))
# print(car1.get_event("The car's light's went off"))
# print(car1.get_event("The car found a barrier on the road"))
# print(car1.get_event("There is a tree on the road"))
# print(car1.get_event("It is raining heavily"))

# print(car1.read_the_data_about_car())
# print(car1.get_the_nearest_car())
# print(Car.add_time())
# print(car1.read_the_data_about_car())
