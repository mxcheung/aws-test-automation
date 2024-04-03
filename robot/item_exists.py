# Sample list of JSON objects
json_list = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]

# Function to check if Alice exists in the 'name' field
def alice_exists(json_list):
    for obj in json_list:
        if obj.get("name") == "Alice":
            return True
    return False

# Check if Alice exists
if alice_exists(json_list):
    print("Alice exists.")
else:
    print("Alice does not exist.")
