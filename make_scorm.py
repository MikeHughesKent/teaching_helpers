"""
Command line tool for creating a SCORM package from html files.
If uploaded to Moodle, these files will then be accessible from within
a single SCORM item.

Mike Hughes, with some LLM help.

Usage:
    
    make_scorm
    
    make_scorm <title>
    
    make_scorm <title> <images path>
    
All html files in current directory will be added to the package. 

Tested with University of Kent Moodle 2025.

Optionally specify:
 
          title : The title of the SCORM package (default is Lecture Notes)
   images path  : relative path to folder of images to include (default is images)


e.g. python make_scorm.py "Lecture Notes" "pictures"

    
"""

import os, sys
import zipfile

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

from html.parser import HTMLParser

class TitleParser(HTMLParser):
    """ Extracts title from an html file.
    """
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title = data.strip()


def get_html_title(file_path):
    """ Get the title of an html file.
    """
    
    parser = TitleParser()
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    parser.feed(content)
    return parser.title or os.path.basename(file_path)


def create_manifest(html_files, image_files, folder_path, titlestr  = ""):
    """ Creates the manifest file that lists all the files in the package.
    """
    
    # Root manifest element
    manifest = Element('manifest', {
        'identifier': 'com.example.scorm',
        'version': '1.2',
        'xmlns': 'http://www.imsproject.org/xsd/imscp_rootv1p1p2',
        'xmlns:adlcp': 'http://www.adlnet.org/xsd/adlcp_rootv1p2',
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xsi:schemaLocation': 'http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd '
                              'http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd'
    })

    # Metadata
    metadata = SubElement(manifest, 'metadata')
    schema = SubElement(metadata, 'schema')
    schema.text = 'ADL SCORM'
    schemaversion = SubElement(metadata, 'schemaversion')
    schemaversion.text = '1.2'

    # Organizations (course structure)
    organizations = SubElement(manifest, 'organizations', {'default': 'ORG-1'})
    organization = SubElement(organizations, 'organization', {'identifier': 'ORG-1'})
    title = SubElement(organization, 'title')
    title.text = titlestr

    # Resources (content files)
    resources = SubElement(manifest, 'resources')

    for i, html_file in enumerate(html_files, 1):

        item_id = f'ITEM-{i}'
        resource_id = f'RES-{i}'
        file_path = os.path.join(folder_path, html_file)
        page_title = get_html_title(file_path)
    
         # Use page_title in <title> element
        item = SubElement(organization, 'item', {'identifier': f'ITEM-{i}', 'identifierref': f'RES-{i}'})
        item_title = SubElement(item, 'title')
        item_title.text = page_title

        # Add resource
        resource = SubElement(resources, 'resource', {
            'identifier': resource_id,
            'type': 'webcontent',
            'adlcp:scormtype': 'sco',
            'href': os.path.basename(html_file)
        })

        # Include all images as files in this resource (so each SCO knows about them)
        for img_file in image_files:
            SubElement(resource, 'file', {'href': os.path.basename(img_file)})

        # Files in resource
        file_element = SubElement(resource, 'file', {'href': os.path.basename(html_file)})

    # Pretty print XML
    xml_str = tostring(manifest)
    dom = parseString(xml_str)
    return dom.toprettyxml(indent="  ")


def make_scorm_package(folder_path, output_zip='scorm_package.zip', titlestr = 'Lecture Notes', images_folder = 'images'):
    
    # Find all HTML files in folder
    html_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.html')]
    image_exts = {'.png', '.jpg', '.jpeg', '.gif', '.svg'}
    image_files = [f for f in os.listdir(folder_path + '\\' +  images_folder) if os.path.splitext(f)[1].lower() in image_exts]

    if not html_files:
        print("No HTML files found in folder.")
        return

    # Create imsmanifest.xml content
    manifest_xml = create_manifest(html_files, image_files, folder_path, titlestr = titlestr)

    # Create ZIP package
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as z:
       
        # Write imsmanifest.xml
        z.writestr('imsmanifest.xml', manifest_xml)

        # Add HTML files
        for f in html_files:
            file_path = os.path.join(folder_path, f)
            z.write(file_path, arcname=f)

        images_path = os.path.join(folder_path, images_folder)
        
        if os.path.exists(images_path):
            for root, _, files in os.walk(images_path):
                for file in files:
                    abs_file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_file_path, folder_path)
                    z.write(abs_file_path, arcname=rel_path)
            if not files:
                 print("No files in images folder.")
        else:
            print("Images folder not found.")

    print(f"SCORM package created: {output_zip}, with title: {titlestr}.")
    print(f"{len(f)} html files and {len(file)} images added.")
    

if __name__ == '__main__':
   
       
    if len(sys.argv) == 3:
        make_scorm_package(os.getcwd(), titlestr = sys.argv[1], images_folder = sys.argv[2])

    elif len(sys.argv) == 2: 
        make_scorm_package(os.getcwd(), titlestr = sys.argv[1])
   
    else:
        make_scorm_package(os.getcwd())


  



