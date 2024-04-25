import os
import sys
import io
from lxml import etree

def validate_xml_with_dtd(xml_file, dtd_file):
    try:
        with open(xml_file, 'rb') as f:
            xml_content = f.read()
        
        with open(dtd_file, 'rb') as f:
            dtd_content = f.read()
        
        dtd = etree.DTD(file=io.BytesIO(dtd_content))
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_content, parser)
        
        if dtd.validate(etree.fromstring(xml_content)):
            print("Validation successful")
            return True
        else:
            print("Validation failed")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    xml_file = 'input.xml'
    dtd_file = 'rules.dtd'
    
    if not os.path.exists(xml_file) or not os.path.exists(dtd_file):
        print("XML file or DTD file not found")
        sys.exit(1)
    
    if not validate_xml_with_dtd(xml_file, dtd_file):
        sys.exit(1)
