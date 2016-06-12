from lxml import etree

# Get XSD schema.
xsd = etree.parse(open('schema.xsd', 'r'))
xmlschema = etree.XMLSchema(xsd)

# Get XML.
xml = etree.parse(open('form.xml', 'r'))

# Validate XML with XSD.
print "XSD validation result: ", xmlschema.validate(xml), "\n\n"

# Get DTD class.
dtd = etree.DTD(open('schema.dtd', 'r'))
print "DTD validation result: ", dtd.validate(xml)

xslt = etree.parse(open('schema.xsl', 'r'))
transform = etree.XSLT(xslt)
newdom = transform(xml)
print(etree.tostring(newdom, pretty_print=True))
