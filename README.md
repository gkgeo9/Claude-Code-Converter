# Claude Code to PDF Converter

This Python script converts Svelte, JavaScript, and HTML files in a specified directory to PDF format. It's particularly useful for developers who want to create documentation or code reviews from their web development projects.

## Features

- Recursively processes all .svelte, .js, and .html files in the given directory
- Preserves original file content and formatting in the PDF
- Handles files across different drives
- Creates a separate PDF for each file, with the filename as the PDF title
- Treats all file content as plain text to avoid issues with HTML-like syntax in Svelte files

## Requirements

- Python 3.x
- ReportLab library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/gkgeo9/claude-code-converter.git
   cd claude-code-converter
   ```

2. Install the required library:
   ```
   pip install reportlab
   ```

## Usage

1. Run the script:
   ```
   python directory_to_pdf_converter.py
   ```

2. When prompted, enter the full path of the input directory containing your Svelte, JS, and HTML files.

3. When prompted, enter the full path of the output directory where you want the PDFs to be saved.

4. The script will process all eligible files and create corresponding PDFs in the output directory, maintaining the original directory structure.

## Example

```
Enter the input directory path: C:\Users\YourName\Projects\SvelteApp\src
Enter the output directory path: C:\Users\YourName\Documents\PDFs
Created PDF: C:\Users\YourName\Documents\PDFs\App_svelte.pdf
Created PDF: C:\Users\YourName\Documents\PDFs\main_js.pdf
...
Conversion completed.
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Contact

If you have any questions or feedback, please open an issue on this GitHub repository.
