import time 
import subprocess 
import socket
import sys 
import requests

#class [color_method] -no parameters -no inheritance
class color_method():
    #declared -variable(s): [RED//YELLOW//WHITE]
    RED = '\033[91m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    
#def [banner] -banner to *console* -program information
def banner():
    print(color_method.YELLOW + '''
████████╗██╗  ██╗███████╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
   ██║   ███████║█████╗      ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
   ██║   ██╔══██║██╔══╝      ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
   ██║   ██║  ██║███████╗    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
    ''')
    print(color_method.YELLOW +'\nprogram_name: ' +color_method.RED +'hackbook')
    print(color_method.YELLOW +'use: ' +color_method.RED +'ethical//unethical_hacking')
    print(color_method.YELLOW +'created_by: ' +color_method.RED +'Philip Naveen')
    print(color_method.YELLOW +'built_with: ' +color_method.RED +'Python 3.83')
    print(color_method.YELLOW +'active_methods: ' +color_method.RED +'4')
    
#class [subdomain_scanner] -for finding subdomains
class subdomain_scanner:
    
    #constructor [init] || [self]
    def __init__(self):
        self.subdomain_file = str(input('enter the file of subdomain names: '))
        self.domain = str(input('enter the domain name: '))
        self.subdomains =[]
        
        #with_statement -to append names to list
        with open(str(self.subdomain_file), 'r+') as text_file:
            
            #for_statement -to append each line to list [self.subdomains]
            for subdomain_name in text_file:
                self.subdomains.append(str(subdomain_name))
                
    #function [subdomain_scan]
    def subdomain_scan(self):
        #try_block -to catch exceptions
        try:
        
            #for_loop -acesses the [self.subdomain] and searches with [requests]
            for name in self.subdomains:
                url = "https://{}.{}".format(self.domain,str(name))
                result = requests.get(url)
                
                #new_statements: if//elifs//else
                if bool(results) == True:
                    print('domain found: {}'.format(url))
                else:
                    pass
        
        #exceptions from the try_block
        except Exception as REQUESTS_ERROR:
            print('error: {}'.format(str(REQUESTS_ERROR)))

#class [email_bomber] -attack emails -spear phishing campaigning
class email_bomber:
    
    #init_[self]
    def __init__(self):
        self.target = str(input('enter target mail: '))
        self.port_number = int(587)
        self.mode = int(input('enter mode [1==1000] <> [2==500] <> [3==250]: '))
        
    #def_[setting]
    def setting(self, mode=None):
        self.amount = None
        mode = int(self.mode)
        
        #ifs_elifs_else
        if int(mode) == int(1):
            self.amount = int(1000)
        elif int(mode) == int(2):
            self.amount = int(500)
        elif int(mode) == int(3):
            self.amount = int(250)
        else:
            print('invalid mode')
            time.sleep(10)
            sys.exit(0)
            
    #def_[mail]
    def mail(self):
        self.subject = str(input('enter subject: '))
        self.text = str(input('enter message: '))
        self.from_address = str(input('enter from address: '))
        self.from_password = str(input('enter from password: '))
        self.message = """
        to: {}
        from: {}
        message: {}
        
        """.format(self.target, self.from_address, self.text)
        
    #def_[send_mail]
    def send_mail(self,message=None,subject=None,from_address=None,from_password=None,target=None,amount=None):
        #for_loop
        amount = int(self.amount)
        
        for email in range(1,amount):
            #try_block
            
            try:
                #redefine_parameters
                message = self.message
                subject = self.subject
                from_address = self.from_address
                from_password = self.from_password
                target = self.target
                port = self.port_number
                
                #send_the_email
                SEND = smtplib.SMTP(str('smtp.gmail.com'), int(port))
                SEND.starttls()
                SEND.login(str(from_address), str(from_password))
                SEND.sendmail(str(from_address), str(target), message)
                SEND.quit()
            
            #exception_block
            except Exception as ERROR:
                print('error: {}'.format(ERROR))
                
#class [port_scanner] -find open ports in a server
class port_scanner:
  
  #constructor [__init__] || [self] -the object of the class
  def __init__(self):
    #name_IP
    self.server_name = str(input('enter server name: '))
    self.server_IP = socket.gethostbyname(self.server_name)
    
  def scan(self):
    
    #try_block -to catch exceptions
    try:
      
      for port in range(1,420):
        self.SOCK_SYNTAX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.results = self.SOCK_SYNTAX.connect_ex((self.server_IP, port))
        #ifs_elifs_else
        
        if self.results == 0:
          print('port: {} found open'.format(port))
        elif self.results != 0:
          print('port: {} found closed'.format(port))
        else:
          pass
    
    #exceptions
    except Exception as SOCKET_ERROR:
      print('error: {}'.format(SOCKET_ERROR))
      
