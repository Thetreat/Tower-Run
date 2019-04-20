import tkinter as tk
import model.Tower as Tow
import tkinter.ttk as ttk


class Interface(tk.Frame):

    # ____________________________Dico avec pour clé le nom de la tour (méthode spé __str__) et pour valeur elle même______
    dico = {"Mage d'Eau": Tow.WaterM, "Mage de Terre": Tow.EarthM, "Mage de Feu": Tow.FireM, "Archer": Tow.Archer,
            "Mortier": Tow.Mortier, "Forgeron": Tow.Forgeron, "Mine": Tow.Mine}

    selected = None
    last_preview = None
    last_lochoice = None
    moneyCallback = None
    range_preview = None
    spotName = None
    spotZone = None
    spotSpeed = None
    spotDamage = None
    spotDamagetype = None
    spotPrice = None

    def __init__(self, parent, *args, **kwargs):
        self.lochoice = tk.PhotoImage(file="view/src/lochoice.png")
        self.hammerSign = tk.PhotoImage(file="view/src/HammerSign.png")
        self.moneyIcon = tk.PhotoImage(file="view/src/Money - Copie.png")
        self.parent = parent
        self.canvas = parent.canvas

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.v = tk.StringVar()

        self.backImg = tk.PhotoImage(file="view/src/Interface.png")
        self.interface = tk.Canvas(
            self, width=200, height=650, highlightthickness=0)
        self.interface.create_image(0, 0, image=self.backImg, anchor="nw")
        self.makeLabel()
        self.emplacementMake()
        self.interface.pack()

        self.makeButton()

