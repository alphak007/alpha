import datetime
import json
import random
import csv

def delay():
    print("-"*50)
    print("We're sorry for the trouble! Your order will reach you soon.")
    print("Are you satisfied with the solution?")
    ch=input("Y/N :")
    if(ch=='n' or ch=='N'):
        print("-"*50)
        print("Press 1 to raise a ticket")
        if(int(input())==1):
            with open("delay_ticket.txt","a") as fp:
                ticket_num=random.randint(100,200)
                fp.write(str(ticket_num)+",")      #writing into csv file
            print("Ticket has been raised concerning your complaint.")
        else:
            print("Invalid Input")

    elif(ch=='y' or ch=='Y'):
        print("Have a nice day, ",name,"!")
        exit
    else:
        print("Invalid input")

             
           
def ret_replace():
    reason={1: "Wrong item delivered", 2: "Item no longer required",3: "Better price available",
            4:"Size too small/large",5:"Used product delivered",6:"Damaged product"}
    print("-"*50)
    ch=int(input("Choose from the given options\n1. Return\n2. Replace:\n "))
    if(ch==1):
        print("-"*50)
        print("Kindly choose the reason for return",reason)
        r=int(input("Your answer : "))
        cmt=input("Kindly explain your reason : ")
        addr=input("Will the pick up address be same as delivery address?(Y/N) :")
        if(addr=='n' or addr=='N'):
            addr=input("Enter the pick up address")

        with open("ret_replace_ticket.txt","a") as f:
            ticket_num=random.randint(100,200)
            f.write(str(ticket_num)+","+reason[r]+","+cmt+","+addr)    #writing into csv file

        print("Ticket has been raised")
        pay_method=input("Do you want refund in your original payment method?(Y/N) :")
        if(pay_method=='y' or pay_method=='Y'):
            print("Amount will be refunded in original payment method")
        elif(pay_method=='n' or pay_method=='N'):
            print("Amount will be refunded in your wallet")
        else:
            print("Invalid input")

    #replace item
    elif(ch==2):
        print("-"*50)
        print("Kindly choose the reason for replacement",reason)
        r=int(input("Your answer : "))
        cmt=input("Kindly explain your reason : ")
        addr=input("Will the pick up address be same as delivery address?(Y/N)")
        if(addr=='n' or addr=='N'):
            addr=input("Enter the pick up address")

        with open("ret_replace_ticket.txt","a") as f:
            ticket_num=random.randint(100,200)
            f.write(str(ticket_num)+","+reason[r]+",",cmt,addr)    #writing into csv file

        print("Ticket has been raised")

    else:
        print("Invalid choice")



def damaged():
    print("-"*50)
    print("We're sorry for the trouble! We'll do what is best for you.")
    msg=str(input("Kindly tell us more about the damaged product:"))
    print("-"*50)
    print("That is not acceptable. We'll ensure this doesn't happen again. ")

    ch=input("Do you want to return/replace the item (Y/N):")
    if(ch=='y' or ch=='Y'):
        ret_replace()

    elif(ch=='n' or ch=='N'):
        print("Have a nice day, ",name,"!")
        exit
    else:
        print("Invalid input")  




time=datetime.datetime.today()
if(time.hour>=6 and time.hour<12):
    print("Good Morning! ")
elif(time.hour>=12 and time.hour<14):
    print("Good Noon! ")
elif(time.hour>=14 and time.hour<17):
    print("Good AfterNoon! ")
elif(time.hour>=17 and time.hour<21):
    print("Good Evening! ")
else:
    print("Hello! What's up! ")

name=input("Whats your name? ")
print("Hello ",name, ". I hope you're doing well. Kindly choose from the following options.")

while 1:
    print("-"*50)
    print("Press 0 for already raised ticket.")
    print("Press 1 to raise a new concern.")
    print("Press 2 to exit")
    print("-"*50)
    try:
        response=int(input())
    except ValueError:
        print("Invalid input")
        
    else:
        #already raised ticket
        if(response==0 ):
            ticket=int(input("Please enter the ticket number : "))
            print("Status")
            

        #new concerns
        elif(response==1):
            try:
                file= open("products.txt","r")
                    
            except FileNotFoundError:
                print("You have not ordered any product")
            else:
                print("-"*50)
                print("Your order list:")
                i=1
                data=json.load(file)
                for k in data:
                    
                    print(i,k)
                    i+=1
                    
                file.close()

                prod=input("Which product you have concern about?:")
                while(prod not in data):
                        print("This product is not in your list. Kindly enter a valid option")
                        prod=input()

                print("-"*50)
                print("Kindly choose from the below options\n1. Delayed Shipping\n2. Damage Product Delivered\n3. Return/Replacement")
                choice=int(input())

                #delay shipping
                if(choice==1):
                    delay()

                #damaged product        
                elif(choice==2):
                    damaged()

                #return/replace
                elif(choice==3):
                    ret_replace()
                else:
                    print("Invalid choice")
                


        elif(response==2):
            print("Have a nice day!")
            break
        else:
            print("Sorry! That's not a valid option.")

    finally:
        pass
            

           








