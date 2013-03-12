from html.parser import HTMLParser

class myparser(HTMLParser):
   

   def new_output(self):
      self.outdata = []   

   def return_output(self):
      return self.outdata

   def handle_starttag(self, tag, attrs):
      if tag == 'a':
         for att in attrs:
            if att[0] == 'title' and 'Mehr Informationen' in att[1] and len(att[1]) > len('Mehr Informationen zu '):
               #print(att[1][22:])
               self.outdata.append(att[1][22:])
               break
   
   def handle_data(self, data):
      weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']    
      if data.strip() in weekdays or (':' in data and len(data.strip()) == 5):
         #print(data.strip())
         self.outdata.append(data.strip())

