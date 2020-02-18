from tkinter import*
import random
alphabet={'.- ':'a','-... ':'b','-.-. ':'c','-.. ':'d','. ':'e',
          '..-. ':'f','--. ':'g','.... ':'h','.. ':'i','.--- ':'j',
          '-.- ':'k','.-.. ':'l','-- ':'m','-. ':'n','--- ':'o',
          '.--. ':'p','--.- ':'q','.-. ':'r','... ':'s','- ':'t',
          '..- ':'u','...- ':'v','.-- ':'w','-..- ':'x','-.-- ':'y',
          '--.. ':'z',' ':' ','.---- ':'1','..--- ':'2','...-- ':'3','....- ':'4','..... ':'5',
          '-.... ':'6','--... ':'7','---.. ':'8','----. ':'9','----- ':'0','.-.-.- ':'.','--..-- ':',','..--.. ':'?'}
Alphabet={'.- ':['a','A'],'-... ':['b','B'],'-.-. ':['c','C'],'-.. ':['d','D'],'. ':['e','E'],
          '..-. ':['f','F'],'--. ':['g','G'],'.... ':['h','H'],'.. ':['i','I'],'.--- ':['j','J'],
          '-.- ':['k','K'],'.-.. ':['l','L'],'-- ':['m','M'],'-. ':['n','N'],'--- ':['o','O'],
          '.--. ':['p','P'],'--.- ':['q','Q'],'.-. ':['r','R'],'... ':['s','S'],'- ':['t','T'],
          '..- ':['u','U'],'...- ':['v','V'],'.-- ':['w','W'],'-..- ':['x','X'],'-.-- ':['y','Y'],
          '--.. ':['z','Z'],'.---- ':'1','..--- ':'2','...-- ':'3','....- ':'4','..... ':'5',
          '-.... ':'6','--... ':'7','---.. ':'8','----. ':'9','----- ':'0','.-.-.- ':'.','--..-- ':',','..--.. ':'?'}
 #tkinter root
root = Tk()
root.title('MORSE CODE                   -KKK')
root.minsize(650,800)

#here the coding script ends
#here the play script starts
  #here the guessing letter code starts
def destroy_play():
    play1.destroy(),play2.destroy(),play_back.destroy()
def guessing_letter():
    destroy_play()
    a=list()
    for i in alphabet:
      a.append(i)
    global code_list
    code_list=''
    global decoded_list
    decoded_list=''
    #times=int(input('how many letters:'))
    for i in range (1):
        b=random.choice(a)
        if b !=' ':
            code_list+=b
            decoded_list+=alphabet[b]

    global letter_lab
    letter_lab=Label(root,text=code_list)
    letter_lab.grid(row=2,column=1)
    letter_lab.config(font=("courier",24),fg='black',bg='white',padx=15,pady=10)
    global letter_entry
    letter_entry=Entry(root,width=25)
    letter_entry.grid(row=3,column=1)
    
    global submit_letter
    submit_letter=Button(root,text="Submit",command=code_submit)
    submit_letter.grid(row=4,column=1,pady=10,padx=10)
    global next_button
    next_button=Button(root,text="Next",command=next_code)
    next_button.grid(row=4,column=2,pady=10,padx=10)
    global back_play1
    back_play1=Button(root,text="Back",command=play1_back)
    back_play1.grid(row=5,column=2,pady=10,padx=10)
def play1_back():
    dest_play1()
    create_play()
def code_submit():
    ans_destroy()
    #global score1
    #score1=Label(root,text='score')
    #score1.config(font=("courier",24),fg='red',bg='white',padx=15,pady=10)
    #ans_letter.config(font=("courier",24),fg='blue',bg='white',padx=15,pady=10)
    #ans_letter.grid(row=5,column=1)
    global guess
    guess=str(letter_entry.get())
    #to convert it into lower case
    l_guess=guess.lower()
    #to cut of the gaps
    f_guess = l_guess.strip()
    if f_guess==decoded_list:
        letter_lab.config(font=("courier",24),fg='white',bg='blue',padx=15,pady=10)
    if f_guess != decoded_list:
        letter_lab.config(font=("courier",24),fg='white',bg='red',padx=15,pady=10)
    if f_guess == None:
        None
    global ans_letter
    ans_letter=Label(root,text=decoded_list)
    ans_letter.config(font=("courier",24),fg='blue',bg='white',padx=15,pady=10)
    ans_letter.grid(row=5,column=1)
