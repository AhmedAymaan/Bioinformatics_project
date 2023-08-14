from tkinter import *
from tkinter import filedialog, messagebox
from Bio import SeqIO
window =Tk()
global req_id
#window['background']='#232023'
def fun():
    win=Tk()
    win.geometry("500x500")
    def fileDialog():
        global filepath
        filepath=filedialog.askopenfilename(initialdir="/",title='data_set', filetypes=(("Exel file",".fasta"), ("All files",".*")))
       # file= open(filepath,'r')
        l = Label(win, text='')
        l.place(x=150,y=130)
        l.configure(text=filepath)
        #v= file.read()
        #print(v)
    def show_Data():
        global sequences,seq_id
        sequences=[]
        record=SeqIO.parse(filepath,"fasta")
        for rec in record:
            sequences.append(rec)
        print(len(sequences))
        for seq in sequences:
            print(seq.id)
        seq_id=[]
        for seq in sequences:
            seq_id.append(seq.id)
        messagebox.showinfo('DATA',sequences)
    def show():
        win2 = Tk()
        win2.geometry("400x400")
        win2.title("ID/Name")
        l2 = Label(win2, text="Enter ID/Name")
        l2.place(x=5, y=10)
        en = Entry(win2)
        en.place(x=100, y=10)
        def valu():
            global value, seq,result
            value = en.get()
            if (value == ''):
                messagebox.showinfo("Error", "enter id")
            # file=value
            # with open((file + 'txt'), 'a') as f:
            #     f.write(file)
            for seq in sequences:
                if value == seq.id or value == seq.name :
                    result=True
                    print(value)
                    print('-----------')
                    print(seq.name)
                    messagebox.showinfo("sequences",seq.seq)




            #GC(value)
            #print(gc_fraction(value))
            #print(GC(value))
           # print(value.complement())     ## complement
            #print(value.reverse_complement()) ##reversr complement
            #print(value.reverse_complement().transcribe()) ##rna
        def reverse():
            value=en.get()
            if (value == ''):
                messagebox.showinfo("Error", "enter id")
            for seqq in sequences:
                if value == seqq.id:
                    value=seqq.seq
            print(value.reverse_complement())
            messagebox.showinfo("reverse sequences",value.reverse_complement())
        def gc():
            value = en.get()
            if (value == ''):
                messagebox.showinfo("Error", "enter id")
            for seqq in sequences:
                if value == seqq.id:
                    value = seqq.seq
            GC = (value.count('G') + value.count('C')) * 100 / len(value)
            if GC == 100.0000:
                print('the  value is: %.3f ' % (GC));
                messagebox.showinfo('GC',GC)
            elif GC == 0.0000:
                print('the  value is: %.5f ' % (GC));
                messagebox.showinfo('GC',GC)
            else:
                print('the  value is: %.4f ' % (GC));
                messagebox.showinfo('GC',GC)
        def rna():
            value = en.get()
            if (value == ''):
                messagebox.showinfo("Error", "enter id")
            for seqq in sequences:
                if value == seqq.id:
                    value = seqq.seq
                    print(value.transcribe())
            messagebox.showinfo("RNA",value.transcribe())
        b3=Button(win2,text="sequences", cursor='hand2', width=15, bg="#7bbefa", fg="black", command=valu)
        b3.place(x=150,y=100)
        b4 = Button(win2, text="reverse", cursor='hand2', width=15, bg="#7bbefa", fg="black", command=reverse)
        b4.place(x=150,y=150)
        b5 = Button(win2, text="GC", cursor='hand2', width=15, bg="#7bbefa", fg="black", command=gc)
        b5.place(x=150,y=200)
        b5 = Button(win2, text="rna", cursor='hand2', width=15, bg="#7bbefa", fg="black", command=rna)
        b5.place(x=150, y=250)
        win2.mainloop()
    b = Button(win, text="Browse Data", cursor='hand2', width=15, bg="black", fg="white", command=fileDialog)
    b.place(x=200,y=100)
    b2 = Button(win, text="show Data", cursor='hand2', width=15, bg="#F4C2C2", fg="black", command=show_Data)
    b2.place(x=100,y=350)
    b1 = Button(win, text="show", width=15, cursor='hand2', bg="#F4C2C2", fg="black", command=show)
    b1.place(x=300,y=350)
    win.mainloop()
l=Label(window,text="Esraa Ibrahim",fg="black",pady=10,padx=30).place(x=190,y=430)
l=Label(window,text="Mariam Mahfouz",fg="black",pady=10,padx=30).place(x=10,y=430)
l=Label(window,text="Ahmed Aymen",fg="black",pady=10,padx=30).place(x=340,y=430)
#l=Label(window,text="Mariam Mahfouz",bg='black',fg="white",pady=10,padx=30).pack()
#L=Label(window,text="Esraa Ibrahim",bg='black',fg="white",pady=10,padx=30).pack(side=LEFT)
#l=Label(window,text="Ahmed Aymen",bg='black',fg="white",pady=10,padx=30).pack(side=RIGHT)#4040E0  #C0C0FF
b = Button(window,text="start", cursor='hand2',bd=2,fg="black",bg='#F4C2C2',command=fun,font=100 ,padx=50,pady=10)
b.place(x=170,y=100)
window.title("bio Bython")
window.geometry("500x500+500+100")
window.mainloop()