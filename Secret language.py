def coder():
    import random
    i = input("ENTER YOUR MESSAGE")
    1

    words=i.split(" ")
    for word in words:
        pre = ""
        post = ""
        if len(word)<3:
            print(word[::-1],end=" ")
        else:
            for j in range(0,3):
                pre=pre + (random.choice(alpha))

            word=word[1:]+word[0]

            for j in range(0,3):
                post = post + (random.choice(alpha))

            print(pre+word+post,end=" ")

def decode():

    i=input("ENTER THE ENCODED MESSAGE")
    words=i.split(" ")
    for word in words:
        if len(word)<3:
            print(word[::-1],end=" ")
        else:
            word=word[3:len(word)-3]
            word=word[-1]+word[:len(word)-1]
            print(word,end=" ")


print("WHAT DO YOU WANTED TO DO?")
print("1.ENCODE           2.DECODE         3.QUIT")
while(True):

    choice=int(input("\nENTER YOUR CHOICE"))
    if choice==1:
        coder()
    elif choice==2:
        decode()
    elif choice==3:
        break;
    else:
        raise ValueError("SORRY YOU HAVE ENTERED THE WRONG VALUE")

print("THANK YOU FOR USING OUR MESSAGING SERVICE")