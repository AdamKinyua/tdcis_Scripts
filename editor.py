import sys

def update_nuc_file(inc, file):
    with open(file, 'r') as nuc:
        lines = nuc.readlines()
        last_line = lines[-2]
        last_value = last_line.split()[-1]
        new_value = float(last_value) + inc
        new_line = last_line.replace(last_value, str(new_value))
        lines[-2] = new_line

    with open(file, "w") as nuc:
        nuc.writelines(lines)

    return file

# getting arguments from the commandline with the syntax highlighted in print statement below
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Correct syntax: $ python3 update_nuc_file.py <increment> <filename>")
        sys.exit(1)
    else:
        inc = float(sys.argv[1])
        file = sys.argv[2]
        update_nuc_file(inc, file)

