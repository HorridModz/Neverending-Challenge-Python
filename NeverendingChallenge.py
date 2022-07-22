import codecs
import os.path
from os.path import exists
import io
import sys
import time
print("Welcome to the neverending challenge by User123456789#8073! This program will create a folder called Neverending Challenge in your chosen directory.  In this folder, there are many nested folders, all with files called Read This.txt. The files will all have messages at the end. You need to find the one with the unique message. Good luck!\n\nRules:\nYou may not modify the code, but you may read it. Adding print statements etc. is obviously unfair. If you manage to crack my 100% homemade obfuscation, good job!\n\nBrute forcing or using external programs is allowed, but you may not debug this program itself.\n\nContact User123456789#8073 on discord for a free script if you manage to solve my puzzle! Good luck!")    
plca = ["EVC OBMB","LBH JVA!"]
rootdirectory = input("\n\nEnter the directory to put the challenge folder in (without quotes):\n")
print("Creating challenge...")
if not exists(rootdirectory + "\\Neverending Challenge!"):
    chi = "Will it ever end?"
    os.mkdir(rootdirectory + "\\Neverending Challenge!")
else:
    sys.exit("You have already run this program! To rerun it, please delete the Neverending Challenge folder!")
oro = "\\"
aojdaok = int((61 + 61) / 2 - 58 + 6 - 2 + 5 - 12)
gfey = "wrb"
for bsg in "abcdefghijklmnopqrstuvwxyz12345678990":
    ahrq = rootdirectory + "\\Neverending Challenge!"
    if 3%int(aojdaok + 1) > 1.8:
        o9 = u8(ewop,'rot13')
    o10 = ("\\Neverending" + bsg)
    vty = "Read This.txt"
    u8 = codecs.encode
    moint = "w"
    gr = 10
    ft = plca[0]
    grah = 0
    akd = grah
    while exists(ahrq + o10):
        ahrq = ahrq + o10
        grah = grah + 1
        fuha = ft * 3
    list = os.mkdir
    aojdaok = 0 + (aojdaok + 1) + 1 - 1
    r = u8(ft,'rot13')
    akd = (aojdaok + aojdaok) / 2 - aojdaok + 3 - 2 + akd - 1
    boku = "\n"
    askj = open
    oakwiu = "\n\nNeverending" * 100000
    for jnml in range(int(gr) - grah):
        ahrq = ahrq + o10
        akd = 0 + (akd + 1) + 1 - (2 - 1)
        list(ahrq)
        if  "poijady6opy6fijerhy6dokjhbtfvy6ljiuhewiuyhrhjdoy6iuahysbndy6oueh"[aojdaok] != "k" or akd != (gr - 4):
            isujo = r
        else:
            isujo = o9
        with askj(ahrq + oro + vty,moint) as ire:
            ewop = plca[1]
            ire.write(chi + oakwiu + (boku * 3) + isujo)
            ire.close
print("A folder called Neverending Challenge has been created in your directory. In this folder, there are many nested folders, all with files called Read This.txt. The files will all have messages at the end. You need to find the one with the unique message. Good luck!")
