# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

f = open('txtFile.txt', 'r')
sentences = ['I', 'Love', 'You', '\n']
i = 0

while True:
        data = f.readline()

        if not data:
                break
        else:
                print(str(i+1) + '번 문장 : ' + data)
                sentences.append(data)
                i += 1
f.close()

f = open('txtFile.txt', 'w')

for i in range(0,len(sentences),1):
        f.write('%s' %(sentences[i]))
f.close()

f = open('txtFile.txt','r')
print()
print(f.read())
f.close()
