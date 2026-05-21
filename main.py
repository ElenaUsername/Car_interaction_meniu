from car_file import Car
import gc

vehicles = []

while True:
    print("\n\n--- Main Menu ---")
    print("1. Read all the indentified cars")
    print("2. Identify a new car")
    print("3. Get into a car")
    print("4. Add time (Events and location will be influenced by speed)")
    print("5. Exit Program")
    choice = input("Enter your choice (1-5): ")
    print("\n\n")
    #Choice of exit
    if choice == '5':
        print("Exiting the program. Goodbye!")
        break 
    if choice == '4':
        print("The time efect was applied, on events and location")
        Car.add_time()
    #Choice of entering a car
    if choice == "3":
        # Search in intances wich car have this id
        number_introduced = int(input("Enter the id of the car you want to get into for a ride: "))
        for obj in gc.get_objects():
            if isinstance(obj, Car):
                print(f"here {obj.id}")
                if obj.id == number_introduced:
                    found = True

                    if obj.id == number_introduced:
                        # Inform about the second meniu of choices
                        print("---Secundary choice ---")
                        print("1. Add a event to a car")
                        print("2. Add a speed to a car")  
                        print("3. Calculate the nearest car")  
                        action_to_be_done_in_car = input("Enter your choice (1-3): ")
                        if action_to_be_done_in_car == "1":
                            Event_to_add = input("Enter your event that happened (Hope the car still exists 0.0): ")
                            print(obj.get_event(Event_to_add))
                        if action_to_be_done_in_car == "2":
                            speed_to_add = input("Enter your speed of the car (Please drive carefull ^-^): ")
                            direction_to_add = input("Enter wich direction x = 1, y = 2: ")
                            while direction_to_add not in ["1", "2"]:
                                direction_to_add = input("Try again and make sure you enter x = 1, y = 2:")
                            print(obj.get_speed(speed_to_add, direction_to_add))
                        if action_to_be_done_in_car == "3":
                            print("The closest car from you is (Maybe it is behind you -_-):")                    
                            print(obj.get_the_nearest_car())

                                
    #Choice of adding cars
    if choice == "2":
          model_you_write = str(input("Enter model of the car: "))
          car = Car(model_you_write)
    #Choice of reading all the cars that are identified
    if choice == "1":
        for obj in gc.get_objects():
            if isinstance(obj, Car):
                vehicles.append(obj)

        print(f"Found {len(vehicles)} vehicle:")
        for vehicle in vehicles:
            print(vehicle.read_the_data_about_car())