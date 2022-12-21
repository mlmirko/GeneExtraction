import sys, argparse, os

def validate_gene(sequence):
    for ind in range(len(sequence)-25):
        subsequence = sequence[ind:ind+25]
        if sequence[ind+25:].find(subsequence) >= 0:
            return False
    return True

def main():

   try:
        parser = argparse.ArgumentParser(description='Program for validating the gene from txt file. Returns True if it is valid and False if it is not valid sequence.')

        parser.add_argument("--input_file", help="Path to the txt file of complete gene. Note: Path should be under quotes!")

        args = parser.parse_args()
        
        
        with open(args.input_file, 'r') as f:
            gene = f.readlines()

        print(validate_gene(gene[0]))


   except Exception as ex:
        print(ex)

if __name__ == "__main__":
   main()