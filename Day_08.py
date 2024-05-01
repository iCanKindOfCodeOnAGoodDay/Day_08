"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 8
    April 30 2024

    ------
    Description:    Ceaser's Cipher - Shift Key Encryption
    ------
    
    ------
    Inputs:         Console input
    ------
    
    ------
    Outputs:        Console output
    ------
    
    ------
    Dependencies:   None.
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

def main():
    """
    
    Description -   Encrypts then decrypts a message [loops if user wants to take another guess, in real application the message could delete if guess is not correct]
    ----------
    Input -         The message, shift key, then the guessed shift key
    ----------
    Output -        Text in console, input functions
    -------

    """ 
    
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    
    caesar_cipher_art = """
 CCCCC   AAA   EEEEE  SSSS   AAA   RRRR    SSSS   ' ' ' SSSS  
C       A   A  E     S      A   A  R   R  S          '  S     
C       AAAAA  EEEE   SSS   AAAAA  RRRR    SSS       '   SSS   
C       A   A  E         S  A   A  R  R       S     '       S  
 CCCCC  A   A  EEEEE SSSS   A   A  R   R  SSSS    ' ' ' SSSS   

 CCCC  IIIII PPPPP  H   H EEEEE RRRR  
C        I   P   P  H   H E     R   R 
C        I   PPPPP  HHHHH EEEE  RRRR  
C        I   P      H   H E     R  R  
 CCCC  IIIII P      H   H EEEEE R   R 
"""

    print( caesar_cipher_art )

    
    actual_s_k = request_shift_key(alphabet)
    m = request_message(alphabet)
    
    
    print(m)
    
    
    e = encrpyt( m, int(actual_s_k), alphabet )
    print(e)
    
    
    while True:

        guessed_s_k = request_shift_key( alphabet )
        
        print('Decryption Result')
        
    
        d = decrypt( e, int(guessed_s_k), alphabet )
    
        print(d)
        
        print('Try again?')
    

def encrpyt( message, shift_k, a ):
    
    """
    
    Description -   Encryptes the message by shifting the characters by the shift key, handling edge cases
    ----------
    Input -         The message, shift key (answer), and the alphabet
    ----------
    Output -        A list of strings which is the encrypted message
    -------

    """ 
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
   
    encrpyted_message = []
    character_list = list(message)
    
    for char in character_list:
        # choose the right letter from the alphabet
        done = False
        index = 0
        
        while done == False: # find and add encrypted letter
            if char == alphabet[index]:
                add_index = 0
                if index + shift_k < len(alphabet):
                    add_index = index + shift_k
                    encrpyted_message.append(alphabet[add_index])
                else:
                    add_index = (index + shift_k) - len(alphabet)
                    encrpyted_message.append(alphabet[add_index])
                done = True
                
            else:
                
                index+=1
                
    return encrpyted_message



def decrypt( message, shift_k_guess, a ): 
    
    """
    
    Description -   Decrypts the scrmabled message and returns it for usage, handles edge cases
    ----------
    Input -         The encrypted message, shift key (guessed), and the alphabet
    ----------
    Output -        A list of strings which is the decrypted message
    -------

    """ 
   
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    decrypted_m = []
    character_list = list(message)

    for char in character_list:
        # choose the right letter from the alphabet
        done = False
        index = 0
    
        while done == False: # find and add decrypted letter 
            if char == alphabet[index]:
                add_index = 0
                if index + shift_k_guess <= len(alphabet):
                    add_index = index - shift_k_guess
                    decrypted_m.append(alphabet[add_index])
                else:
                    add_index = (index - shift_k_guess) - len(alphabet)
                    decrypted_m.append(alphabet[add_index]) # range error with high index
                done = True
                
            else:
                
                index+=1
                
    return decrypted_m
        
    
def request_shift_key( a ):
    """
    
    Description -   Input func modified to only accept certain values, Only accpeting a few values, in real application could allow for more values with some updates to code
    ----------
    Input -         User input
    ----------
    Output -        error messages in console, or acceptable response using input func to be saved to var in main
    -------

    """ 
    while True:
        
        # make sure that the result of the input is one of the acceptable choices
        
        #user_input = input( 'Set the shift key:'  ).lower() # parse string into int
        
        while True:
            
            try:
                
                user_input = int( input( 'type a number for the shift key: ' ) ) # parse string into int
                
                if type(user_input) == int:
                    
                    if user_input >= 0:
                        
                        if user_input <= (len(a) / 2): # for now, we will limit the possible keys to work with our code
                    
                            return user_input
                        
                        else: 
                            print(f'Type an integer less than {str(round(len(a) + 1)/2)}')
                        
                    else: 
                        
                        print('type a postive number')
                
                else:
                    print('Type a number')
                
            except ValueError:
                
                print( "Try again." )
                
                continue
            
            #return user_input
        
    
def request_message( a ):
    """
    
    Description -   Input func modified to only accept certain values
    ----------
    Input -         Make sure user input matches alphabet input - else it would break the code
    ----------
    Output -        Error message or user message to encrypt to be used in main as a result of python prompt func
    -------

    """ 
    while True:
        
            
        # make sure that the result of the input is one of the acceptable choices
        
        user_input = input( 'What would you like to encrypt? '  ).lower() # set all char to lowercase
        
        found_illegal_character = False
        i = 0
        
        for char in user_input: # check each letter
            
            done = False
            index = 0
            while done == False:
                if index > len(a):
                    found_illegal_character = True
                    print(f'you cant use the character {char[i]}')
                    done = True
                    user_input = input( 'What would you like to encrypt?'  ).lower() # set all char to lowercase
                else:
                    done = True
                    if i == len(char):
                        return user_input
                    
                    
                index +=1 
            i+=1
            
        
        else: 
            print('Only letters or spaces')
    
# run code 
if __name__ == '__main__':
    main()