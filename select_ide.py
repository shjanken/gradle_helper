class SelectIDE:

    def __init__(self):
        self.ides = { "1" : "eclipse", "2" : "idea" }
        self.description = """
        please select an ide
            1) elipse
            2) idea
        """
        self.selected_ide = ""

    def get_input(self):
        while self.selected_ide not in self.ides.values():
            print(self.description)
            result = raw_input("please input 1 or 2 > ")

            for key in self.ides :
                if key == result :
                    self.selected_ide = self.ides[key]

        return self.selected_ide

