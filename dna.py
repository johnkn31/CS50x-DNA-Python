import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Missing command-line argument")
        exit(1)

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage of command-line argument")
        exit(1)

    # TODO: Read database file into a variable
    file = csv.DictReader(open(sys.argv[1]))

    # TODO: Read DNA sequence file into a variable
    dna = open(sys.argv[2], "r").read()  # file is a text file

    # TODO: Find longest match of each STR in DNA sequence
    str_sequence = csv.DictReader(open(sys.argv[1])).fieldnames[1:]

    counts = {}  # dictionary to count each person STR
    for subseq_str in str_sequence:
        counts[subseq_str] = longest_match(dna, subseq_str)

    # TODO: Check database for matching profiles
    for people in file:
        if(int(people["AGATC"]) == counts["AGATC"] and int(people["AATG"]) == counts["AATG"] and int(people["TATC"]) == counts["TATC"]):
            print(people["name"])
            return
    print("No Match")


def longest_match(sequence, subsequence):  # sequence is the DNA to be passed in; subsequence can be the STR
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence

        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
