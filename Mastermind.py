acid_dict = {'UUU':'Phenylalanine','UUC':'Phenylalanine','UUA':'Leucine','UUG':'Leucine','CUU':'Leucine','CUC':'Leucine','CUA':'Leucine','CUG':'Leucine','AUU':'Isoleucine','AUC':'Isoleucine','AUA':'Isoleucine','AUG':'Methionine', 'GUU':'Valine', 'GUC':'Valine','GUA':'Valine','GUG':'Valine','UCU':'Serine', 'UCC':'Serine','UCA':'Serine','UCG':'Serine','CCU':'Proline','CCC':'Proline','CCA':'Proline','CCG':'Proline','ACU':'Threonine','ACC':'Threonine','ACA':'Threonine','ACG':'Threonine','GCU':'Alanine','GCC':'Alanine','GCA':'Alanine','GCG':'Alanine','UAU':'Tyrosine','UAC':'Tyrosine','UAA':'stop codon (this codon signals the termination of the protein-creation process)','UAG':'stop codon (this codon signals the termination of the protein-creation process)','CAU':'Histidine','CAC':'Histadine','CAA':'Glutamine','CAG':'Glutamine','AAU':'Asparagine','AAC':'Asparagine','AAA':'Lysine','AAG':'Lysine','GAU':'Aspartic Acid','GAC':'Aspartic Acid','GAA':'Glutamic Acid','GAG':'Glutamic Acid','UGU':'Cysteine','UGC':'Cysteine','UGA':'stop codon (this codon signals the termination of the protein-creation process)','UGG':'Tryptophan','CGU':'Arginine','CGC':'Arginine','CGA':'Arginine','CGG':'Arginine','AGU':'Serine','AGC':'Serine','AGA':'Arginine','AGG':'Arginine','GGU':'Glycine','GGC':'Glycine','GGA':'Glycine','GGG':'Glycine'}

def Usumstring(int):
	#takes the number of 'U' nucleotides and turns them into a string
	Usumstring = str(Usum * "U")
	return Usumstring
	
def Csumstring(int):
	#takes the number of 'C' nucleotides and turns them into a string
	Csumstring = str(Csum * "C")
	return Csumstring
	
def Asumstring(int):
	#takes the number of 'A' nucleotides and turns them into a string
	Asumstring = str(Asum * "A")
	return Asumstring
	
def Gsumstring(int):
	#takes the number of 'G' nucleotides and 
	Gsumstring = str(Gsum * "G")
	return Gsumstring

print("Let's play a game!")
print("Amino Acids are the building blocks of life.")
print("They combine to form proteins and are used by the body to perform ")
print("a number of functions including breaking down food and repairing tissue.")
print("Amino Acids are made up of nucleotides.")
print("These nucleotides are Adenine, Cytosine, Guanine, and Uracil,")
print("represented by the corresponding letters 'A', 'C', 'G' and 'U'")
print("These three-letter codes of nucleotides are called 'codons'."  )
print("Your job in this game is to think of your own nucleotide sequence, UAG, for example.")
print("The computer will try to guess your sequence or 'codon' and give you the amino acid")
print("which is made up of that sequence.")
print("Now, are you ready to begin? ('y' or 'yes')" )
	
if input() == 'y' or 'yes' or 'Yes':   
        print ("My first guess is UUU. How many nucleotides here are correct and in the right place?") # the computer guesses this first
Usum = int(input())
if Usum == 3:
    guess = 'UUU'
    print("I've guessed your code! The nucleic acid with this codon is " + acid_dict[guess]+"!")
else:
        print("My second guess is CCC. How many nucleotides here are correct and in the right place?")# the computer guesses this second
Csum = int(input())
if Csum == 3:
    guess = 'CCC'
    print("I've guessed your code! The nucleic acid with this codon is " + acid_dict[guess]+"!")
else:
        print("My third guess is AAA. How many nucleotides here are correct and in the right place?")# the computer guesses this third
Asum = int(input())
if Asum == 3:
        guess = 'AAA'
        print("I've guessed your code! The nucleic acid with this codon is " + acid_dict[guess]+"!")
    
Gsum = 3 - Usum - Asum - Csum

permutation = list(Usumstring(Usum) + Csumstring(Csum) + Asumstring(Asum) + Gsumstring(Gsum))

guesses = 4
while guesses < 10:
        guess = permutation[0] + permutation[2] + permutation[1]
        print('Is this your codon :' + guess + '?')
        guesses = guesses + 1
        response = str(input())
        if response == 'yes' or response == 'y' or response == 'Yes':
                print("I've guessed your code! The nucleic acid with this codon is " + acid_dict[guess]+"!") 
                break
        else:
                guess = permutation[0] + permutation[1] + permutation[2] 
                print('Is this your codon :' + guess + '?')
                response = str(input())
                guesses = guesses + 1
                if response == 'yes' or response == 'y' or response == 'Yes':
                        print("I've guessed your code! The nucleic acid with this codon is " + acid_dict[guess]+"!")
                        break

                else:
                        order = [2,0,1]
                        permutation = [permutation[i] for i in order]
                        continue
if guesses >= 10:
    print('Sorry, I could not guess your codon.')