# ___________________________On va faire les check buttons ici max/yann ______________
    def makeButton(self):
        self.waterchb = tk.Radiobutton(self.interface, value="Mage d'Eau", variable=self.v,
                                       bg="#1ea7e1", activebackground="#1ea7e1", highlightthickness=0, command=self.preView)
        self.waterchb.place(x=160, y=23)
        self.earthchb = tk.Radiobutton(self.interface, value="Mage de Terre", variable=self.v,
                                       bg="#73cd4b", activebackground="#73cd4b", highlightthickness=0, command=self.preView)
        self.earthchb.place(x=160, y=81)
        self.firechb = tk.Radiobutton(self.interface, value="Mage de Feu", variable=self.v,
                                      bg="#e86a17", activebackground="#e86a17", highlightthickness=0, command=self.preView)
        self.firechb.place(x=160, y=135)
        self.archerchb = tk.Radiobutton(self.interface, value="Archer", variable=self.v,
                                        bg="#ffcc00", activebackground="#ffcc00", highlightthickness=0, command=self.preView)
        self.archerchb.place(x=160, y=191)
        self.mortierchb = tk.Radiobutton(self.interface, value="Mortier", variable=self.v,
                                         bg="#eeeeee", activebackground="#eeeeee", highlightthickness=0, command=self.preView)
        self.mortierchb.place(x=160, y=246)
        self.forgeronchb = tk.Radiobutton(
            self.interface, value=Tow.Forgeron, text="F", variable=self.v, command=self.preView)
        self.forgeronchb.place(x=160, y=300)

        self.buttonList = [self.forgeronchb, self.waterchb,
                           self.earthchb, self.firechb, self.archerchb, self.mortierchb]

        self.waterchb.select()  # on choisit les mages d'eaux par défaut au début
        self.buildButton = tk.Button(
            self.interface, command=self.buildTower, text="Construire", width=24, state="disabled")
        # self.interface, command=self.buildTower, text="Construire", image=self.buttonImage, state = "disabled")
        self.buildButton.place(x=12, y=585)

    def makeLabel(self):
        self.wallet = tk.Label(
            self.interface, textvariable=self.parent.gold, bg="#743A3A", fg="white")
        self.wallet.place(x=31, y=617)

        self.life = tk.Label(self.interface, textvariable=self.parent.health,
                             bg="#743A3A", fg="white", font=("Arial", 8))
        self.life.place(x=150, y=617)

        self.mageWLabel = tk.Label(
            self.interface, text="50", bg="#1ea7e1", fg="black", font=("Arial", 8))
        self.mageWLabel.place(x=75, y=26)

        self.mageELabel = tk.Label(
            self.interface, text="50", bg="#73cd4b", fg="black", font=("Arial", 8))
        self.mageELabel.place(x=75, y=82)

        self.mageFLabel = tk.Label(
            self.interface, text="50", bg="#e86a17", fg="black", font=("Arial", 8))
        self.mageFLabel.place(x=75, y=137)

        self.archerLabel = tk.Label(
            self.interface, text="50", bg="#ffcc00", fg="black", font=("Arial", 8))
        self.archerLabel.place(x=75, y=192)

        self.mortierLabel = tk.Label(
            self.interface, text="50", bg="#eeeeee", fg="black", font=("Arial", 8))
        self.mortierLabel.place(x=75, y=250)

    def selectSpot(self, event):
        area = 45
        found = False
        for spot in self.parent.spots:
            if spot.x-area < event.x < spot.x+area and spot.y-area < event.y < spot.y+area:

                self.selected = spot
                found = True
                break

        if found != True:
            self.selected = None
        self.preView()

    def preView(self):
        state = ''.join([i for i in self.v.get() if not i.isdigit()])
        for btn in self.buttonList:
            btn["state"] = "normal"
        if self.spotName:
            self.spotName.destroy()
        if self.spotDamage:
            self.spotDamage.destroy()
        if self.spotSpeed:
            self.spotSpeed.destroy()
        if self.spotZone:
            self.spotZone.destroy()
        if self.spotDamagetype:
            self.spotDamagetype.destroy()
        if self.spotPrice:
            self.spotPrice.destroy()

        self.canvas.delete(self.last_lochoice)
        self.canvas.delete(self.range_preview)
        self.interface.delete(self.moneyCallback)

        self.interface.delete(self.last_preview)

        if self.selected:

            self.buildButton["state"] = "normal"

            self.spotName = tk.Label(
                self.interface, text="Nom: ", bg="#743A3A", fg="white")
            self.spotName.place(x=10, y=300)

            self.spotDamage = tk.Label(
                self.interface, text="Dégâts: ", bg="#743A3A", fg="white")
            self.spotZone = tk.Label(
                self.interface, text="Zone de dégâts: ", bg="#743A3A", fg="white")
            self.spotDamagetype = tk.Label(
                self.interface, text="Type: ", bg="#743A3A", fg="white")
            self.spotSpeed = tk.Label(
                self.interface, text="Cadence de tir: ", bg="#743A3A", fg="white")

            self.spotDamage.place(x=10, y=320)
            self.spotZone.place(x=10, y=340)
            self.spotDamagetype.place(x=10, y=360)
            self.spotSpeed.place(x=10, y=380)

            # self.half_range = self.dico[state].range
            # self.range_preview = self.canvas.create_oval(self.selected.x+self.half_range, self.selected.y+self.half_range, self.selected.x - self.half_range, self.selected.y - self.half_range,
            #                                                 outline="blue")

            self.last_lochoice = self.canvas.create_image(
                self.selected.x, self.selected.y-12, image=self.lochoice)
            self.spotPrice = tk.Label(
                self.interface, bg="#743A3A", fg="white", font=("Arial", 18), justify="left")

            self.spotPrice.place(x=105, y=535)
            self.moneyCallback = self.interface.create_image(
                175, 550, image=self.moneyIcon)

            if self.selected.tower:
                for btn in self.buttonList:
                    btn["state"] = "disabled"

                self.buildButton["text"] = "Améliorer"

                self.half_range = self.selected.tower.range
                self.spotDamage.place(x=10, y=320)
                self.spotZone.place(x=10, y=340)
                self.spotDamagetype.place(x=10, y=360)
                self.spotSpeed.place(x=10, y=380)

                self.spotPrice["text"] = self.selected.tower.price

                if self.selected.tower.lvl == 1:
                    self.last_preview = self.interface.create_image(
                        100, 475, image=self.selected.tower.lv1)

                elif self.selected.tower.lvl == 2:
                    self.last_preview = self.interface.create_image(
                        100, 475, image=self.selected.tower.lv2)

                elif self.selected.tower.lvl == 3:
                    self.last_preview = self.interface.create_image(
                        100, 475, image=self.selected.tower.lv3)
                    self.buildButton["text"] = "MAX"
                    self.buildButton["state"] = "disabled"
                self.spotName["text"] += str(self.selected.tower)

                if hasattr(self.selected.tower, "zone"):
                    self.spotDamage["text"] += str(self.selected.tower.damage) + \
                        " ⇢ " + str(self.selected.tower.ndamage)
                    self.spotZone["text"] += str(self.selected.tower.zone)
                    self.spotDamagetype["text"] += str(
                        self.selected.tower.damagetype)
                    self.spotSpeed["text"] += str(self.selected.tower.speed) + \
                        " ⇢ " + str(self.selected.tower.nspeed)
                else :
                    self.spotDamage.destroy()
                    self.spotZone.destroy()
                    self.spotDamagetype.destroy()
                    self.spotSpeed.destroy()

                if type(self.selected.tower.price) is "int" and self.selected.tower.price > self.parent.gold.get():
                    self.buildButton["state"] = "disabled"
                    self.buildButton["text"] = "Pas Assez d'Or"

            else:
                self.last_preview = self.interface.create_image(
                    100, 475, image=self.hammerSign)

                self.half_range = self.dico[state].range
                self.buildButton["text"] = "Construire"

                self.spotName["text"] += "Vide ⇢ " + str(state)
                self.spotPrice["text"] = self.dico[state].price
                if hasattr(self.dico[state], "zone"):
                    self.spotDamage["text"] += "0 ⇢ " + \
                        str(self.dico[state].damage)
                    self.spotZone["text"] += "Aucun ⇢ " + \
                        str(self.dico[state].zone)
                    self.spotDamagetype["text"] += "Aucun ⇢ " + \
                        str(self.dico[state].damagetype)
                    self.spotSpeed["text"] += "0 ⇢ " + str(self.dico[state].speed)

                if self.dico[state].price > self.parent.gold.get():
                    self.buildButton["state"] = "disabled"
                    self.buildButton["text"] = "Pas Assez d'Or"

            self.range_preview = self.canvas.create_oval(self.selected.x+self.half_range, self.selected.y+self.half_range, self.selected.x - self.half_range, self.selected.y - self.half_range,
                                                         outline="blue")

        else:
            self.buildButton["state"] = "disabled"
            self.buildButton["text"] = "Construire"

    def buildTower(self):
        state = ''.join([i for i in str(self.v.get()) if not i.isdigit()])

        if self.selected:
            self.canvas.delete(self.selected.last_img)
            if self.selected.state is None:
                
                self.selected.state = state
                if state == "Forgeron":
                    self.selected.tower = self.dico[state](
                        self.parent, self.selected.x, self.selected.y, self.parent.heros)
                else:
                    self.selected.tower = self.dico[state](
                        self.parent, self.selected.x, self.selected.y)
                self.parent.gold.set(
                    self.parent.gold.get()-self.dico[state].price)
                
            else:
                self.parent.gold.set(
                    self.parent.gold.get()-self.selected.tower.price)
                self.selected.tower.upgrade()

            self.preView()

    def emplacementMake(self):
        for spot in self.parent.spots:
            if spot.state == None:
                spot.last_img = self.canvas.create_image(
                    spot.x, spot.y, image=self.hammerSign, anchor="s")
            else:
                spot.tower.construction()