
from subprocess import call
from sys import exit
    
main = input("Petlja link  .. ")
    
#try:
#    call("wget -e robots=off -r -U Mozilla --no-parent --no-verbose " + main, shell=True)
#except:
#    print("\n Wget call failure. Were the link right? \n")
#    exit(1)
    
dir = "/biblioteka/r/lekcije/"
key = 'a href="' + dir
    
dfile = open( main.replace("https://", ""), "r")
data = dfile.read()
dfile.close()

links = [main.replace("https://petlja.org", "")] 
u = -1
while (u < len(data)-1):
    u = (u+1)
    p = data[u]
    id = ""
    link = ""
    for x in key:
        if u+ len(id) < len(data):
            id = id + data[u+ len(id)]
    if key != id:
        continue
    i = len(key)-len(dir)-1
    while(i < len(data)):
        i = (i+1)
        if(data[i+u] == '"') or (i+u >= len(data)):
             break
        link = link + data[i+u]
    links.append(link)
 
print("\n")
rfile = open("links.txt", "w+")
rfile.truncate()
for x in links:
    print(x)
    rfile.write(x + "\n")
rfile.close()

print("\n")