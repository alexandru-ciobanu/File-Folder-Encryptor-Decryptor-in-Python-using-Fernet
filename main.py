from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog
import cryptography
import os
from cryptography.fernet import Fernet, InvalidToken
from tkinter import messagebox
import glob

def file_encryptor():
    def crypth(file, key_f):
        
        input_file = file
        output_file = f"{file}.lol"
        
        with open(key_f, 'rb') as key_file:
            key = key_file.read()  
            key_file.close()

        with open(input_file, 'rb') as f:
            data = f.read()  

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)  
            
        os.remove(input_file)
        showinfo("Crypth", "File Encrypthed!")
        
        
        
    def open_file():
        window.filename = filedialog.askopenfilename(title="File 2 Crypth")
        file_insert.delete(0,"end")
        file_insert.insert(0, window.filename)



    def open_key():
        window.filename = filedialog.askopenfilename(title="File of the key")
        key_insert.delete(0,"end")
        key_insert.insert(0, window.filename)
        


        

        
    def key_wind():
        
        def open_dir_key():
            key_window.filename = filedialog.askdirectory(title="Directory for create the key file")
            file_dir.delete(0,"end")
            file_dir.insert(0, key_window.filename)
            
            
        def write_key_file(location_file):
        
            
            key = Fernet.generate_key()
            with open(f"{location_file}.key", "wb") as key_file:
                key_file.write(key)
                showinfo(f"Generate Key", "Key file generated!")
                
        def generate_key_file():
            
        
            name_file = file_name.get()
        
            if "." in name_file:
                name_file = name_file[:name_file.find(".")]
            
            directory = file_dir.get()
            
            if name_file == "File Name" or directory == "File Dir" or name_file == "" or directory == "":
                messagebox.showerror("Scemetto", "Completa tutti i campi!")
            
            location_file = directory + "/" + name_file
            
            
            print(location_file)
            write_key_file(location_file)
            
            file_name.delete(0,"end")
            file_name.delete(0,"end")
            key_insert.insert(0, "File To Encrypth")
            key_insert.insert(0, "Key File")
            
        key_window = Toplevel()
        key_window.geometry("235x150")
        key_window.iconbitmap("chiuso.ico")
        key_window.title("Key Gen - Cioba")
        key_window.resizable(False, False)
        
        titolo_gen_key = Label(key_window, text="Key Generator")
        titolo_gen_key.grid(pady=20, row=0, column=6)
        
        file_name = Entry(key_window, width=30)
        file_name.insert(0, "File Name")
        file_name.grid(row=3, column=6)
        
        file_dir = Entry(key_window, width=30)
        file_dir.insert(0, "File Dir")
        file_dir.grid(row=4, column=6)
        
        browse_dir = Button(key_window, text="browse",   command=open_dir_key)
        browse_dir.grid(row=4, column=7)
        
        generate = Button(key_window, text="Generate", command=generate_key_file)
        generate.grid(row=5, column=6)
        
        

    window = Toplevel()
    window.title("File Encryptor - Cioba")
    window.iconbitmap("chiuso.ico") #icona
    window.geometry("400x220")
    window.resizable(False, False)


    titolo = Label(window, text="File Encryptor", )
    titolo.grid(pady=20, row=0, column=6)

    file_insert = Entry(window, width=30)
    file_insert.insert(0, "File To Encrypth")
    file_insert.grid(row=3, column=6)





    label_clear = Label(window, text="", ).grid(row=3, column=4)



    browse_file = Button(window, text="browse",   command=open_file)
    browse_file.grid(row=3, column=7)



    key_insert = Entry(window, width=30)
    key_insert.insert(0, "Key File")
    key_insert.grid(row=4, column=6)


    browse_key = Button(window, text="browse",  command=open_key)
    browse_key.grid(row=4, column=7)

    def bottone():
        
        file = file_insert.get()
        key_f = key_insert.get()
        
        if key_f == "Key File" or file == "File To Encrypth" or key_f == "" or file == "":
            messagebox.showerror("Scemetto", "Completa tutti i campi!")
        
        crypth(file, key_f)
        file_insert.delete(0,"end")
        key_insert.delete(0,"end")
        file_insert.insert(0, "File To Encrypth")
        key_insert.insert(0, "Key File")
        

    button = Button(window, text="Encrypt", command=bottone)
    button.grid(row=5, column=6)





    gen_key_button = Button(window, text="Generate Key", command=key_wind)
    gen_key_button.grid(row=7, column=0)
    
