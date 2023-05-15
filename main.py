import tkinter
import customtkinter
import webbrowser




customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500x300")
root.title("Boost Bot")



def login():

    def boost_window():
        main.destroy()
        boost = customtkinter.CTk()
        boost.geometry('250x250')
        boost.title("Boost settings")
        tabview = customtkinter.CTkTabview(master=boost)
        tabview.pack(padx=20, pady=20)

        tabview.add("Settings")
        tabview.set("Settings")


        def start_boost():
            #add your boost start now
            boost.destroy()

        entry = customtkinter.CTkEntry(master=tabview.tab("Settings"), placeholder_text="anzhl boosts")
        entry.pack(fill="x")

        buttonstartboost_1 = customtkinter.CTkButton(master=tabview.tab("Settings"), text="Start Boost", width=200, command=start_boost)
        buttonstartboost_1.pack(pady=20)


        boost.mainloop()
    root.destroy()
    main=customtkinter.CTk()
    main.geometry('750x450')
    main.title("Boost Bot")
    tabview = customtkinter.CTkTabview(master=main)
    tabview.pack(padx=20, pady=20)

    tabview.add("Start Boost")
    tabview.add("View Stock")
    tabview.add("Clear Stock")
    tabview.add("Credits")
    
    tabview.set("Start Boost")  # set currently visible tab



    def add_todo():
        todo = entry.get()
        label42 = customtkinter.CTkLabel(scrollable_frame, text=todo)
        label42.pack()
        button = customtkinter.CTkButton(scrollable_frame, text="Boost", command=boost_window)
        button.pack(pady=0, padx=5)
        entry.delete(0, customtkinter.END)



    scrollable_frame = customtkinter.CTkScrollableFrame(master=tabview.tab("Start Boost"), width=200, height=200)
    scrollable_frame.pack()



    FileCreatorButton = customtkinter.CTkButton(master=tabview.tab("Clear Stock"), text="clear stock", width=200)
    FileCreatorButton.pack(pady=20)

    entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text="discord invite hier")
    entry.pack(fill="x")

    addbutton = customtkinter.CTkButton(master=tabview.tab("Start Boost"), text="add to List", width=200, command=add_todo)
    addbutton.pack(pady=20)

    labensoon = customtkinter.CTkLabel(master=tabview.tab("View Stock"), text="Stock View")
    labensoon.pack(pady=12, padx=10)


    labencredit = customtkinter.CTkLabel(master=tabview.tab("Credits"), text="Programmed by bane02#0001")
    labencredit.pack(pady=12, padx=10)

    def github_link():
        webbrowser.open('https://github.com/BaneQuadrat')


    creditbutton = customtkinter.CTkButton(master=tabview.tab("Credits"), text="Github", width=200, command=github_link)
    creditbutton.pack(pady=20)


    main.mainloop()






frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry1.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)





root.mainloop()

























#DONT LEAK CODE












