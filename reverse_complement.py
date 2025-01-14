def dnaComplement(s):
    # Write your code here
    
    # define a dictionary that contains the complement for each base
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    # reverse the string
    reversed_dna = s[::-1]
    # complement each base in the reversed string
    res = ''.join(complement[base] for base in reversed_dna)
    
    return res

# Example usage
dna_sequence = "GTCAG"
result = dnaComplement(dna_sequence)
print("Original DNA sequence:", dna_sequence)
print("Reverse complement:", result)
