import json
import os

def read_json_file(file_path):
    """
    Reads a JSON file and returns its content.
    
    :param file_path: Path to the JSON file.
    :return: Parsed JSON content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file at {file_path}")
        return None

def main():
    # Define file paths
    base_path = './static'
    files = [
        'all-properties.en.json',
        'servo-css-properties.json',
        'google-css-popularity.json'
    ]

    # Load JSON files
    json_data = {}
    for file_name in files:
        file_path = os.path.join(base_path, file_name)
        json_data[file_name] = read_json_file(file_path)

    # Check loaded data
    for file_name, content in json_data.items():
        if content is not None:
            print(f"Loaded data from {file_name}: {len(content)} entries")
        else:
            print(f"Failed to load data from {file_name}")

if __name__ == '__main__':
    main()
