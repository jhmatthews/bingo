import numpy as np 
import matplotlib.pyplot as plt 
import sys
from matplotlib import rc
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=False)

your_name = name = input("What is your name? (no caps)")

boys = ["rob", "aarran", "james", "sam"]

if your_name not in boys: 
	raise ValueError ("YOU ARE NOT ONE OF THE BOIZ!")

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
			print (boy)
			entries = [line for line in f]
			f.close()

			#print (entries)

			#indices = np.random.randint(0,len(entries), size=Nper_person)
			np.random.shuffle(entries)

			for i in range(Nper_person):
				bingo_card.append("{}\n{}".format(boy.capitalize(), entries[i]))

	print (bingo_card)
	np.random.shuffle(bingo_card)
	print (bingo_card)

	plt.figure(figsize=(10,6))
	for i in range(N):
		plt.subplot(NX, NY, i+1)
		plt.text(0.5,0.5,bingo_card[i], ha='center', va='center')
		plt.tick_params(axis='both',which='both',bottom=False,top=False,left=False, right=False, labelleft=False, labelbottom=False)

	print (your_name)
	plt.subplots_adjust(top=0.98, right=0.98, left=0.02, bottom=0.02, hspace=0, wspace=0)
	plt.savefig("card_for_{}.pdf".format(your_name))



make_bingo()
