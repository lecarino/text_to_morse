from morse import Morse

morse_code = Morse()
is_finished = False
print('''
         
   _____                               _________              ____      
  /     \   ___________  ______ ____   \_   ___ \  _____   __| _/____  
 /  \ /  \ /  _ \_  __ \/  ___// __ \  /    \  \/ /  _ \ / __ |/ __ \ 
/    Y    (  <_> )  | \/\___ \\  ___/  \     \___(  <_> ) /_/ \  ___/ 
\____|__  /\____/|__|  /____  >\___  >  \______  /\____/\____ |\___  >
        \/                  \/     \/          \/            \/    \/ 

by Larrenz Carino
      ''')

print('Welcome to my text to morse_code program')

while not is_finished:
    choice = input('Press "e" to encode your message. \nPress "q" to quit.\n')

    if choice == 'e':
        text = input('\nWhat text would you like to convert to morse code?')
        converted_text = morse_code.encode(text)
        print(f'\nHere is your encoded text:\n{converted_text}')

    # elif choice =='d':
    #     message = input('\nPlease input the morse code to convert to text: ')
    #     decoded_message = morse_code.decode(message)
    #     print(f'Here is your decoded text:\n {message}')

    elif choice =='q':
        print('\nThank you! Good bye!')
        is_finished = True

    else:
        print('\nPlease press input "e" or "q" only.')
