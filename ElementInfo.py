import requests
from tkinter import *
import tkinter as tk
import webbrowser
from os import path

def writeHTML(datajson, ):

    print(datajson)
    with open("YusufMianElementInformation.html", "w") as ofile:
        ofile.write(""" 
            <head>
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>

            <b><h1>""" + datajson["name"] + """</h1></b>


              <p> <b>Element Symbol:</b> """ + datajson['symbol'] + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Introductory_Chemistry/Book%3A_Introductory_Chemistry_(CK-12)/02%3A_Matter_and_Change/2.12%3A_Chemical_Symbols_and_Formulas" target="_blank">Learn More About Element Symbols</a>
 
            <p> <b>Atomic Mass:</b> """ + str(datajson['atomicMass']) + """</p>
                <a href="https://chem.libretexts.org/Courses/Furman_University/CHM101%3A_Chemistry_and_Global_Awareness_(Gordon)/03%3A_Atoms_and_the_Periodic_Table/3.4%3A_Atomic_Mass_and_Atomic_Number" target="_blank">Learn More About the Atomic Mass</a>

            <p> <b>Atomic Number:</b> """ + str(datajson['atomicNumber']) + """</p>
                <a href="https://chem.libretexts.org/Courses/Furman_University/CHM101%3A_Chemistry_and_Global_Awareness_(Gordon)/03%3A_Atoms_and_the_Periodic_Table/3.4%3A_Atomic_Mass_and_Atomic_Number" target="_blank">Learn More About the Atomic Number</a>

            <p> <b>Atomic Radius:</b> """ + str(datajson['atomicRadius']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Introductory_Chemistry/Book%3A_Introductory_Chemistry_(CK-12)/06%3A_The_Periodic_Table/6.15%3A_Periodic_Trends%3A_Atomic_Radius" target="_blank">Learn More About Atomic Radius</a>

            <p> <b>Bonding Type:</b> """ + str(datajson['bondingType']) + """</p>
            <p> <b>cpkHexColour of the Element:</b> """ + datajson['cpkHexColor'] + """</p> 
            <p> <b>Density:</b> """ + str(datajson['density']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Introductory_Chemistry/Map%3A_Introductory_Chemistry_(Tro)/02%3A_Measurement_and_Problem_Solving/2.09%3A_Density" target="_blank">Learn More About Density</a>

            <p> <b>Electron Affinity:</b> """ + str(datajson['electronAffinity']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/Atomic_and_Molecular_Properties/Electron_Affinity" target="_blank">Learn More About Electron Affinity</a>
          
            <p> <b>Electronnegativity:</b> """ + str(datajson['electronegativity']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/Atomic_and_Molecular_Properties/Electronegativity" target="_blank">Learn More About Electronegativity</a>
            
            <p> <b>Electronic Configuration:</b> """ + str(datajson['electronicConfiguration']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/General_Chemistry/Map%3A_Chemistry_-_The_Central_Science_(Brown_et_al.)/06._Electronic_Structure_of_Atoms/6.8%3A_Electron_Configurations" target="_blank">Learn More About Electronic Configuration</a>
           
            <p> <b>Group Block:</b> """ + datajson['groupBlock'] + """</p>
            <p> <b>Ion Radius:</b> """ + str(datajson['ionRadius']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Supplemental_Modules_(Inorganic_Chemistry)/Descriptive_Chemistry/Periodic_Trends_of_Elemental_Properties/Periodic_Trends_in_Ionic_Radii" target="_blank">Learn More About Ion Radius</a>

            <p> <b>Ionization Energy:</b> """ + str(datajson['ionizationEnergy']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/Atomic_and_Molecular_Properties/Ionization_Energy" target="_blank">Learn More About Ionization Energy</a>

            <p> <b>Melting Point:</b> """ + str(datajson['meltingPoint']) + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Book%3A_Organic_Chemistry_Lab_Techniques_(Nichols)/6%3A_Miscellaneous_Techniques/6.1%3A_Melting_Point" target="_blank">Learn More About Melting Point</a>

            <p> <b>Oxidation States:</b> """ + datajson['oxidationStates'] + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Electrochemistry/Redox_Chemistry/Oxidation_State" target="_blank">Learn More About Oxidation States</a>

            <p> <b>Standard State:</b> """ + datajson['standardState'] + """</p>
                <a href="https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/DeVoe's_%22Thermodynamics_and_Chemistry%22/07%3A_Pure_Substances_in_Single_Phases/7.7_Standard_States_of_Pure_Substances" target="_blank">Learn More About Standard States</a>

        """)

def getAPI():
    myrequest  = requests.get("https://neelpatel05.pythonanywhere.com/element/atomicname?atomicname=" + tkvar.get())
    datajson = myrequest.json()
    writeHTML(datajson)
    webbrowser.open('file:///Users/yusuf.mian/Documents/YusufMianElementInformation.html')
      
def change_dropdown(*args):
    print(tkvar.get() )

def clickme():
    print(tkvar.get())
    x = " "
    b1 = Button()
    myrequest = requests.get("https://neelpatel05.pythonanywhere.com/element/atomicname?atomicname=")
    datajson = myrequest.json()
    print(str(datajson))

root = Tk()
root.title("Choose Your Element")

mainframe = Frame(root)
mainframe.grid(column=4,row=5)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkvar = StringVar(root) 
choices = { 'Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen','Neon', 'Sodium','Magnesium','Aluminum','Silicon','Phosphorus','Sulfur','Chlorine','Argon','Potassium','Calcium','Scandium','Titanium','Vanadium','Chromium','Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Gold', 'Platinum', 'Mercury', 'Francium', 'Barium', 'Cerium'} 
tkvar.set('') 

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose Your Element").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

submit1 = Button(root, text = "Submit", command = getAPI)
#   submit1.configure(font=("Times New Roman", 14))
submit1.pack()

root.mainloop()

