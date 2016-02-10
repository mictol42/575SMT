import sys

# this is a DUMMY DATA SET
# it's not even taking in arguments right now; just to test a very, very basic
# implementation of the "random walk" technique :)

# theoretically, this PHRASE TABLE
# information would be pre-processed in another
# piece of code from the GIZA++ generated table. 
# This isn't theoretically hard-- it's just splitting the string
# and saving it-- but it's not needed for this dummy implementation 

# phrase table data:
# [(english_phrase, spanish_phrase, prob)]
# the current phrase table is in english-to-german 
# for ease of examples for myself, lol.
phrase_table = [("the coast is clear","die luft ist rein",0.5)]

print "Original Phrase Table"
print "(English, German, Probability)"
print phrase_table
print ""

# english to spanish and spanish to english phrases. 
# ideally, this will be computed elsewhere from panlex. 

# format
# english-to-spanish
# [(english_phrase, [spanish translation, spanish translation....]), ...]
	
# spanish-to-english
# [(spanish_phrase, [english translation, english translation...]), ...]

# again; dummy data with german to see if this works...
english_german = [("the coast is clear",["die luft ist rein"]), 
				("it's clear",["alles klar","es ist klar"])]
german_english = [("die luft ist rein",["the coast is clear","it's clear"])]

augment_info = []

for (phrase, trans, prob) in phrase_table:

	german_translations = []
	
	# find translation in panlex
	for (panlex_eng,panlex_ger) in english_german:
		if phrase == panlex_eng:
			for pl_trans in panlex_ger:
				german_translations.append(pl_trans)

	english_pivot = []
		
	# find the re-translations into english
	for german_phrase in german_translations:
		for (panlex_ger,panlex_eng) in german_english:
			if german_phrase == panlex_ger:
				for pl_trans in panlex_eng:
					english_pivot.append(pl_trans)

	# re translate this into german 
	# these are added to the PHRASE TABLE with same probabilities as before 
	for pivot in english_pivot:
		for (panlex_eng,panlex_ger) in english_german:
			if (panlex_eng == pivot) and not (pivot == phrase):
				#print pivot
				augment_info.append((pivot,trans,prob))
					
	
	

for augment in augment_info:
	phrase_table.append(augment)
	
	
print "Augmented Phrase Table"
print "(English, German, Probability)"
print phrase_table

