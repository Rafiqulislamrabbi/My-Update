import json

filenames = ["data1.json", "data2.json"]
output_filename = "combined_data.json"

combined_data = []

for filename in filenames:
    with open(filename, "r") as file:
        data = json.load(file)
        combined_data.append(data)

with open(output_filename, "w") as file:
    json.dump(combined_data, file)

print("Combined data written to:", output_filename)