# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib,wikipedia,tweepy,ctypes,goslate
import re,string,os,shutil,urllib2,urllib3,subprocess
from bs4 import BeautifulSoup
from urllib import urlopen
import requests,tempfile
from gtts import gTTS
import html5lib

#kk = LINETCR.LINE()
#kk.login(qr=true)
#kk.loginResult()

cl = LINETCR.LINE()
cl.login(token="EntzqdNnUZYVIfkaEgqf.rUfb7D9I4YRXjon6FGLadW.qzHNDJfonqtTLQCc2WJ90pODzcaLEZkQeDDrRHUiG8M=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EnW6WwnT5Q3tqaoVrze8.N81Z19f9HnO5Xn8TmpC+sa.DNyBxHMZ8pKPQPiwFGCasM5zsptzMp9WxulEq/yrpdU=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EnZoFqIZLdcyeWgHDTKa.Vkaew7bAxuQ2wpRlpniLMG.ZvOJb9asqHHiAf6UlAs7Tl7qtYL1W/jQIcQQwwW4s4c=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EnkUMxkMojO6cPs9aBac.5gUMnnLdd2hpQQ39vzdhBa.0NBLnbKjToBtOqUUAhPodCR+IkLncG43YEZPoJ93Q/A=")
kc.loginResult()

cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""=====[TAUFIQ BOT v.0.48]=====

[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅]
☫[Me]
☫[My mid]
☫[Mid @]
☫[Ginfo]
☫[Respon]
☫[/pict group]
☫[/steal dp @]
☫[/steal home @]
☫[Absen]
☫[CCTV]
☫[Ciduk]
☫[/cekig]
☫[/wikipedia]
☫[Youtube]
☫[Bilang]
☫[/en]
☫[/id]
☫[Apakah...]
☫[Jodoh]
☫[Quote]
☫[Kapan...]
☫[Creator]
☫[Oi]
☫[Chant,Chant2,Chant3]
☫[Creator]

private command :
Set group = Melihat private menu"""


Setgroup =""" Private Menu 􀔃􀄆red check mark􏿿

[Protect Group]
-- Gr on/off
[Mid Via Contact]
 -- Contact on/off
[Cancel All Invited]
-- Cancl on/off
[No Joinned]
-- Joinn on/off

