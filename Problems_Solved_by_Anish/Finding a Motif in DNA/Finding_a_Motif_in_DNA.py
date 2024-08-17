def find_substring_locations(s, t):
    locations = []
    start = 0
    while True:
        start = s.find(t, start)
        if start == -1:
            break
        locations.append(start + 1)  
        start += 1
    return locations

def read_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        s = file.readline().strip()
        t = file.readline().strip()
    return s, t

file_path = 'rosalind_subs.txt'

s, t = read_strings_from_file(file_path)

locations = find_substring_locations(s, t)

print(" ".join(map(str, locations)))
