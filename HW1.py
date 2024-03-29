# Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True,
# если команда успешно выполнена и текст найден в ее выводе и False в противном случае. Передаваться должна только одна
# строка, разбиение вывода использовать не нужно.

import subprocess


def check_command_output(command, text):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return text in output
    except(subprocess.CalledProcessError, FileNotFoundError):
        return False


command = "ls"
text = "HW1.py"
result = check_command_output(command, text)
print(result)

