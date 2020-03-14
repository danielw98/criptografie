from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Titlu temporar")
A = ord('A')
my_dict = {i:chr(A+i) for i in range(0,26)}
plain = list()
cipher = list()
cezar_label = None
left, right = None, None
shift = None
shift_num = 3

plain_num = list()
cipher_num = list()


plain_textbox = None
cipher_textbox = None


def caesar_save_plaintext():
    global plain_textbox
    f =filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text = plain_textbox.get()
    f.write(text)
    f.close()


def caesar_load_plaintext():
    global plain_textbox
    path = filedialog.askopenfilename()
    plain_textbox.delete(0,END)
    with open(path) as f:
        new_str = f.readlines()
        plain_textbox.insert(0,new_str)

def caesar_save_ciphertext():
    global cipher_textbox
    f =filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text = cipher_textbox.get()
    f.write(text)
    f.close()

def caesar_load_ciphertext():
    global cipher_textbox
    path = filedialog.askopenfilename()
    cipher_textbox.delete(0,END)
    with open(path) as f:
        new_str = f.readlines()
        cipher_textbox.insert(0,new_str)

# polybus

def polybus_save_plaintext():
    global plain_textbox2
    f =filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text = plain_textbox2.get()
    f.write(text)
    f.close()


def polybus_load_plaintext():
    global plain_textbox2
    path = filedialog.askopenfilename()
    plain_textbox2.delete(0,END)
    with open(path) as f:
        new_str = f.readlines()
        plain_textbox2.insert(0,new_str)

def polybus_save_ciphertext():
    global cipher_textbox2
    f =filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text = cipher_textbox2.get()
    f.write(text)
    f.close()

def polybus_load_ciphertext():
    global cipher_textbox2
    path = filedialog.askopenfilename()
    cipher_textbox2.delete(0,END)
    with open(path) as f:
        new_str = f.readlines()
        cipher_textbox2.insert(0,new_str)

def update_labels():
    global cipher,cipher_num,my_dict,shift_num
    i = 0
    for elem in cipher:
        elem.config(text=my_dict[(i+shift_num)%26])
        i+=1
    i = 0
    for elem in cipher_num:
        elem.config(text=(i+shift_num)%26)
        i+=1

def shift_right():
    global shift_num,shift, root
    shift_num = (shift_num+1)%26
    shift.config(text=shift_num)
    update_labels()
   

def shift_left():
    global shift_num, shift, root
    shift_num = (shift_num-1)%26
    shift.config(text=shift_num)
    update_labels()

def do_cipher():
    global plain_textbox, cipher_textbox
    global shift_num
    text = plain_textbox.get().upper()
    new_str = ""
    for c in text:
        if (ord(c) > ord('Z')) or (ord(c) < ord('A')):
            new_str = new_str + c
            continue
        poz = ord(c)-ord('A')
        poz = (poz + shift_num)%26
        new_str = new_str + chr(ord('A')+poz)
    
    cipher_textbox.delete(0,END)
    cipher_textbox.insert(0,new_str)

def do_decipher():
    global plain_textbox, cipher_textbox
    global shift_num
    text = cipher_textbox.get().upper()
    new_str = ""
    for c in text:
        if (ord(c) > ord('Z')) or (ord(c) < ord('A')):
            new_str = new_str + c
            continue
        poz = ord(c)-ord('A')
        poz = (poz - shift_num)%26
        new_str = new_str + chr(ord('A')+poz)
    
    plain_textbox.delete(0,END)
    plain_textbox.insert(0,new_str)


def make_square():
    global polybus_square, polybus_inverse
    global polybus_key
    global alphabet_list

    current_key = polybus_key.get().upper()

    unique_list = list()
    for c in current_key:
        if ord('Z') >= ord(c) >= ord('A'):
            if c not in unique_list:
                if c is 'I' or c is 'J':
                    if "I/J" not in unique_list:
                        unique_list.append("I/J")
                else:
                    unique_list.append(c)
                    
    for c in alphabet_list:
        if c not in unique_list:
             if c not in unique_list:
                if c is 'I' or c is 'J':
                    if "I/J" not in unique_list:
                        unique_list.append("I/J")
                else:
                    unique_list.append(c)
    
    k=0
    for i in range(1,6):
        for j in range(1,6):
            polybus_square[10*i+j].config(text=unique_list[k])
            polybus_inverse[unique_list[k]]=10*i+j
            k += 1
            


