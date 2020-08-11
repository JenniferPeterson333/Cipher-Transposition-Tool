# Cipher-Transposition-Tool

The Cipher Transposition Tool decodes messages that have been encoded by transposing columns. The program proposes a plaintext solution for each transposition and then evaluates that solution. Evaluation is a two step process. The program first screens each solution to see if it contains one or more of the words in a keyword dictionary. Each solution that passes the screening criteria is then presented to the user who can accept it or reject it. Accepted solutions are saved to a file for further analysis. The program is written in Python. An algorithm was chosen to minimize memory usage and increase speed. 

The most significant computational challenge is handling the very large number of possible solutions. A cipher which has n characters in each row has n factorial possible column transpositions. This means that a cipher with 17 characters per row, such as the Zodiac Z340 cipher, has approximately 3.56x10^14 possible solutions. The program assigns an index number for each of the columns and produces a solution for every possible permutation of those index numbers. Python provides a method called "permutations" which produces all possible permutations, but all of those permutations must be stored at once. Storing billions of index permutations is inefficient and in some cases may be impossible depending on the number of columns in the cipher and the amount of available memory. The Cipher Transposition Tool uses a different technique. The program generates index permutations one at a time by defining a function which uses the keyword "yield" which returns a generator object. Solutions are evaluated "on the fly" and not stored unless the user decides they are of interest.

Sample input files:
The file mat06-nospaces.txt contains a ciphertext matrix composed of the unsolved last ten rows of the famous Zodiac Z-340 cipher. This matrix was generated by taking the original ciphertext, which contains symbols, and applying symbol-to-letter substitutions. The substitutions used were those developed by Dr. Craig Bauer, professor of mathematics at York College, in his solution of the first eight rows of this same ciphertext.
The file ZodiacDictionary.txt is a keyword dictionary. Each proposed solution will be screened to see if it contains one or more of these words. The file contains words commonly used by the Zodiac killer in his messages to the police.