def ans_destroy():
    try:
        ans_letter.destroy()
    except:
        None
def dest_play1():
    try:
        letter_lab.destroy(),letter_entry.destroy(),submit_letter.destroy(),next_button.destroy(),
        ans_letter.destroy(),back_play1.destroy()
    except:
        letter_lab.destroy(),letter_entry.destroy(),submit_letter.destroy(),next_button.destroy(),back_play1.destroy()
def next_code():
    dest_play1()
    guessing_letter()

def dest_play2():
    try:
      back_play2.destroy(),code_lab.destroy(),code_entry.destroy(),next_button2.destroy(),ans_code.destroy(),submit_code.destroy()
    except:
      back_play2.destroy(),code_lab.destroy(),code_entry.destroy(),next_button2.destroy(),submit_code.destroy()
def play2_back():
    dest_play2()
    create_play()
def guessing_code():
    destroy_play()
    a=list()
    for i in alphabet:
      a.append(i)
    global letter_list
    letter_list=''
    global coded_list
    coded_list=''
    #times=int(input('how many letters:'))
    for i in range (1):
        b=random.choice(a)
        if b !=' ':
            coded_list+=b
            letter_list+=alphabet[b]

    global code_lab
    code_lab=Label(root,text=letter_list)
    code_lab.grid(row=2,column=1)
    code_lab.config(font=("courier",24),fg='black',bg='white',padx=15,pady=10)
    global code_entry
    code_entry=Entry(root,width=25)
    code_entry.grid(row=3,column=1)
    
    global submit_code
    submit_code=Button(root,text="Submit",command=letter_submit)
    submit_code.grid(row=4,column=1,pady=10,padx=10)
    global next_button2
    next_button2=Button(root,text="Next",command=next_letter)
    next_button2.grid(row=4,column=2,pady=10,padx=10) 
    global back_play2
    back_play2=Button(root,text="Back",command=play2_back)
    back_play2.grid(row=5,column=2,pady=10,padx=10)
    
def letter_submit():
    ans_letter_destroy()
    global guess2
    guess2=str(code_entry.get())
    #to cut of the gaps
    f_guess2 = guess2.strip()
    f_guess2+=' '
    if f_guess2==coded_list:
        code_lab.config(font=("courier",24),fg='black',bg='blue',padx=15,pady=10)
    if f_guess2 != coded_list:
        code_lab.config(font=("courier",24),fg='white',bg='red',padx=15,pady=10)
    if f_guess2 == None:
        None   
    global ans_code
    ans_code=Label(root,text=coded_list)
    ans_code.config(font=("courier",24),fg='blue',bg='white',padx=15,pady=10)
    ans_code.grid(row=5,column=1)
def ans_letter_destroy():
    try:
        ans_code.destroy()
    except:
        None
def next_letter():
    dest_play2()
    guessing_code()


# code for decoding the morse code starsts herex
def create():
    global code
    code=Button(root,text="CODE",padx=50,pady=25,command=coding_fuction)#here pady is for spacing of the widgets
    global decode
    decode=Button(root,text="DECODE",padx=42,pady=25,command=decoding_function)
    global play
    play=Button(root,text="PLAY",padx=50,pady=25,command=create_play)
    
    code.grid(row=2,column=1,pady=20)
    decode.grid(row=3,column=1,pady=20)
    play.grid(row=4,column=1,pady=20)
def destroy():
    code.destroy(),decode.destroy(),play.destroy()
def destroy_play():
    play1.destroy(),play2.destroy(),play_back.destroy()
  #play button script
def create_play():
    destroy()
    global play1
    play1=Button(root,text='Guessing the letters',command=guessing_letter)
    play1.grid(row=2,column=1,pady=20,padx=20)
    global play2
    play2=Button(root,text='Guessing the code',command=guessing_code)
    play2.grid(row=3,column=1,pady=20,padx=20)
    global play_back
    play_back=Button(root,text='Back',command=back_play)
    play_back.grid(row=4,column=2,pady=20,padx=20)
#def click_play():
#    create_play()
def back_play():
    destroy_play()
    create()
