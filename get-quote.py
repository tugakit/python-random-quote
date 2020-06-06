import random
#def main():

 #f = open("quotes.txt")
 #quotes = f.readlines()
 #.close()
 #last = len(quotes) - 1
 #rnd = random.randint(0, last)

 #print(quotes[rnd]+ (quotes)[0] + (quotes)[last])

#if __name__== "__main__":
  #main()



def chiffres():
  i = 0
  while i < 20:
    d = open("numbers.txt")
    numbers = d.readlines()
    d.close()
    last = len(numbers)
    resultat = last + 1
    print(resultat)
    f = open("numbers.txt", "a")
    f.write(str(resultat))
    f.close()
    e = open("numbers.txt", "a")
    e.write(" \n")
    e.close()
    i += 1

    if i == 20:
      print("Ajout de nouveau contenu avec succes")

chiffres()
