
import sys
import os


def main():

    input_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
    input_path = os.path.abspath(os.path.realpath(input_path))
    print(input_path)
    d = {}
    with open(input_path,"r+") as inpFile:
        # Skip the header
        next(inpFile)

        for line in inpFile:

            #Format each line
            line = line.replace("\n", "")
            line = line.split(',')
            ID = line[0]
            drug = line[3]
            cost = float(line[-1])
            if drug not in d:
                d[drug]= [[],0]
            if ID not in d[drug][0]:
                d[drug][0].append(ID)
            d[drug][1]+= cost
        inpFile.close()
        
    data = []
    for key in d:
        data.append((key,len(d[key][0]),d[key][1]))

    sorted_by_second = sorted(data, key=lambda tup: tup[2], reverse = True)

    # Create new file, and write

    output_path = os.path.join(os.path.dirname(__file__), sys.argv[2])
    output_path = os.path.abspath(os.path.realpath(output_path))
    
    with open(output_path,'w+') as outFile:
        header = "drug_name,num_prescriber,total_cost\n"
        outFile.write(header)
        for d in sorted_by_second:
            outFile.write(str(d[0]) + "," + str(d[1]) + "," + str(d[2]) +"\n")
        outFile.close()


# D = {ambien: [[],0] }
if __name__ == '__main__':
    
    main()