#class [username_hunter] -use: scower internet for usernames
class username_hunter():
    
    #init_[self]
    def __init__(self, username=None):
        self.username = str(input('enter username: '))
        
        # INSTAGRAM
        instagram = 'https://www.instagram.com/{}'.format(self.username)
        
        # FACEBOOK
        facebook = 'https://www.facebook.com/{}'.format(self.username)
        
        #TWITTER
        twitter = 'https://www.twitter.com/{}'.format(self.username)
        
        # YOUTUBE
        youtube = 'https://www.youtube.com/{}'.format(self.username)
        
        # BLOGGER
        blogger = 'https://{}.blogspot.com'.format(self.username)
        
        # GOOGLE+
        google_plus = 'https://plus.google.com/s/{}/top'.format(self.username)
        
        # REDDIT
        reddit = 'https://www.reddit.com/user/{}'.format(self.username)
        
        # WORDPRESS
        wordpress = 'https://{}.wordpress.com'.format(self.username)
        
        # PINTEREST
        pinterest = 'https://www.pinterest.com/{}'.format(self.username)
        
        # GITHUB
        github = 'https://www.github.com/{}'.format(self.username)
        
        # TUMBLR
        tumblr = 'https://{}.tumblr.com'.format(self.username).format(self.username)
        
        # FLICKR
        flickr = 'https://www.flickr.com/people/{}'.format(self.username)
        
        # STEAM
        steam = 'https://steamcommunity.com/id/{}'.format(self.username)
        
        # VIMEO
        vimeo = 'https://vimeo.com/{}'.format(self.username)
        
        # SOUNDCLOUD
        soundcloud = 'https://soundcloud.com/{}'.format(self.username)
        
        # DISQUS
        disqus = 'https://disqus.com/by/{}'.format(self.username)
        
        # MEDIUM
        medium = 'https://medium.com/@{}'.format(self.username)
        
        # DEVIANTART
        deviantart = 'https://{}.deviantart.com'.format(self.username)
        
        # VK
        vk = 'https://vk.com/{}'.format(self.username)
        
        # ABOUT.ME
        aboutme = 'https://about.me/{}'.format(self.username)
        
        # IMGUR
        imgur = 'https://imgur.com/user/{}'.format(self.username)
        
        # FLIPBOARD
        flipboard = 'https://flipboard.com/@{}'.format(self.username)
        
        # SLIDESHARE
        slideshare = 'https://slideshare.net/{}'.format(self.username)
        
        # FOTOLOG
        fotolog = 'https://fotolog.com/{}'.format(self.username)
        
        # SPOTIFY
        spotify = 'https://open.spotify.com/user/{}'.format(self.username)
        
        # MIXCLOUD
        mixcloud = 'https://www.mixcloud.com/{}'.format(self.username)
        
        # SCRIBD
        scribd = 'https://www.scribd.com/{}'.format(self.username)
        
        # BADOO
        badoo = 'https://www.badoo.com/en/{}'.format(self.username)
        
        # PATREON
        patreon = 'https://www.patreon.com/{}'.format(self.username)
        
        # BITBUCKET
        bitbucket = 'https://bitbucket.org/{}'.format(self.username)
        
        # DAILYMOTION
        dailymotion = 'https://www.dailymotion.com/{}'.format(self.username)
        
        # ETSY
        etsy = 'https://www.etsy.com/shop/{}'.format(self.username)
        
        # CASHME
        cashme = 'https://cash.me/{}'.format(self.username)
        
        # BEHANCE
        behance = 'https://www.behance.net/{}'.format(self.username)
        
        # GOODREADS
        goodreads = 'https://www.goodreads.com/{}'.format(self.username)
        
        # INSTRUCTABLES
        instructables = 'https://www.instructables.com/member/{}'.format(self.username)
        
        # KEYBASE
        keybase = 'https://keybase.io/{}'.format(self.username)
        
        # KONGREGATE
        kongregate = 'https://kongregate.com/accounts/{}'.format(self.username)
        
        # LIVEJOURNAL
        livejournal = 'https://{}.livejournal.com'.format(self.username)
        
        # ANGELLIST
        angellist = 'https://angel.co/{}'.format(self.username)
        
        # LAST.FM
        last_fm = 'https://last.fm/user/{}'.format(self.username)
        
        # DRIBBBLE
        dribbble = 'https://dribbble.com/{}'.format(self.username)
        
        # CODECADEMY
        codecademy = 'https://www.codecademy.com/{}'.format(self.username)
        
        # GRAVATAR
        gravatar = 'https://en.gravatar.com/{}'.format(self.username)
        
        # PASTEBIN
        pastebin = 'https://pastebin.com/u/{}'.format(self.username)
        
        # FOURSQUARE
        foursquare = 'https://foursquare.com/{}'.format(self.username)
        
        # ROBLOX
        roblox = 'https://www.roblox.com/user.aspx?username={}'.format(self.username)
        
        # GUMROAD
        gumroad = 'https://www.gumroad.com/{}'.format(self.username)
        
        # NEWSGROUND
        newsground = 'https://{}.newgrounds.com'.format(self.username)
        
        # WATTPAD
        wattpad = 'https://www.wattpad.com/user/{}'.format(self.username)
        
        # CANVA
        canva = 'https://www.canva.com/{}'.format(self.username)
        
        # CREATIVEMARKET
        creative_market = 'https://creativemarket.com/{}'.format(self.username)
        
        # TRAKT
        trakt = 'https://www.trakt.tv/users/{}'.format(self.username)
        
        # 500PX
        five_hundred_px = 'https://500px.com/{}'.format(self.username)
        
        # BUZZFEED
        buzzfeed = 'https://buzzfeed.com/{}'.format(self.username)
        
        # TRIPADVISOR
        tripadvisor = 'https://tripadvisor.com/members/{}'.format(self.username)
        
        # HUBPAGES
        hubpages = 'https://{}.hubpages.com'.format(self.username)
        
        # CONTENTLY
        contently = 'https://{}.contently.com'.format(self.username)
        
        # HOUZZ
        houzz = 'https://houzz.com/user/{}'.format(self.username)
        
        #BLIP.FM
        blipfm = 'https://blip.fm/{}'.format(self.username)
        
        # WIKIPEDIA
        wikipedia = 'https://www.wikipedia.org/wiki/User:{}'.format(self.username)
        
        # HACKERNEWS
        hackernews = 'https://news.ycombinator.com/user?id={}'.format(self.username)
        
        # CODEMENTOR
        codementor = 'https://www.codementor.io/{}'.format(self.username)
        
        # REVERBNATION
        reverb_nation = 'https://www.reverbnation.com/{}'.format(self.username)
        
        # DESIGNSPIRATION
        designspiration = 'https://www.designspiration.net/{}'.format(self.username)
        
        # BANDCAMP
        bandcamp = 'https://www.bandcamp.com/{}'.format(self.username)
        
        # COLOURLOVERS
        colourlovers = 'https://www.colourlovers.com/love/{}'.format(self.username)
        
        # IFTTT
        ifttt = 'https://www.ifttt.com/p/{}'.format(self.username)
        
        # EBAY
        ebay = 'https://www.ebay.com/usr/{}'.format(self.username)
        
        # SLACK
        slack = 'https://{}.slack.com'.format(self.username)
        
        # OKCUPID
        okcupid = 'https://www.okcupid.com/profile/{}'.format(self.username)
        
        # TRIP
        trip = 'https://www.trip.skyscanner.com/user/{}'.format(self.username)
        
        # ELLO
        ello = 'https://ello.co/{}'.format(self.username)
        
        # TRACKY
        tracky = 'https://tracky.com/user/~{}'.format(self.username)
        
        # BASECAMP
        basecamp = 'https://{}.basecamphq.com/login'.format(self.username)
        
        self.sites = [
        instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
        wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
        medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
        mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
        goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
        dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
        wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
        contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
        bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
        ]
        
    #def_[hunt]
    def hunt(self,USERNAME=None,WEBSITES=None):
        #rename_variables_for_parameters
        USERNAME = self.username
        WEBSITES = self.sites 
        
        #for_loops
        for URL in WEBSITES:
            time.sleep(0.5)
            
            #try_block
            try:
                results = requests.get(URL)
                
                #if_elifs_else
                if bool(results) == True:
                    print('\naccount' + ' {} '.format(USERNAME) +'tracked: {}'.format(URL))
                else:
                    print('\naccount {}'.format(USERNAME)+ ' not found')
            
            #exceptions
            except Exception as REQUESTS_ERROR:
                print('errors: {}'.format(REQUESTS_ERROR))
                time.sleep(10)
                sys.exit(1)
                
