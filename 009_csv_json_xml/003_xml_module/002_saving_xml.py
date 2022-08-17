from xml.etree import ElementTree

tree = ElementTree.parse('xml_files//cd_catalog.xml')
root = tree.getroot()

cd = root[0]
data = next(cd.iter('Y1985'))
print(data.text)
data.text = str(int(data.text) + 50000)
print(data.text)
total_count = cd[6]
total_count.set("type", "All Sold")

total_sold = ElementTree.Element('TOTAL')
total_sold.text = "2000000"
cd.append(total_sold)
print(total_sold.text)

total_sold = cd.find("TITLE")
cd.remove(total_sold)



tree.write("xml_files//xml_edited.xml")