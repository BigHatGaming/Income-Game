#remember to pip install pygame if you haven't already, or the game will not run
#make sure to follow the instructions for importing images if you wish to run this code
#time limit is the number of weeks you want your game to go to, for simplicity's sake it's located at the very top of the script
time_limit = 52
#not sure where the import image came from, was added by vscode. Not going to mess with it in fear of the code breaking
from cgitb import small
from email.mime import image
import pygame
import math
import _curses
import random
random.seed()
pygame.init()
pygame.display.init
#make classes here:
#when creating a user(will probably only be used for the "me" user), input initial balance
class User():
    week_num = 0
    def __init__(self,balance):
        self.balance = balance
#when creating products,input cost to buy, price to be sold at,true or false for perishable, and the description
class Product():
    amount = 0
    def __init__(self,buyprice,sellprice,perishable,description):
        self.buyprice = buyprice
        self.sellprice = sellprice
        self.perishable = perishable
        self.description = description
#when creating upgrades, input the increase to the sell price of the product, decrease to the price to buy, description of the upgrade, and the product effected
class Upgrade():
    purchased = False
    #other num is used for upgrades that do not increase or decrease prices, just so that we have a number to work with
    def __init__(self,price,increasetosell,decreasetobuy,othernum,description,):
        self.price=price
        self.increasetosell = increasetosell
        self.decreasetobuy = decreasetobuy
        self.othernum = othernum
        self.description = description
             
#make upgrades here 
better_beans = Upgrade(1000,5,0,0,"Beans sell for more")
beanincrease = 0
better_cooling = Upgrade(2000,0,0,15,"Perishables rot less")
#end of make upgrades

#make products here
eggs = Product(55,7,True,"10 dozen eggs")
canned_beans = Product(30,(35+beanincrease),False,"A unit of ten cans of beans")
apples = Product(10,12,False,"Ten Apples")
milk = Product(40,60,True,"Ten Jugs of Milk")
#end of make products
def purchase_upgrades(Upgrade):
    if me.balance > Upgrade.price + 30:
        me.balance = me.balance - Upgrade.price
        Upgrade.purchased = True
def purchase(Product):
    if me.balance > Product.buyprice:
        me.balance = me.balance - Product.buyprice
        Product.amount += 1
        
        product_list.append(Product)
#product list is used to know what products to run through, if there are zero of a product they wont be checked
product_list = []
me = User(500)
#Getitng pygame startup stuff out of the way, as well as some text, the images, and the blue background
screen=pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
background = pygame.Surface((1000,700))
background.fill('Blue')
texts=pygame.font.Font(None,50)
textsurface=texts.render('Getting Started',False,'Black')
smallfont=pygame.font.Font(None,35)
introductiontext = smallfont.render("Welcome to income game, buy upgrades and products to improve the income of your ",False,'Black')
introductiontext2 = smallfont.render("shop,pressing end week will enact all decisions/give you last weeks income.",False,'Black')
productsmenutext = texts.render("Products:",False,'Black')
perishwarning = texts.render("Perishables have a chance to rot",False,'Black')
#images are through path in computer, so will only work on Matt's computer unless the code is updated for specific computers
#if you need to use this code, download the code assets folder here:https://drive.google.com/drive/u/0/folders/12uTnJEp7ENd0zCawJ7b29tnaBOCNKpoO
#download and put in your documents folder, then chance the user from gr8t2 to your user
beanimg = pygame.image.load(r'C:\Users\gr8t2\Documents\Code Assets\imag\beancan.png' )
appleimg = pygame.image.load(r'C:\Users\gr8t2\Documents\Code Assets\imag\apple.png' )
eggimg = pygame.image.load(r'C:\Users\gr8t2\Documents\Code Assets\imag\eggs.png' )
milkimg = pygame.image.load(r'C:\Users\gr8t2\Documents\Code Assets\imag\milk.png' )
upgradesmenutext = texts.render("Upgrades:",False,'Black')
#displays what the product looks like, as well as the buy/sell information and how many you have
def Prod_amount_counter(Product,prodimage,x,y):
    screen.blit(prodimage,(x-75,y-25))
    productcount = texts.render("X "+str((Product.amount)*10),False,'Black')
    prodbuy = texts.render("Buy at:"+str(Product.buyprice),False,'Black')
    prodsell = texts.render("Sell at: "+str(Product.sellprice),False,'Black')
    #updater is necessary to erase old text to make way for new text, as it is printed during an update
    updater=pygame.Surface((150,100))
    updater.fill('Blue')
    screen.blit(updater,(x,y))
    screen.blit(productcount,(x,y))
    screen.blit(prodbuy,(x+85,y))
    screen.blit(prodsell,(x+85,y+30))
