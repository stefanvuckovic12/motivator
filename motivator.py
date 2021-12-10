import random
import tkinter as tk
from tkinter import *






root= Tk()

root.geometry("400x200")
root.title("Motivator")
root.configure(bg='orange')
root.resizable(False, False)




def popupBonus():
    messages = ['Sve uvek deluje nemoguće, dok to ne uradite.','Čak i ako padnete na lice, i dalje idete unapred.','Dobro urađeno’ je mnogo bolje od ‘dobro rečeno.','Uvek je prerano za odustajanje','Samo napred i to odmah. Budućnost nikome nije obećana.','Pronaći ćete granice samo ako ih budete prelazili.','Mudar radi jednom ono što budala uradi poslednje.',''
                                                                                                                                                                                                                                                                                                                                                                        'Ne gledajte na sat. Činite ono što i sat čini- nastavite da radite',
                'Ne gledajte na sat. Činite ono što i sat čini- nastavite da radite',
                'Korak po korak i stvar je gotova.',
                'Iznova i iznova doživljavao sam neuspehe. Baš zato sam i uspeo.',
                'Tajna napretka krije se u tome da počnete.',
                'Ukoliko možete da sanjate o tome, možete to i da uradite.',
                'Radite kao da ono što činite pravi razliku. Jer je zaista tako.',
                'Radije ću pokušati da uradim nešto sjajno i da doživim poraz, nego da ne radim ništa i uspem u tome.',
                'Vaša sopstvena odluka da uspete bitnija je od bilo čije druge.',
                'Ono što učinite danas, može da popravi sve sutrašnje dane.',
                'Uvek ima mesta na vrhu.',
                'Reputacija se ne gradi na osnovu onoga što ćete uraditi.',
                'Pre ili kasnije pobeđuje onaj koji misli da može.',
                'Ne čekajte da se stvari dese same od sebe, već preuzmite korake.',
                'Ponekad kasnije nikada ne dođe. Uradite to sada.',
                'Gde postoji volja, postoji i način.',
                'Gurajte sebe, jer niko drugi to neće učiniti za Vas.',
                'Odlučio sam da budem srećan jer je to dobro za moje zdravlje.',
                'Održavati dobro zdravlje tela je Vaša obaveza. U suprotnom, nećete moći da održite um snažnim i bistrim.',
                'Svaki dan je novi početak.',
                'Ti si divno, jedinstveno stvorenje i tebe je lako voleti.',
                'Ti to možeš.',
                'Niko još nije naučio da vozi biciklu, a da nije pao.',
                'Ako potrošite previše vremena razmišljajući o nečemu, to nikada nećete uraditi.',
                'Uspeh se sastoji od prelaska sa jednog neuspeha na drugi bez gubljenja entuzijazma.',
                'Budućnost zavisi od onoga što radite danas.',
                'Otkrijte šta radite najbolje i pronađite nekoga da Vas za to plati.',
                'Postavite takav cilj da želite ujutru da iskočite iz kreveta da biste ga ostvarili.',
                'Nikada više nećete imati ovaj dan i zato ga učinite vrednim.',
                'Ne morate biti sjajni da biste počeli, ali morate početi da biste bili sjajni.',
                'Život je 10% ono što nam se dešava i 90% ono kako mi reagujemo na to.',
                'Kada pomislite da je život težak, zapitajte se šta birate kao poređenje.',
                'U sebi možete pronaći ili najvećeg prijatelja ili najvećeg neprijatelja.',
                'Ne hodajte na prstima, već čvrsto gazite kroz život.',
                'Da biste bili srećni upamtite da Vaša sreća ne zavisi od drugih.',
                'Sanjajte kao da ćete živeti večno i živite kao da ćete umreti sutra.',
                'Budite zadovoljni onim što imate. Budite uzbuđeni zbog onoga što želite.',
                'Ne možete suditi o onome što bi drugima trebalo da donosi sreću, kao što drugi ne mogu da procene šta bi moglo da usreći Vas.',
                ]

    message = (random.choice(messages))
    popupBonusWindow = tk.Tk()
    popupBonusWindow.resizable(False,False)
    popupBonusWindow.wm_title("Poruka!")
    colors=('light blue','#E666A8','cyan','#47B96D','#E1FE0D','#F89999','#C970C0')
    color= (random.choice(colors))
    labelBonus = Label(popupBonusWindow, text=message, font=('Cabeza Grossa',24,'bold'), bg=color )
    labelBonus.grid(row=0, column=0)




Label(root,text="Motiviši se!", font=("Modern No. 20",25,"bold"),bg='orange').grid(row=0, column=0, columnspan=1, padx=115)
p=Button(root, text="Klikni me", font=("Modern No. 20",15),bg='cyan',command=popupBonus)
p.grid(row=1,column=0,columnspan=2,padx=5,pady=15)

e=Button(root,text="Izađi",  font=("Modern No. 20",10),bg='light yellow',command= quit)
e.grid(row=10,column=0, pady=60)



root.mainloop()