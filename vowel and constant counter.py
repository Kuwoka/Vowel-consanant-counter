text = input("Write a text :")
vowel_count = 0
consonant_count = 0
space_count = 0
for word in text:
    if (word in "aAeEiIuUoOöÖüÜıİ"):
        vowel_count += 1
    elif word in " ":
        space_count += 1
    else :
        consonant_count += 1
print ("There is {} vowel i this text" .format(vowel_count))
print ("There is {} consonant in this text" .format(consonant_count)) 
print ("There is {} space in this text" .format(space_count))
 