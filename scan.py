from pathlib import Path

nested_example = {
    'src': [
        {'maze_solver': [
            {'models': [
                'border.py', 'edge.py'
            ]}
        ]}
    ]
}

flat = {}

def store_flat(flat:dict, path:Path):
    if not path.parts[0].startswith('.'):
        if path.is_file():
            parent = str(path.parent)
            flat[parent] = flat.get(parent, [])
            flat[parent].append(path.name)

nested = {}
def store_nested(nested:dict, parts:tuple):
    '''
    BASE_CASE:  length of parts is 1
                
    RECURSIVE_CASE: length of parts is > 1
                    check if parts[0] is in nested
                    if not add new key (parts[0])
                        add new value, empty list
                    else
                        append
    '''
    parent = parts[0]
    if len(parts) > 1:
        nested[parent] = nested.get(parent, {})
        store_nested(nested[parent], parts[1:])
    else:
        nested[parent] = nested.get(parent, [])
        nested[parent].append(parts[0])

for path in Path(".").glob("**/*"):
    store_flat(flat, path)
print(flat)

exit()
for path in Path(".").glob("**/*"):
    store_nested(nested, path.parts)
print(nested)