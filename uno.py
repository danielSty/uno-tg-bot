import telebot
import ast
import time
import random
from telebot import types
from emoji import emojize


group=00000
bot = telebot.TeleBot("923980103:AAH8qayGZgKB8n10ykPctc0HsCOsrGwutwo")
player={}
gameongoing=False
deck=['red_0', 'red_1', 'red_2', 'red_3', 'red_4', 'red_5', 'red_6', 'red_7', 'red_8', 'red_9', 'red_+2', 'red_reverse', 'red_skip', 'blue_0', 'blue_1', 'blue_2', 'blue_3', 'blue_4', 'blue_5', 'blue_6', 'blue_7', 'blue_8', 'blue_9', 'blue_+2', 'blue_reverse', 'blue_skip', 'yellow_0', 'yellow_1', 'yellow_2', 'yellow_3', 'yellow_4', 'yellow_5', 'yellow_6', 'yellow_7', 'yellow_8', 'yellow_9', 'yellow_+2', 'yellow_reverse', 'yellow_skip', 'green_0', 'green_1', 'green_2', 'green_3', 'green_4', 'green_5', 'green_6', 'green_7', 'green_8', 'green_9', 'green_+2', 'green_reverse', 'green_skip', 'red_1', 'red_2', 'red_3', 'red_4', 'red_5', 'red_6', 'red_7', 'red_8', 'red_9', 'red_+2', 'red_reverse', 'red_skip', 'blue_1', 'blue_2', 'blue_3', 'blue_4', 'blue_5', 'blue_6', 'blue_7', 'blue_8', 'blue_9', 'blue_+2', 'blue_reverse', 'blue_skip', 'yellow_1', 'yellow_2', 'yellow_3', 'yellow_4', 'yellow_5', 'yellow_6', 'yellow_7', 'yellow_8', 'yellow_9', 'yellow_+2', 'yellow_reverse', 'yellow_skip', 'green_1', 'green_2', 'green_3', 'green_4', 'green_5', 'green_6', 'green_7', 'green_8', 'green_9', 'green_+2', 'green_reverse', 'green_skip','black_轉色','black_轉色','black_轉色','black_轉色','black_轉色+4','black_轉色+4','black_轉色+4','black_轉色+4']
display={"red":emojize(':heart:', use_aliases=True),"green":emojize(':green_heart:', use_aliases=True),"yellow":emojize(':yellow_heart:', use_aliases=True),"blue":emojize(':blue_heart:', use_aliases=True),"black":emojize(':black_heart:', use_aliases=True)}
a=1
direction={1:"&#x2193;",-1: "&#x2191;"}
try_to_play_list=[]
on_desk_list=[]
drawongoing=False
def card_renew():
    if len(deck_play)==0:
        for i in range(len(on_desk_list)-2):
            deck_play.append(on_desk_list[0])
            on_desk_list.pop(0)
def start_me():
    markup = types.InlineKeyboardMarkup()
    
        
       
    markup.add(types.InlineKeyboardButton(text="start me",
                                          
                                              url="tg://resolve?domain=ds_uno_bot&start=923980103:AAH8qayGZgKB8n10ykPctc0HsCOsrGwutwo"),
                                         
               
        )
    return markup        
def card_on_hand():
    global playerdeck
    global player_id
    global current_playeri
    markup = types.InlineKeyboardMarkup()
    for i in playerdeck[player_id[current_playeri]]:
       
       
       markup.add(types.InlineKeyboardButton(text=display[i.split("_")[0]]+" "+i.split("_")[1],
                                              callback_data="['played', '" + i + "']"),
        )
    markup.add(types.InlineKeyboardButton(text="攞牌",
                                              callback_data="['played', '" + "take" + "']"),
        )
    markup.add(types.InlineKeyboardButton(text="完成",
                                              callback_data="['played', '" + "done" + "']"),
        )
    

    return markup
def card_cut():
    global playerdeck
    global player_id
    global current_playeri
    markup = types.InlineKeyboardMarkup()
    for i in playerdeck[player_id[current_playeri]]:
       
       
       markup.add(types.InlineKeyboardButton(text=display[i.split("_")[0]]+" "+i.split("_")[1],
                                              callback_data="['cut', '" + i + "']"),
        )
    

    return markup
