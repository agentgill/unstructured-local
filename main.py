#!/usr/bin/env python3
import json

from unstructured.partition.pdf import partition_pdf

# Fake Patient Data
elements = partition_pdf(filename="document.pdf")

element_dicts = [element.to_dict() for element in elements]
json_elements = json.dumps(element_dicts, indent=2)

print(json_elements)

with open("output.json", "w") as file:
    file.write(json_elements)
