import json
import UnityPy

function = {}
res = {
    'res':[]
}
indent_num = 0


def parseNameArgs(func, fp):
    global indent_num
    name = func['name']
    args = str(func['args']).replace("['", "").replace("']", "").replace("', '", ", ").replace("[]", "")
    res = f'{name}({args})'
    fp.write(f'def {res}:\n')
    indent_num = 1
    return res

def parseCommandArgs(func, fp):
    global indent_num
    command = func['command']
    args = str(func['args']).replace("['", "").replace("']", "").replace("', '", ", ").replace("[]", "")
    res = f'{command}({args})'
    py_str = '' 
    if command == 'endif':
        indent_num -= 1
    elif command == 'else':
        indent_num -= 1
        py_str += '    ' * indent_num
        py_str += command
        py_str += ':\n'
        indent_num += 1
    elif command == 'if':
        py_str += '    ' * indent_num
        py_str += command
        py_str += f'({args.replace(", ", " == ")}):\n'
        indent_num += 1
    elif command == 'elif':
        indent_num -= 1
        py_str += '    ' * indent_num
        py_str += command
        py_str += f'({args.replace(", ", " == ")}):\n'
        indent_num += 1
    else:
        py_str += '    ' * indent_num
        py_str += f'{command}({args})\n'
    res = f'{command}({args})'
    fp.write(py_str)
    return res

def main():
    env = UnityPy.load('assets/story/function')
    for obj in env.objects:
        if obj.type in ['MonoBehaviour']:
            data = obj.read()
            function = data.type_tree
            #json.dump(tree, open('function.json', 'w', encoding='utf-8'), ensure_ascii=False)
    function = function['functions']

    fp = open('func/parsed_function.py', 'w', encoding= 'utf-8')

    for f in function:#list
        if f['name'] == '':
            pass
        else:
            func = {}
            func['name'] = parseNameArgs(f, fp)
            func['process'] = []
            for c in f['commandList']:
                func['process'].append(parseCommandArgs(c, fp))
            res['res'].append(func)
            fp.write('\n')
    json.dump(res, open('func/parsed_function.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
        

        
        