def file_decryptor():
    def decrypt(file, key_f):
    
        input_file = file
        output_file =  input_file.replace('.lol','')
        
        with open(key_f, 'rb') as key_file:
            key = key_file.read()  # The key will be type bytes
            key_file.close()


        with open(input_file, 'rb') as f:
            data = f.read()  # Read the bytes of the encrypted file

        fernet = Fernet(key)
        try:
            decrypted = fernet.decrypt(data)

            with open(output_file, 'wb') as f:
                f.write(decrypted)  # Write the decrypted bytes to the output file
                os.remove(input_file)
                showinfo("Decrypt", "File Decrypthed!")
            # Note: You can delete input_file here if you want
        except InvalidToken as e:
            print("Invalid Key - Unsuccessfully decrypted")
        
    def bottone():
        
        file = file_insert.get()
        key_f = key_insert.get()
        
        if key_f == "Key File" or file == "File To Decrypth" or key_f == "" or file == "":
            messagebox.showerror("Scemetto", "Completa tutti i campi!")
        
        decrypt(file, key_f)
        file_insert.delete(0,"end")
        key_insert.delete(0,"end")
        file_insert.insert(0, "File To Decrypth")
        key_insert.insert(0, "Key File")
        
    
    def open_file():
        window.filename = filedialog.askopenfilename(title="File 2 Decrypth")
        file_insert.delete(0,"end")
        file_insert.insert(0, window.filename)

    def open_key():
        window.filename = filedialog.askopenfilename(title="File of the key")
        key_insert.delete(0,"end")
        key_insert.insert(0, window.filename)

    window = Toplevel()
    window.title("File Decryptor - Cioba")
    window.iconbitmap("aperto.ico") #icona
    window.geometry("325x220")
    window.resizable(False, False)


    titolo = Label(window, text="File Decryptor", )
    titolo.grid(pady=20, row=0, column=6)

    file_insert = Entry(window, width=30)
    file_insert.insert(0, "File To Decrypth")
    file_insert.grid(row=3, column=6)

    label_clear = Label(window, text="                ", ).grid(row=3, column=4)

    browse_file = Button(window, text="browse",   command=open_file)
    browse_file.grid(row=3, column=7)

    key_insert = Entry(window, width=30)
    key_insert.insert(0, "Key File")
    key_insert.grid(row=4, column=6)

    browse_key = Button(window, text="browse",  command=open_key)
    browse_key.grid(row=4, column=7)

    button = Button(window, text="Decrypt", command=bottone)
    button.grid(row=5, column=6)

