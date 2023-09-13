
# Exercise 2: Working With JSON
# Instructions



# Access the nested “salary” key from the JSON-string below.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.


import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson) #turns it into a dictionary

salary = data["company"]["employee"]["payable"]["salary"] #points to salary
print("Salary:", salary) 

data["company"]["employee"]["birth_date"] = "1989-12-09" #adds a birthday

modifiedJson = json.dumps(data, indent=4) #changes it back to JSON

with open("modified_data.json", "w") as json_file: #saves it to an external file
    json_file.write(modifiedJson)
    
print("Modified JSON saved to 'modified_data.json") # wow