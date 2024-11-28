#!/usr/bin/env python3
from unstructured.partition.pdf import partition_pdf

# from unstructured.documents.elements import Title, NarrativeText
from unstructured.staging.base import convert_to_csv


# Fake Patient Data
elements = partition_pdf(filename="document.pdf")
with open("output.csv", "w") as file:
    isd_csv = convert_to_csv(elements)
    file.write(isd_csv)
