class MainMenu:
    def __init__(self, app):
        self.app = app

    def list_of_menu_elements(self):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//*[@id='menu']/div[2]/ul/li")