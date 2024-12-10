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

def generate_line(data):
    line = f"{data['property_name']}"
    # display the percentage of usage of the property, with a % sign, formatted with only 2 decimal places
    line += f" | {data['day_percentage']*100:.2f}%"
    # display if the property is supported by Servo
    line += f" | " + ("✅" if data['servo_supports'] else "❌")
    # display the relevant specs for the property
    line += f" | {generate_spec_links(data)}\n"
    return line

def generate_spec_links(data):
    if 'specs' not in data:
        return 'N/A'
    return ', '.join([f"[{spec['status']}]({spec['url']})" for spec in data['specs']])

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


    # We'll create a dictionary where the key is the property name and the value is a list of entries.
    spec_data = {}
    for entry in w3_properties:
        property_name = entry['property']
        if property_name not in spec_data:
            spec_data[property_name] = [entry]
        else:
            spec_data[property_name].append(entry)

    # We'll create a list of dictionaries where each dictionary represents a CSS property.
    # We'll also check if the property is supported by Servo and if it's in the W3C spec.
    correlated_data = []
    for entry in google_popularity:
        property_name = entry['property_name']
        if property_name.startswith('webkit-') or property_name.startswith('alias-'):
            continue
        entry['servo_supports'] = property_name in servo_properties
        if property_name in spec_data:
            entry['specs'] = spec_data[property_name]
        correlated_data.append(entry)

    # We'll filter out the properties that have a usage of over 5%.
    number_of_properties_over_five_percent = [data for data in correlated_data if data['day_percentage'] >= 0.05]
    # We'll filter out the properties that are supported by Servo.
    number_of_supported_properties_over_five_percent = [data for data in number_of_properties_over_five_percent if data['servo_supports']]
    stat_element = f"{len(number_of_supported_properties_over_five_percent)} / {len(number_of_properties_over_five_percent)}"


    # We'll write down the servo_properties list into a markdown table
    with open('./content/metrics/css.md', 'a', encoding='utf-8') as file:
#         file.write("""+++
# insert_anchor_links = "left"
# title = "Servo CSS Coverage"
# +++
# """)
        file.write(f"Servo supports {stat_element} of the properties that have a usage of over 5%. (while the total css property count is {len(correlated_data)})\n\n")
        file.write('Property | Percentage | Supported by Servo | Relevant Spec\n')
        file.write('--- | --- | --- | ---\n')
        for data in correlated_data:
            file.write(generate_line(data))



if __name__ == '__main__':
    main()
