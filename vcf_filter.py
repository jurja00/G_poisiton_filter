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

def parse_positions(positions):
    result = []
    for pos in positions:
        result.append(int(pos[0]))

    return result

def parse_vcf(data_VCF, positions):
    result = []

    for row in data_VCF:
        if row[0].startswith("#"):
            result.append(row)
            continue

        current_pos = int(row[1])

        if current_pos in positions:
            result.append(row)
        
    return result


def __init__(params = None):
    pos_file = input_vcf = outputfile = None

    try:
        opts, args = getopt.getopt(params,"hp:i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('test.py -p <position_file> -i <vcf_file> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -p <position_file> -i <vcf_file> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_vcf = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-p", "--pfile"):
            pos_file = arg

    if not input_vcf or not outputfile or not pos_file:
        print("Wrong input...")
        print('test.py -p <position_file> -i <vcf_file> -o <outputfile>')
        sys.exit()

    print("Parsing position datafile...")
    positions = load_data(pos_file, "\t")
    positions = parse_positions(positions)

    print("Parsing VCF file...")
    data_VCF = load_data(input_vcf, "\t")

    print("Filtering VCF file...")
    result = parse_vcf(data_VCF, positions)

    # Write result
    print("Writing result")
    with open(outputfile, "w") as output_file:
        writer = csv.writer(output_file, delimiter="\t", quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(result)

__init__(sys.argv[1:])