􀔃􀅕red arrow right􏿿 Command Private
[Set View] = Melihat proteksi bot
[Get ready] = Cek respon bot
[Gn namagroup] = Ganti nama grup
[Open url] = Membuka url grup
[Gurl] = Membuka dan mengirim url grup
[Close url] = Menutup url grup
[Cancel] = Cancel user masuk grup
[Staff add @] = Menambah user admin
[Staff remove @] = Menghapus user dari admin
[Stafflist] = Melihat daftar admin
[Ban @] = Ban target with mention
[Ban] = Ban target with send contact 
[Unban @] = Unban target with mention
[Unban] = Unban target with send contact
[Banlist] = Melihat daftar akun ter-banned
[Kill @] = Kick target banned
[Nk @] = Kick target user
[List group] = Melihat daftar grup pada bot
[Group id] = Melihat daftar id grup pada bot
[Invite mid] = Invite via mid
[inv: (gid)] = Invite admin ke group id yang dituju
[Kick mid] = Kick via mid
[My Oshi Join] = Invite semua bot
[Dadah semuanya] = Mengeluarkan semua bots assist
[Dadah yupi] = Mengeluarkan bot utama
[Maaf ya] = Mengeluarkan bot utama dari semua grup
[Bc ...] = Untuk broadcast ke semua grup
[Kernel] = Melihat kernel bot"""
KAC=[cl,ki,kk,kc]
DEF=[ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,"u46899806e905e2350f791064ace3278e"]
admin=["u46899806e905e2350f791064ace3278e"]
admsa=["u46899806e905e2350f791064ace3278e"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Terima kasih udah add aku kak\nDukung aku terus ya 􀄃􀆏moon wink􏿿\nmohon bantuannya :)",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Ard",
    "cName2":"Ard 1",
    "cName3":"Ard 2",
    "cName4":"Ard 3",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
	
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "\n・" + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
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
		
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
					
		if op.type == 32:
			if wait["Protectgr"] == True:
				if op.param2 not in Bots + admin:
					ki.findAndAddContactByMid(op.param3)
					ki.inviteIntoGroup(op.param1,[op.param3])
					ki.kickoutFromGroup(op.param1,[op.param2])
			else:
				pass

        #------Protect Group Kick start------#
        if op.type == 11:
            if wait["Protectgr"] == True:
                if ki.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        ki.reissueGroupTicket(op.param1)
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        #------Cancel Invite User Finish------#

		if op.type == 13:
			if wait["Protectcancl"] == True:
				try:
					X = ki.getGroup(op.param1)
					gInviMids = [contact.mid for contact in X.invitee]
					ki.cancelGroupInvitation(op.param1, gInviMids)
					print gInviMids + "invite canceled"
				except:
					try:
						print "Retry canceling invitation"
						X = ki.getGroup(op.param1)
						gInviMids = [contact.mid for contact in X.invitee]
						ki.cancelGroupInvitation(op.param1, gInviMids)
						print gInviMids + "invite canceled"
					except:
						print "Bot can't cancel the invitation"
		
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"
            else:
				pass
		
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

		if op.type == 15:
			group = cl.getGroup(op.param1)
			cb = Message()
			cb.to = op.param1
			cb.text = "Good bye " + cl.getContact(op.param2).displayName
			cl.sendMessage(cb)
			print op.param2 + "has left the group"
                    
        #------Joined User Kick start------#
		if op.type == 17:
			if op.param2 in wait["blacklist"]:
				try:
					ki.kickoutFromGroup(op.param1, op.param2)
				except:
					random.choice(KAC).kickoutFromGroup(op.param1, op.param2)

        if op.type == 17:
			if wait["Protectjoin"] == True:
				if op.param2 not in Bots:
					random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#

        if op.type == 19:
			print "someone was kicked"
			if op.param3 in admin:
				print "Admin has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admsa:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					try:
						cl.inviteIntoGroup(op.param1,admin)
					except:
						cl.inviteIntoGroup(op.param1,admin)
				print "Admin invited back"      

			if mid in op.param3:
				print "BOT1 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					ki.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					ki.updateGroup(G)
					Ti = ki.reissueGroupTicket(op.param1)
					cl.acceptGroupInvitationByTicket(op.param1,Ti)
					X = ki.getGroup(op.param1)
					X.preventJoinByTicket = True
					ki.updateGroup(X)
					Ti = ki.reissueGroupTicket(op.param1)
					print "BOT1 Joined"
				
			if Amid in op.param3:
				print "BOT2 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					Ti = cl.reissueGroupTicket(op.param1)
					ki.acceptGroupInvitationByTicket(op.param1,Ti)
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					print "BOT2 Joined"
				
			if Bmid in op.param3:
				print "BOT3 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					Ti = cl.reissueGroupTicket(op.param1)
					kk.acceptGroupInvitationByTicket(op.param1,Ti)
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					print "BOT3 Joined"
				
			if Cmid in op.param3:
				print "BOT4 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					Ti = cl.reissueGroupTicket(op.param1)
					kc.acceptGroupInvitationByTicket(op.param1,Ti)
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					print "BOT4 Joined"
				
			else:
				if wait["Protectgr"] == True:
					if op.param2 in Bots + admin:
						pass
					else:
						ki.kickoutFromGroup(op.param1,[op.param2])
						kk.kickoutFromGroup(op.param1,[op.param2])
						kc.kickoutFromGroup(op.param1,[op.param2])
						wait["blacklist"][op.param2] = True
						print "autokick executed"
                    
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
                if msg.from_ == "ue11fc7860247c63bd3da149613a793f6":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already in blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Decided not to comment.")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed from blacklist.")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"There's no target in blacklist.")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to blacklist.")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed from blacklist.")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"There's no target in blacklist.")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"display name : " + msg.contentMetadata["displayName"] + "\n\nmid : " + msg.contentMetadata["mid"] + "\n\nstatus message : " + contact.statusMessage + "\n\ndisplay picture : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\ncover URL : " + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"display name : " + msg.contentMetadata["displayName"] + "\n\nmid : " + msg.contentMetadata["mid"] + "\n\nstatus message : " + contact.statusMessage + "\n\ndisplay picture : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\ncover URL : " + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
					msg.contentType = 0
					msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
					cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Key","help","Help","/help"]:
                cl.sendText(msg.to,helpMessage)
#--------------------------------------------------------
            elif msg.text.lower() == 'set group':
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,Setgroup)
					else:
						cl.sendText(msg.to,Sett)
				else:
					cl.sendText(msg.to,"Command denied.")
					cl.sendText(msg.to,"Admin permission required.")
            elif ("Gn " in msg.text):
	       if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "inv: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("inv: ","")
                if gid == "":
                    cl.sendText(msg.to,"invalid group id.")
                else:
                    try:
						cl.findAndAddContactsByMid(msg.from_)
						cl.inviteIntoGroup(gid,[msg.from_])
						cl.sendText(msg.to,"invited.")
                    except:
						cl.sendText(msg.to,"you are has been invited.")
            elif "leave: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("leave: ","")
                if gid == "":
                    cl.sendText(msg.to,"invalid group id.")
                else:
                    try:
						cl.leaveGroup(gid)
						cl.sendText(msg.to,"Bot leaving the group.")
                    except:
						cl.sendText(msg.to,"Bot has left the group.")
            elif msg.text in ["Bot?"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                cl.sendText(msg.to, "Created By: Taufiq Ismail")
                msg.contentMetadata = {'mid': 'u46899806e905e2350f791064ace3278e'}
                cl.sendMessage(msg)
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
	       if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open url","open url"]:
                if msg.from_ in admin:
		   if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close url","close url"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Invite by link Close")
					else:
						cl.sendText(msg.to,"Already close")
				else:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Can not be used outside the group")
					else:
						cl.sendText(msg.to,"Not for use less than group")
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
                        cl.sendText(msg.to,"group name :\n" + str(ginfo.name) + "\n\ngid :\n" + msg.to + "\n\ngroup creator :\n" + gCreator + "\n\nprofile status :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nmembers : " + str(len(ginfo.members)) + " members\npending : " + sinvitee + " people\nQR/Link : " + u + " it is inside")
                    else:
                        cl.sendText(msg.to,"group name :\n" + str(ginfo.name) + "\n\ngid :\n" + msg.to + "\n\ngroup creator :\n" + gCreator + "\n\nprofile status :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nmembers : " + str(len(ginfo.members)) + " members\npending : " + sinvitee + " people\nQR/Link : " + u + " it is inside")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == "id group":
                cl.sendText(msg.to,msg.to)
            elif msg.text.lower() == "my mid":
                cl.sendText(msg.to, msg.from_)
            elif msg.text.lower() == "mid all":
			  if msg.from_ in admin:
				cl.sendText(msg.to,mid)
				ki.sendText(msg.to,Amid)
				kk.sendText(msg.to,Bmid)
				kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Gabut"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Lu"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Hadeh"]:
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
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
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
            elif msg.text in ["TL: "]:
			  if msg.from_ in admin:	
				tl_text = msg.text.replace("TL: ","")
				cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr on","gr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr off","gr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
				if msg.from_ in admin:	
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
				if msg.from_ in admin:	
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set View"]:
			  if msg.from_ in admin:	
				md = ""
				if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
				else: md+=" Block Join Off\n"
				if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
				else: md+=" Block Group Off\n"
				if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
				else: md+=" Cancel All Invited Off\n"
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
				cl.sendText(msg.to,md)
            elif msg.text.lower() in ["group id"]:
			  if msg.from_ in admin:	
				gid = cl.getGroupIdsJoined()
				h = ""
				for i in gid:
					h += "[ %s ] :\n%s\n\n" % (cl.getGroup(i).name,i)
				cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
			  if msg.from_ in admin:
				gid = cl.getGroupIdsInvited()
				for i in gid:
					cl.rejectGroupInvitation(i)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"All invitations have been refused")
				else:
					cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Gurl"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					x = cl.getGroup(msg.to)
					if x.preventJoinByTicket == True:
						x.preventJoinByTicket = False
						cl.updateGroup(x)
					gurl = cl.reissueGroupTicket(msg.to)
					cl.sendText(msg.to,"line://ti/g/" + gurl)
				else:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Can't be used outside the group")
					else:
						cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == 'cctv':
                    cl.sendText(msg.to, "􀔃􀇜black large square􏿿􁄁􀄍cctv􏿿 CCTV ON 􁄁􀄍kamera􏿿 􀔃􀇜black large square􏿿")
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
            elif msg.text.lower() == 'ciduk':
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "Hayoo kk tercyduk 􀄃􀅹hahaha􏿿\n%s\nTercyduk pada:\n[%s]"  % (chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik 'CCTV' dulu kak.")
#-----------------------------------------------
#--------------------------------- Hy / HAy ---------------------------------
            elif msg.text.lower() in ["hay","hi"]:
                if msg.from_ in admin:
                    beb = "Hay sayang " + cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    cl.sendText(msg.to,beb)
                    bebek = "Hay sayang " + ki.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ki.sendText(msg.to,bebek)
                    bebeg = "Hay sayang " + kk.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,bebeg)
                    bebeh = "Hay sayang " + kc.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kc.sendText(msg.to,bebeh)
                else:
                    hi = "Hai kak " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hi)
                    hias = "Hai kak " + ki.getContact(msg.from_).displayName
                    ki.sendText(msg.to,hias)
                    hiat = "Hai kak " + kk.getContact(msg.from_).displayName
                    kk.sendText(msg.to,hiat)
                    hiau = "Hai kak " + kc.getContact(msg.from_).displayName
                    kc.sendText(msg.to,hiau)
            elif msg.text.lower() in ["hay yupi","hai yupi"]:
                if msg.from_ in admin:
                    bebz = "Hay sayang " + cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    cl.sendText(msg.to,bebz)
                else:
                    hiz = "Hai kak " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hiz)
            elif msg.text.lower() in ["hay sayang","hai sayang"]:
                if msg.from_ in admin:
                    bebf = "Hay juga sayang love you " + cl.getContact(msg.from_).displayName + " 􀄃􀆖cony kiss􏿿"
                    cl.sendText(msg.to,bebf)
                else:
                    hig = "sayang pala lu peang kak" + cl.getContact(msg.from_).displayName + "􀜁􀅔Har Har􏿿"
                    cl.sendText(msg.to,hig)
            elif msg.text.lower() in ["hay gracia","hai gracia"]:
                if msg.from_ in admin:
                    bebx = "Hay sayang " + ki.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ki.sendText(msg.to,bebx)
                else:
                    hi = "Hai kak " + ki.getContact(msg.from_).displayName
                    ki.sendText(msg.to,hi)
            elif msg.text.lower() in ["hay anin","hai anin"]:
                if msg.from_ in admin:
                    beby = "Hay sayang " + kk.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,beby)
                else:
                    hiy = "Hai kak " + kk.getContact(msg.from_).displayName
                    kk.sendText(msg.to,hiy)			
            elif msg.text.lower() in ["hay ayana","hai ayana"]:
                if msg.from_ in admin:
                    bebu = "Hay sayang " + kc.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kc.sendText(msg.to,bebu)
                else:
                    hiu = "Hai kak " + kc.getContact(msg.from_).displayName
                    kc.sendText(msg.to,hiu)
            elif msg.text.lower() in ["pagi"]:
                if msg.from_ in admin:
                    pagia = "Pagi sayang " + cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    cl.sendText(msg.to,pagia)
                else:
                    pagie = "Pagi kak " + cl.getContact(msg.from_).displayName + " \n udah sarapan belum?? \n semangat ya pagi ini 􀄃􀄷heart􏿿"
                    cl.sendText(msg.to,pagie)
			
            elif msg.text.lower() in ["siang"]:
                if msg.from_ in admin:
                    siangb = "Siang sayang " + ki.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ki.sendText(msg.to,siangb)
                else:
                    siangf = "Siang kak " + ki.getContact(msg.from_).displayName + " \n walaupun diluar panas \n tapi tetap semangat ya!! 􀄃􀅹hahaha􏿿"
                    ki.sendText(msg.to,siangf)
		
            elif msg.text.lower() in ["sore"]:
                if msg.from_ in admin:
                    sorec = "Sore sayang " + kk.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,sorec)
                else:
	            soreg = "Sore kak " + kk.getContact(msg.from_).displayName + " \n ga kerasa udah sore aja ya?? \n pulangnya hati hati dijalan ya kak 􀄃􀄷heart􏿿"
                    kk.sendText(msg.to,soreg)

            elif msg.text.lower() in ["malam"]:
                if msg.from_ in admin:
                    malamd = "Malam sayang " + kc.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kc.sendText(msg.to,malamd)
                else:
                    malamh = "Malam kak " + kc.getContact(msg.from_).displayName + " \n met bobo ya \n jangan bobo kemaleman nanti besok kesiangan 􀄃􀄷heart􏿿"
                    kc.sendText(msg.to,malamh)
			
            elif "Jodoh " in msg.text:
                tanya = msg.text.replace("Hasil Analisa","")
                jawab = ("Kadar cinta 0.1% \n Mati ae lu!!","Kadar cinta 0% \n dah ngaca bang?","Kadar cinta 35% \n siapin duit banyak ae yg penting","Kadar cinta 10% \n hmm coba sama yg lain aja deh","Kadar cinta 99% \n idaman fix","Kadar cinta 20% \n Masih banyak cewe cantik diluar sana!","Kadar cinta 48% \n sepertinya anda lebih cocok jadi wota","Kadar cinta 50% \n cakep ga pen?","Kadar cinta 60% \n wah ada kesempatan nih","Kadar cinta 70% \n Kejar terus bang!","Kadar cinta 80% \n wah cocok nih jangan disiasiain dah","Kadar cinta 90% \n mantap bang gas terus :v :v","Kadar cinta 100% \n putus ae lah kalian dari pada bikin orang ngiri")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------

#--------------------------------------------------------
#--------------------------------------------------------
#pake tag

            elif "/info @" in msg.text:
                nama = msg.text.replace("/info @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = cl.getContact(linedev.mid)
                        # @riorenata_ix #
                        try:
                            cover = cl.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n\n[Mid]:\n" + linedev.mid + "\n\n[Bio]:\n" + mid.statusMessage + "\n\n[Foto Profile]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n\n[Cover]:\n" + str(cover))
                    else:
                        pass

#pake mid

            elif "/info: " in msg.text:
                mid = msg.text.replace("/info: ","")
                anu = cl.getContact(mid)
                try:
                    cover = cl.channel.getCover(mid)
                except:
                    cover = ""
                cl.sendText(msg.to,"[Display Name]:\n" + anu.displayName + "\n\n[Mid]:\n" + mid + "\n\n[Bio]:\n" + anu.statusMessage + "\n\n[Foto Profile]:\nhttp://dl.profile.line-cdn.net/" + anu.pictureStatus + "\n\n[Cover]:\n" + str(cover))

#Fitur random qoute
            elif msg.text in ["Quote","quote","quotes","Quotes","/quote"]:
                quote = ['Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL','No Smoking']
                psn = random.choice(quote)
                cl.sendText(msg.to,psn)

#---------------------------------------------------------
            elif "/pict group" in msg.text:
                   group = cl.getGroup(msg.to)
                   path ="http://dl.profile.line-cdn.net/" + group.pictureStatus
                   cl.sendImageWithURL(msg.to, path)
#---------------------------------------------------------
#---------------------------------------------------------
            elif "/steal home @" in msg.text:
                   print "[Command]COVER executing"
                   _name = msg.text.replace("/steal home @","")
                   _nametarget = _name.rstrip(' ')
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
                   print "[Command]COVER executed"
                   
            elif "/steal dp @" in msg.text:            
                   print "[Command]DP executing"
                   _name = msg.text.replace("/steal dp @","")
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
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               print "[Command]DP executed"
#---------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "/en " in msg.text:
                   txt = msg.text.replace("/en ","")
                   try:
                       gs = goslate.Goslate()
                       trs = gs.translate(txt,'en')
                       cl.sendText(msg.to,trs)
                       print '[Command] Translate EN'
                   except Exception as njer:
		        cl.sendText(msg.to, str(njer))

            elif "/id " in msg.text:
                   txt = msg.text.replace("/id ","")
                   try:
                        gs = goslate.Goslate()
                        trs = gs.translate(txt,'en')
                        cl.sendText(msg.to,trs)
                        print '[Command] Translate ID'
                   except Exception as njer:
		        cl.sendText(msg.to, str(njer))


            elif "Bilang " in msg.text:
					bctxt = msg.text.replace("Bilang ","")
					cl.sendText(msg.to,(bctxt))
					ki.sendText(msg.to,(bctxt))
					kk.sendText(msg.to,(bctxt))
					


#---------------------------------------------------------
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Wikipedia : "
                      pesan+=wikipedia.page(wiki).title
                      pesan+="\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Text Terlalu Panjang Silahkan Click link di bawah ini\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
			#---------------------------------------------------------
#----------------------------------------------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "Youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------

            elif 'ig ' in msg.text.lower():
              try:
                    instagram = msg.text.lower().replace("/cekig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
               	    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Nama: " + text[-2] + "\n"
                    user1 = text[-1]
                    followers = "Pengikut: " + text[0] + "\n"
                    following = "Mengikuti: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "Info Akun: " + user1 + "\n\n"
                    details = " "
                    cl.sendText(msg.to, detail + user + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
              except Exception as njer:
              	    cl.sendText(msg.to, str(njer))

            elif "apakah" in msg.text:
                    tanya = msg.text.replace("Apakah ","")
                    jawab = ("iya","Tidak","mungkin","bisa jadi")
                    jawaban = random.choice(jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mp3')
                    cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Wacana" in msg.text:
                    tanya = msg.text.replace("Apa ","")
                    jawab = ("Tanya Osan","Tidak Ada","Wacana ae lu","Ke bulan","Jangan Wacana ae sia goblog")
                    jawaban = random.choice(jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mp3')
                    cl.sendAudio(msg.to,'tts.mp3')
                
			
            elif "ingin" in msg.text:
                    tanya = msg.text.replace("Ingin ","")
                    jawab = ("Kasar","Anjing","Hilih Kintil","Ngentot","Kontol","Bangsat Kau","Asu","kentod")
                    jawaban = random.choice(jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mp3')
                    cl.sendAudio(msg.to,'tts.mp3')

            elif "Wkwk" in msg.text:
                    tanya = msg.text.replace("Wkwk ","")
                    jawab = ("HAHAHAHAHAAHA","WKWKWKWKWKK","Hehehehe","KAKAKAKAKK","XIXIXIXIIXIXI","WEKAWEKAKA","NGIKNGIKNGIK","JIAHAHAA")
                    jawaban = random.choice(jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mp3')
                    cl.sendAudio(msg.to,'tts.mp3')
                  	
                  	
            elif "Kapan " in msg.text:
                    tanya = msg.text.replace("Kapan ","")
                    jawab = ("kapan  kapan","besok","satu  abad  lagi")
                    jawaban = random.choice(jawab)
                    tts = gTTS(text=jawaban, lang='id')
                    tts.save('tts.mp3')
                    cl.sendAudio(msg.to,'tts.mp3')
#---------------------------------------------------------
            elif msg.text.lower() == '.reboot':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#----------------------------------------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["My oshi join"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Bot Complete"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["Yupi sini"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Gracia sini"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Anin sini"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Ayana sini"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Dadah semuanya","Bye bots"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Dadah yupi"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["ikutan sini","Nongol dong","Oi"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Good Bye")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "sweep this group" in msg.text.lower():
              if msg.from_ in admsa:
                if msg.toType == 2:
                    print "sweeping"
                    _name = msg.text.replace("Sweep this group","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"maaf kalo gak sopan")
                    kk.sendText(msg.to,"makasih semuanya..")
                    kc.sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': 'ue11fc7860247c63bd3da149613a793f6'}
                    cl.sendMessage(msg)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
						   if target not in admin:
							try:
								klist=[cl,ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[target])
								print (msg.to,[g.mid])
							except:
								pass

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
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
                        cl.sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
						  if targets not in Bots:
						    if targets not in admin:
								try:
									klist=[cl,ki,kk,kc]
									kicker=random.choice(klist)
									ki.sendText(msg.to, "Good bye.")
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									pass
        #----------------Fungsi Kick User Target Finish----------------------#      
            #elif "Blacklist @" in msg.text:
                #_name = msg.text.replace("Blacklist @","")
                #_kicktarget = _name.rstrip(' ')
                #gs = ki2.getGroup(msg.to)
                #targets = []
                #for g in gs.members:
                    #if _kicktarget == g.displayName:
                        #targets.append(g.mid)
                        #if targets == []:
                            #cl.sendText(msg.to,"Not found")
                        #else:
                            #for target in targets:
                                #try:
                                    #wait["blacklist"][target] = True
                                    #f=codecs.open('st2__b.json','w','utf-8')
                                    #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    #k3.sendText(msg.to,"Target locked.")
                                #except:
                                    #ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] executed"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets in Bots:
                        cl.sendText(msg.to,"Can't ban bot")
                    else:
                        for target in targets:
                            try:
								wait["blacklist"][target] = True
								f=codecs.open('st2__b.json','w','utf-8')
								json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
								cl.sendText(msg.to,"Target locked.")
								print "[Banned] success"
                            except:
                                ki.sendText(msg.to,"Target already in blacklist.")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] executed"
                    _name = msg.text.replace("Unban @","")
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
                        cl.sendText(msg.to,"Target not found")
                    else:
                        for target in targets:
                            try:
								del wait["blacklist"][target]
								f=codecs.open('st2__b.json','w','utf-8')
								json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
								cl.sendText(msg.to,"Target cleaned.")
								print "[Unban] success"
                            except:
                                ki.sendText(msg.to,"There's no target in blacklist.")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Oy"]:
                cl.sendText(msg.to,"􀤁􀄥Glowstick􏿿Oi Oi Oi 􀤁􀄥Glowstick􏿿")
                ki.sendText(msg.to,"􀤁􀄥Glowstick􏿿Oi Oi Oi 􀤁􀄥Glowstick􏿿")
                kk.sendText(msg.to,"􀤁􀄥Glowstick􏿿Oi Oi Oi 􀤁􀄥Glowstick􏿿")
                kc.sendText(msg.to,"􀤁􀄥Glowstick􏿿Oi Oi Oi 􀤁􀄥Glowstick􏿿")

        #-------------Fungsi Spam Finish---------------------#
	        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Chant","chant"]:
                cl.sendText(msg.to,"􀤁􀄥Glowstick􏿿􀤁􀄥Glowstick􏿿􀤁􀄥Glowstick􏿿")
                cl.sendText(msg.to,"Aaa…Yossha-ikuzo")
                cl.sendText(msg.to,"Taigaa")
                cl.sendText(msg.to,"Faiyaa")
                cl.sendText(msg.to,"Saibaa")
                cl.sendText(msg.to,"Faibaa")
                cl.sendText(msg.to,"Daibaa")
                cl.sendText(msg.to,"Baibaa")
                cl.sendText(msg.to,"Jyaa Jyaa")
        #-------------Fungsi Spam Finish---------------------#
	        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Chant2","chant2"]:
                ki.sendText(msg.to,"􀤁􀄥Glowstick􏿿􀤁􀄥Glowstick􏿿􀤁􀄥Glowstick􏿿")
                ki.sendText(msg.to,"Aaa…Mou-iccho-ikuzo")
                ki.sendText(msg.to,"Tora")
                ki.sendText(msg.to,"Hi")
                ki.sendText(msg.to,"Jinzou")
                ki.sendText(msg.to,"Seni")
                ki.sendText(msg.to,"Ama")
                ki.sendText(msg.to,"Shindou")
                ki.sendText(msg.to,"Kasen Tobi Jyokyo")
        #-------------Fungsi Spam Finish---------------------#
			    	        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Chant3","chant3"]:
                ki.sendText(msg.to,"􀤁􀄥Glowstick􏿿􀤁􀄥Glowstick􏿿􀤁􀄥Glowstick􏿿")
                ki.sendText(msg.to,"Aaa…Mou-iccho-ikuzo")
                ki.sendText(msg.to,"Chape")
                ki.sendText(msg.to,"Ape")
                ki.sendText(msg.to,"Kara")
                ki.sendText(msg.to,"Kina")
                ki.sendText(msg.to,"Rara")
                ki.sendText(msg.to,"Tosuke")
                ki.sendText(msg.to,"Myohontosuke")
        #-------------Fungsi Spam Finish---------------------#
        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
			  if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				n = cl.getGroupIdsJoined()
				for manusia in n:
					cl.sendText(manusia, (bctxt))
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["Hai"]:
		cl.sendText(msg.to,"Hai juga kak  􂜁􀆀heart􏿿")
                ki.sendText(msg.to,"Hai juga kak 􀄃􀆍moon grin􏿿")
                kk.sendText(msg.to,"Hai juga kak 􀄃􀇁Cony􏿿")
                kc.sendText(msg.to,"Hai juga kak 􀄃􀆝aww􏿿")

#-----------------------------------------------
            elif msg.text in ["Hai sider","Sider","Woi sider","Oi sider"]:
                cl.sendText(msg.to,"Jangan diem aja kak sini ikut ramein")
            elif msg.text in ["Yupi","yupi","ipuy","puy"]:
                cl.sendText(msg.to,"Iya kak? ketik Petunjuk kalo butuh sesuatu ya kak 􀄃􀇁Cony􏿿 ")
            elif msg.text in ["Solat dulu","Maghrib dulu","Magrib dulu","Solat wey"]:
                cl.sendText(msg.to,"Fix idaman")
            elif msg.text in ["Eh gw ada kontak cewe","Eh gw kemarin liat cewe","Minta kontak","Minta kontaknya dong"]:
                cl.sendText(msg.to,"Cakep ga pen?")
            elif msg.text in ["Ayana","ayana","ay"]:
                kc.sendText(msg.to,"Iya kak?")
            elif msg.text in ["Ayana","ayana","ay"]:
                kc.sendText(msg.to,"Iya kak?􀄃􀅹hahaha􏿿")
            elif msg.text in ["Anaya","Ayaba","ayaba"]:
                kc.sendText(msg.to,"Aku ayanaaa kaa 􀄃􀅹hahaha􏿿")
            elif msg.text in ["Yupi jiko","yupi jiko","Yupi Jiko"]:
                cl.sendText(msg.to,"Si mungil yang Limited Edition, dan selalu tersenyum, Aku CindVia.")
            elif msg.text in ["Gracia jiko","gracia jiko","Gracia Jiko"]:
                ki.sendText(msg.to,"Senyumku akan terekam jelas dalam ingatanmu seperti foto dengan sejuta warna, Namaku Gracia, Always Smile!")
            elif msg.text in ["Anin jiko","anin jiko"]:
                kk.sendText(msg.to,"Bagaikan angin yang akan selalu menghembuskan keceriaan pada hari-harimu. Aku Anin.")
            elif msg.text in ["Ayana jiko","ayana jiko","Ayana Jiko"]:
                kc.sendText(msg.to,"Haaaiii...! Meskipun mataku sayu, senyumku selalu menghiburmu. Namaku Ayana, panggil aku Achan")
            elif msg.text in ["Assalamualaikum"]:
                kc.sendText(msg.to,"Walaikumsalam")
            elif msg.text in ["siapa ini?","Siapa sih","siapa sih","Siapa ini?","Bot apa ini","bot apa ini?","Bot apa ini?","bot apa ini"]:
                cl.sendText(msg.to,"Iya kak perkenalkan aku yupi? ketik petunjuk kalo butuh sesuatu ya kak 􀄃􀇁Cony􏿿 ")
            elif msg.text in ["Bacot","bacot","bcd","bct"]:
                cl.sendText(msg.to,"kakak kasar ih :( 􀄃􀇄Cony sad􏿿 ")
            elif msg.text in ["Bgsd","bgsd","Bangsat","bangsat"]:
                cl.sendText(msg.to,"kenape njer 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Bgsd","bgsd","Bangsat","bangsat"]:
                cl.sendText(msg.to,"kenape njer 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Bot apa sih ini gajelas","Gajelas","Gjls","Ga jelas"]:
                cl.sendText(msg.to,"bacot!")
            elif msg.text in ["beri salam","Beri salam"]:
                cl.sendText(msg.to,"welcome kak semoga betah ya 􀄃􀇂Cony happy􏿿")
            elif msg.text in ["welcome","Welcome"]:
                cl.sendText(msg.to,"Intro dulu kak 􀄃􀇂Cony happy􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen"]:
			  if msg.from_ in admin:
				cl.sendText(msg.to,"Aku hadir kak 􀄃􀆍moon grin􏿿")
				ki.sendText(msg.to,"Hai kak aku hadir 􀄃􀇁Cony􏿿")
				kk.sendText(msg.to,"Aku hadir kak 􀄃􀆌hee􏿿")
				kc.sendText(msg.to,"Aku juga hadir hehehe 􀄃􀆝aww􏿿")
            elif msg.text in ["Yuhuu"]:
				cl.sendText(msg.to,"Aku hadir kak 􀄃􀆍moon grin􏿿")
				ki.sendText(msg.to,"Hai kak aku hadir 􀄃􀇁Cony􏿿")
				kk.sendText(msg.to,"Aku hadir kak 􀄃􀆌hee􏿿")
				kc.sendText(msg.to,"Aku juga hadir hehehe 􀄃􀆝aww􏿿")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Respon", "Sp", "speed", "Speed"]:
                start = time.time()
                cl.sendText(msg.to, "Bentar ya kak...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sdetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
	          if msg.from_ in admin:
				wait["wblacklist"] = True
				cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
			  if msg.from_ in admin:
				wait["dblacklist"] = True
				cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
			  if msg.from_ in admin:
				if wait["blacklist"] == {}:
					cl.sendText(msg.to,"There's no banned user")
				else:
					ki.sendText(msg.to,"Blacklist user")
					mc = ""
					for mi_d in wait["blacklist"]:
						mc += "->" +cl.getContact(mi_d).displayName + "\n"
					cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					group = cl.getGroup(msg.to)
					gMembMids = [contact.mid for contact in group.members]
					matched_list = []
					for tag in wait["blacklist"]:
						matched_list+=filter(lambda str: str == tag, gMembMids)
					if matched_list == []:
						cl.sendText(msg.to,"There was no blacklist user")
						return
					for jj in matched_list:
						cl.sendText(msg.to,"Good bye.")
						cl.kickoutFromGroup(msg.to,[jj])
						ki.kickoutFromGroup(msg.to,[jj])
						kk.kickoutFromGroup(msg.to,[jj])
						kc.kickoutFromGroup(msg.to,[jj])
            elif msg.text in ["Clear"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					group = cl.getGroup(msg.to)
					gMembMids = [contact.mid for contact in group.invitee]
					for _mid in gMembMids:
						cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"I pretended to cancel and canceled.")

            elif msg.text in ["Bot Like", "Bot like"]:
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s)")
                    try:
                        likePost()
                    except:
                        pass

            elif msg.text.lower() == 'maaf ya':
			  if msg.from_ in admsa:
				gid = cl.getGroupIdsJoined()
				gid = ki.getGroupIdsJoined()
				gid = kk.getGroupIdsJoined()
				gid = kc.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
					ki.leaveGroup(i)
					kk.leaveGroup(i)
					kc.leaveGroup(i)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Ard Squad bot leaving all groups.")
				else:
					cl.sendText(msg.to,"He declined all invitations")
            elif msg.text.lower() == 'yupi keluar':
			  if msg.from_ in admsa:
				gid = cl.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Ard bot leaving all groups.")
				else:
					cl.sendText(msg.to,"He declined all invitations")
			
#-------------------------------------------------------------------------------
            elif "copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["backup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
						
            elif msg.text.lower() in ["list group"]:
              if msg.from_ in admin:
				gid = cl.getGroupIdsJoined()
				h = ""
				for i in gid:
					h += "%s\n" % (cl.getGroup(i).name +" → ["+str(len(cl.getGroup(i).members))+"]")
				cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
												
            elif "Staff add @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
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
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Staff added")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Staff remove @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff remove @","")
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
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Staff deleted")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"please wait...")
                    mc = ""
                    for mi_d in admin:
                        mc += "\n- " + cl.getContact(mi_d).displayName
                    cl.sendText(msg.to, "Staff :\n" + mc)
                    print "[Command]Stafflist executed"
					
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
		
            elif "Apakah " in msg.text:
				tanya = msg.text.replace("Apakah ","")
				jawab = ("Ya","Tidak")
				jawaban = random.choice(jawab)
				cl.sendText(msg.to,jawaban)
				
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n- " + Name
						wait2['ROM'][op.param1][op.param2] = "- " + Name
				else:
					cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


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
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=200)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
			cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
			cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Nice")
			ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
			kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
			kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
			print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(200)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