def dir_encryptor():
    
    def crypth(folder_to_crypth, key_f):
        showinfo("Dont close the program","Dont close the program we are crypting your folder")
        for cartella, sottocartella, files in os.walk(folder_to_crypth, topdown=True):
            
            for file in files:
                
                try: 
                    input_file = glob.glob(folder_to_crypth + f"/**/*{file}", recursive = True)
                    input_file = input_file[0]
                    print(input_file)
                
                    output_file = f"{input_file}.lol"
                    
                    
                    with open(key_f, 'rb') as key_file:
                        key = key_file.read()  
                        key_file.close()
                        

                    with open(input_file, 'rb') as f:
                        data = f.read()  
                        

                    fernet = Fernet(key)
                    encrypted = fernet.encrypt(data)

                    with open(output_file, 'wb') as f:
                        f.write(encrypted)  
                        
                        
                    os.remove(input_file)
                
                except:
                    pass
        
        
        showinfo("Crypth", "Dir Encrypthed!")
        
        
        
    def open_file():
        window.filename = filedialog.askdirectory(title="Dir to encrypt")
        dir_insert.delete(0,"end")
        dir_insert.insert(0, window.filename)



    def open_key():
        window.filename = filedialog.askopenfilename(title="File of the key")
        key_insert.delete(0,"end")
        key_insert.insert(0, window.filename)
        


        

        
    def key_wind():
        
        def open_dir_key():
            key_window.filename = filedialog.askdirectory(title="Directory for create the key file")
            file_dir.delete(0,"end")
            file_dir.insert(0, key_window.filename)
            
            
        def write_key_file(location_file):
        
            
            key = Fernet.generate_key()
            with open(f"{location_file}.key", "wb") as key_file:
                key_file.write(key)
                showinfo(f"Generate Key", "Key file generated!")
                
        def generate_key_file():
            
        
            name_file = file_name.get()
        
            if "." in name_file:
                name_file = name_file[:name_file.find(".")]
            
            directory = file_dir.get()
            
            if name_file == "File Name" or directory == "File Dir" or name_file == "" or directory == "":
                messagebox.showerror("Scemetto", "Completa tutti i campi!")
            
            location_file = directory + "/" + name_file
            
            
            print(location_file)
            write_key_file(location_file)
            
            file_name.delete(0,"end")
            file_name.delete(0,"end")
            key_insert.insert(0, "Dir To Encrypth")
            key_insert.insert(0, "Key File")
            
        key_window = Toplevel()
        key_window.geometry("235x150")
        key_window.iconbitmap("chiuso.ico")
        key_window.title("Key Gen - Cioba")
        key_window.resizable(False, False)
        
        titolo_gen_key = Label(key_window, text="Key Generator")
        titolo_gen_key.grid(pady=20, row=0, column=6)
        
        file_name = Entry(key_window, width=30)
        file_name.insert(0, "File Name")
        file_name.grid(row=3, column=6)
        
        file_dir = Entry(key_window, width=30)
        file_dir.insert(0, "File Dir")
        file_dir.grid(row=4, column=6)
        
        browse_dir = Button(key_window, text="browse",   command=open_dir_key)
        browse_dir.grid(row=4, column=7)
        
        generate = Button(key_window, text="Generate", command=generate_key_file)
        generate.grid(row=5, column=6)
        
        

    window = Toplevel()
    window.title("File Encryptor - Cioba")
    window.iconbitmap("chiuso.ico") #icona
    window.geometry("400x220")
    window.resizable(False, False)


    titolo = Label(window, text="Dir Encryptor", )
    titolo.grid(pady=20, row=0, column=6)

    dir_insert = Entry(window, width=30)
    dir_insert.insert(0, "Dir To Encrypth")
    dir_insert.grid(row=3, column=6)





    label_clear = Label(window, text="", ).grid(row=3, column=4)



    browse_file = Button(window, text="browse",   command=open_file)
    browse_file.grid(row=3, column=7)



    key_insert = Entry(window, width=30)
    key_insert.insert(0, "Key File")
    key_insert.grid(row=4, column=6)


    browse_key = Button(window, text="browse",  command=open_key)
    browse_key.grid(row=4, column=7)

    def bottone():
        
        dir_to_encrypt = dir_insert.get()
        key_f = key_insert.get()
        
        if key_f == "Key File" or dir_to_encrypt == "Dir To Encrypth" or key_f == "" or dir_to_encrypt == "":
            messagebox.showerror("Scemetto", "Completa tutti i campi!")
        
        crypth(dir_to_encrypt, key_f)
        dir_insert.delete(0,"end")
        key_insert.delete(0,"end")
        dir_insert.insert(0, "dir_to_encrypt")
        key_insert.insert(0, "Key File")
        

    button = Button(window, text="Encrypt", command=bottone)
    button.grid(row=5, column=6)





    gen_key_button = Button(window, text="Generate Key", command=key_wind)
    gen_key_button.grid(row=7, column=0)

