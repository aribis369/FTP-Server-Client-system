from ftplib import FTP
import glob
import os


ftp=FTP()
# setting connection with the server taking username and password as input from the user
def conn():
    ftp.connect("localhost",8000)
    user=input("Username:")
    passwrd=input("Password:")
    ftp.login(user,passwrd)

# sending the server those files which are stared i.e. their name end with a star
def send(fname):
    os.chdir("/home/arindam/Desktop/c")
    q=open(fname,"rb")
    m=fname.replace("/home/arindam/Desktop/c/","")
    print m
    l="STOR "+m
    ftp.storbinary(l,q)
    nf=m.replace("*","")
    os.rename(m,nf)

#extractig paths of files in the directory and calling the send() function on them
def exfiles():
    files=glob.glob("/home/arindam/Desktop/c/*.*")
    for f in files:
        print f
        k=f.index(".")
        ch=f[k-1]
        if ch=='*':
            send(f)

#this module is used to get command from the user
def command():
    com=input("command>>>")
    if com=="upload":
        exfiles()
        command()
    elif com=="exit": 
        print "---------------------------------------"
        print "           PROGRAM EXITED              "
        print "---------------------------------------"
        exit()
    else:
        print "---------------------------------------"
        print "   UNKNOWN COMMAND PLEASE TRY AGAIN    "
        print "---------------------------------------"
        command()
# This module provides the CLI to the user to interact with the user
def interface():
    try:
        conn()
    except:
        print "---------------------------------------"
        print "           ACCESS DENIED               "
        print "---------------------------------------"
        interface()
    print "---------------------------------------"
    print "           ACCESS GRANTED              "
    print "---------------------------------------"
    command()


if __name__=="__main__":
    interface()



        

