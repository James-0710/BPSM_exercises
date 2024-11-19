#!usr/bin/python3
import re

accessions = [
  'xkn59438',
  'yhdck2',
  'eihd39d9',
  'chdsye847',
  'hedle3455',
  'xjhd53e',
  '45da',
  'de37dp']

for acc in accessions:
    print(acc)


outputs = []

for acc in accessions:
    if re.search(r'5', acc) : 
        outputs.append('contain the number 5: ' + acc)
    if re.search(r'[de]', acc) :
        outputs.append('contain the letter d or e: ' + acc)
    if re.search(r'de', acc) :
        outputs.append('contain the letter d and e (have to be adjacent): ' + acc)
    if re.search(r'd.*e', acc) :
        outputs.append('contain the letter d and e in that order (dont have to be adjacent): ' + acc)
    if re.search(r'd.e', acc) :
        outputs.append('contain the letter d and e in that order with a single letter between them: ' + acc)
    if re.search(r'd', acc) and re.search(r'e', acc) :
        outputs.append('contain both the letters d and e in any order: ' + acc)
    if re.search(r'(^x|^y)', acc) :
        outputs.append('start with x or y: ' + acc)
    if re.search(r'(^x|^y)', acc) and re.search(r'(e$)', acc) :
        outputs.append('start with x or y and end with e: ' + acc)
    if len(re.findall(r'\d',acc)) == 3 :
        outputs.append('contains any 3 numbers in any order: ' + acc)
    if len(set(re.findall(r'\d',acc))) == 3 :
        outputs.append('contains 3 different numbers: ' + acc)
    if re.search(r'\d{3,}', acc):
        outputs.append('contain three or more numbers in a row: ' + acc)
    if re.search(r'd[arp]$', acc):
        outputs.append('end with d followed by either a, r or p: ' + acc)

outputs.sort()
print(('\n').join(outputs))

dict_approach = {}
dict_approach['contain the letter d or e'] = '45da'
dict_approach['contain the letter d or e']=dict_approach['contain the letter d or e'] + ', chdsye847'
dict_approach
list(dict_approach.values())
list(dict_approach.values())[0].split(',')
list(dict_approach.items())



