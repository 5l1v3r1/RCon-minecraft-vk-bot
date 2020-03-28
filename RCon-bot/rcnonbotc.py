from mcipc.rcon import Client
from mcipc.rcon.datastructures import Help, Location, Players, Seed
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import time
import random
import json

#pip install mcipc
#pip install vk_api

vk = vk_api.VkApi(token="token")


vk._auth_token()
 
vk.get_api()
 
longpoll = VkBotLongPoll(vk, id)
 
keyboard = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "банлист"
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "онлайни"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "онлайн"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "вайтлистлист"
                },
                "color": "secondary"
            }
        ]
    ]
}
 
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))



#укажите тут id ВК тех, кто будет админом
adminlist = [1,2 ]

with Client('ip', port) as client:
    client.login('password')
    print("connect")


    while True:
        

         

        for event in longpoll.listen():

                        
            if event.type == VkBotEventType.MESSAGE_NEW:


                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "начать":
                    if event.object.from_id in adminlist:
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "загрузка", "random_id": 0,
                                            "keyboard": keyboard})

                
                if "Negative" in event.object.text:
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Работаю!", "random_id": 0
                                            })

                if "Positive" in event.object.text:
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Работаю!", "random_id": 0
                                                })
                if "Primary" in event.object.text:
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Работаю!", "random_id": 0
                                                })
                if "Secondary" in event.object.text:
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Работаю!", "random_id": 0
                                                })
                
                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "банлист":
                    if event.object.from_id in adminlist:

                        

                        res222 = client.run("banlist players")
                        res111 = res222.replace("There", "")
                        res333 = res111.replace("are", "")
                        res444 = res333.replace("bans", "игрока в бане")
                        res555 = res444.replace("was", "был")
                        res666 = res555.replace("banned", "забанен")
                        res777 = res666.replace("by", "")
                        res888 = res777.replace("Banned", "")
                        res999 = res888.replace("an", "")
                        res1111 = res999.replace("operator", "")
                         
                        
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": (res1111),
                                                    "random_id": 0})

                        
                        
                
                            
                        



                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "title":
                    if event.object.from_id in adminlist:

                        messageget11 = event.object.text

                        startcom = 'title @a title {"text":"textforreplace","bold":true, "color" : "red"}'
                        textresultmestitle = messageget11.replace("title", "")
                        resulcomoc = startcom.replace("textforreplace", (textresultmestitle))
                         
                        
                           
                         
                        

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "готово !",
                                                    "random_id": 0})


                        client.run(resulcomoc)

                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "say":
                    if event.object.from_id in adminlist:

                        messageget = event.object.text
                         

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Отправил!",
                                                    "random_id": 0})

                         
                            
                        client.run(str(messageget))


                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "whitelist":
                    if event.object.from_id in adminlist:

                        messageget2 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Готово!",
                                                    "random_id": 0})
                        
                        
                            
                        client.run(messageget2) 


                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "time":
                    if event.object.from_id in adminlist:

                        messageget55 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Готово!",
                                                    "random_id": 0})
                        
                        
                            
                        client.run(messageget55) 



                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "op":
                    if event.object.from_id in adminlist:

                        messageget3 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Сделано!",
                                                    "random_id": 0})
                        
                       
                            
                        client.run(messageget3)
        

                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "deop":
                    if event.object.from_id in adminlist:

                        messageget4 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Сделано!",
                                                    "random_id": 0})
                        
                        
                            
                        client.run(messageget4)


                if event.object.text.lower() == "seed":
                    if event.object.from_id in adminlist:

                        messageget4 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Держи!",
                                                    "random_id": 0})
                        
                       
                            
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": ((client.seed)),
                                                    "random_id": 0})


                if event.object.text.lower() == "онлайн":
                    if event.object.from_id in adminlist:

                        messageget4 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Вот!",
                                                    "random_id": 0})
                        
                        
                            
                        an2 = (client.players.online)
                        if an2<1:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "На сервере нет игроков!",
                                                "random_id": 0})

                        else:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": str(an2),
                                                    "random_id": 0})


                if event.object.text.lower() == "онлайни":
                    if event.object.from_id in adminlist:

                        messageget4 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Вот!",
                                                    "random_id": 0})
                        
                       

                        an = (client.players.names)

                        if client.players.online<1:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "На сервере нет игроков!",
                                                "random_id": 0})
                        else:
                            ana = str(an)

                            res1 = (ana.replace("(", ""))
                            res2 = (res1.replace(")", ""))
                            res3 = (res2.replace("[", ""))
                            res4 = (res3.replace("]", ""))
                            res5 = (res4.replace("'", ""))
                            res6 = (res5.replace(",", "\n"))

                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": str(res6),
                                                    "random_id": 0})
                
            
                if event.object.text.lower() == "команды":
                    if event.object.from_id in adminlist:

                        messageget4 = event.object.text

                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "say [сообщение]\nwhitelist [команда]\nop [ник]\ndeop [ник]\nseed\nонлайн\nонлайни\nкоманды\nвайтлистлист\nban [ник]\npardon [ник]\nkick [ник]\nбанлист\ntitle [текст]\ntime\nrun ",
                                                    "random_id": 0})


                if event.object.text.lower() == "вайтлистлист":
                    if event.object.from_id in adminlist:

                        messageget5 = event.object.text

                        res222 = client.run("whitelist list")
                        res111 = res222.replace("There", "")
                        res333 = res111.replace("are", "")
                        res444 = res333.replace("whitelisted", "игрок в вайтлисте")
                        res555 = res444.replace("players", "")
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": (res555),
                                                    "random_id": 0})


                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "ban":
                    if event.object.from_id in adminlist:

                        messageget6 = event.object.text
                        
                        
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "бан!",
                                                    "random_id": 0})


                        client.run(messageget6)

                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "pardon":
                    if event.object.from_id in adminlist:

                        messageget7 = event.object.text
                        
                        client.run(messageget7)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Всё!",
                                                    "random_id": 0})     

                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "kick":
                    if event.object.from_id in adminlist:

                        messageget8 = event.object.text
                        
                        client.run(messageget8)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "кик!!",
                                                    "random_id": 0}) 
                
                if event.object['text'].lower().split(" ", maxsplit=1)[0] == "tp":
                    if event.object.from_id in adminlist:

                        messageget9 = event.object.text
                        
                        
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "уже готово !",
                                                    "random_id": 0}) 

                        client.run(messageget9)
                


                         
                        
                        
                

               
           

