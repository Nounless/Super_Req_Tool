from tkinter import *
import time
import requests

checkpage = False
url = None
response = None
check_bool = False

class App:
    def __init__(self):
        
        self.main_page = Tk()

        #---------Configs--------

        self.config_title = "Super_Req_Tool"
        self.background_color = "#000000"
        self.foreground_color = "#FFFFFF"
        self.config_width = 600
        self.config_height = 600
        self.config_resizable = [False,False]

        #--------load functions-------

        self.load_configs()
        self.load_objects()
        self.load_buttons()

        #-------mainloop--------
        
        mainloop()

    #---------------Screen settings-----------

    def load_configs(self):
        self.main_page.title(self.config_title)
        self.main_page.config(background = self.background_color,width = self.config_width,height = self.config_height)
        self.main_page.resizable(self.config_resizable[0],self.config_resizable[1])
        
    def load_objects(self):
        first_Page_Title = Label(
            self.main_page,
            text = "Ŝűҏԙ ȐȅɊ ƬƟǾȈ",
            bg = self.background_color,
            foreground="#FF0000",
            font=("arial", 26 ,"bold")
        )
        first_Info1 = Label(
            self.main_page,
            text ="Welcome to the super reg tool.",
            bg = self.background_color,
            foreground ="#530896",
            font =("arial",20,"bold")
        )
        first_Info2 =Label(
            self.main_page,
            text = """Here you will have a graphical environment\n to get rid of the console environment.""",
            bg = self.background_color,
            foreground =  "#530896",
            font = ("arial",20,"bold")
        )
        first_Info3 =Label(
            self.main_page,
            text = "With this tool you can:",
            bg = self.background_color,
            foreground =  "#530896",
            font = ("arial",20,"bold")
        )
        first_Info4 =Label(
            self.main_page,
            text = "• Make requests to websites\n and see the result.",
            bg = self.background_color,
            foreground =  "#00FF0F",
            font = ("arial",20,"bold")
        )
        first_Info5 =Label(
            self.main_page,
            text = "• To find the main pages of the website.",
            bg = self.background_color,
            foreground =  "#00FF0F",
            font = ("arial",20,"bold")
        )
        first_Info1.place(x = 15,y = 100)
        first_Info2.place(x = 15,y = 132)
        first_Info3.place(x = 15,y = 197)
        first_Info4.place(x = 15,y = 300)
        first_Info5.place(x = 15,y = 400)
        first_Page_Title.place(x = 300 ,y =33,anchor="center")

        
#-----------Button Settings---------------        

    def load_buttons(self):
        start_Button = Button(
            self.main_page,
            text = "START",
            bg =self.background_color,
            foreground = "#F7FF00",
            font = ("Arial",16,"bold"),
            border = 4,
            padx =4,
            pady =4,
            activeforeground="#00FF0F",
            activebackground=self.background_color,
            command =(self.start_button_click)
            
            
        )
        about_button =Button(
            self.main_page,
            text ="About",
            bg = self.background_color,
            fg ="#00FFA2",
            width= 2,
            height =1,
            activeforeground ="#F7FF00",
            activebackground ="#000000",
            border=2,
            command = (self.about_button_click)
        )
            
        about_button.place(x = 10 , y = 5 )
        start_Button.place(x = 450,y =500)

        #----------clickbuttons Setting-----------

    def about_button_click(self):

        about_window = About()

    def start_button_click(self):
        global checkpage
        checkpage = True
        close_open =print("Main page closed\nTool page open")
        self.main_page.destroy()
        
        return (close_open)
        
