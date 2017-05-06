from ftplib import FTP
import glob
import os


ftp=FTP()
# setting connection with the server taking username and password as input from the user
def conn():
    # connecting to server ip address
    ftp.connect("localhost",8000)
    # taking input from user
    user=input("Username:")
    passwrd=input("Password:")
    # sending credentials for verification
    ftp.login(user,passwrd)

# sending the server those files which are stared i.e. their name end with a star
def send(fname):
    # going to the specified directory
    os.chdir("/home/arindam/Desktop/c")
    q=open(fname,"rb")
    m=fname.replace("/home/arindam/Desktop/c/","")
    print m
    l="STOR "+m
    # performing STOR command to upload file to server
    ftp.storbinary(l,q)
    # changing file names that have been uploaded by replacing * in their names
    nf=m.replace("*","")
    os.rename(m,nf)

#extractig paths of files in the directory and calling the send() function on them
def exfiles():
    # finding all files in the specified directory
    files=glob.glob("/home/arindam/Desktop/c/*.*")
    # checking files with * at their end
    for f in files:
        print f
        k=f.index(".")
        ch=f[k-1]
        if ch=='*':
            send(f)

# this module is used to get command from the user
# some error handling applied more to be applied
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



        

