class Language:

    def __init__(self):
        """
        init var
        """
        self.languages = {"1":"java","2":"groovy","3":"scala"}
        self.description = """
        please select an language:
        1) java
        2) groovy
        3) scala

        """
        self.language = ""



    def get_input(self):

        while self.language not in self.languages.values():
            print(self.description)
            result = raw_input("please input 1 , 2 or 3 > ")

            for key in self.languages:
                if result == key:
                    self.language = self.languages[key]

        return self.language
