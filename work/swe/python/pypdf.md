
https://pypdf.readthedocs.io/en/stable/


Tool for reading and editing pdf files.

## Main Objects

**PdfReader**

```python
from pypdf import PdfReader

reader = PdfReader("file_name.pdf")

```


**PdfWriter**

```python
from pypdf import PdfWriter

writer = PdfWriter()
```


## Example usage

Creating a pdf with only pages 6 and 7 of an input pdf (0-indexed).

```python
from pypdf import PdfReader, PdfWriter
  
reader = PdfReader("problems-scl-2026-2027.pdf")
writer = PdfWriter()
writer.append(reader, pages=[6, 7])
writer.write("problem3.pdf")
```