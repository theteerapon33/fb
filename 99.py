# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate


cl = LINETCR.LINE()
cl.login(qr=True)
#cl.login(token="EnIPg4tThACAoRXylxd9.szDkFhIVNZQp7d4DX8zgQq.o3cWl/9BNrV1n+Vvd6B0N1IVgTx8AKGqr26BnpMJIOo=")
cl.loginResult()
#vidia
#kt = LINETCR.LINE()
#kt.login(token="EmcHKy7OJP3IChWh89o7.w2t8Z9Xjv6gelJSDmXaO9W.kOJqwINfM0b5vU/Ocd3Op8uggQ8fmC9YIrcc8RJotjI=")
#kt.loginResult()
#rosetta
#ks = LINETCR.LINE()
#ks.login(token="EmxkNlZXeYujhwzsihX4.sGaMXmjviJMROq5S4Cc39a.y4PKP22mOaCCA1aqFRLgrFI3zzzOhfWREzUhV0eK8iw=")
#ks.loginResult()
#sirvelmist
#ki = LINETCR.LINE()
#ki.login(token="EmLT4QmZDTOhuT3YWa8e.6xqhRUmgRAnJkNHgUf9pRG.cYeoV8xeMhVTFMGG+QWH1qaVB6vmO0kcF5z0yVr4dGE=")
#ki.loginResult()
#fawn
#kk = LINETCR.LINE()
#kk.login(token="Em12iy3uGiMtThUdUeF0.1fr9c+yGB9KiIPMXgRT+aa.X7rZOQsgp+nDs2Xx5tJJ9Z6HGyfI+Mo347UPGpoCsx0=")
#kk.loginResult()
#iridessa
#kc = LINETCR.LINE()
#kc.login(token="EmcRs7TR2ZTODz50pVq9.uxyX0wPToHk+Po1M6IzIIq.+2sr01OPoP41ner8K4FDgth0WhL9ye+o+wKhrHV/bHw=")
#kc.loginResult()

#kicker ghost
#kl = LINETCR.LINE()
#kl.login(token="")
#kl.loginResult()

print "Bffff"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage= """\n
=======================
=======================\n

"""
KAC=[cl]#,ki,kk,kc,ks,kt]
mid = cl.getProfile().mid
#Amid = ki.getProfile().mid
#Bmid = kk.getProfile().mid
#Cmid = kc.getProfile().mid
#Dmid = ks.getProfile().mid
#Emid = kt.getProfile().mid
#Fmid = kl.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid]#,Amid,Bmid,Cmid,Dmid,Emid]
admin = ["u832d6b22ecdb23a673a2ae6a8784f714",""]
staff = ["u49974a7c78af9f3a8fec3e1dc7c646a9",""]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me",
    "lang":"JP",
    "comment":"AutoLike by ayana",
    "welmsg":"welcome to group",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "welcomemsg":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus



def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


