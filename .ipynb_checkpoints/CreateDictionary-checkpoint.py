import csv, json

# Open the CSV file in read mode
with open('./products_export_1.csv', mode='r') as csv_file:

    # Use the CSV module to read the file
    csv_reader = csv.reader(csv_file)

    # Get the header row (first row) and store it in a list
    header = next(csv_reader)

    # Create an empty array to store the dictionaries
    dict_array = []

    # Iterate through each row in the CSV file
    for row in csv_reader:

        # Create an empty dictionary for the current row
        current_dict = {}

        # Iterate through each element in the row and add it to the dictionary
        for i in range(len(row)):
            current_dict[header[i]] = row[i]

        # Append the dictionary to the array
        dict_array.append(current_dict)
       
# Save the array of dictionaries in a variable
Shopify_dict_array = dict_array

with open('ShopifyProductFields.json', 'w') as json_file:
    json.dump(dict_array, json_file)

# Print the array of dictionaries
print(dict_array)
