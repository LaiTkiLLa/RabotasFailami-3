def compile_files(files_list):
    data = {}
    for file in files_list:
        with open(file, encoding="utf-8") as f:
            file_data = f.readlines()
            data[len(file_data)] = (file, " ".join(file_data))

    data = dict(sorted(data.items()))

    with open("itog", "w", encoding="utf-8") as new_file:
        for key, value in data.items():
            for value_2 in value:
                new_file.write(f'{value_2}\n{key}\n')

files_list = ["1.txt", "2.txt", "3.txt"]

compile_files(files_list)


