def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    num_line = 1
    for string in strings:
        num_byte = file.tell()
        file.write(string + '\n')
        strings_positions[(num_line,num_byte)] = string
        num_line += 1
    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