def change_colour():
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text=display["red"],
                                              callback_data="['colour', '" + "red" + "']"),
        )
    markup.add(types.InlineKeyboardButton(text=display["yellow"],
                                              callback_data="['colour', '" + "yellow" + "']"),
        )
    markup.add(types.InlineKeyboardButton(text=display["green"],
                                              callback_data="['colour', '" + "green" + "']"),
        )
    markup.add(types.InlineKeyboardButton(text=display["blue"],
                                              callback_data="['colour', '" + "blue" + "']"),
        )
    

    return markup
def play_now():
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="出",
                                              callback_data="['after_draw', '" + "yes" + "']"),
        )
    markup.add(types.InlineKeyboardButton(text="留喺手",
                                              callback_data="['after_draw', '" + "no" + "']"),
        )
    

    return markup
def join_game(f_id,c_id,name):  
    global group
    global player
    print (f_id)


    if not f_id in player:
          
         try:
             bot.send_message(chat_id=f_id,
                     text="你已經成功加入咗遊戲喇&#x1f60c;",
                     parse_mode='HTML'
                         )
             bot.send_message(chat_id=group,
                     text="【<a href='tg://user?id="+str(f_id)+"'>"+name+"</a>】加入咗遊戲",
                     parse_mode='HTML'
                         )
             player[f_id]=name
             print(player)
             
             
         except:  
              bot.send_message(chat_id=group,
                     text="【{}】你都未 start我 點同你玩啊 快啲撳下面粒掣啟動我再返嚟 /join 啦🤪".format("<a href='tg://user?id="+str(f_id)+"'>"+name+"</a>"),
                  reply_markup=start_me(),
                  parse_mode='HTML'
                         )
@bot.message_handler(commands=['startgame'])
def handle_command_adminwindow(message):
 global gameongoing
 print("hi")
 if gameongoing==False:
    print("hi")
    if message.chat.id<0:
     global group
     if not group == message.chat.id:
        
        group=message.chat.id
        f_id=message.from_user.id
        bot.send_message(chat_id=group,
                     text="有條垃圾【<a href='tg://user?id="+str(f_id)+"'>"+message.from_user.first_name+"</a>】開咗個新嘅uno game\n快啲打 /join 一齊玩啦🥳🥳🥳",
                     parse_mode='HTML',
                    
                    )
        join_game(message.from_user.id,message.chat.id,message.from_user.first_name)
        
          
        global x
        x=177
        while x>0:
         time.sleep(1)
         if x==90 or x==60 or x==30:
             bot.send_message(chat_id=group,
                     text="仲有"+str(x)+"秒就開始遊戲，快啲加入遊戲啦🥳",
                     parse_mode='HTML'
                         )
             
         x=x-1
        print(message.from_user.id)
        print(message.from_user.first_name)
        gameongoing=True
        
    
        game_start()
     else:
         join_game(message.from_user.id,message.chat.id,message.from_user.first_name)
         
    else:
        bot.send_message(chat_id=message.chat.id,
                     text="你想喺邊度玩啊&#10067;\n去grp度打呢個command啦&#9989;",
                     parse_mode='HTML'
                         )
@bot.message_handler(commands=['extend'])
def handle_command_adminwindow(message):
 global gameongoing
 if gameongoing==False:   
  if message.chat.id<0: 
    global x
    x=x+30
    bot.send_message(chat_id=group,
                     text="加入時間多咗30秒,而家仲有"+str(x)+"秒就開始遊戲，快啲加入遊戲啦🥳",
                     parse_mode='HTML'
                         )
  else:
        bot.send_message(chat_id=message.chat.id,
                     text="呢個command只可以喺group度用㗎咋&#128558;\n去grp度打呢個command啦&#9989;",
                     parse_mode='HTML'
                         )
@bot.message_handler(commands=['join'])
def handle_command_adminwindow(message):
 global gameongoing
 if gameongoing==False:
  if message.chat.id<0: 
   join_game(message.from_user.id,message.chat.id,message.from_user.first_name)
  else:
        bot.send_message(chat_id=message.chat.id,
                     text="你想喺邊度玩啊&#10067;\n去grp度打呢個command啦&#9989;",
                     parse_mode='HTML'
                         )
@bot.message_handler(commands=['forcestart'])
def handle_command_adminwindow(message):
 if message.chat.id<0: 
    global x
    x=1
 else:
       bot.send_message(chat_id=message.chat.id,
                     text="呢個command只可以喺group度用㗎咋&#128558;\n去grp度打呢個command啦&#9989;",
                     parse_mode='HTML'
                         )

