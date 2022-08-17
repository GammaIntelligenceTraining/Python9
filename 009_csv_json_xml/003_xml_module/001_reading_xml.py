# Documentation
# https://docs.python.org/3/library/xml.etree.elementtree.html
from xml.etree import ElementTree

tree = ElementTree.parse('xml_files//cd_catalog.xml')
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

# # Will print all cd elements and add id number
for cd in root:
    print(cd.tag, cd.attrib)


# # Parent and sibling rule applies
print(root[0][0].text)

# # Iterable object can be created with iter() method
# print(root.iter('CD'))

# for element in root.iter('CD'):
#     print(element[0].text)
#     print(element[1].text)
#     print(element[2].text)
#     print('\n')
#
# for element in root.iter('SELLS'):
#     sold_albums = 0
#     for child in element:
#         sold_albums += int(child.text)
#     print(sold_albums)
#
# for element in root.iter('CD'):
#     for child in element:
#         print(child.text)