def dir_decryptor():
    def decrypth(folder_to_decrypth, key_f):
        
        showinfo("Dont close the program","Dont close the program we are decrypting your folder")
        for cartella, sottocartella, files in os.walk(folder_to_decrypth, topdown=True):
            
            for file in files:
                
                try: 
                    input_file = glob.glob(folder_to_decrypth + f"/**/*{file}", recursive = True)
                    
                    input_file = input_file[0]
                    print(f"decrypting:  {input_file}")
                
                    output_file =  input_file.replace('.lol','')
                    
                    
                    with open(key_f, 'rb') as key_file:
                        key = key_file.read()  # The key will be type bytes
                        key_file.close()


                    with open(input_file, 'rb') as f:
                        data = f.read()  # Read the bytes of the encrypted file

                    fernet = Fernet(key)
                    try:
                        decrypted = fernet.decrypt(data)

                        with open(output_file, 'wb') as f:
                            f.write(decrypted)  # Write the decrypted bytes to the output file
                            os.remove(input_file)
                            
                        # Note: You can delete input_file here if you want
                    except InvalidToken as e:
                        showerror("Error",f"Invalid Key - File {input_file} unsuccessfully decrypted")

                except:
                    pass
                        
                    
                
        
        
        showinfo("Decrypth", "Dir Decrypthed!")
        
        
        
    def open_file():
        window.filename = filedialog.askdirectory(title="Dir to decrypt")
        dir_insert.delete(0,"end")
        dir_insert.insert(0, window.filename)



    def open_key():
        window.filename = filedialog.askopenfilename(title="File of the key")
        key_insert.delete(0,"end")
        key_insert.insert(0, window.filename)
        


        

        
    def key_wind():
        
        def open_dir_key():
            key_window.filename = filedialog.askdirectory(title="Directory for create the key file")
            file_dir.delete(0,"end")
            file_dir.insert(0, key_window.filename)
            
            
        def write_key_file(location_file):
        
            
            key = Fernet.generate_key()
            with open(f"{location_file}.key", "wb") as key_file:
                key_file.write(key)
                showinfo(f"Generate Key", "Key file generated!")
                
        def generate_key_file():
            
        
            name_file = file_name.get()
        
            if "." in name_file:
                name_file = name_file[:name_file.find(".")]
            
            directory = file_dir.get()
            
            if name_file == "File Name" or directory == "File Dir" or name_file == "" or directory == "":
                messagebox.showerror("Scemetto", "Completa tutti i campi!")
            
            location_file = directory + "/" + name_file
            
            
            print(location_file)
            write_key_file(location_file)
            
            file_name.delete(0,"end")
            file_name.delete(0,"end")
            key_insert.insert(0, "Dir To Encrypth")
            key_insert.insert(0, "Key File")
            
        key_window = Toplevel()
        key_window.geometry("235x150")
        key_window.iconbitmap("chiuso.ico")
        key_window.title("Key Gen - Cioba")
        key_window.resizable(False, False)
        
        titolo_gen_key = Label(key_window, text="Key Generator")
        titolo_gen_key.grid(pady=20, row=0, column=6)
        
        file_name = Entry(key_window, width=30)
        file_name.insert(0, "File Name")
        file_name.grid(row=3, column=6)
        
        file_dir = Entry(key_window, width=30)
        file_dir.insert(0, "File Dir")
        file_dir.grid(row=4, column=6)
        
        browse_dir = Button(key_window, text="browse",   command=open_dir_key)
        browse_dir.grid(row=4, column=7)
        
        generate = Button(key_window, text="Generate", command=generate_key_file)
        generate.grid(row=5, column=6)
        
        

    window = Toplevel()
    window.title("Dir Decryptor - Cioba")
    window.iconbitmap("chiuso.ico") #icona
    window.geometry("400x220")
    window.resizable(False, False)


    titolo = Label(window, text="Dir Decryptor", )
    titolo.grid(pady=20, row=0, column=6)

    dir_insert = Entry(window, width=30)
    dir_insert.insert(0, "Dir To Decrypth")
    dir_insert.grid(row=3, column=6)





    label_clear = Label(window, text="", ).grid(row=3, column=4)



    browse_file = Button(window, text="browse",   command=open_file)
    browse_file.grid(row=3, column=7)



    key_insert = Entry(window, width=30)
    key_insert.insert(0, "Key File")
    key_insert.grid(row=4, column=6)


    browse_key = Button(window, text="browse",  command=open_key)
    browse_key.grid(row=4, column=7)

    def bottone():
        
        dir_to_decrypt = dir_insert.get()
        key_f = key_insert.get()
        
        if key_f == "Key File" or dir_to_decrypt == "Dir To Decrypth" or key_f == "" or dir_to_decrypt == "":
            messagebox.showerror("Scemetto", "Completa tutti i campi!")
        
        decrypth(dir_to_decrypt, key_f)
        dir_insert.delete(0,"end")
        key_insert.delete(0,"end")
        dir_insert.insert(0, "dir_to_encrypt")
        key_insert.insert(0, "Key File")
        

    button = Button(window, text="Decrypt", command=bottone)
    button.grid(row=5, column=6)





    gen_key_button = Button(window, text="Generate Key", command=key_wind)
    gen_key_button.grid(row=7, column=0)




    
    

menu = Tk()
menu.title("File Encryptor and Decryptor Menu - Cioba")
menu.iconbitmap("chiuso.ico") 
menu.geometry("200x200")
menu.resizable(False, False)

titolo = Label(menu, text=" Menu \n -Cioba-", )
titolo.grid(pady=25, padx=0, row=0, column=0)

bottone_file_encryptor = Button(menu, width=27, text="File Encryptor", command=file_encryptor)
bottone_file_encryptor.grid()

bottone_file_decryptor = Button(menu,width=27, text="File Decryptor", command=file_decryptor)
bottone_file_decryptor.grid()

bottone_file_decryptor = Button(menu,width=27, text="Dir Encryptor", command=dir_encryptor)
bottone_file_decryptor.grid()

bottone_file_decryptor = Button(menu,width=27, text="Dir Decryptor", command=dir_decryptor)
bottone_file_decryptor.grid()

menu.mainloop()
