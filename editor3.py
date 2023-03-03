import argparse
import math
import fileinput

def vibrations(file_name, time, w):
    for i, line in enumerate(fileinput.input(file_name, inplace=True)):
        if i < 2:
            # ignoring the first two lines indicating # of atoms and title
            print(line.rstrip())
            continue

        # Split the line into four values: charge, x, y, z
        values = line.split()

        # Makes sure lines to be edited have atleast four characters
        if len(values) < 4:
            # If not, just print the line as is
            print(line.rstrip())
            continue

        # Determine the sign to use behind the sin(wt) function based on the line number
        # LInes whose index is odd get +sin(wt) and even indexes get -sin(wt)
        sign = 1 if i % 2 == 1 else -1

        # Modify the last value in the line
        values[-1] = str(sign * math.sin(w*time))

        # Print the updated line
        print(" ".join(values))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='input file')
    parser.add_argument('time', type=float, help='time value')
    parser.add_argument('w', type=int, help='w value')
    args = parser.parse_args()

    vibrations(args.file, args.time, args.w)

