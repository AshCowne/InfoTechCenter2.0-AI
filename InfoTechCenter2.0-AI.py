# Printing a header
print("*************************************************")
print("Gasoline Branch\n\n")

# Importing required libraries
import random
from time import sleep


# Function to simulate gas level gauge
def gasLevelGauge():
    # List of possible gas level indicators
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly selecting a gas level
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Function to simulate listing gas stations
def listOfGasStations():
    # List of available gas stations
    gasStations = ["Shell", "Speedway", "Marathon", "Circle", "K", "Mobile", "Costco", "Meijer", "7Eleven"]
    # Randomly selecting a gas station
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


# Function to alert the user based on gas level
def gasLevelAlert():
    # Generating random distances to gas stations for low and quarter tank levels
    milesToGasStationsLow = round(random.uniform(1, 25), 1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)

    # Getting the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Handling different gas level scenarios
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), ", which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a quarter tank, checking Google Maps for the closest gas station.")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), ", which is", milesToGasStationsQuarterTank,
              "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half tank that is enough for your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is a three-quarter tank.")
    elif gasLevelIndicator == "Full Tank":
        print("Your gas tank is full.")


# Calling the main function to start the program
gasLevelAlert()