def cipher_polybus():
    global plain_textbox2, cipher_textbox2, polybus_inverse
    my_str = plain_textbox2.get().upper()
    out_str = ""
    
    for ch in my_str:
        if ord('A') <= ord(ch) <= ord('Z'):
            if ch is 'I' or ch is 'J':
                out_str = out_str + str(polybus_inverse["I/J"])
            else:
                out_str = out_str + str(polybus_inverse[ch])
        if ch is ' ':
            out_str = out_str + ' '

    cipher_textbox2.delete(0,END)
    cipher_textbox2.insert(0,out_str)


def decipher_polybus():
    global plain_textbox2, cipher_textbox2, polybus_square

    my_str = cipher_textbox2.get()
    out_str = ""
    first = True

    my_int = int()
    for ch in my_str:
        if ch is ' ':
            out_str = out_str + ' '
        elif ch >= '1' and ch <= '5':
            if first:
                my_int = int(ch)*10
                first = False
            else:
                my_int += int(ch)
                curr = polybus_square[my_int].cget("text")
                if curr in "I/J":
                    curr = 'I'
                out_str = out_str + curr
                first = True
    plain_textbox2.delete(0,END)
    plain_textbox2.insert(0,out_str)


def tema_cifrare():
    # deschid un fisier de input
    pass

