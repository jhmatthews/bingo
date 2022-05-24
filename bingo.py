import numpy as np 
import matplotlib.pyplot as plt 
import sys
from matplotlib import rc
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=False)

def deal_with_long_sentences (entry):
	'''
	only allow 5 words per line
	'''
	max_words_per_line = 5
	words = entry.split()
	nwords = len(words)
	lines = (nwords // max_words_per_line) + 1


	if lines == 1:
		return entry 
	else:
		new_entry = ""
		for i in range(nwords):
			new_entry += " " + words[i]
			if ( (i+1) % max_words_per_line == 0) and (i != 0):
				new_entry += "\n"

	return new_entry 


def make_bingo(): 
	NX = 6
	NY = 4
	N = NX * NY

	Nper_person = N // 3 

	bingo_card = []

	for i, boy in enumerate(boys):
		if boy == your_name:
			print ("You are {}".format(boy))

		else:
			print ("Reading bingo for {}".format(boy))

			f = open("{}.txt".format(boy))
			entries = [line for line in f]
			f.close()

			#print (entries)

			#indices = np.random.randint(0,len(entries), size=Nper_person)
			np.random.shuffle(entries)

			for i in range(Nper_person):
				entry = deal_with_long_sentences(entries[i])
				bingo_card.append("{}\n{}".format(boy.capitalize(), entry))

	
	np.random.shuffle(bingo_card)
	#print (bingo_card)
	print ("Making bingo card....")

	red_square = np.random.randint(N)
	green_square = np.random.randint(N)
	while green_square == red_square:
		green_square = np.random.randint(N)

	plt.figure(figsize=(11,7))
	for i in range(N):
		plt.subplot(NX, NY, i+1)
		plt.text(0.5,0.5,bingo_card[i], ha='center', va='center')
		if i == red_square:
			plt.fill_between([0,1],0,1, color="C3", alpha=0.5)
		if i == green_square:
			plt.fill_between([0,1],0,1, color="C2", alpha=0.5)

		plt.tick_params(axis='both',which='both',bottom=False,top=False,left=False, right=False, labelleft=False, labelbottom=False)
		plt.xlim(0,1)
		plt.ylim(0,1)

	plt.subplots_adjust(top=0.98, right=0.98, left=0.02, bottom=0.02, hspace=0, wspace=0)
	plt.savefig("card_for_{}.pdf".format(your_name))
	print ("saved as card_for_{}.pdf".format(your_name))


if __name__ == "__main__":
	your_name = name = input("What is your name? (no caps): ")

	boys = ["rob", "aarran", "james", "sam"]

	if your_name not in boys: 
		raise ValueError ("YOU ARE NOT ONE OF THE BOIZ!")
	make_bingo()
