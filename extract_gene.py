import sys, argparse, os

def get_gene(readings):
    if len(readings) > 1:
        sequences = [readings[0]]
        del readings[0]
        for next_reading in readings:  
            for sequence_i, sequence in enumerate(sequences):

                if sequence.find(next_reading) >= 0:
                    break
                sequence_end = sequence[-25:]  
                i = next_reading.find(sequence_end) 
                if i >= 0:                  
                    sequences[sequence_i] += next_reading[-(len(next_reading)-i-25):]                
                    break
                        
            else:
                sequences.append(next_reading)

        return get_gene(sequences)
    else:
        return readings[0]



def main():

   try:
        parser = argparse.ArgumentParser(description='Program for extracting the gene from FASTA file.')

        parser.add_argument("--input_file", help="Path to the fasta file. Note: Path should be under quotes!")

        args = parser.parse_args()
        
        
        data_collection = []
        with open(args.input_file, "r") as fh:
                for line in fh:
                    data_collection.append(line)

        reads = []
        for i in range(len(data_collection)):
                if data_collection[i][0] == '>':
                    continue
                reads.append(data_collection[i].replace("\n", ""))

        result = get_gene(reads.copy())
        with open(os.path.join(os.path.dirname(args.input_file), 'result.txt'), 'w') as f:
                f.writelines(result)
   except Exception as ex:
        print(ex)

if __name__ == "__main__":
   main()