#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the binary representation. We only need the least significant 8 bits
        # for any given number, so we discard the rest.
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we are to start processing a new UTF-8 character.
        if n_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            # This determines how many bytes we get. 
            # 1000 0000 -> 0 bytes
            # 1100 0000 -> 2 bytes
            # 1110 0000 -> 3 bytes
            # 1111 0000 -> 4 bytes
            for bit in bin_rep:
                if bit == '0': break
                n_bytes += 1

            # 1 byte characters
            if n_bytes == 0:
                continue
        
        # Else, we are to validate the current UTF-8 character.
        else:
            # Else, only the 2 most significant bits should be 10.
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # We reduce the number of bytes to process by 1 after each integer.
        n_bytes -= 1

    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return n_bytes == 0
