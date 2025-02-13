import json

data = json.load(open("sample-data.json", 'r', encoding='utf-8'))

print("Interface status: ")
print("="*80)
print("{:<50} {:<20} {:<20}".format("DN", "Description", "Speed", "MTU"))
print("-"*80)

for item in data["imdata"]:
    interface = item["l1PhysIf"]["attributes"]
    print("{:<50} {:<20} {:<20} {:<20}".format(interface["dn"], interface.get("descr", ""), interface["speed"], interface["mtu"]))