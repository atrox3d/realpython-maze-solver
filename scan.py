from pathlib import Path

nested = {
    'src': [
        {'maze_solver': [
            {'models': [
                'border.py', 'edge.py'
            ]}
        ]}
    ]
}

flat = {
}

for p in [p for p in Path('.').glob('**/*')]:
     if p.parts[0] != '.git':
        if p.is_file():
            # print(p.as_posix(), p.parent)
            parent = p.parent.as_posix()
            flat[parent] = flat.get(parent, [])
            flat[parent].append(p.name)

print(flat)

# Path('/tmp/sub1/sub2').mkdir(parents=True, exist_ok=True)
# Path('path/to/file.txt').touch()
