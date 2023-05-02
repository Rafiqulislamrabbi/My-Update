### problem name

Reads in multiple JSON files and then combines them into a single file.


## Description

1st step: import json
2nd step: creat empty json file
3rd step: read the multiple json file 
4th step: teak a empty list and using for loop in multiple json file and append it in to the list
5th step:Then write the list in to the empty json file


## Input
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}

{
    "ID":{
        "0":23,
        "1":43,
        "2":12,
        "3":13,
        "4":67,
        "5":89
        },
    "Name":{
        "0":"Ram",
        "1":"Deep",
        "2":"Yash",
        "3":"Aman",
        "4":"Arjun",
        "5":"Aditya"
        },
    "Marks":{
        "0":89,
        "1":97,
        "2":45,
        "3":78,
        "4":56,
        "5":76
        },
    "Grade":{
        "0":"B",
        "1":"A",
        "2":"F",
        "3":"C",
        "4":"E",
        "5":"C"
        }
}

## Output
[
  {
    "size": "Medium",
    "price": 15.67,
    "toppings": [
      "Mushrooms",
      "Extra Cheese",
      "Pepperoni",
      "Basil"
    ],
    "client": {
      "name": "Jane Doe",
      "phone": "455-344-234",
      "email": "janedoe@email.com"
    }
  },
  {
    "ID": {
      "0": 23,
      "1": 43,
      "2": 12,
      "3": 13,
      "4": 67,
      "5": 89
    },
    "Name": {
      "0": "Ram",
      "1": "Deep",
      "2": "Yash",
      "3": "Aman",
      "4": "Arjun",
      "5": "Aditya"
    },
    "Marks": {
      "0": 89,
      "1": 97,
      "2": 45,
      "3": 78,
      "4": 56,
      "5": 76
    },
    "Grade": {
      "0": "B",
      "1": "A",
      "2": "F",
      "3": "C",
      "4": "E",
      "5": "C"
    }
  }
]