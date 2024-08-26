# Unstructured.io Local

## Resources

<https://docs.unstructured.io/open-source/installation/full-installation>
<https://github.com/Unstructured-IO/unstructured>

## Installation

Install System Dependencies (macOS)

```bash
brew install libmagic
brew install poppler
brew install tesseract
brew install pandoc
brew install libreoffice
```

Create Venv

```bash
python3.12 -m venv .venv && source .venv/bin/activate
```

Install unstructured

```bash
pip install unstructured
```

## Usage

Turn unstructured data (pdf) into strunctured data (json)

```python
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
```

## Unstanding structured data

<https://docs.unstructured.io/open-source/concepts/document-elements#element-type>