
import tkinter
from tkinter import ttk

from constants.programInfo import ProgramInfo
from constants.hexCodesReference import AttributesAndRaces, Archetypes

from classes.sql import CardsCDB
from classes.downloadManager import DownloadManager

from interfaces.guiTabs.domGenTab import DomainGeneratorGUI
from interfaces.guiTabs.deckCheckerTab import DeckCheckerGUI

# Class that handles the CLI interface of the program
class GraphicalUserInterface:

    TITLE = "Yugioh Domain Generator ({})"

    # Runs setups for classes which require external classes.
    def Setup(self):
        DownloadManager.DownloadFiles()
        Archetypes.Setup()
        AttributesAndRaces.Setup()
        CardsCDB.Setup()
        print("")

    # The main interface loop.
    def StartInterface(self) -> None:            
        # Setup stuff.
        self.Setup()
        
        # TKinter setup.
        frame = tkinter.Tk()
        frame.geometry("500x450+700+300")
        frame.title(self.TITLE.format(ProgramInfo.VERSION))

        # Tab setup
        tabControl = ttk.Notebook(frame)
        domainGeneratorTab = ttk.Frame(tabControl)
        deckCheckerTab = ttk.Frame(tabControl) 

        tabControl.add(domainGeneratorTab, text="Domain Generator")
        tabControl.add(deckCheckerTab, text="Deck Validator")
        tabControl.pack(expand = 1, fill ="both") 

        # Domain Generator
        domGenTabClass = DomainGeneratorGUI()
        domGenTabClass.Tab(domainGeneratorTab)
        
        # Deck Checker
        deckCheckerClass = DeckCheckerGUI()
        deckCheckerClass.Tab(deckCheckerTab)

        frame.mainloop()
        