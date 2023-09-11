import os
import json
import yaml

# Path to the JSON file containing key-value pairs
json_file_path = 'release.conf'

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    key_value_pairs = json.load(json_file)

# Loop through the key-value pairs
for key, value in key_value_pairs.items():
    # Change directory to the key name
    os.chdir(key)
    
    # Path to the kustomize file
    kustomize_yaml_path = 'Kustomization.yaml'
    
    # Read the kustomize file
    with open(kustomize_yaml_path, 'r') as yaml_file:
        try:
            yaml_data = yaml.safe_load(yaml_file)
        except yaml.YAMLError as exc:
            print(exc)
    
    # Replace the 'images\newTag' value with the JSON value
    yaml_data['images'][0]['newTag'] = value
    
    # Write the modified YAML data back to the file
    with open(kustomize_yaml_path, 'w') as yaml_file:
        try:
            yaml.dump(yaml_data, yaml_file, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)

    # Change back to the original directory
    os.chdir('..')
