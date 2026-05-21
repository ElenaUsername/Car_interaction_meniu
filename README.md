# Autonomous Cars Communication System

## 📋 Project Overview

Autonomous Cars Chatting It Out 🚗💬

Cars that can talk! They share their location, speed, and all the drama that happened in the last 100km. Basically a soap opera with wheels where vehicles gossip about each other and find out who's closest. Pure automotive chaos. 🍿

This project implements a communication system for autonomous vehicles that allows cars to interact, share information, and make decisions based on real-time data. Cars can communicate with each other, track events, manage speed and location, and identify nearby vehicles.

---

## 🎯 Features

### ✅ Core Requirements Implemented

1. **Car Information Management**
   - Unique ID (auto-incremented)
   - Manufacturer model
   - Current location (X and Y coordinates)
   - Speed and direction tracking

2. **Communication Between Cars**
   - Receive information from other vehicles
   - Send information to other vehicles
   - Share event history (last 100km)

3. **Speed Management**
   - Set current speed
   - Set direction (X-axis = 1, Y-axis = 2)
   - Dynamic position updates based on speed

4. **Distance Calculation**
   - Uses Euclidean distance formula
   - Calculates distance to all other cars
   - Identifies the nearest vehicle

5. **Event Tracking**
   - Log events with timestamp location
   - Automatically remove events beyond 100km
   - Share event data with other vehicles

6. **Time Simulation**
   - Update all car positions based on speed
   - Manage event expiration
   - Track environmental changes

---

## 📁 Project Structure

```
.
├── car_file.py       # Car class and vehicle management
├── main.py           # Main menu and user interface
└── README.md         # This file with information
```

---

## 🚗 File Descriptions

### `car_file.py`

**Class: Car**

#### Attributes:
- `id` - Unique identifier (auto-incremented)
- `model` - Vehicle model name (string)
- `coordonate_x` - X-axis position (0-1000)
- `coordonate_y` - Y-axis position (0-1000)
- `event` - List of events with coordinates
- `speed` - Current speed value
- `direction` - Direction of movement (0=stationary, 1=X-axis, 2=Y-axis)

#### Methods:

**`get_event(event)`**
- Adds an event to the car's event list
- Records event location (X, Y coordinates)
- Returns: Event confirmation message

**`get_speed(speed, direction)`**
- Sets the car's speed
- Sets the direction of movement
- Returns: Speed confirmation message

**`get_the_nearest_car()`**
- Calculates Euclidean distance to all other cars
- Identifies the closest vehicle
- Returns: Information about the nearest car

**`read_the_data_about_car()`**
- Displays complete car information
- Shows: ID, model, events, coordinates, speed
- Returns: Formatted vehicle data

**`add_time()` (Class Method)**
- Updates all car positions based on speed/direction
- Removes events older than 100km
- Called periodically to simulate time passage

### `main.py`

Interactive menu system with 5 main options:

1. **Read all identified cars** - Display all vehicles and their data
2. **Identify a new car** - Create a new autonomous vehicle
3. **Get into a car** - Select a car and perform actions
4. **Add time** - Simulate time passage and update positions
5. **Exit Program** - Close the application

---

## 🎮 How to Use

### Starting the Program

```bash
python main.py
```

### Menu Options

#### Option 1: Read All Identified Cars
- Displays all created vehicles
- Shows detailed information for each car
- Updates vehicle list automatically

#### Option 2: Identify a New Car
```
Enter model of the car: Tesla Model 3
```
- Creates a new autonomous vehicle
- Assigns unique ID automatically
- Randomly generates initial coordinates

#### Option 3: Get Into a Car
```
Enter the id of the car you want to get into: 1
```

**Secondary Menu:**

1. **Add an Event**
   - Log what happened (e.g., "Traffic jam", "Engine check")
   - Records location where event occurred
   - Stores in event history

2. **Add a Speed**
   - Set speed: `50` (km/h or units)
   - Set direction: `1` (X-axis) or `2` (Y-axis)
   - Car will move in selected direction

3. **Calculate the Nearest Car**
   - Finds closest vehicle
   - Shows distance and vehicle ID
   - Uses real-time coordinate data

#### Option 4: Add Time
- Simulates time passage
- Updates positions of moving cars
- Removes old events (>100km away)
- Affects all vehicles simultaneously

#### Option 5: Exit Program
- Closes the application

---

## 📊 Example Workflow

```
1. Create 3 cars (Volvo, Audi, BMW)
2. Select Car 1 (Volvo)
   → Add event: "Traffic detected"
   → Set speed: 80, direction: 1 (move on X-axis)
3. Select Car 2 (Audi)
   → Check nearest car (should show Volvo or BMW)
4. Add time (cars move, events managed)
5. Select Car 1 again
   → Read updated location
   → See if events are still valid
```

---

## 🔧 Technical Details

### Distance Formula
Cars use **Euclidean distance** to calculate proximity:

```
distance = √[(x₂ - x₁)² + (y₂ - y₁)²]
```

### Event Management
- Events are stored with X, Y coordinates at creation time
- Events are removed when car moves >100 units away
- Multiple events can be tracked simultaneously

### ID System
- IDs are class-level (shared across all instances)
- Starts at 1 and auto-increments
- Ensures each car has a unique identifier

### Movement System
- Speed is applied only in ONE direction (X or Y)
- Direction: 1 = X-axis, 2 = Y-axis, 0 = stationary
- Coordinates update with `add_time()` method

---

