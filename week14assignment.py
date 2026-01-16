def build_baggage_map(flight_manifest):
    bag_map = {}
    for item in flight_manifest:
        bag_map[item['tag_id']] = item['passenger_name']
    return bag_map
def reconcile_bags(bag_map, scanned_tags):
    manifest_tags = set(bag_map.keys())
    scanned_set = set(scanned_tags)
    l = manifest_tags - scanned_set
    m = scanned_set - manifest_tags
    return l, m
def generate_lost_report(bag_map, lost_tag_set):
    report = ["MISSING: Bag " + tag + " (Owner: " + bag_map[tag] + ")" for tag in lost_tag_set]
    report.sort()
    return report
manifest = [
    {'tag_id': "BAG-001", 'passenger_name': "Wei Chen"},
    {'tag_id': "BAG-002", 'passenger_name': "Anita Roy"},
    {'tag_id': "BAG-003", 'passenger_name': "Leo Das"}
]
scanned = ["BAG-001", "BAG-003", "BAG-999"]



t = build_baggage_map(manifest)
a, b = reconcile_bags(t, scanned)
r = generate_lost_report(t, a)
print("Lost Bags:", a)
print("Mystery Bags:", b)
print("Report:", r)