@bot.message_handler(commands=['cut'])
def handle_command_adminwindow(message):
 global cut
 global original_current_playeri
 global player_id
 if message.chat.id<0: 
    if gameongoing==True:
        if message.from_user.id in player_id:
            if cut==True:
             global current_playeri
             global msg
             global playerdeck
             print(msg.message_id)
             bot.edit_message_text(chat_id=msg.chat.id,
                                   message_id=msg.message_id,
                                   text="有條粉腸cut你牌"
                                   )
             global try_to_play_list
             playerdeck[player_id[current_playeri]]=playerdeck[player_id[current_playeri]]+try_to_play_list
             cut=False
             
             try_to_play_list=[]
             original_current_playeri=current_playeri
             current_playeri=player_id.index(message.from_user.id)
             global card_text
             card_text=""
             
             for i in playerdeck[player_id[current_playeri]]:
                  card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
             bot.send_message(chat_id=player_id[current_playeri],
                     text="你嘅手牌係:\n"+card_text+"\n\n你想cut咩牌?",
                     reply_markup=card_cut(),
                     parse_mode="HTML"
                     )
             
             
    
 else:
        bot.send_message(chat_id=message.chat.id,
                     text="呢個command只可以喺group度用㗎咋&#128558;\n去grp度打呢個command啦&#9989;",
                     parse_mode='HTML'
                         )        
@bot.message_handler(commands=['kick'])
def handle_command_adminwindow(message):
  global player_id
  global player
  global playerdeck
  global try_to_play_list
  global first_card
  global current_playeri
  global group
  global gameongoing
  global a
  global on_desk_list
  global drawongoing
  c_id=message.chat.id
  f_id=message.from_user.id
  text=message.text
  a=[int(s) for s in text.split() if s.isdigit()]
  a=a[0]
  print(a)
  if f_id==366917887 :
    player_id.remove(a)
    
    bot.send_message(chat_id=group,
                     text=player[a]+" is kicked",
                     parse_mode='HTML'
                         )
    del player[a]
    del playerdeck[a]
    try:
        try_to_play_list.clear()
        play_order()   
        bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
        player_play()
    except:
        bot.send_message(chat_id=group,
                     text=(player_text+"not enough people,game ended"),
                     parse_mode="HTML"
                     )
        group=00000
        player={}
        gameongoing=False
        a=1
        try_to_play_list=[]
        on_desk_list=[]
        drawongoing=False
    print (player_id,player,playerdeck)  
