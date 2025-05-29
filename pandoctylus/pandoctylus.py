
from docxtpl import DocxTemplate
import pypandoc

# Interpolate jinja2 style
doc = DocxTemplate("custom-reference.docx")
context = { 
    "doc_id" : "DOC-0034 rec C",
    "project_id" : "PROJ-0001",
    "doc_name" : "Pandoctylus -- A crazy and opinionated way of generating documents",
}

doc.render(context)
doc.save("preprocessed-reference.docx")

# Now run pandoc.
output = pypandoc.convert_file(
    "my_doc.md",
    "docx",
    outputfile="final.docx",
    extra_args = [
        "--reference-doc=preprocessed-reference.docx",
        "--toc",
        "--toc-depth=3",
    ],
)
