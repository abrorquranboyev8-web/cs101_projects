def audit_access(entries, min_risk):
    result = []
    for entry in entries:
        if entry != "":
            # print(entry)
            risk1 = entry.find("[") + 1
            risk2 = entry.find("]")
            risk = entry[risk1:risk2]
            time = entry[6:11]
            parts = entry.split(" | ")
            if len(parts) >= 3:
                zone = parts[1].strip()
                event = parts[2].strip()
                summary = f"{risk} ({time}): {zone} - {event}"
                if min_risk == "LOW":
                    result.append(summary)
                elif min_risk == "MED" and (risk == "MED" or risk == "HIGH"):
                    result.append(summary)
                elif min_risk == "HIGH" and risk == "HIGH":
                    result.append(summary)
    return result                
   



access_log = [
    "[LOW] 07:55:00 | Lobby | Employee badge scan.",
    "[MED] 08:05:12 | Server Room | Door held open too long.",
    "[LOW] 08:10:00 | Cafeteria | Vendor delivery.",
    "",
    "[HIGH] 19:30:45 | Executive Wing | Unidentified keycard used.",
    "[HIGH] 19:35:00 | Vault | Motion sensor triggered.",
    "[MED] 20:00:00 | Parking Garage | Gate malfunction."
]

medium_and_high = audit_access(access_log, "MED")
print(medium_and_high)

high_only = audit_access(access_log, "HIGH")
print(high_only)