def game_start():
    global deck_play
    global player
    global player_id
    global playerdeck
    global player_text
    global current_playeri
    global a
    global first_card
    global drawongoing
    global draw_count
    global cut
    cut=False
    playerdeck={}
    player_id=[]
    deck_play=deck.copy()
    for i in player:
       player_id.append(i)
       print(player_id)
       print(len(deck_play))
       playerdeck[i]=[]
       for x in range(7):
          card_renew()  
          addcard=deck_play[random.randrange(len(deck_play))]
          playerdeck[i].append(addcard)
          deck_play.remove(addcard)
          print(deck_play)
       print(playerdeck)   
       card_text=""
       for x in playerdeck[i]:
        card_text=card_text+display[x.split("_")[0]]+" "+x.split("_")[1]+"\n"
       bot.send_message(chat_id=i,
                     text="你嘅手牌係:\n"+card_text,
                     parse_mode="HTML"
                     )   
    current_playeri=random.randrange(len(player_id))
    player_text=""
    for i in player_id:
        player_text=player_text+player[i]+"\n&#x2193;\n"
    first_card=deck_play[random.randrange(len(deck_play))]
    if first_card.split("_")[1]=="skip":
        play_order()
        print("skip")
    if first_card.split("_")[1]=="reverse":
       print("reverse")
       if len(player)<=2:
         play_order()
       else:    
          a=-a
    if first_card.split("_")[1]=="+2":
           if drawongoing==False:
                drawongoing=True
                draw_count=2
           else:
                draw_count=draw_count+2
    deck_play.remove(first_card)                           
    if first_card.split("_")[0]=="black":
            if first_card.split("_")[1]=="轉色+4":
                    if drawongoing==False:
                               drawongoing=True
                               draw_count=4
                    else:
                       draw_count=draw_count+4
            rcolour=["red","yellow","green","blue"]
            randomcoulour=rcolour[random.randrange(4)]
            first_card=first_card.replace("black",randomcoulour)
            
    
    print(player_text)
    print(first_card)
    print(player[player_id[current_playeri]])
    bot.send_message(chat_id=group,
                     text=("遊戲開始喇\n\n"+player_text+"\n\n而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n第一位玩家係"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
    
    player_play()
        

    
def player_play():
    global playerdeck
    global player_id
    global current_playeri
    global card_text
    global msg
    global cut
    
    card_text=""
    for i in playerdeck[player_id[current_playeri]]:
        card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
    msg=bot.send_message(chat_id=player_id[current_playeri],
                     text="你嘅手牌係:\n"+card_text+"\n\n你想出咩牌?",
                     reply_markup=card_on_hand(),
                     parse_mode="HTML"
                     )
    print(msg.message_id)
    cut=True

        
        
    
    
@bot.callback_query_handler(func=lambda call: True )
def handle_query(call):
    global try_to_play_list
    global playerdeck
    global player_id
    global current_playeri
    global card_text
    global first_card
    global on_desk_list
    global player_text
    global addcard
    global a
    global drawongoing
    global draw_count
    global cut
    global original_current_playeri
    
    
    checked=True
    if (call.data.startswith("['cut'")):
        cut_check=True
        valueFromCallBack = ast.literal_eval(call.data)[1]
        playerdeck[player_id[current_playeri]].remove(valueFromCallBack)
        if (valueFromCallBack.split("_")[1]=="轉色+4" or  valueFromCallBack.split("_")[1]=="轉色" or valueFromCallBack.split("_")[1]=="skip" or valueFromCallBack.split("_")[1]=="reverse" or valueFromCallBack.split("_")[1]=="+2"):
            cut_check=False
        
        if (valueFromCallBack.split("_")[0]==first_card.split("_")[0] and valueFromCallBack.split("_")[1]==first_card.split("_")[1]):
            bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先cut,出咗"+str(display[valueFromCallBack.split("_")[0]]+" "+valueFromCallBack.split("_")[1])),
                     parse_mode="HTML"
                     )
            card_text=""
            for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
            bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你成功cut完牌喇\n你而家嘅手牌係\n"+card_text)
            card_text=""
            on_desk_list.append(valueFromCallBack)
            try_to_play_list.clear()
                    
            if len(playerdeck[player_id[current_playeri]])==0:
                        end_game()
            else:
                     try_to_play_list.clear()
                     play_order()
                     first_card=on_desk_list[len(on_desk_list)-1]
                     
                     bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                     player_play()
        else:
            cut_check=False
        if cut_check==False:
                
                 bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先cut,想出"+str(display[valueFromCallBack.split("_")[0]]+" "+valueFromCallBack.split("_")[1])+"所以抽咗5隻"),
                     parse_mode="HTML"
                     )
                 if drawongoing==True:      
                   bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"cut錯要俾人draw 而家抽"+str(draw_count)+"隻"),
                     parse_mode="HTML"
                     )
                   for x in range(draw_count):
                    card_renew()   
                    addcard=deck_play[random.randrange(len(deck_play))]
                    playerdeck[player_id[current_playeri]].append(addcard)
                    deck_play.remove(addcard)
                    print(deck_play)
                   draw_count=0
                   drawongoing=False
                 playerdeck[player_id[current_playeri]].append(valueFromCallBack)
                 print (playerdeck[player_id[current_playeri]])
                 
                 for x in range(5):
                   card_renew()  
                   addcard=deck_play[random.randrange(len(deck_play))]
                   playerdeck[player_id[current_playeri]].append(addcard)
                   deck_play.remove(addcard)
                   print(deck_play)
                  
                 card_text=""
                 for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                 bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="cut錯牌 抽5隻!\n你而家嘅手牌係\n"+card_text)
                 try_to_play_list.clear()
                 print (playerdeck[player_id[current_playeri]])
                 print(len(deck_play))
                 if len(playerdeck[player_id[current_playeri]])==0:
                        end_game()
                 else:
                     try_to_play_list.clear()
                     current_playeri=original_current_playeri
                     bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                     player_play()        
    if (call.data.startswith("['played'")):
        
        valueFromCallBack = ast.literal_eval(call.data)[1]
        if not valueFromCallBack=="take":
            if not valueFromCallBack=="done":
                try_to_play_list.append(valueFromCallBack)
                playerdeck[player_id[current_playeri]].remove(valueFromCallBack)
                bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你嘅手牌係:\n"+card_text+"\n\n你想出咩牌?",
                                      reply_markup=card_on_hand())
                print(try_to_play_list)
            else:
               cut=False
               if drawongoing==True:
                   print("draw")
                   if first_card.split("_")[1]=="轉色+4":
                       if not try_to_play_list[0].split("_")[1]=="轉色+4":
                           if not (try_to_play_list[0].split("_")[1]=="+2" and try_to_play_list[0].split("_")[0]==first_card.split("_")[0]):
                            checked=False
                   elif not (try_to_play_list[0].split("_")[1]=="+2" or try_to_play_list[0].split("_")[1]=="轉色+4"):
                           checked=False
               if try_to_play_list[0].split("_")[0]==first_card.split("_")[0] or try_to_play_list[0].split("_")[1]==first_card.split("_")[1] or try_to_play_list[0].split("_")[0]=="black":
                    for i in try_to_play_list:
                      if not i.split("_")[1]==try_to_play_list[0].split("_")[1]:
                         checked=False
     
               else:
                 checked=False
               try_to_play_text=""
               for i in try_to_play_list:
                       try_to_play_text=try_to_play_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"  
               if checked==False:
                 
                 bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先想出"+str(try_to_play_text)+"所以抽咗5隻"),
                     parse_mode="HTML"
                     )
                 if drawongoing==True:      
                   bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"出唔到要俾人draw 而家抽"+str(draw_count)+"隻"),
                     parse_mode="HTML"
                     )
                   for x in range(draw_count):
                    card_renew()   
                    addcard=deck_play[random.randrange(len(deck_play))]
                    playerdeck[player_id[current_playeri]].append(addcard)
                    deck_play.remove(addcard)
                    print(deck_play)
                   draw_count=0
                   drawongoing=False
                 playerdeck[player_id[current_playeri]]=playerdeck[player_id[current_playeri]]+try_to_play_list
                 print (playerdeck[player_id[current_playeri]])
                 
                 for x in range(5):
                   card_renew()  
                   addcard=deck_play[random.randrange(len(deck_play))]
                   playerdeck[player_id[current_playeri]].append(addcard)
                   deck_play.remove(addcard)
                   print(deck_play)
                  
                 card_text=""
                 for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                 bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="出錯牌 抽5隻!\n你而家嘅手牌係\n"+card_text)
                 try_to_play_list.clear()
                 print (playerdeck[player_id[current_playeri]])
                 print(len(deck_play))
                 if len(playerdeck[player_id[current_playeri]])==0:
                        end_game()
                 else:
                     play_order()
                     try_to_play_list.clear()
                     bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                     player_play() 
               else:
                   if len(playerdeck[player_id[current_playeri]])==0:
                      if (try_to_play_list[len(try_to_play_list)-1].split("_")[1]=="轉色+4" or  try_to_play_list[len(try_to_play_list)-1].split("_")[1]=="轉色" or try_to_play_list[len(try_to_play_list)-1].split("_")[1]=="skip" or try_to_play_list[len(try_to_play_list)-1].split("_")[1]=="reverse" or try_to_play_list[len(try_to_play_list)-1].split("_")[1]=="+2"):
                          card_renew()  
                          addcard=deck_play[random.randrange(len(deck_play))]
                          playerdeck[player_id[current_playeri]].append(addcard)
                          deck_play.remove(addcard)
                          print(deck_play)
                   
                               
                   if try_to_play_list[0].split("_")[0]=="black":
                       if try_to_play_list[0].split("_")[1]=="轉色+4":
                           if drawongoing==False:
                               drawongoing=True
                               draw_count=4
                           else:
                               draw_count=draw_count+4
                       bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你而家嘅手牌係\n"+card_text+"\n你想轉咩顏色?",
                             reply_markup=change_colour(),
                                             parse_mode="HTML")
                           
                   
                   else: 
                    bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先出咗"+str(try_to_play_text)),
                     parse_mode="HTML"
                     )
                    card_text=""
                    for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                    bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你成功出完牌喇\n你而家嘅手牌係\n"+card_text)
                    card_text=""
                    for i in try_to_play_list:
                       if i.split("_")[1]=="skip":
                           play_order()
                       if i.split("_")[1]=="reverse":
                           if len(player)<=2:
                               play_order()
                           else:    
                               a=-a
                       if i.split("_")[1]=="+2":
                           if drawongoing==False:
                               drawongoing=True
                               draw_count=2
                           else:
                               draw_count=draw_count+2
                    
                    on_desk_list=on_desk_list+try_to_play_list
                    try_to_play_list.clear()
                    
                    if len(playerdeck[player_id[current_playeri]])==0:
                        end_game()
                    else:
                     try_to_play_list.clear()
                     play_order()
                     first_card=on_desk_list[len(on_desk_list)-1]
                     
                     bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                     player_play()  
        else:
            cut=False
            playerdeck[player_id[current_playeri]]=playerdeck[player_id[current_playeri]]+try_to_play_list
            print (playerdeck[player_id[current_playeri]])
            print(first_card)
            try_to_play_list.clear()
            
            if drawongoing==True:      
                   bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"出唔到要俾人draw 而家抽"+str(draw_count)+"隻"),
                     parse_mode="HTML"
                     )
                   for x in range(draw_count):
                    card_renew()  
                    addcard=deck_play[random.randrange(len(deck_play))]
                    playerdeck[player_id[current_playeri]].append(addcard)
                    deck_play.remove(addcard)
                    print(deck_play)
                    draw_count=0
                    drawongoing=False
                   card_text=""
                   for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                   bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text="你抽咗"+str(draw_count)+"隻牌\n你而家嘅手牌係\n"+card_text)
                   
                   if len(playerdeck[player_id[current_playeri]])==0:
                     end_game()
                   else:
                      try_to_play_list.clear()
                      play_order()
                      first_card=on_desk_list[len(on_desk_list)-1]
                      bot.send_message(chat_id=group,
                      text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                      parse_mode="HTML"
                       )
                      player_play()
            else:
             addcard=deck_play[random.randrange(len(deck_play))]            
             deck_play.remove(addcard)
             print(addcard)
             if addcard.split("_")[0]==first_card.split("_")[0] or addcard.split("_")[1]==first_card.split("_")[1] or addcard.split("_")[0]=="black": 
                 bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你啱啱抽到"+display[addcard.split("_")[0]]+" "+addcard.split("_")[1]+"\n你想唔想即刻出?",
                                       reply_markup=play_now(),
                                       parse_mode="HTML")
             else:
                playerdeck[player_id[current_playeri]].append(addcard)
                print(deck_play)
                card_text=""
                for i in playerdeck[player_id[current_playeri]]:
                    card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text="你抽咗一隻牌\n你而家嘅手牌係\n"+card_text)
                print (playerdeck[player_id[current_playeri]])
                print(len(deck_play))
                bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先抽咗一隻牌上手"),
                     parse_mode="HTML"
                     )
                if len(playerdeck[player_id[current_playeri]])==0:
                   end_game()
                else:
                   try_to_play_list.clear()
                   play_order()
                   bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                   player_play()
            
    if (call.data.startswith("['colour'")):
        valueFromCallBack = ast.literal_eval(call.data)[1]
        try_to_play_text=""
        for i in try_to_play_list:
                       try_to_play_text=try_to_play_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
        try_to_play_list[len(try_to_play_list)-1]=try_to_play_list[len(try_to_play_list)-1].replace("black",valueFromCallBack)
        print(try_to_play_list[len(try_to_play_list)-1])
        print(valueFromCallBack)
        print(try_to_play_list)
        
        bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先出咗"+str(try_to_play_text)+"\n轉咗做"+display[valueFromCallBack]+"色"),
                     parse_mode="HTML"
                     )
        on_desk_list=on_desk_list+try_to_play_list
        try_to_play_list.clear()
        card_text=""
        for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你成功出完牌喇\n你而家嘅手牌係\n"+card_text)
        card_text=""
        if len(playerdeck[player_id[current_playeri]])==0:
                        end_game()
        else:
                     try_to_play_list.clear()
                     play_order()
                     first_card=on_desk_list[len(on_desk_list)-1]
                     bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                     player_play()
    if (call.data.startswith("['after_draw'")):
        valueFromCallBack = ast.literal_eval(call.data)[1]
        if valueFromCallBack=="yes":
                   
                   
                   
                   if addcard.split("_")[0]=="black":
                       if addcard.split("_")[1]=="轉色+4":
                           if drawongoing==False:
                               drawongoing=True
                               draw_count=4
                           else:
                               draw_count=draw_count+4
                       try_to_play_list.append(addcard)
                       bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你而家嘅手牌係\n"+card_text+"\n你想轉咩顏色?",
                             reply_markup=change_colour(),
                                             parse_mode="HTML")
                           
                   
                   else:
                    try_to_play_text=display[addcard.split("_")[0]]+" "+addcard.split("_")[1]+"\n" 
                    bot.send_message(chat_id=group,
                    text=(player[player_id[current_playeri]]+"頭先抽咗"+str(try_to_play_text))+"上手然後即刻出咗",
                     parse_mode="HTML"
                     )   
                    on_desk_list.append(addcard)
                    bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先出咗"+str(try_to_play_text)),
                     parse_mode="HTML"
                     )
                    card_text=""
                    for i in playerdeck[player_id[current_playeri]]:
                       card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                    bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                                      text="你抽完牌即刻成功出咗\n你而家嘅手牌係\n"+card_text)
                    try_to_play_list.append(addcard)
                    for i in try_to_play_list:
                       if i.split("_")[1]=="skip":
                           play_order()
                       if i.split("_")[1]=="reverse":
                           if len(player)<=2:
                               play_order()
                           else:    
                               a=-a
                       if i.split("_")[1]=="+2":
                           if drawongoing==False:
                               drawongoing=True
                               draw_count=2
                           else:
                               draw_count=draw_count+2
                    
                    card_text=""
                    if len(playerdeck[player_id[current_playeri]])==0:
                        end_game()
                    else:
                        try_to_play_list.clear()
                        play_order()
                        first_card=on_desk_list[len(on_desk_list)-1]
                        bot.send_message(chat_id=group,
                                  text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                              parse_mode="HTML"
                                 )
                        player_play()
                   
            
        else:
                playerdeck[player_id[current_playeri]].append(addcard)
                print(deck_play)
                card_text=""
                for i in playerdeck[player_id[current_playeri]]:
                    card_text=card_text+display[i.split("_")[0]]+" "+i.split("_")[1]+"\n"
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text="你抽咗一隻牌\n你而家嘅手牌係\n"+card_text)
                print (playerdeck[player_id[current_playeri]])
                print(len(deck_play))
                bot.send_message(chat_id=group,
                     text=(player[player_id[current_playeri]]+"頭先抽咗一隻牌上手"),
                     parse_mode="HTML"
                     )
                if len(playerdeck[player_id[current_playeri]])==0:
                   end_game()
                else:
                   try_to_play_list.clear()
                   play_order()
                   first_card=on_desk_list[len(on_desk_list)-1]
                   bot.send_message(chat_id=group,
                     text=(player_text+"而家枱面上嘅牌係"+display[first_card.split("_")[0]]+" "+first_card.split("_")[1]+"\n輪到"+player[player_id[current_playeri]]+"  請去pm出牌 順次序撳好牌再撳完成就ok㗎喇\n記住出錯牌係要罰五隻㗎"),
                     parse_mode="HTML"
                     )
                   player_play()
                   
                   
