
def update_main_py(version_to):
    with open('main.py', 'w') as main_py:
        lines = main_py.readlines()
        version_line = 0
        for index, line in enumerate(lines):
            if 	'setApplicationVersion' not in line:
                continue
            # Encontrou em qual linha ta, salve
            version_line = index
            break

        #Se não encontrou a linha
        if not version_line:
            raise Exception("Erro ao procurar por linha que vai ser alterada a versão do arquivo main.py")

        # Achar um jeito de alterar o valor da linha
        # Ex: Alterar app.setApplicationVersion('5.6.3') para app.setApplicationVersion('5.6.4')
        # Da pra colocar parametro de tipo de atualização: fix, minor, major -> fix: aumenta o ultimo numero, minor aumenta o numero do meio, manjor aumenta o numero primeio

        #Fazer isso para main.py e para main_dir.spec

def update_main_dir(version_to):
    with open('main_dir.spec', 'w') as main_py:
        lines = main_py.readlines()
        version_line = 0
        for index, line in enumerate(lines):
            if 	'pdv_version_value' not in line:
                continue
            # Encontrou em qual linha ta, salve
            version_line = index
            break

        #Se não encontrou a linha
        if not version_line:
            raise Exception("Erro ao procurar por linha que vai ser alterada a versão do arquivo main.py")


    line_string_main_dir = "roverpix_version_value = 'RoverpixPDV_5_6_3'    "
    line_string_main_py = "	app.setApplicationVersion('5.6.3')"

    conjunto = set([1, 1, 2, 3, 4]) # -> set(1, 2, 3, 4)
    lista = list([1, 1, 2, 3, 4]) # -> [1, 1, 2, 3, 4]

    current_main_dir_version = line_string_main_dir.split("=")[1].strip(" ", "'", '"')
    current_main_dir_version_value = current_main_dir_version.split("_", 1)[1]
    current_main_dir_version_values = current_main_dir_version_value.split('_')
    major_version = int(current_main_dir_version_values[0])
    minor_version = int(current_main_dir_version_values[1])
    fix_version = int(current_main_dir_version_values[2])

    update_type = 'minor' ###OBTER UPDATE TYPE COMPARANDO AS VERSOES ATUAL E NOVA
    if update_type == 'major':
        minor_version = 0
        fix_version = 0
        major_version += 1

    if update_type == 'minor':
        minor_version += 1
        fix_version = 0

    if update_type == 'fix':
        fix_version +=1

    new_version_string = "roverpix_version_value = 'RoverpixPDV_{}_{}_{}".format(major_version, minor_version, fix_version)

    ## agora da um jeito de escrever isso no arquivo
    # Achar um jeito de alterar o valor da linha
    result = change_line_of_file('main.py', index, new_version_string)
    # Ex: Alterar app.setApplicationVersion('5.6.3') para app.setApplicationVersion('5.6.4')
    # Da pra colocar parametro de tipo de atualização: fix, minor, major -> fix: aumenta o ultimo numero, minor aumenta o numero do meio, manjor aumenta o numero primeio
    return result

def change_line_of_file(file_to_change_line, index_of_line_to_change, new_line):
    deubom = True
    return True if deubom else False

def update(version_to):
    main_dir = update_main_dir(version_to)
    main_py = update_main_py(version_to)

    # se deu bom atualizar os dois arquivos, retorna que deu bom, se não, deu ruim
    if main_dir and main_py:
        return True
    else:
        return False
