#Name: Dom Acuna
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sports = {
    "sport1": {
    "Name" : "Basketball",
    "Players" : 5,
    "Ball" : True,
},
    "sport2": {
    "Name" : "Football",
    "Players" : 11,
    "Ball" : True,
},
  "sport3": {
    "Name": "Baseball",
    "Players": 9,
    "Ball": True,
      },
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sport_function(a,b,c):
    print(a + b + c)

#3. Call the function with arguments here
sport_function(sports["sport1"]["Players"],sports["sport2"]["Players"],sports["sport3"]["Players"])