#function that looks to see if folder is a sub-folder in another directory. if it's there it returns it

    def grower_specific_templates(self): 
        self.cwd = os.getcwd() #this gets the current dir
        os.chdir(self.cwd + "/data/test/isfolderhere") # change to the dir you want to goto

        subfolders = [f.name for f in os.scandir(os.getcwd()) if f.is_dir()]
        print(subfolders)
        return subfolders
