# Import libraries
from spire.doc import *
from spire.doc.common import *
import argparse
import os
import re

# Add arguments for command line
def StartCommandLine():
    parser = argparse.ArgumentParser('Syllabus website generation tool')
    parser.add_argument('-doc', '--word_doc', type = str, required = True, help = 'Paste the path to your syllabus Word doc')
    parser.add_argument('-folder', '--output_folder', type = str, required = True, help = 'Paste the path to the folder where you want your website files to be stored')
    parser.add_argument('-title', '--title', type = str, required = True, help = 'Specify what you want the browser tab to display when someone opens your syllabus site (course number, semester, and year might be good pieces of information to include!)')

    args = parser.parse_args()

    word_doc = args.word_doc
    output_folder = args.output_folder
    title = args.title

    if os.path.exists(word_doc):
        root, extension = os.path.splitext(word_doc)

        if extension in ['.doc', '.docx']:
        
            if os.path.exists(output_folder):
                print('Document and folder exist. Converting to HTML...')

                # Create Document instance and load Word document
                document = Document()
                document.LoadFromFile(word_doc)

                # Generate external CSS file (commented out because not needed now)
                # document.HtmlExportOptions.CssStyleSheetType = CssStyleSheetType.External 

                # Save the document as an HTML file
                output_file = os.path.join(output_folder, 'word_doc_content.html')
                document.SaveToFile(output_file, FileFormat.Html)
                document.Close()

                # Tweak HTML and insert it into index template
                tweak_html(output_file)

                index = os.path.join(output_folder, 'index.html')
                customize_html(output_file, index, title)

# Clean up HTML that SpireDoc generates
# because it won't let you remove inline styling
def tweak_html(html_file):
    re_head = re.compile(r'<head\b[^>]*>.*?</head\s*>', re.IGNORECASE | re.DOTALL)
    re_style = re.compile(r'\s*style\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\'"\s>]+)', re.IGNORECASE)

    with open(html_file, 'r') as file:
        html_content = file.read()

        # Remove inline CSS styling
        html_content = re_head.sub('', html_content)
        html_content = re_style.sub('', html_content)

    with open(html_file, 'w') as file:
        file.write(html_content)

# Plug HTML from Word and title into index.html template
def customize_html(html_file, index, title):
    with open(html_file, 'r') as output_file:
        output_html = output_file.read()

    with open(index, 'r') as index_file:
        index_html = index_file.read()
        customized_html = index_html.replace('<!-- insert custom html -->', output_html)
        customized_html = customized_html.replace('<!-- insert title -->', title)

    with open(index, 'w') as index_file:
        index_file.write(customized_html)
