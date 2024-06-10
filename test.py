import json

# Load the JSON file
with open('data/coco/annotations/instances_test2017.json') as f:
    data = json.load(f)

# Check the keys
print(f"Keys: {data.keys()}")

# Check the number of entries in each section
print(f"Number of images: {len(data['images'])}")
print(f"Number of annotations: {len(data['annotations'])}")
print(f"Number of categories: {len(data['categories'])}")

# Sample entries
print(f"Sample image entry: {data['images'][0]}")
print(f"Sample annotation entry: {data['annotations'][0]}")
print(f"Sample category entry: {data['categories'][0]}")

print("ojozd")

