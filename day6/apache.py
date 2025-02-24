files = ["day6/apache_access_1.log", "day6/apache_access_2.log"]


file_counters = {}
file_ip_sets = {}
for file in files:
    counter = {}
    with open(file) as fh:
        for line in fh:
            #parts = line.split(" ")
            #parts = line.split(" ", 1)
            #print(parts)
            #print(parts[0])
            ip, _ = line.split(" ", 1)
            #print(ip)
            if ip not in counter:
                counter[ip] = 1
            else:
                counter[ip] += 1
            # counter[ip] = counter[ip] + 1
    print(counter)
    file_counters[file] = counter
    file_ip_sets[file] = set(counter.keys())

print(file_counters)
print(file_ip_sets)

print("print intersection")
for ip in file_counters["day6/apache_access_1.log"]:
    print(ip)
    if ip in file_counters["day6/apache_access_2.log"]:
        print(f"in both: {ip}")

print("print only in 2nd")
for ip in file_counters["day6/apache_access_2.log"]:
    if ip not in file_counters["day6/apache_access_1.log"]:
        print(ip)

print("-" * 20)
print("union")
print(file_ip_sets["day6/apache_access_1.log"] | file_ip_sets["day6/apache_access_2.log"])

print("intersection")
print(file_ip_sets["day6/apache_access_1.log"] & file_ip_sets["day6/apache_access_2.log"])

print("only in 2nd")
print(file_ip_sets["day6/apache_access_2.log"] - file_ip_sets["day6/apache_access_1.log"])

