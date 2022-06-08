

def get_pass_1 ():       # Генерация ключей доступа
    import random
    ps = ''
    strSM = "01234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvnm"
    for number1 in range(7):
        rn = random.randint(0,len(strSM))
        ps = ps + strSM[rn:rn+1]
    return ps   

def get_pass_2 ():       # Генерация ключей доступа
    import random
    ps = ''
    strSM = "01234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvnm"
    for number1 in range(9):
        rn = random.randint(0,len(strSM))
        ps = ps + strSM[rn:rn+1]
    return ps   

def get_pass_3 ():       # Генерация ключей доступа
    import random
    ps = ''
    strSM = "01234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvnm"
    for number1 in range(12):
        rn = random.randint(0,len(strSM))
        ps = ps + strSM[rn:rn+1]

    strSM = "!@#$%*"
    for number1 in range(1):
        rn = random.randint(0,len(strSM))
        ps = ps + strSM[rn:rn+1]
    return ps   



def get_message (user_id,namebot,nomer):
    import iz_telegram

    if nomer == 1:
        password = get_pass_1 ()
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        comd11 = 'pasword_1'
        menu11 = "<<"
        mn11   = types.InlineKeyboardButton(text=menu11,callback_data=comd11)
        comd13 = 'pasword_save_'+str(password)
        menu13 = "Сохранить"
        mn13   = types.InlineKeyboardButton(text=menu13,callback_data=comd13)
        comd14 = 'pasword_2'
        menu14 = ">>"
        mn14   = types.InlineKeyboardButton(text=menu14,callback_data=comd14)
        markup.add(mn11,mn13,mn14)

    if nomer == 2:
        password = get_pass_2 ()
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        comd11 = 'pasword_2'
        menu11 = "<<"
        mn11   = types.InlineKeyboardButton(text=menu11,callback_data=comd11)
        comd13 = 'pasword_save_'+str(password)
        menu13 = "Сохранить"
        mn13   = types.InlineKeyboardButton(text=menu13,callback_data=comd13)
        comd14 = 'pasword_3'
        menu14 = ">>"
        mn14   = types.InlineKeyboardButton(text=menu14,callback_data=comd14)
        markup.add(mn11,mn13,mn14)

    if nomer == 3:
        password = get_pass_3 ()
        from telebot import types
        markup = types.InlineKeyboardMarkup(row_width=4)
        comd11 = 'pasword_2'
        menu11 = "<<"
        mn11   = types.InlineKeyboardButton(text=menu11,callback_data=comd11)
        comd13 = 'pasword_save_'+str(password)
        menu13 = "Сохранить"
        mn13   = types.InlineKeyboardButton(text=menu13,callback_data=comd13)
        comd14 = 'pasword_3'
        menu14 = ">>"
        mn14   = types.InlineKeyboardButton(text=menu14,callback_data=comd14)
        markup.add(mn11,mn13,mn14)

    message_out,menu = iz_telegram.get_message (user_id,'Вывести пароль набор',namebot)
    message_out = message_out.replace('%%Пароль%%',str(password))   
    return message_out,markup
        
def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_telegram 
    label = "Yes"

    if message_in == 'Создать пароль':
        label = "No"
        message_out,markup = get_message (user_id,namebot,1)
        print ('[+]',message_out)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''

    if message_in.find ('pasword_save_') != -1:
        label = "No"        
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''
        import iz_func
        db,cursor = iz_func.connect ()
        word = message_in.replace('pasword_save_','')
        sql = "INSERT INTO password_save (about,name,user_id,status) VALUES ('{}','{}','{}','{}')".format ('',word,user_id,'')
        cursor.execute(sql)
        db.commit()        
        lastid = cursor.lastrowid
        db.close
        iz_telegram.save_variable (user_id,namebot,"status",'save_word_'+str(lastid)) 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Пароль сохранен в базе данных",'S',0) 

    if message_in == 'Мой список':
        label = "No"        
        db,cursor = iz_func.connect ()
        #message_out,markup = get_message (user_id,namebot,1)
        message_out,menu = iz_telegram.get_message (user_id,'Мой список вывод',namebot)
        sql = "select id,name,about from password_save where user_id = '{}'  and status <> 'delete'  ;".format(user_id)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close
        id = 0
        for rec in data: 
            id,name,about = rec.values() 
            message_out = message_out + name +' -  <code>'+ about + '</code>\n'
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''

    if message_in == '/help':
        label = "No"        
        message_out,menu = iz_telegram.get_message (user_id,'Помощь',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)   


    if message_in == '/delete':
        label = "No"        
        db,cursor = iz_func.connect ()
        #message_out,markup = get_message (user_id,namebot,1)
        message_out,menu = iz_telegram.get_message (user_id,'Мой список вывод',namebot)
        sql = "select id,name,about from password_save where user_id = '{}' and status <> 'delete' ;".format(user_id)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close
        id = 0
        for rec in data: 
            id,name,about = rec.values() 
            message_out = message_out + name +' -  <code>'+ about + '</code> (/delete_'+str(id)+')\n'
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''        
        #message_out,menu = iz_telegram.get_message (user_id,'Удалить',namebot)
        #markup = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)   
        db.close


    if message_in.find('/delete_') != -1:
        label = "No"        
        word = message_in.replace('/delete_','')
        db,cursor = iz_func.connect ()
        sql = "UPDATE password_save SET status = 'delete' WHERE `id` = "+str(word)+""
        print ('[sql]',sql)
        cursor.execute(sql)
        db.commit()  
        db.close   
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Удаление",'S',0)   

    if message_in == 'pasword_1':
        label = "No"
        message_out,markup = get_message (user_id,namebot,1)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''

    if message_in == 'pasword_2':
        label = "No"        
        message_out,markup = get_message (user_id,namebot,2)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''

    if message_in == 'pasword_3':
        label = "No"        
        message_out,markup = get_message (user_id,namebot,3)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''


    if status.find ('save_word_') != -1 and label == "Yes":
        import iz_func
        db,cursor = iz_func.connect ()
        word = status.replace('save_word_','')
        sql = "UPDATE password_save SET about = '"+str(message_in)+"' WHERE id = "+str(word)+""
        print ('[+] sql',sql)
        cursor.execute(sql)
        db.commit()        
        db.close
        iz_telegram.save_variable (user_id,namebot,"status",'')
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Информация по паролю обновлена",'S',0)         

