# Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True,
# если команда успешно выполнена и текст найден в ее выводе и False в противном случае. Передаваться должна только одна
# строка, разбиение вывода использовать не нужно.

# Доработать функцию из предыдущего задания таким образом,
# чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import string
import subprocess
import re


def check_command_output(command, text):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
        translator = str.maketrans("", "", string.punctuation)
        output = output.translate(translator)
        print(output)
        return text in output
    except(subprocess.CalledProcessError, FileNotFoundError):
        return False


command = "ls"
text = "HW1py"
result = check_command_output(command, text)
print(result)