#class for button creation
class Button():
    #initializing the color, position, size, and text
    def __init__(self,color,x,y,width,height,text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    #call to display the button, button will not be displayed otherwise
    def draw(self,screen,outline=None):
        #outline, standard to all buttons, called if writing"True" in the draw funciton
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        #makes the text, will not run if there is no text
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    #checks if the mouse is over the button, used for pressing the button
    def isOver(self, mouse):
        #mouse is the mouse position
        if mouse[0] > self.x and mouse[0] < self.x + self.width:
            if mouse[1] > self.y and mouse[1] < self.y + self.height:
                return True
            
        return False
#for buttons the list in the initilization is: color,x,y,width,height,text.
#buttons
startbutton = Button((20,70,0),600,400,250,200,"Start")
quitbutton =Button((255,20,20),600,450,300,100,"Quit")
endweekbutton = Button((150,150,0),100,450,300,100,"End Week")
upgradesbutton = Button((100,255,50),100,150,300,100,"Upgrades")
productsbutton = Button((255,35,100),600,150,300,100,"Products")
backbutton = Button((255,0,0),700,600,300,100,"<--Back")
beanbutton = Button((20,70,0),25,35,300,100,"Buy Beans")
eggsbutton = Button((20,70,0),25,135,300,100,"Buy Eggs")
betterbeanbutton = Button((20,70,0),25,35,375,100,"Better Beans")
bettercoolingbutton = Button((200,200,255),25,200,400,100,"Better Cooling")
applebutton = Button((20,70,0),25,235,300,100,"Buy Apples")
milkbutton = Button((20,70,0),25,335,300,100,"Buy Milk")
#end of buttons
#show balance function, erases old counter and prints new one each time it's updated
def show_bal(x,y):
    Balancecounter = texts.render("Your balance is: "+str(me.balance)+"$",False,'Black')
    #updater is necessary because it draws oer the old text each time show_bal is updated, otherwise the new text would just print over the old one
    updater = pygame.Surface((450,100))
    updater.fill('Blue')
    screen.blit(updater,(x,y))
    screen.blit(Balancecounter,(x,y))
#same as show balance, but with the current week
def show_week(x,y):
    Weekcounter = texts.render("It is Week: "+str(me.week_num),False,'Black')
    updater = pygame.Surface((300,75))
    updater.fill('Blue')
    screen.blit(updater,(x,y))
    screen.blit(Weekcounter,(x,y))
def upgradeinfo(x,y,Upgrade):
    if Upgrade.purchased == False:
        txt1 = texts.render(str(Upgrade.description),False,'Black')
        pritxt = texts.render("Price: "+str(Upgrade.price),False,'Black')
    if Upgrade.purchased == True:
        txt1 = texts.render("Sold",False,'Black')
        pritxt =texts.render("Sold",False,'Black')
    updater = pygame.Surface((250,60))
    updater.fill('Blue')
    screen.blit(updater,(x,y))
    screen.blit(txt1,(x,y))
    screen.blit(pritxt,(x,y+30))
#end week function:NEEDS FINISHING!!!!!!!!!!!!!!!! (Plan to only aquire a percentage of profits, other units get lost/destroyed and cant be sold)
def end_week():
    me.week_num +=1
    if me.week_num == time_limit:
        game_end()
    else:
        if better_cooling.purchased ==False:
            cooling = 0
        elif better_cooling.purchased == True:
            cooling = better_cooling.othernum
        for Product in product_list:
            #chance is the chance that you lose some of your perishable items
            chance = False
            chancenum = random.randint(1,100)
            amtlost=0
            if chancenum <(60-cooling):
                chance = True
            if Product.amount > 0:
                if chance == True:
                    if Product.perishable == True:
                        #rane is the maximum number of items lost when items is even, rano is the odd variant. This is defaulted to half of all perishables
                        rane = (Product.amount/2)
                        if Product.amount ==1:
                            rano = (0)
                        else:
                            rano =((Product.amount-1)/2)
                        if Product.amount%2 == 0:
                            print(rane)
                            amtlost = random.randint(1,rane)
                        elif Product.amount ==1:
                            amtlost = 0
                        else:
                            amtlost = random.randint(1,rano)
                    elif Product.perishable == False:
                        amtlost = 0
                if Product.amount > 0:
                    #user's balance is updated to reflect the amount of products sold, minus the amount of items lost. All items are sold each week, hence being set to zero
                    me.balance = me.balance + ((Product.amount-amtlost) * Product.sellprice)
                    Product.amount = 0
                if Product.amount ==0:
                    product_list.remove(Product)
                    print(Product,"Was removed from the list")
#the main screen where you will always come back to    
def main_game():
    pygame.init()
    pygame.display.update()
    main_running=True
    is_running = False
    #call the global products inside each function to make sure they update after upgrading
    global eggs 
    global canned_beans
    if better_beans.purchased ==True:
        beanincrease = better_beans.increasetosell
    else:
        beanincrease=0
    eggs = Product(55,70,True,"10 dozen eggs")
    canned_beans = Product(30,(35+beanincrease),False,"A unit of ten cans of beans")
    
    while main_running == True:
        
       
        quitbutton.draw(screen,True)
        endweekbutton.draw(screen,True)
        upgradesbutton.draw(screen,True)
        productsbutton.draw(screen,True)
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitbutton.isOver(mouse):
                    main_running = False
                    pygame.quit()
                if productsbutton.isOver(mouse):
                    #background is drawn over everything each time a new menu is called, this is to erase any old images
                    screen.blit(background,(0,0))
                    Products_Menu()
                if upgradesbutton.isOver(mouse):
                    screen.blit(background,(0,0))
                    Upgrades_Menu()
                if endweekbutton.isOver(mouse):
                    end_week()            
            
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        show_bal(0,0)
        show_week(650,600)
# the product menu, planned to have multiple pages down the road
def Products_Menu():
    products_running = True
    #call the global products inside each function to make sure they update after upgrading
    global eggs 
    global canned_beans 
    global apples
    global milk
    while products_running ==True:
        
        pygame.display.update()
        backbutton.draw(screen,True)
        beanbutton.draw(screen,True)
        eggsbutton.draw(screen,True)
        applebutton.draw(screen,True)
        milkbutton.draw(screen,True)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.isOver(mouse):
                    screen.blit(background,(0,0))
                    main_game()
                if beanbutton.isOver(mouse):
                    purchase(canned_beans)
                if eggsbutton.isOver(mouse):
                    purchase(eggs)
                if applebutton.isOver(mouse):
                    purchase(apples)
                if milkbutton.isOver(mouse):
                    purchase(milk)
        #display update is necessary for well, updating the display
        #calling counters and show bal to show them properly
        pygame.display.update()
        screen.blit(productsmenutext,(0,0))
        screen.blit(perishwarning,(350,0))
        Prod_amount_counter(canned_beans,beanimg,415,75)
        Prod_amount_counter(eggs,eggimg,415,160)
        Prod_amount_counter(apples,appleimg,415,250)
        Prod_amount_counter(milk,milkimg,415,360)
        show_bal(0,650)
def Upgrades_Menu():
    upgrades_running = True
    #call the global products inside each function to make sure they update after upgrading
    global eggs 
    global canned_beans
    while upgrades_running ==True:
        pygame.display.update()
        betterbeanbutton.draw(screen,True)
        bettercoolingbutton.draw(screen,True)
        backbutton.draw(screen,True)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.isOver(mouse):
                    screen.blit(background,(0,0)) 
                    main_game()  
                if betterbeanbutton.isOver(mouse):
                    purchase_upgrades(better_beans)
                if bettercoolingbutton.isOver(mouse):
                    purchase_upgrades(better_cooling)
        screen.blit(upgradesmenutext,(0,0))
        upgradeinfo(475,35,better_beans)
        upgradeinfo(525,200,better_cooling)
        show_bal(0,650)
#start menu to give breif description, will never be used after pressing the start button
def start_menu():
    is_running = True
    while is_running ==True:
     
        startbutton.draw(screen,True)
    
        pygame.display.update()
    
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbutton.isOver(mouse):
                    screen.blit(background,(0,0))
                    main_game()
                
   
        screen.blit(background,(0,0))
        screen.blit(introductiontext,(5,0))
        screen.blit(introductiontext2,(5,100))
#starting the game
def game_end():
    #self explanatory, just prints some text onto the screen, and only gives you the option of quitting
    is_running = True
    endtext1 = texts.render("You have reached the end of your time",False,'Black')
    endtext2 = texts.render("Your final balance was: "+str(me.balance),False,'Black')
    quitbutton.draw(screen,True)
    while is_running == True:
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitbutton.isOver(mouse):
                    pygame.quit()
        screen.blit(background,(0,0))
        screen.blit(endtext1,(150,100))
        screen.blit(endtext2,(250,250))    
start_menu()