#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: HW4

#Print Hello World!
print("Hello World!")

#Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing three numbers inside
phoneDict = {
    "Brand" : "Apple",
    "Model" : "iPhone 16",
    "Color" : ["black", "ultramarine", "white", "pink"]

}

#Print one of the three numbers by itself
print(phoneDict["Color"][2])

#Using the update function, add a fourth key to the dictionary and give it a value
phoneDict.update({"size": 6.1})

#Print the entire dictionary
print(phoneDict)

#Clear all of the data inside of the dictionary and print it
phoneDict.clear()
print(phoneDict)

#Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information within each entry
fifthHour = {
    "student1": {
        "Name" : "Zach",
        "Grade" : 12,
        "esports" : False,
    },

    "student2": {
        "Name" : "Ryley",
        "Grade" : 11,
        "esports" : False,
    },

    "student3": {
        "Name" : "Gabriel",
        "Grade" : 12,
        "esports" : True,
    }
}

#Print out the names of all three classmates on the same line
print(fifthHour["student1"]["Name"], fifthHour["student2"]["Name"], fifthHour["student3"]["Name"])