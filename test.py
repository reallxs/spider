
profile = {}

with open('config.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
        if '=' in line:
            k,v = line.split('=')
            profile[k.strip()] = v.strip()

print(profile['username'], profile['password'])


