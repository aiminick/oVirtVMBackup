from __future__ import print_function
from xml.dom import minidom


file_name_old = "/home/binary/696121ff-d098-4b3b-bd23-f357037608b1.ovf"
file_name_new = "/home/binary/b2f27e88-71a9-4934-8ad1-8b933a7e7ff4.ovf"
xml_doc = minidom.parse(file_name_old)
xml_doc_new = minidom.parse(file_name_new)

disks_old = xml_doc.getElementsByTagName('Disk')
disks_new = xml_doc_new.getElementsByTagName('Disk')

disks_old[0].attributes["ovf:fileRef"].value

for attr in range(len(disks_old)):
    print("disk id{} {} == {}".format(
        attr, disks_old[attr].attributes["ovf:diskId"].value,
        disks_new[attr].attributes["ovf:diskId"].value))

print("Changing...")
for attr in range(len(disks_old)):
    disks_new[attr].attributes["ovf:diskId"].value = disks_old[attr]\
        .attributes["ovf:diskId"].value
print("Changed Sucessful...")
for attr in range(len(disks_old)):
    print("disk id{} {} == {}".format(
        attr, disks_old[attr].attributes["ovf:diskId"].value,
        disks_new[attr].attributes["ovf:diskId"].value))

print(xml_doc_new.toprettyxml())