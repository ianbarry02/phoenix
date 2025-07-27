# Import libraries
from spire.doc import *
from spire.doc.common import *
import argparse
import os

# Add arguments for CLI
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

                # Save the document as an HTML file
                output_file = os.path.join(output_folder, 'word_doc_content.html')
                document.SaveToFile(output_file, FileFormat.Html)
                document.Close()

                # Tweak HTML and insert it into index template
                tweak_html(output_file)

                index = os.path.join(output_folder, 'index.html')
                customize_html(output_file, index, title)

def tweak_html(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
        tweaked_output_file = html_content.replace('<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Content-Style-Type" content="text/css" /><meta name="generator" content="Spire.Doc" /><title></title><link href="styles.css" type="text/css" rel="stylesheet" /></head><body><div><p><span style="color:#ff0000">Evaluation Warning: The document was created with Spire.Doc for Python.</span></p><h1><span>Hello again</span></h1>', '')
        tweaked_output_file = tweaked_output_file.replace('<span style="font-family:Arial">', '')
        tweaked_output_file = tweaked_output_file.replace('<html>', '')
        tweaked_output_file = tweaked_output_file.replace('</html>', '')
        tweaked_output_file = tweaked_output_file.replace('<span>', '')
        tweaked_output_file = tweaked_output_file.replace('</span>', '')

    with open(html_file, 'w') as file:
        file.write(tweaked_output_file)
    

def customize_html(html_file, index, title):
    with open(html_file, 'r') as output_file:
        output_html = output_file.read()

    with open(index, 'r') as index_file:
        index_html = index_file.read()
        customized_html = index_html.replace('<!-- insert custom html -->', output_html)
        customized_html = customized_html.replace('<!-- insert title -->', title)

    with open(index, 'w') as index_file:
        index_file.write(customized_html)