def guess_letter():
    destroy_play()
    
    a = list()
    for i in alphabet:
        a.append(i)

def undestroy_decode():
    try:
        lab.destroy(),e.destroy(),sub.destroy(),back_decode.destroy(),decoded_answer.destroy(),clear_decode.destroy()
    except:
        lab.destroy(),e.destroy(),sub.destroy(),back_decode.destroy(),clear_decode.destroy()
    create()
def undestroy_code():
    try:
        lab2.destroy(),E.destroy(),clearer.destroy(),sub2.destroy(),coded_letter.destroy(),back_code.destroy()
    except:
        lab2.destroy(),E.destroy(),clearer.destroy(),sub2.destroy(),back_code.destroy()
    create()
def decoding_function():
    destroy()
    global lab
    lab=Label(root,text="CODE: ")
    lab.grid(row=2,column=0)
    global e
    e=Entry(root,width=25)
    
    e.grid(row=2,column=1,padx=5,pady=10)   
     #submit button
     #creation and showing
    global sub
    sub=Button(root,text="submit",command=submit_button)
    sub.grid(column=1,row=3)
    global back_decode
    back_decode=Button(root,text="Back",command=undestroy_decode)
    back_decode.grid(column=1,row=5)
    global clear_decode
    clear_decode=Button(root,text='Clear',command=decode_clearer)
    clear_decode.grid(column=2,row=3)
def submit_button():
    try:
        decode_clearer()
        submitting_code()
    except:
        submitting_code()
def submitting_code():
    code_get=e.get()
    y=list(str(code_get))
    y.append(' ')
    word=list()
    letter=''
    decoded=list()
    #for creating the list of letters
    for i in y:
        if i != ' ':
            letter+=i
        if i == ' ':
            letter+=' '
            word.append(letter)
            del letter
            letter=''
           #decoding
    for char in word:
        for l in alphabet:
            if char == l:
                decoded.append(alphabet[l])
    final=''
    for alp in decoded:
        final += alp
    global decoded_answer
    decoded_answer=Label(root,text=final)
    decoded_answer.config(font=("courier",24),fg='black',bg='white',padx=15,pady=10)
    decoded_answer.grid(row=4,column=1)

#till this submitting is defined   
#decoding script end's here

#coding script starts here
def code_clearer():
    try:
        coded_letter.destroy()
    except:
        None
def decode_clearer():
    try:
        decoded_answer.destroy()
    except:
        None      
def coding_fuction():
    destroy()
    global lab2
    lab2=Label(root,text="Sentence :")
    lab2.grid(row=2,column=0)
    global E
    E=Entry(root,width=25)
    
    E.grid(row=2,column=1,padx=5,pady=10)
    global sub2
    sub2=Button(root,text="submit",command=submitting_sentence)
    sub2.grid(column=1,row=3)
    global clearer
    clearer=Button(root,text="clear",command=code_clearer)
    clearer.grid(column=2,row=2)
    global back_code
    back_code=Button(root,text="Back",command=undestroy_code)
    back_code.grid(column=1,row=5)

#here the submitting funtion

def submitting_sentence():
    global coded_letter
    try:
        coded_letter.destroy()
    except:
        None
    code_get =E.get()
    y=tuple(code_get)
    final=list()
    for i in y:
        if i ==' ':
            final.append(' ')
        for char in Alphabet:
            for letter in Alphabet[char]:
                if i == letter:
                    final.append(char)
    coded=''
    for charecter in final:
        coded+=charecter
    
    coded_letter=Label(root,text=coded)
    coded_letter.config(font=("courier",24),fg='black',bg='white',padx=15,pady=10)
    coded_letter.grid(row=4,column=1)

#object creation
space=Label(root,text="    MORSE CODE")
space.config(font=("courier",44),fg='blue',padx=15,pady=10)

code=Button(root,text="CODE",padx=50,pady=25,command=coding_fuction) #here pady is for spacing of the widgets

decode=Button(root,text="DECODE",padx=42,pady=25,command=decoding_function)

play=Button(root,text="PLAY",padx=50,pady=25,command=create_play)








#object showing or object function
space.grid(row=1,column=0,columnspan=3)
code.grid(row=2,column=1,pady=20)
decode.grid(row=3,column=1,pady=20)
play.grid(row=4,column=1,pady=20)










root.mainloop()







































