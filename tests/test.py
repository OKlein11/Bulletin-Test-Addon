from bulletin.bulletin import Bulletin
from bulletin.email_server import EmailServer
from bulletin.section import Section
from bulletin.individual_rss import IndividualRSSFeed
from auth import * 
from bulletin_test_addon.test_addon import Test_Addon

server = EmailServer(username,password,"smtp.gmail.com")
bullet = Bulletin(server)
bullet.add_section(Test_Addon({}))
bullet.send(username,"test")