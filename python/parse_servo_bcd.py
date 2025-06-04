import json

with open("data/servo-bcd.json") as f:
    d = json.load(f)

results = {}

items = list(d["results"].values())[0]
for item in items:
    exposure = item["exposure"].lower()
    name = item["name"].lower()
    supported = item["result"]

    if exposure not in results:
        results[exposure] = {}

    name_parts = name.split(".")

    parent_dict = results[exposure]
    for idx, name in enumerate(name_parts):
        # first part of the name is like 'api' or 'css', 'webassembly', etc.
        # we skip it as it will increase the complexity to match the feature name with
        # mdn feature groups
        if idx == 0:
            continue

        if idx == len(name_parts) - 1:
            if name not in parent_dict:
                parent_dict[name] = {"@supported": supported}
            else:
                parent_dict[name]["@supported"] = supported
        else:
            if name not in parent_dict:
                parent_dict[name] = {"@total_count": 0, "@supported_count": 0}
            parent_dict[name]["@total_count"] += 1
            parent_dict[name]["@supported_count"] += 1 if supported else 0

        parent_dict = parent_dict[name]

with open("data/servo-bcd-groups.json", "w") as f:
    json.dump(results, f, indent=2)
