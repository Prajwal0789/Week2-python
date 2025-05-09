#anagram of 2 Strings

word1=input("Enter the First Word")
word2=input("Enter the Second Word")
if len(word1)!=len(word2):
    print("The two words are not Anagrams")
else:
    word1=sorted(word1)
    word2=sorted(word2)
    if word1==word2:
        print("The two words are Anagrams")
    else:
        print("The two words are not Anagrams")