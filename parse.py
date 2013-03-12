import myparser

montag = []
dienstag = []
mittwoch = []
donnerstag = []
freitag = []

def split_weekdays(inlist):
   global montag, dienstag, mittwoch, donnerstag, freitag

   cnt = 0
   title = ''

   while cnt + 1< len(inlist):

      if inlist[cnt+1] == 'Montag':
         montag.append((inlist[cnt],inlist[cnt+2],inlist[cnt+3]))
         title = inlist[cnt]
         cnt += 4
      elif inlist[cnt+1] == 'Dienstag':
         dienstag.append((inlist[cnt],inlist[cnt+2],inlist[cnt+3]))
         title = inlist[cnt]
         cnt += 4
      elif inlist[cnt+1] == 'Mittwoch':
         mittwoch.append((inlist[cnt],inlist[cnt+2],inlist[cnt+3]))
         title = inlist[cnt]
         cnt += 4
      elif inlist[cnt+1] == 'Donnerstag':
         donnerstag.append((inlist[cnt],inlist[cnt+2],inlist[cnt+3]))
         title = inlist[cnt]
         cnt += 4
      elif inlist[cnt+1] == 'Freitag':
         freitag.append((inlist[cnt],inlist[cnt+2],inlist[cnt+3]))
         title = inlist[cnt]
         cnt += 4
      else:
         # if multiple exercise, a weekday will be at cnt
         if inlist[cnt] == 'Montag':
            montag.append((title,inlist[cnt+1],inlist[cnt+2]))
            cnt += 3
         elif inlist[cnt] == 'Dienstag':
            dienstag.append((title,inlist[cnt+1],inlist[cnt+2]))
            cnt += 3
         elif inlist[cnt] == 'Mittwoch':
            mittwoch.append((title,inlist[cnt+1],inlist[cnt+2]))
            cnt += 3
         elif inlist[cnt] == 'Donnerstag':
            donnerstag.append((title,inlist[cnt+1],inlist[cnt+2]))
            cnt += 3
         elif inlist[cnt] == 'Freitag':
            freitag.append((title,inlist[cnt+1],inlist[cnt+2]))
            cnt += 3

         # if this course has no date, skip
         elif len(inlist[cnt]) > len('Donnerstag'):
            cnt += 1
         
         else:
            #print('-----Error!-----')
            #print(inlist[cnt])
            cnt += 1
      

parser = myparser.myparser()

institutes = ['mmk','pi','ise','thi','vs','tnt','ikt','ims']

for inst in institutes:

   source = open('lsf_'+inst+'.htm').read()
   parser.new_output()
   parser.feed(source)
   data = parser.return_output()
   split_weekdays(data)

   parser.close()
   parser.reset()


print('Montags: ', len(montag), ' Veranstaltungen.')
print('Dienstags: ',  len(dienstag), ' Veranstaltungen.')
print('Mittwochs: ', len(mittwoch), ' Veranstaltungen.')
print('Donnerstags: ', len(donnerstag), ' Veranstaltungen.')
print('Freitags: ', len(freitag), ' Veranstaltungen.')
print()
print()
print('Folgende Veranstaltungen finden am Donnerstag statt (ungeordnet):')
print()
for elem in donnerstag:
   print(elem[0], 'von', elem[1], 'bis', elem[2])
