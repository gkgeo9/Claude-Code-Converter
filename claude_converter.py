import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT


def get_safe_filename(path):
    return "".join([c if c.isalnum() or c in ('-', '_') else '_' for c in path])


def convert_file_to_pdf(file_path, output_dir, input_dir):
    try:
        relative_path = os.path.relpath(file_path, input_dir)
    except ValueError:
        relative_path = file_path

    safe_filename = get_safe_filename(relative_path)
    pdf_filename = os.path.join(output_dir, f"{safe_filename}.pdf")

    os.makedirs(os.path.dirname(pdf_filename), exist_ok=True)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Warning: Unable to read {file_path}. It might be a binary file.")
        return

    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a custom style for code
    code_style = ParagraphStyle('Code', parent=styles['Code'], fontSize=8, leftIndent=0, rightIndent=0)

    story = []
    story.append(Paragraph(f"File: {relative_path}", styles['Title']))
    story.append(Spacer(1, 0.25 * inch))

    # Use Preformatted instead of Paragraph for code content
    story.append(Preformatted(content, code_style))

    doc.build(story)
    print(f"Created PDF: {pdf_filename}")


def convert_directory_to_pdfs(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.svelte', '.js', '.html')):
                file_path = os.path.join(root, file)
                convert_file_to_pdf(file_path, output_dir, input_dir)


if __name__ == "__main__":
    input_directory = input("Enter the input directory path: ")
    output_directory = input("Enter the output directory path: ")

    if not os.path.exists(input_directory):
        print(f"Error: Input directory '{input_directory}' does not exist.")
    elif not os.path.exists(output_directory):
        print(f"Error: Output directory '{output_directory}' does not exist.")
    else:
        convert_directory_to_pdfs(input_directory, output_directory)
        print("Conversion completed.")
