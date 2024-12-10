import json

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
    w3_css_properties = './static/w3-all-properties.json'
    google_css_popularity = './static/google-css-popularity.json'
    servo_css_properties = './static/servo-css-properties.json'

    w3_properties = read_json_file(w3_css_properties)
    google_popularity = read_json_file(google_css_popularity)
    servo_properties_raw = read_json_file(servo_css_properties)
    
    # Servo's supported properties will be listed in two categories: shorthand and longhand.
    # We'll simply extract both into one list.
    # the 'shorthands' and 'longhands' keys both return a dictionaries.
    # We'll extract the key alone and append it to the list.
    servo_properties = []
    for key in servo_properties_raw['shorthands'].keys():
        servo_properties.append(key)

    for key in servo_properties_raw['longhands'].keys():
        servo_properties.append(key)

    # We'll write down the servo_properties list into a markdown table
    with open('./content/servo-properties.md', 'w', encoding='utf-8') as file:
        file.write('Property | Description\n')
        file.write('--- | ---\n')
        for property_name in servo_properties:
            file.write(f'{property_name} | \n')



if __name__ == '__main__':
    main()
