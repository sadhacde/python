# takes a starting letter and replaces [name] with each name in the invited names file
# which is a list of names. each new letter is then saved to the ready_to_send folder

with open("./invited_names.txt") as names:
    name_list = [line.strip() for line in names]

with open("./starting_letter.txt") as letter_file:
    letter_template = letter_file.read()
    for n in name_list:
        replaced_content = letter_template.replace("[name]", n)
        with open(f"./ready_to_send/letter for {n}", mode="w") as new_letter:
            new_letter.write(replaced_content)
