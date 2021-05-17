def main():
   print()

f = open("quotes.txt")
quotes = f.readlines()
f.close()

print(quotes[6])
print(quotes[8])
print(quotes[15])

if __name__== "__main__":
  main()
