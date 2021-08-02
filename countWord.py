kalimat = 'I believe I can code'
arr = []
s = ""
count_word = 0

for i in kalimat:
    if(i != " "):
        s+= i
    elif(i == " "):
        if(s!=""):
            count_word +=1
            arr.append(s)
            s = ""
if(s!=""):
    arr.append(s)
print(arr)

# abc = list(map(str, kalimat.split()))
# print(len(abc))