def method_subdomain_scanner():
    SS = subdomain_scanner()
    SS.subdomain_scan()
    
def method_email_bomber():
    EB = email_bomber()
    EB.setting()
    EB.mail()
    EB.send_mail()
    
def method_port_scanner():
    PS = port_scanner()
    PS.scan()
    
def method_username_hunter():
    UH = username_hunter()
    UH.hunt()
    
#final_call [main]
if __name__ == '__main__':
    banner()
    print(color_method.WHITE +'''
\nA BruteForce bot that should
ONLY be used legally for hunting
illegal operations''')
    print(color_method.YELLOW +'''
\noption 1: subdomain_scanner
option 2: email_bomber//spear_phishing
option 3: port_scanner
option 4: username_hunter
    ''')
    options = int(input(color_method.WHITE +'enter 1 2 3 or 4: '))
    
    if int(options) == int(1):
        subdomain_scanner()
    elif int(options) == int(2):
        email_bomber()
    elif int(options) == int(3):
        port_scanner()
    elif int(options) == int(4):
        username_hunter()
    else:
        pass
        
    end = input()
    if options == 1:
        method_subdomain_scanner()
    elif options == 2:
        method_email_bomber()
    elif options == 3:
        method_port_scanner()
    elif options == 4:
        method_username_hunter
        
    end = str(input())
    
#program_terminated -ends the program
