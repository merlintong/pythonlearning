#purely testing
word1="192.168.10.1"
word2="GIE2PLABS010001"
word3="10.100.17.11"
result="test"
result2=word2[-6:]
result3=str(int(word2[-6:-3]))+"."+str(int(word2[-3:]))

if word2[3]=="1":
    result="10.100"
elif word2[3]=="2":
    result="10.104"
elif word2[3]=="4":
    result="10.107"
elif word2[3]=="5":
    result="10.108"

result=result+"."+str(int(word2[-6:-3]))+"."+str(int(word2[-3:]))
print (result)
