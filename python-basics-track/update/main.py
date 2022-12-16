import sys

from update_version import update


ultima_version = "5.6.6" # procurar isso no banco de dados na tarefa seguinte
version_arg = '' if len(sys.argv) == 1 else sys.argv[1]

version_to = ultima_version if not version_arg else version_arg

if __name__ == '__main__':
    result  = update(version_to)
    # faz algo com o resultado