def setup():
    # cezar
    global root, cezar_label,left,shift,right,plain_label,cipher_label,plain,cipher
    global plain_num, cipher_num, plain_textbox, cipher_textbox
    cezar_label = Label(root,text="Cifrul lui Cezar",font=('times', 20, 'bold'))
    cezar_label.grid(row=0,column=0,columnspan=8)

    left = Button(root,text="<<",command=shift_left,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    left.grid(row=1,column=1)

    shift = Label(root,text=shift_num,font=('times', 15, 'bold'))
    shift.grid(row=1,column=2)


    right = Button(root,text=">>",command=shift_right,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    right.grid(row=1,column=4)

    plain_label = Label(root,text="Plain Text",pady=10)
    plain_label.grid(row=2,column=1)

    cipher_label = Label(root,text="Cipher Text")
    cipher_label.grid(row=2,column=4)

    for i in range(0,26):
        l1 = Label(root,text=i)
        l1.grid(row=3+i,column=0)
        plain_num.append(l1)

        l1 = Label(root,text=my_dict[i],font=('times', 15, 'bold'))
        l1.grid(row=3+i,column=1,padx=5)
        plain.append(l1)

        l2 = Label(root,text=(i+shift_num)%26)
        l2.grid(row=3+i,column=3)
        cipher_num.append(l2)

        l2 = Label(root,text=my_dict[(i+shift_num)%26],font=('times', 15, 'bold'))
        l2.grid(row=3+i,column=4,padx=5)
        cipher.append(l2)

    l = Label(root,text="Plain Textbox")
    l.grid(row=10,column=6,columnspan=2)
    plain_textbox = Entry(root,width=50,borderwidth=5)
    plain_textbox.grid(row=11,column=6,columnspan=2)

    l = Label(root,text="Cipher Textbox")
    l.grid(row=12,column=6,columnspan=2)
    cipher_textbox = Entry(root,width=50,borderwidth=5)
    cipher_textbox.grid(row=13,column=6,columnspan=2)

    b1 = Button(root,text="Cipher",command=do_cipher,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    b1.grid(row=15,column=6)
    b2 = Button(root,text="Decipher",command=do_decipher,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    b2.grid(row=15,column=7)    
    

    # save and load
    b1_save = Button(root,text="Save Plain",command=caesar_save_plaintext)
    b1_save.grid(row=20,column=6)

    b1_load = Button(root,text="Load Plain",command=caesar_load_plaintext)
    b1_load.grid(row=20,column=7)

    b2_save = Button(root,text="Save Cipher",command=caesar_save_ciphertext)
    b2_save.grid(row=21,column=6)

    b2_load = Button(root,text="Load Cipher",command=caesar_load_ciphertext)
    b2_load.grid(row=21,column=7)

    # padding
    l = Label(root,text="",padx=20)
    l.grid(row=0,column=8)

    # Polybus
    polybus_label = Label(root,text="Sistemul Polybus (I=J)",font=('times', 20, 'bold'))
    polybus_label.grid(row=0,column=18,columnspan=8)

    l = Label(root,text="Key:",pady=40)
    l.grid(row=1,column=17)

    global polybus_key
    polybus_key = Entry(root,width=50,borderwidth=5)
    polybus_key.insert(0,"Enter a key")
    polybus_key.grid(row=1,column=18,columnspan=5)

    global alphabet_list
    alphabet_list = [chr(c) for c in range(ord('A'),ord('Z')+1)]
    
    for i in range(5):
        l1 = Label(root,text=i+1)
        l1.grid(row=3+i,column=17)
        l2 = Label(root,text=i+1)
        l2.grid(row=2,column=18+i)

    global polybus_square, polybus_inverse
    polybus_square = dict()
    polybus_inverse = dict()
    k = 0
    for i in range(1,6):
        for j in range(1,6):
            curr = alphabet_list[k]
            if curr is 'I':
                k += 1
                curr = "I/J"
            elem = Label(root,text=curr,font=('times', 15, 'bold'))
            elem.grid(row=2+i,column=17+j)
            polybus_square[10*i+j] = elem
            polybus_inverse[curr] = 10*i+j
            k += 1
    
    polybus_ok = Button(root,text="Ok",command=make_square,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    polybus_ok.grid(row=1,column=23)


    global plain_textbox2
    l = Label(root,text="Plain Textbox")
    l.grid(row=10,column=18,columnspan=5)
    plain_textbox2 = Entry(root,width=50,borderwidth=5)
    plain_textbox2.grid(row=11,column=18,columnspan=5)

    global cipher_textbox2
    l = Label(root,text="Cipher Textbox")
    l.grid(row=12,column=18,columnspan=5)
    cipher_textbox2 = Entry(root,width=50,borderwidth=5)
    cipher_textbox2.grid(row=13,column=18,columnspan=5)

    b12 = Button(root,text="Cipher",command=cipher_polybus,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    b12.grid(row=15,column=18,columnspan=2)
    b22 = Button(root,text="Decipher",command=decipher_polybus,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    b22.grid(row=15,column=21,columnspan=2)    

    # padding
    l = Label(root,text="",padx=50)
    l.grid(row=0,column=24)

    # save and load
    b12_save = Button(root,text="Save Plain",command=polybus_save_plaintext)
    b12_save.grid(row=20,column=18)

    b12_load = Button(root,text="Load Plain",command=polybus_load_plaintext)
    b12_load.grid(row=20,column=21)

    b22_save = Button(root,text="Save Cipher",command=polybus_save_ciphertext)
    b22_save.grid(row=21,column=18)

    b22_load = Button(root,text="Load Cipher",command=polybus_load_ciphertext)
    b22_load.grid(row=21,column=21)

    # rezolvare tema
    tema_label = Label(root,text="Rezolvare Tema",font=('times', 20, 'bold'))
    tema_label.grid(row=0,column=32,columnspan=10,padx=20,pady=10)

    global r 
    r = IntVar()
    r.set(1)

    r1 = Radiobutton(root,text="Criptare",variable=r,value=1,font=('times', 15, 'bold'),padx=10)
    r1.grid(row=9,column=32,columnspan=5)
    r2 = Radiobutton(root,text="Decriptare",variable=r,value=2,font=('times', 15, 'bold'))
    r2.grid(row=9,column=37,columnspan=5)

    l = Label(root,text="Fisier input:")
    l.grid(row=11,column=32)

    global file_in
    file_in = Entry(root,borderwidth=5)
    file_in.grid(row=11,column=33,columnspan=7)

    fb1 = Button(root,text="Browse",command=load_file,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    fb1.grid(row=11,column=40,columnspan=2)
    
    fb2 = Button(root,text="Save",command=save_file,fg="#ff00ff",bg="#ffff00",font=('times', 15, 'bold'))
    fb2.grid(row=15,column=34,columnspan=3)



def load_file():
    file_in.delete(0,END)
    file_in.insert(0, filedialog.askopenfilename())

def save_file():
    f =filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return

    file_path = file_in.get()
    global r
    with open(file_path,'r') as g:
        my_str = g.readlines()
        # criptare
        if r.get() == 1:
            # inserez textul citit din fisier in plain_textbox cezar
            plain_textbox.delete(0,END)
            plain_textbox.insert(0,my_str)

            # criptez textul (cezar)
            do_cipher()

            # incarc output-ul in plain_textbox2 polybus
            plain_textbox2.delete(0,END)
            plain_textbox2.insert(0,cipher_textbox.get())

            # aplic criptarea (polybus)
            cipher_polybus()

            # scriu output-ul in fisier
            f.write(cipher_textbox2.get())
        
        # decriptare
        if r.get() == 2:
            # inserez textul citit din fisier in cipher_texbox2 polybus
            cipher_textbox2.delete(0,END)
            cipher_textbox2.insert(0,my_str)

            # decriptez textul
            plain_textbox2.delete(0,END)
            decipher_polybus()

            # incarc output-ul in cipher_textbox cezar
            cipher_textbox.delete(0,END)
            cipher_textbox.insert(0,plain_textbox2.get())

            # decriptez textul (cezar)
            do_decipher()

            # scriu output-ul in fisier
            f.write(plain_textbox.get())

        f.close()


def do_stuff():
    global root
    setup()
    root.mainloop()


do_stuff()