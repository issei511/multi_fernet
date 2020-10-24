#instructions

First clone the repo 

Importing:-

->Importing of multi_fernet  ::: from multi_fernet import multi_fernet as f

Functions of multi_fernit:-

->  f.enc('string','string',int)
    f.enc('message','password',no_of_stages)  #default no of stages 1

->  f.dec('string','string',int)
    f.dec('encrypted_message','password',no_of_stages) #default no of stages 1

NOTE:-

    It uses Memory for encryption and decryption, so encrypt and decrypt the text accordingly with the memory size.