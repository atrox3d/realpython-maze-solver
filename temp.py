from pathlib import Path

flat = {}

for path in Path(".").glob("**/*"):
    # print(path)

    if not path.parts[0].startswith('.'):
        if path.is_file():
            parent = str(path.parent)
            flat[parent] = flat.get(parent, [])
            flat[parent].append(path.name)

print(flat)