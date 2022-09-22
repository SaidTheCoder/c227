
print("Welcome to the world of cryptography")

def main():
   print()
   print("chose one option")
   choice=int(input("1.encryption\n 2.decryption\n choose(1,2)"))
   if choice==1:
    encryption()

   elif choice==2:
    decryption()

   else:
    print("wrong choice! (piseek 1 or 2)") 

def encryption():
    print("you have chose encryption")
    msg=input("enter your message")
    key=int(input("enter key(1-94):"))
    encrypted_text=""

    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32
        encrypted_text+=chr(temp)
    print("encrypted: "+encrypted_text)
    main()


def decryption():
    print("you have chose decryption")
    print("message can only or upper case alphabestes")
    encrp_msg=input("enter encrypted text")
    decrp_key=int(input("enter key(1-94):"))
    decrypted_text=""

    for i in range(len(encrp_msg)):
        temp=(ord(encrp_msg[i])-decrp_key)
        if(temp<32):
            temp=temp+127-32
        decrypted_text+=chr(temp)
    print("decrypted: "+decrypted_text)
    





    
    

        
if __name__ == "__main__":
    main()