class Error:
    def __init__(self):
        self.error_page =Tk()

        #-----------configs-----------------

        self.config_title = "ERROR"
        self.config_background = "#000000"
        self.config_foreground ="#FF0000"
        self.config_width = 300
        self.config_height = 200

        #------------Load Obj---------------

        self.error_window()
        self.error_labels()

        #------------call mainloop----------

        self.error_page.mainloop()

    #--------------Screen Settings------------

    def error_window(self):
        self.error_page.title (self.config_title)
        self.error_page.config(bg =self.config_background,width=self.config_width,height=self.config_height)
        self.error_page.resizable(False,False)
        
    def error_labels(self):
        self.errorlabel1 = Label(
            self.error_page,
            text = "There was a problem with",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.errorlabel2 = Label(
            self.error_page,
            text = "the program.Reopen the",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.errorlabel3 = Label(
            self.error_page,
            text = "application or enter another",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.errorlabel4 = Label(
            self.error_page,
            text = "value.",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.errorlabel1.place(x = 10 , y = 10 )
        self.errorlabel2.place(x = 10 , y = 40)
        self.errorlabel3.place(x = 10 , y = 70)
        self.errorlabel4.place(x = 10 , y = 100)

class Not_found:
    def __init__(self):
        self.not_found_page =Tk()

        #-----------configs-----------------

        self.config_title = "NOT FOUND"
        self.config_background = "#000000"
        self.config_foreground ="#FF0000"
        self.config_width = 300
        self.config_height = 120

        #------------Load Obj---------------

        self.not_found_window()
        self.not_found_labels()

        #------------call mainloop----------

        self.not_found_page.mainloop()

    #--------------Screen Settings------------

    def not_found_window(self):
        self.not_found_page.title (self.config_title)
        self.not_found_page.config(bg =self.config_background,width=self.config_width,height=self.config_height)
        self.not_found_page.resizable(False,False)
        
    def not_found_labels(self):
        self.notfoundlabel1 = Label(
            self.not_found_page,
            text = "Search completed.",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.notfoundlabel2 = Label(
            self.not_found_page,
            text = "And no result was found.",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.notfoundlabel3 = Label(
            self.not_found_page,
            text = "Please try again.",
            bg =self.config_background,
            fg = self.config_foreground,
            font = ("arial",16,"bold")
        )
        self.notfoundlabel1.place(x = 10 , y = 10 )
        self.notfoundlabel2.place(x = 10 , y = 40)
        self.notfoundlabel3.place(x = 10 , y = 70)


class Labels:
    def __init__(self,linkshow):
        self.labels_page =Tk()

        #-----------configs--------------

        self.labels_title = "Result"
        self.labels_background_color ="#000000"
        self.labels_foreground_color = "#00FF0F"
        self.labels_width = 300
        self.labels_height = 60
        self.labels_showurl = linkshow

        #--------------call obj------------

        self.config_labels_window()
        self.linklabels_show()

        #--------------mainloop------------

        mainloop()

    #-------------Screen Settings--------------
    
    def config_labels_window(self):
        self.labels_page.title(self.labels_title)
        self.labels_page.config(
            bg =self.labels_background_color,
            width =self.labels_width,
            height =self.labels_height
        )
        self.labels_page.resizable(False,False)
    
    def linklabels_show(self):
        urllabel = Label(
            self.labels_page,
            text = self.labels_showurl,
            bg =self.labels_background_color,
            fg = self.labels_foreground_color,
        )
        urllabel.place(x =10, y =20)
    

class Tool:
    def __init__(self):
        self.super_req = Tk()
        
        #-------------configs---------------

        self.config_title = "Super_Req_Tool"
        self.config_width = 600
        self.config_height = 600
        self.config_backgroundcolor = "#000000"
        self.config_resizable =[False,False]

        #------------load Founction------------

        self.config_windo()
        self.config_labels()
        self.config_entry()
        self.config_buttons()

        #----------------mainloop---------------

        mainloop()

    #---------------Screen Settings--------------

    def config_windo(self):
        self.super_req.title(self.config_title)
        self.super_req.config(width=self.config_width,height=self.config_height,bg=self.config_backgroundcolor)
        self.super_req.resizable (self.config_resizable[0],self.config_resizable[1])
    
    def config_labels(self):
        self.titel_label = Label(
            self.super_req,
            text = "Ŝűҏԙ ȐȅɊ ƬƟǾȈ",
            bg = self.config_backgroundcolor,
            foreground="#FF0000",
            font=("arial", 22 ,"bold")
        )
        self.help_label =Label(
            self.super_req,
            text = """To start the tool, you must enter the link of\n the desired site in the box below.Example:\n https://exampel.com or exampel.com""",
            bg =self.config_backgroundcolor,
            fg= "#0023FF",
            font =("Arial",18,"bold")
        )
        self.help_label.place(x =300,y=100,anchor ="center")
        self.titel_label.place(x =300, y =30,anchor = "center")

    def config_entry(self):
        self.get_string = Entry(
            self.super_req,
            width = 30
        )
        self.get_string.place (x =350, y = 200,anchor ="center")
        global url
        url = self.get_string

    def config_buttons(self):
        self.search_button = Button(
            self.super_req,
            text ="Search",
            bg =self.config_backgroundcolor,
            fg = "#ffffff",
            activebackground =self.config_backgroundcolor,
            activeforeground ="#00FF0F",
            border =4,
            width =8 ,
            height =1,
            command =(self.search_botton_click)
        )
        self.search_button.place (x= 170, y =200,anchor ="center")

    #------------click button setting------------
    
    def search_botton_click(self):
        url = self.get_string.get()
        if "https://" not in url:
            url = ("https://"+ url)
            self.requests_site(url)
            
        else:
            url = url
            self.requests_site(url)
        
    def requests_tool_on(self,urllink):
        self.pathlist = ['admin/','administrator/','login.php','administration/','masters','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
        'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
        'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
        'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
        'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
        'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
        'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
        'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
        'panel-administracion/index.html']
        self.count_link = 0 
        self.perfect_link_list = []
        for row in self.pathlist :
            self.perfect_urllink = (urllink + "/" + row)
            self.response_urllink = requests.get(self.perfect_urllink)
            if self.response_urllink.status_code == 200:
                self.count_link  = self.count_link + 1
                self.perfect_link_list.append(self.perfect_urllink)
        if self.count_link != 0 :
            self.labels_on(self.perfect_link_list)
        else:
            not_found_page = Not_found()
               
    def labels_on(self,count):
        self.super_req.destroy()
        for i in count:
            create_labels = Labels(i)
            
        

    def requests_site(self,link):
        try:
            global response
            response = requests.get(link)
            if response.status_code == 200:
                print("The program is running.please wait...")
                self.requests_tool_on(link)
            elif response.status_code != 200:
                self.error = Error()
        except:
            self.except_error =Error()


class About:
    def __init__(self):
        self.about_page =Tk()

        #-----------configs--------------

        self.about_title = "About"
        self.about_background_color ="#000000"
        self.about_foreground_color = "#F000FF"
        self.about_width = 500
        self.about_height = 500

        #--------------call obj------------

        self.config_about_window()
        self.about_labels()

        #--------------mainloop------------

        mainloop()

    #-------------Screen Settings--------------
    def config_about_window(self):
        self.about_page.title(self.about_title)
        self.about_page.config(
            bg =self.about_background_color,
            width =self.about_width,
            height =self.about_height
        )
        self.about_page.resizable(False,False)

    def about_labels(self):
        about_label = Label(
            self.about_page,
            text ="With this graphic program, you\n can easily do things (requests)\nWithout special expertise.",
            bg = "#000000",
            fg = self.about_foreground_color,
            font =("Arial",23,"bold")

        )
        about_label.place(x =250,y =250,anchor ="center")


#-----cal obj----------

applicatin = App()
if checkpage == True:
    time.sleep(1.0)
    toolpage = Tool()
else:
    print("Something went wrong please try agin!")



