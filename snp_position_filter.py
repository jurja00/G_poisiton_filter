import sys, getopt
import csv

def load_data(filename, delimiter):
       with open(filename) as file:
           data = file.readlines();
        
       data = [x.strip() for x in data];
       result = [];

       for i in range(len(data)):
           result.append(data[i].split(delimiter));
       
       return result;

def find_positions(data):
    if not data:
        print ('Wrong data input...')
        sys.exit()

    positions = []

    last_index = -1
    for row in data:
        index = row[1]
        probability = row[4]

        if(last_index == index and index not in positions):
            positions.append(int(index))

        if(float(probability) > 0.85 and index not in positions):
            positions.append(int(index))
            
        last_index = index

    return positions


def __init__(params = None):
    inputpositions = outputfile = None

    try:
        opts, args = getopt.getopt(params,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile>  -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputpositions = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if not inputpositions or not outputfile:
        print("Wrong input...")
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit()

    print("Parsing first datafile...")
    data_pos = load_data(inputpositions, "\t")

    # Required positions
    print("Filtering positions...")
    positions = find_positions(data_pos)

    # Write positions
    print("Writing positions")
    with open(outputfile, "w") as output_file:
        writer = csv.writer(output_file, delimiter="\n", quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerow(positions)

__init__(sys.argv[1:])