def bot2(op):
    try:
        if op.type == 0:
            return
        # ------Protect Group Kick start------#
        if op.type == 11:
            if wait["Protectgr"] == True:
                if op.param2 not in Bots:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(DEF).kickoutFromGroup(op.param1, [op.param2])
                    random.choice(DEF).updateGroup(G)
        # ------Protect Group Kick finish-----#

        # ------Cancel Invite User start------#
        if op.type == 13:
            if wait["Protectcancl"] == True:
                if op.param2 not in Bots:
                    group = ki.getGroup(op.param1)
                    gMembMids = [contact.mid for contact in group.invitee]
                    random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        # ------Cancel Invite User Finish------#

        # ------Joined User Kick start------#
        if op.type == 17:
            if wait["Protectjoin"] == True:
                if op.param2 not in Bots:
                    random.choice(DEF).kickoutFromGroup(op.param1, [op.param2])

        # ------Joined User Kick start------#

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        if op.type == 17:
            group = cl.leaveGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param3).displayName + " \n\n[ขอไห้คุณโชคดี..]\n\n " + group.name
            cl.sendMessage(cb)

        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName + " \n\n[ยินดีต้อนรับเข้ากลุ่ม]\n\n " + group.name
            cl.sendMessage(cb)




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        if op.type == 13:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1], list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to, "error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid=" + mid + "&postId=" + "new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to, "already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to, "decided not to comment")

                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to, "deleted")
                        ki.sendText(msg.to, "deleted")
                        kk.sendText(msg.to, "deleted")

                        wait["dblack"] = False

                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to, "It is not in the black list")
                        ki.sendText(msg.to, "It is not in the black list")
                        kk.sendText(msg.to, "It is not in the black list")

                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to, "already")
                        ki.sendText(msg.to, "already")
                        kk.sendText(msg.to, "already")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to, "aded")
                        ki.sendText(msg.to, "aded")
                        kk.sendText(msg.to, "aded")

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to, "deleted")
                        ki.sendText(msg.to, "deleted")
                        kk.sendText(msg.to, "deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to, "It is not in the black list")
                        ki.sendText(msg.to, "It is not in the black list")
                        kk.sendText(msg.to, "It is not in the black list")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to, msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" +msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to, "[displayName]:\n" + contact.displayName + "\n[mid]:\n" +msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to, msg.text)
            elif msg.text is None:
                return
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Key", "help", "Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage)
                else:
                    cl.sendText(msg.to, helpt)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ", "")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to, "It can't be used besides the group.")

            elif ("เปลี่ยนชื่อกลุ่ม " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("เปลี่ยนชื่อกลุ่ม ", "")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to, "It can't be used besides the group.")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ", "")
                cl.kickoutFromGroup(msg.to, [midd])

            elif "เตะ " in msg.text:
                midd = msg.text.replace("เตะ ", "")
                cl.kickoutFromGroup(msg.to, [midd])


            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif "เชิญ " in msg.text:
                midd = msg.text.replace("เชิญ ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["คท"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "All gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["cancel", "Cancel", "ยกเชิญ"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "No one is inviting")
                        else:
                            cl.sendText(msg.to, "Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Ourl", "Link on", "เปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "ลิ้งเปิด")
                    else:
                        cl.sendText(msg.to, "already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")

            elif msg.text in ["Curl", "Link off", "ปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "ลิ้งปิด")
                    else:
                        cl.sendText(msg.to, "already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "jointicket " in msg.text.lower():
                rplace = msg.text.lower().replace("jointicket ")
                if rplace == "on":
                    wait["atjointicket"] = True
                elif rplace == "off":
                    wait["atjointicket"] = False
                cl.sendText(msg.to, "Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links = []
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group = cl.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.id, ticket_id)
                        cl.sendText(msg.to, "Sukses join ke grup %s" % str(group.name))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to, "[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to, "[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to, "[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nสมาชิก:" + str(len(ginfo.members)) + "คน\npending:" + sinvitee + "เชิญค้างอยู่\nURL:" + u + "ลิ้งกลุ่ม")
                    else:
                        cl.sendText(msg.to, "[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Id" == msg.text:
                cl.sendText(msg.to, msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to, mid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to, mid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "100",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "10",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "9",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "7",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "6",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "4",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "3",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "110",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "101",
                    "STKPKGID": "1",
                    "STKVER": "100"}
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                    "STKID": "247",
                    "STKPKGID": "3",
                    "STKVER": "100"}
                ki.sendMessage(msg)
                kk.sendMessage(msg)

            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:", "")
                cl.sendText(msg.to, "line://home/post?userMid=" + mid + "&postId=" +
                            cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ", "")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "name " + string + " done")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:", "")
                msg.contentType = 13
                msg.contentMetadata = {"mid": mmid}
                cl.sendMessage(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Joinn on", "joinn on", "เข้ากลุ่มออน"]:
                if msg.from_ in admin:
                    if wait["Protectjoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group On")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectjoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group On")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Joinn off", "joinn off", "เข้ากลุ่มออฟ"]:
                if msg.from_ in admin:
                    if wait["Protectjoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group Off")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectjoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "kick Joined Group Off")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Cancl on", "cancl on", "เชิญออน"]:
                if msg.from_ in admin:
                    if wait["Protectcancl"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited On")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectcancl"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited On")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Cancl off", "cancl off", "เชิญออฟ"]:
                if msg.from_ in admin:
                    if wait["Protectcancl"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited Off")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectcancl"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Cancel All Invited Off")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Gr on", "gr on", "ลบออน"]:
                if msg.from_ in admin:
                    if wait["Protectgr"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group On")
                        else:
                            cl.sendtext(msg.to, "done")
                    else:
                        wait["Protectgr"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group On")
                        else:
                            cl.sendText(msg.to, "done")

            elif msg.text in ["Gr off", "gr off", "ลบออฟ"]:
                if msg.from_ in admin:
                    if wait["Protectgr"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group Off")
                        else:
                            cl.sendText(msg.to, "done")
                    else:
                        wait["Protectgr"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Protect Group Off")
                        else:
                            cl.sendText(msg.to, "done")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Invite cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Invite cancel:", "")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "The group of people canceled off.❗")
                        else:
                            cl.sendText(msg.to, "关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num = int(strnum)
                        wait["leaveRoom"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "done..❗")
                        else:
                            cl.sendText(msg.to, strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "al ready on。")
                    else:
                        cl.sendText(msg.to, "价值奇怪。")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "leave on already❗")
                    else:
                        cl.sendText(msg.to, "already on❗")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "Done..❗")

            elif msg.text in ["Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "leave off already❗")
                    else:
                        cl.sendText(msg.to, "already off❗")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "要了开。")

            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "already on❗")
                    else:
                        cl.sendText(msg.to, "Done..❗")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "要了开。")

            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "already on❗")
                    else:
                        cl.sendText(msg.to, "Done..❗")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Done..❗")
                    else:
                        cl.sendText(msg.to, "要了关断。")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Set"]:
                md = ""
                if wait["Protectjoin"] == True:md += "[􀔃􀆑lock􏿿  Block Join]\n"
                else:md += " [Block Join Off]\n"
                if wait["Protectgr"] == True:md += "[􀔃􀆑lock􏿿   Block Group]\n"
                else:md += " [Block Group Off]\n"
                if wait["Protectcancl"] == True:md += "[􀔃􀆑lock􏿿 Cancel All Invited]\n"
                else:md += " [Cancel All Invited Off]\n"
                if wait["contact"] == True:md += " [Contact    : on]\n"
                else:md += " [Contact    : off]\n"
                if wait["autoJoin"] == True:md += " [Auto join : on]\n"
                else:md += " [Auto join : off]\n"
                if wait["autoCancel"]["on"] == True:md += " Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else:md += " [Group cancel : off]\n"
                if wait["leaveRoom"] == True:md += " [Auto leave    : on]\n"
                else:md += " [Auto leave : off]\n"
                if wait["timeline"] == True:md += " [Share   : on]\n"
                else:md += " [Share   : off]\n"
                if wait["autoAdd"] == True:md += " [Auto add : on]\n"
                else:md += " [Auto add : off]\n"
                if wait["commentOn"] == True:md += " [Comment : on]\n"
                else:md += " [Comment : off]\n"
                cl.sendText(msg.to, md)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Clock on", "Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to, "already on❗")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2, "(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "done。")
            elif msg.text in ["Clock off", "Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to, "already on❗")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to, "done..❗")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Message change:" in msg.text:
                wait["message"] = msg.text.replace("Massage add change:", "")
                cl.sendText(msg.to, "The message was changed。")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:", "")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, "done..❗")
                else:
                    cl.sendText(msg.to, "变更了信息。")
            elif msg.text in ["Check add", "Com"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, "It is Massage auto add:" + wait["message"])
                else:
                    cl.sendText(msg.to, "Bot Phet hack bot\n\n" + wait["message"])
            elif msg.text in ["言語変更", "言語變更"]:
                if wait["lang"] == "JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to, "切換中國語。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to, "言語を日本語にしました。")
            elif "Comment change:" in msg.text:
                c = msg.text.replace("Comment change:", "")
                if c in ["", " ", "\n", None]:
                    cl.sendText(msg.to, "The character string which can't be changed。")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to, "変更しました。\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:", "")
                if c in ["", " ", "\n", None]:
                    cl.sendText(msg.to, "String that can not be changed。")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to, "changed。\n\n" + c)
            elif msg.text in ["Comment on", "コメント：オン", "コメント:on", "自動首頁留言：開"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done。")
                    else:
                        cl.sendText(msg.to, "already on❗")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done..❗")
                    else:
                        cl.sendText(msg.to, "要了开。")
            elif msg.text in ["Comment off", "コメント：オフ", "コメント:off", "自動首頁留言：關"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done..❗")
                    else:
                        cl.sendText(msg.to, "already off❗")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "done。")
                    else:
                        cl.sendText(msg.to, "要了关断。")
            elif msg.text in ["Comment", "留言確認"]:
                cl.sendText(msg.to, "message changed to\n\n。" + str(wait["comment"]))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Gurl", "ลิ้งกลุ่ม"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to, "line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group❗")
                    else:
                        cl.sendText(msg.to, "Not for use less than group❗")

            elif "Gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→", "")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to, "line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to, "以小组以外不能使用")


            elif "ลิ้งกลุ่ม" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→", "")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to, "line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to, "以小组以外不能使用")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Blacklist"]:
                wait["wblack"] = True
                cl.sendText(msg.to, "add to comment bl❗")
            elif msg.text in ["Whitelist"]:
                wait["dblack"] = True
                cl.sendText(msg.to, "White to comment bl❗")
            elif msg.text in ["Cblacklist"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to, "confirmed❗")
                else:
                    cl.sendText(msg.to, "It is a black list。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Name clock:" in msg.text:
                n = msg.text.replace("Name clock:", "")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to, "Last name clock❗")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to, "Name clock change done.\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2, "(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "Update to refresh❗")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Bf " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Bf ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"error")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ki, kk, kc, kd]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"คุณไม่ได้ไปต่อ..")
                                    kk.sendText(msg.to,"")

            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to, "คุณอยู่ในรายชื่อสีดำ")
                        kc.sendText(msg.to, "")
                        return
                    for jj in matched_list:
                        try:
                            klist = [ki, kk, kc, kd]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to, [jj])
                            print (msg.to, [jj])
                        except:
                            pass

            elif msg.text in ["เตะ"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to, "คุณอยู่ในร่ายชื่อสีดำ")
                        kc.sendText(msg.to, "")
                        return
                    for jj in matched_list:
                        try:
                            klist = [ki, kk, kc, kd]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to, [jj])
                            print (msg.to, [jj])
                        except:
                            pass

            elif msg.text in ["Bfลบห้อง"]:
                        if msg.toType == 2:
                            if msg.from_ in admin:
                                print "[Command]Cleanse executing"
                                _name = msg.text.replace("Bfลบห้อง", "")
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                kk.sendText(msg.to, "โชคดี**")
                                kc.sendText(msg.to, "")
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                # --------------[Bot and Admin MID]----------------
                                targets.remove(adminMID)
                                targets.remove(mid)
                                targets.remove(Amid)
                                targets.remove(Bmid)
                                targets.remove(Cmid)
                                # --------------[Bot and Admin MID]----------------
                                if targets == []:
                                    ki.sendText(msg.to, "Not found.")
                                else:
                                    for target in targets:
                                        try:
                                            klist = [ki, kk, kc, kd]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to, [target])
                                            print (msg.to, [g.mid])
                                        except:
                                            ki.sendText(msg.to, "Group cleansed")
                                print "[Command]Cleanse executed"
                            else:
                                cl.sendText(msg.to, "Command denied.")
                                cl.sendText(msg.to, "Admin permission required.")
                                print "[Error]Command denied - Admin permission required"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ", "")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "ล้มเหลว")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f = codecs.open('st2__b.json', 'w', 'utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to, "กำลังตรวจสอบ")
                                except:
                                    ki.sendText(msg.to, "สำเร็จ")

            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @", "")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to, "ล้มเหลว")
                        kk.sendText(msg.to, "")
                        kc.sendText(msg.to, "")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f = codecs.open('st2__b.json', 'w', 'utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to, "แบน.....")
                                ki.sendText(msg.to, "")
                                kk.sendText(msg.to, "")
                                kc.sendText(msg.to, "")
                            except:
                                ki.sendText(msg.to, "สำเร็จ")
                                kk.sendText(msg.to, "")
                                kc.sendText(msg.to, "")

            elif "แบน @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("แบน @", "")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to, "ล้มเหลว")
                        kk.sendText(msg.to, "")
                        kc.sendText(msg.to, "")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f = codecs.open('st2__b.json', 'w', 'utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to, "แบน....")
                                ki.sendText(msg.to, "")
                                kk.sendText(msg.to, "")
                                kc.sendText(msg.to, "")
                            except:
                                ki.sendText(msg.to, "สำเร็จ")
                                kk.sendText(msg.to, "")
                                kc.sendText(msg.to, "")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Unban]ok"
                    _name = msg.text.replace("Unban @", "")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "ล้มเหลว")
                        kk.sendText(msg.to, "")
                        kc.sendText(msg.to, "")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f = codecs.open('st2__b.json', 'w', 'utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to, "แก้แบน....")
                                ki.sendText(msg.to, "")
                                kk.sendText(msg.to, "")
                                kc.sendText(msg.to, "")
                            except:
                                cl.sendText(msg.to, "สำเร็จ")
                                kk.sendText(msg.to, "")
                                kc.sendText(msg.to, "")

            elif "แก้แบน @" in msg.text:
                if msg.toType == 2:
                        print "[แก้แบน]ok"
                        _name = msg.text.replace("แก้แบน @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "ล้มเหลว")
                            kk.sendText(msg.to, "")
                            kc.sendText(msg.to, "")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f = codecs.open('st2__b.json', 'w', 'utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to, "แก้แบน....")
                                    ki.sendText(msg.to, "")
                                    kk.sendText(msg.to, "")
                                    kc.sendText(msg.to, "")
                                except:
                                    ki.sendText(msg.to, "สำเร็จ")
                                    kk.sendText(msg.to, "")
                                    kc.sendText(msg.to, "")

            elif msg.text in ["Gcancel"]:
                try:
                    strnum = msg.text.replace("Gcancel", "")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to, "å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                            num = int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to, strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "Value is wrong")
                        else:
                            cl.sendText(msg.to, "Bizarre ratings")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Ban", "แบนคท"]:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to, "ลง คท ต่อ....")

            elif msg.text in ["Unban", "แก้แบนคท"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to, "ลง คท ต่อ....")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "Tidak Ada user Blacklist")
                else:
                    cl.sendText(msg.to, "Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "ไม่มีรายชื่อสีดำ")
                    ki.sendText(msg.to, "")
                    kk.sendText(msg.to, "")
                    kc.sendText(msg.to, "")
                else:
                    cl.sendText(msg.to, "Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]: mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Me ban"]:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to, "nothing..❗")
                    else:
                        cl.sendText(msg.to, "It is a black list❗")
                        mc = ""
                        for mi_d in wait["blacklist"]:
                            mc += "・" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to, mc)

            elif msg.text in ["Check ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" + cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to, cocoa + "รายชื่อคนที่ถูกแบน..")

            elif msg.text in ["เช็คริส"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "กลุ่มนี้ไม่มีรายชื่อสีดำ")
                    ki.sendText(msg.to, "")
                    kk.sendText(msg.to, "")
                    kc.sendText(msg.to, "")
                else:
                    cl.sendText(msg.to, "รายชื่อสีดำ")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Cek ban", "เช็คแบน"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to, cocoa + "")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "ชื่อ:" in msg.text:
                    string = msg.text.replace("P1name:", "")
                    if len(string.decode('utf-8')) <= 20:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to, "name " + string + " done..❗")
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to, "name " + string + " done..❗")
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to, "name " + string + " done..❗")
                        profile = kd.getProfile()
                        profile.displayName = string
                        kd.updateProfile(profile)
                        kd.sendText(msg.to, "name " + string + " done..❗")
                        profile = ke.getProfile()
                        profile.displayName = string
                        ke.updateProfile(profile)
                        ke.sendText(msg.to, "name " + string + " done..❗")
                        profile = kf.getProfile()
                        profile.displayName = string
                        kf.updateProfile(profile)
                        kf.sendText(msg.to, "name " + string + " done..❗")
                        profile = kg.getProfile()
                        profile.displayName = string
                        kg.updateProfile(profile)
                        kg.sendText(msg.to, "name " + string + " done..❗")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif msg.text in ["Speed", "Sp", "speed"]:
                start = time.time()
                cl.sendText(msg.to, "ตรวจความเร็วบอท...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Bf@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members) // 100
                for j in xrange(k + 1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s = 0
                    d = []
                    for i in group.members[j * 100: (j + 1) * 100]:
                        d.append({"S": str(s), "E": str(s + 8), "M": i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION': json.dumps({"MENTIONEES": d})}
                    cl.sendMessage(msg)
                #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif msg.text == "ใครแอบ":
                cl.sendText(msg.to, "ตั้งเวลาตรวจสอบคนอ่าน")
                try:
                    del wait2['readPoint'][msg.to]
                    del wait2['readMember'][msg.to]
                except:
                    pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "ออกมา":
                if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        chiya = ""
                    else:
                        chiya = ""
                        for rom in wait2["ROM"][msg.to].items():
                            print rom
                            chiya += rom[1] + "\n"
                    cl.sendText(msg.to,
                                "รายชื่อคนอ่าน %s\n􀜁􀅔Har Har􏿿\n\nรายชื่อคนอ่าน\n%s􀜁􀅔Har Har􏿿\n\nฺํตรวจสอบ By:BFFFf\n[%s]" % (
                                wait2['readMember'][msg.to], chiya, setTime[msg.to]))
                else:
                    cl.sendText(msg.to, "ใช้คำสั่ง [ใครแอบ]ก่อนคับ")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "#終了" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:

                    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Cancelinvite1", "ยกเชิญ1"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to, [_mid])
                    cl.sendText(msg.to, "ยกเชิญเสำเร็จ..")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Steal dp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @", "")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to, "Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            elif msg.text in ["Test", "เทส"]:
                cl.sendText(msg.to, "บอท ใช้ได้ปกติ 😁")
# -----------------------------------------------

            elif "Hi bf" in msg.text:
                cl.sendText(msg.to, "Hi 😁")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text in ["Reject", "ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, "*********")
                else:
                    cl.sendText(msg.to, "拒绝了全部的邀请。")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            elif msg.text.lower() == 'bot restart':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to, "ทำการรีโปรแกรมเรียบร้อย")
                        restart_program()
                    except:
                        cl.sendText(msg.to, "Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'รีเซ็ทบอท':
                print "[Command]Like executed"
                try:
                    cl.sendText(msg.to, "ทำการรีโปรแกรมเรียบร้อย")
                    restart_program()
                except:
                    cl.sendText(msg.to, "Please wait")
                    restart_program()
                    pass
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname", "-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")

            elif "youtube " in msg.text.lower():
                        query = msg.text.split(" ")
                        try:
                            if len(query) == 3:
                                isi = yt(query[2])
                                hasil = isi[int(query[1]) - 1]
                                cl.sendText(msg.to, hasil)
                            else:
                                isi = yt(query[1])
                                cl.sendText(msg.to, isi[0])
                        except Exception as e:
                            cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Vidio ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif "Bff#" in msg.text:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                kk.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                kc.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                kd.acceptGroupInvitationByTicket(msg.to, Ticket)
                time.sleep(0.1)
                print "kicker ok"
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)



# ----------------------------------------------
            elif "Bye" in msg.text:
                if msg.from_ in staff:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        print "kicker ok"
                        try:
                            ki.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kd.leaveGroup(msg.to)
                            ke.leaveGroup(msg.to)
                        except:
                            pass


            elif msg.text in ["Like", "like"]:
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to, "Like post")
                    try:
                        likePost()
                    except:
                        pass

#----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
            elif "Add staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff add executing"
                        _name = msg.text.replace("Add staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.append(target)
                                    cl.sendText(msg.to, "Added to the staff list")
                                except:
                                    pass
                        print "[Command]Staff add executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif "Add Staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff add executing"
                        _name = msg.text.replace("Add Staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.append(target)
                                    cl.sendText(msg.to, "Added to the staff list")
                                except:
                                    pass
                        print "[Command]Staff add executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif "Remove Staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff remove executing"
                        _name = msg.text.replace("Remove Staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.remove(target)
                                    cl.sendText(msg.to, "Removed to the staff list")
                                except:
                                    pass
                        print "[Command]Staff remove executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif "Remove staff @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff remove executing"
                        _name = msg.text.replace("Remove staff @", "")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.remove(target)
                                    cl.sendText(msg.to, "Removed to the staff list")
                                except:
                                    pass
                        print "[Command]Staff remove executed"
                    else:
                        cl.sendText(msg.to, "Command denied.")
                        cl.sendText(msg.to, "Admin permission required.")

            elif msg.text in ["Stafflist", "stafflist"]:
                    if staff == []:
                        cl.sendText(msg.to, "The stafflist is empty")
                    else:
                        cl.sendText(msg.to, "Staff list:")
                        mc = ""
                        for mi_d in staff:
                            mc += "->" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to, mc)
                        print "[Command]Stafflist executed"

# ------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = kicker.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)



                elif op.param3 in Amid:
                    if op.param2 in Bmid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)



                elif op.param3 in Bmid:
                    if op.param2 in Cmid:
                        G = kc.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kc.updateGroup(G)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = kc.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        kc.updateGroup(G)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)



                elif op.param3 in Cmid:
                    if op.param2 in Dmid:
                        G = kd.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kd.updateGroup(G)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)
                    else:
                        G = kd.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        kd.updateGroup(G)
                        Ticket = kd.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)



                elif op.param3 in Dmid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        klist = [ki, kk, kc, kd]
                        kicker = random.choice(klist)
                        kicker.kickoutFromGroup(op.param1, [op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)



                #elif op.param3 in Emid:
                    #if op.param2 in Fmid:
                        #G = kf.getGroup(op.param1)
                        #G.preventJoinByTicket = False
                        #kf.updateGroup(G)
                        #Ticket = kf.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #ki.acceptGroupInvitationByTicket(op.param1, Ticket)
#                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
 #                       kc.acceptGroupInvitationByTicket(op.param1, Ticket)
  #                      kd.acceptGroupInvitationByTicket(op.param1, Ticket)
   #                     ke.acceptGroupInvitationByTicket(op.param1, Ticket)
    #                    kf.acceptGroupInvitationByTicket(op.param1, Ticket)
     #                   kg.acceptGroupInvitationByTicket(op.param1, Ticket)
      #                  G.preventJoinByTicket = True
       #                 kf.updateGroup(G)
        #            else:
         #               G = kf.getGroup(op.param1)
#
 #                       klist = [ki, kk, kc, kd, ke, kf, kg]
  #                      kicker = random.choice(klist)
   #                     kicker.kickoutFromGroup(op.param1, [op.param2])
#
 #                       G.preventJoinByTicket = False
  #                      kf.updateGroup(G)
   ##                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
     ##                  kk.acceptGroupInvitationByTicket(op.param1, Ticket)
       #                 kc.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               kd.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                ke.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kf.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             kg.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            G.preventJoinByTicket = True
             #           kf.updateGroup(G)



              #  elif op.param3 in Fmid:
               #     if op.param2 in Gmid:
                #        G = kg.getGroup(op.param1)
                 #       G.preventJoinByTicket = False
                  #      kg.updateGroup(G)
                   #     Ticket = kg.reissueGroupTicket(op.param1)
                    #    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                     #   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                      #  kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                       # kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #kd.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #ke.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #kf.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #kg.acceptGroupInvitationByTicket(op.param1, Ticket)
                        #G.preventJoinByTicket = True
                        #kg.updateGroup(G)
#                    else:
 #                       G = kg.getGroup(op.param1)
#
 #                       klist = [ki, kk, kc, kd, ke, kf, kg]
  #                      kicker = random.choice(klist)
   #                     kicker.kickoutFromGroup(op.param1, [op.param2])
#
 #                       G.preventJoinByTicket = False
  #                      kg.updateGroup(G)
   ##                    cl.acceptGroupInvitationByTicket(op.param1, Ticket)
     #                   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
      #                  kk.acceptGroupInvitationByTicket(op.param1, Ticket)
       #                 kc.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                kd.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               ke.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kf.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             kg.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            G.preventJoinByTicket = True
             #           kg.updateGroup(G)



#                elif op.param3 in Gmid:
 #                   if op.param2 in mid:
  #                      G = kk.getGroup(op.param1)
   #                     G.preventJoinByTicket = Fals
    #                    kk.updateGroup(G)
     #                   Ticket = kk.reissueGroupTicket(op.param1)
      #                  cl.acceptGroupInvitationByTicket(op.param1, Ticket)
       #                 ki.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                kk.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               kc.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kd.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             ke.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            kf.acceptGroupInvitationByTicket(op.param1, Ticket)
             #           kg.acceptGroupInvitationByTicket(op.param1, Ticket)
              #          G.preventJoinByTicket = True
               #         kk.updateGroup(G)
                #    else:
                 #       G = kk.getGroup(op.param1)
#
 #                       klist = [ki, kk, kc, kd, ke, kf, kg]
  #                      kicker = random.choice(klist)
   #                     kicker.kickoutFromGroup(op.param1, [op.param2])
#
 #                       G.preventJoinByTicket = False
  #                      kk.updateGroup(G)
   #                     Ticket = kk.reissueGroupTicket(op.param1)
    #                    kk.acceptGroupInvitationByTicket(op.param1, Ticket)
     #                   ki.acceptGroupInvitationByTicket(op.param1, Ticket)
      ##                 kc.acceptGroupInvitationByTicket(op.param1, Ticket)
        #                kd.acceptGroupInvitationByTicket(op.param1, Ticket)
         #               ke.acceptGroupInvitationByTicket(op.param1, Ticket)
          #              kf.acceptGroupInvitationByTicket(op.param1, Ticket)
           #             kg.acceptGroupInvitationByTicket(op.param1, Ticket)
            #            G.preventJoinByTicket = True
             #           kk.updateGroup(G)

            except:
                pass

#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                else:
                    cl.sendText
            except:
                pass


        if op.type == 59:
            print op


    except Exception as error:
        print error

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


def bot3(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)



        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("postEndUrl")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
# ---------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---------------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#---------------------------------------------------------------------------------------------------







            elif msg.text in ["Set"]:
                md = " "
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                else:md+=" Auto Join Group by Ticket : off\n"
                cl.sendText(msg.to,md)

            elif msg.text in ["Key", "help", "Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage)
                else:
                    cl.sendText(msg.to, helpt)


            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif "เชิญ " in msg.text:
                midd = msg.text.replace("เชิญ ", "")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to, [midd])

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["คท"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ", "All gift"]:
                msg.contentType = 9
                msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                       'PRDTYPE': 'THEME',
                                       'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)

            elif msg.text in ["cancel", "Cancel", "ยกเชิญ"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to, "No one is inviting")
                        else:
                            cl.sendText(msg.to, "Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Can not be used outside the group")
                    else:
                        cl.sendText(msg.to, "Not for use less than group")

            elif msg.text in ["Curl","Link off","ปิดลิ้ง"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ลิ้งปิด")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif "jointicket " in msg.text.lower():
                    rplace = msg.text.lower().replace("jointicket ")
                    if rplace == "on":
                        wait["atjointicket"] = True
                    elif rplace == "off":
                        wait["atjointicket"] = False
                    cl.sendText(msg.to, "Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(msg.text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        if wait["atjointicket"] == True:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id, ticket_id)
                            cl.sendText(msg.to, "Sukses join ke grup %s" % str(group.name))

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to,"[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nสมาชิก:" + str(len(ginfo.members)) + "คน\npending:" + sinvitee + "เชิญค้างอยู่\nURL:" + u + "ลิ้งกลุ่ม")
                    else:
                        cl.sendText(msg.to,"[ชื่อกลุ่ม]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)

            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")

            elif msg.text in ["Contact on","K on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")

            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
            elif msg.text in ["Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")

            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")

            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")

            elif msg.text in ["Comment on","コメント：オン","コメント:on","自動首頁留言：開"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done。")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Comment off","コメント：オフ","コメント:off","自動首頁留言：關"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done。")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Comment","留言確認"]:
                cl.sendText(msg.to,"message changed to\n\n。" + str(wait["comment"]))

            elif "Gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"以小组以外不能使用")


            elif "ลิ้งกลุ่ม" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"以小组以外不能使用")

            elif msg.text in ["Clock on","Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on❗")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done。")
            elif msg.text in ["Clock off","Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already on❗")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done..❗")



            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update to refresh❗")

            elif msg.text in ["Check ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" + cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to, cocoa + "รายชื่อคนที่ถูกแบน..")

            elif msg.text in ["เช็คริส"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "กลุ่มนี้ไม่มีรายชื่อสีดำ")
                    ki.sendText(msg.to, "")
                    kk.sendText(msg.to, "")
                    kc.sendText(msg.to, "")
                else:
                    cl.sendText(msg.to, "รายชื่อสีดำ")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" + cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, mc)

            elif msg.text in ["Cek ban", "เช็คแบน"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list += filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to, cocoa + "")



            elif msg.text in ["Test", "เทส"]:
                cl.sendText(msg.to, "บอท ใช้ได้ปกติ 😁")
#-----------------------------------------------

            elif "Hi bf" in msg.text:
                cl.sendText(msg.to, "Hi 😁")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Speed", "Sp", "speed"]:
                start = time.time()
                cl.sendText(msg.to, "ตรวจความเร็วบอท...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))


            elif msg.text in ["Cancelinvite1", "ยกเชิญ1"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to, [_mid])
                    cl.sendText(msg.to, "ยกเชิญเสำเร็จ..")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif msg.text in ["Bf@", "Tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]

                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)

                    cb += """{"S":""" + json.dumps(str(strt)) + ""","E":""" + json.dumps(
                        str(akh)) + ""","M":""" + json.dumps(md) + "},"""

                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"

                cb = (cb[:int(len(cb) - 1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata = {'MENTION': '{"MENTIONEES":[' + cb + ']}', 'EMTVER': '4'}

                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error

            elif msg.text == "ใครแอบ":
                cl.sendText(msg.to, "ตั้งเวลาตรวจสอบคนอ่าน")
                try:
                    del wait2['readPoint'][msg.to]
                    del wait2['readMember'][msg.to]
                except:
                    pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "ออกมา":
                if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        chiya = ""
                    else:
                        chiya = ""
                        for rom in wait2["ROM"][msg.to].items():
                            print rom
                            chiya += rom[1] + "\n"

                    cl.sendText(msg.to,"รายชื่อคนอ่าน %s\n􀜁􀅔Har Har􏿿\n\nรายชื่อคนอ่าน\n%s􀜁􀅔Har Har􏿿\n\nฺํตรวจสอบ By:BFFFf\n[%s]" % (wait2['readMember'][msg.to], chiya, setTime[msg.to]))
                else:
                    cl.sendText(msg.to, "ใช้คำสั่ง [ใครแอบ]ก่อนคับ")



        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ks.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kt.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ks.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kt.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot2(Op),bot3(Op)
