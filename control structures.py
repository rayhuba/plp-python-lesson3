marks = 65 
result = "" 
if marks < 30: 
	result = "Failed" 
elif marks > 75: 
	result = "Passed with distinction" 
else: 
	result = "Passed"

print(result)

#next program
def checkVowel(n): 
   match n: 
      case 'a': return "Vowel alphabet" 
      case 'e': return "Vowel alphabet" 
      case 'i': return "Vowel alphabet" 
      case 'o': return "Vowel alphabet" 
      case 'u': return "Vowel alphabet" 	
      case _: return "Simple alphabet" 	
print (checkVowel('a')) 
print (checkVowel('m')) 
print (checkVowel('o'))

#another data structure