def end_game():
    global group
    global player
    global gameongoing
    global a
    global try_to_play_list
    global on_desk_list
    global drawongoing
    end_text=""
    for i in player_id:
        end_text=end_text+player[i]+":"
        for x in playerdeck[i]:
             end_text=end_text+display[x.split("_")[0]]+" "+x.split("_")[1]+"  "
        end_text=end_text+"\n"
    bot.send_message(chat_id=group,
                     text=player[player_id[current_playeri]]+"出晒所有牌贏咗\n其他人剩低嘅手牌有:\n"+end_text+"\n恭喜"+player[player_id[current_playeri]],
                     parse_mode='HTML')
    
    group=00000
    player={}
    gameongoing=False
    a=1
    try_to_play_list=[]
    on_desk_list=[]
    drawongoing=False
                             
def play_order():
    global a
    global current_playeri
    global player
    global player_id
    global player_text
    if a==1:
        player_text=""
        for i in player_id:
          player_text=player_text+player[i]+"["+str(len(playerdeck[i]))+"]\n&#x2193;\n"
        if current_playeri<(len(player)-1):
                      current_playeri=current_playeri+1
        else:
                      current_playeri=0
    else:
     player_text=""
     for i in player_id:
          player_text=player_text+player[i]+"["+str(len(playerdeck[i]))+"]\n&#x2191;\n"   
     if current_playeri>0:
                      current_playeri=current_playeri-1
     else:
                      current_playeri=(len(player)-1)                  
        
    
    
         
       
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)