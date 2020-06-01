from tkinter import *
from tkinter import filedialog
from bitstring import BitArray

def get_primes(lower,upper):
	# generez o lista de nr prime posibile pentru calcularea produsului pq
	l = list()
	for num in range(lower,upper+1):
		if num > 1:
			for i in range(2,num):
				if(num % i) == 0:
					break
			else:
				if(num % 4) == 3:
					l.append(num)
	return l


def random_seed(n):
	# determin germenele x_0, de la care incep calculul
	import random
	return random.randint(n//2,n-1)

def get_pq(l):
	import random
	import math
	rand_list = random.choices(l, k=2)
	print("Cele 2 nr prime alese: ", rand_list)
	return math.prod(rand_list)
	
def blum_blum_shub(n,m):
	# functia principala ... salveaza output-ul intr-un string binar pentru a il scrie in fisier
	print("Inceput algoritm")
	out = str()
	x_0 = random_seed(n)

	for i in range(0, m):
		x_i = x_0 ** 2 % n
		x_0 = x_i
		new_out = out + str(x_i % 2)
		out = new_out
	print("\nRezultatul dorit: ")
	print(out)
	print("Final algoritm")
	b = BitArray(bin=out)
	return b


def get_bounds(size):
	import math
	a = size
	b = 3*size
	return a,b


def algoritm():
	# introduc dimensiunea in MB a fisierului dorit de la tastatura
	in_size = citeste_mb()
	print("Generez nr aleatoare - nr MB: ", in_size)
	size = in_size * 8 * 1024 #(dimensiunea in biti)
	# procesez dimensiunea dorita, astfel incat sa stiu de ce dimensiune sa imi aleg numarul prim
	a,b = get_bounds(size)
	print("intervalul din care aleg nr prime: ", a, b)
	# generez o lista de numere prime in intervalul gasit
	l = get_primes(a,b)

	# din lista de nr prime generate, aleg 2 aleatoare p,q si returnez rezultatul inmultirii p*q (eu nu vad numerele p,q)
	n = get_pq(l)
	print("n = ", n)
	print("Apelez bbs ", n, size)
	text = blum_blum_shub(n,size)

	f = filedialog.asksaveasfile(mode='wb', defaultextension=".txt")
	if f is None:
		return

	text.tofile(f)
	f.close()


global textbox


def citeste_mb():
    return int(textbox.get())


def salveaza_fisier():
	pass


def do_stuff():
	global textbox

	root = Tk()
	root.title("Titlu temporar")

	label = Label(root,text="Introduceti numarul de MB: ")
	label.grid(row=0,column=0)

	textbox = Entry(root)
	textbox.grid(row=0,column=1)

	button = Button(root,text="Salveaza fisier",command=algoritm,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
	button.grid(row=0,column=2)

	root.mainloop()

do_stuff()
