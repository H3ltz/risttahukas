from Controller import Controller

class App:
    def __init__(self):
        game = Controller()
        game.view.main() #Teeb põhi akna nähtavaks

if __name__ == '__main__': #käivitamisel loob objekti App
    App()