#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import sys
import urllib2
import urllib
import gaemechanize2
import re


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        login = self.request.get('login')
        password = self.request.get('password')
        to = self.request.get('to')
        body = self.request.get('body')
        if len(login) == 0:
                self.response.out.write('ERROR 1')
                return
        if len(password) == 0:
                self.response.out.write('ERROR 2')
                return
        if len(to) == 0:
                self.response.out.write('ERROR 3')
                return
        if len(body) == 0:
                self.response.out.write('ERROR 4')
                return
        try:
                send_sms(login,password,to,body)
        except:
                self.response.out.write('ERROR 5')
                return        
        self.response.out.write('OK')
        return

def send_sms(logins,passs,number,message):
	czas='0'
        sets = {"login":"%s"%logins,"pass":"%s"%passs}
        values = {'login' : sets['login'],'haslo' : sets['pass'] }

        br = gaemechanize2.Browser()
        br.open('https://24.play.pl/Play24/')
        br.select_form(nr=0)
        br.submit()

        sms=-1;

        br.select_form(name="loginForm")
        br['login']=sets['login']
        br['password']=sets['pass']
        br.submit()

        cookie=br.response().info()['set-cookie']

        br.select_form(nr=0)
        res=br.submit()

        br.open('https://bramka.play.pl/composer/public/editableSmsCompose.do')
        br.select_form(nr=0)
        br.submit()

        br.select_form(nr=0)
        br.submit()

        br.select_form(nr=0)
        br.submit()
        br.select_form(nr=0)
        br.form.set_all_readonly(False)
        br['recipients']=number
        br['content_out']=message
        br['content_in']=message
        br['czas']=['%s'%czas]
        br['sendform']='on'
        br['old_content']=message
        br.form.action='https://bramka.play.pl/composer/public/editableSmsCompose.do'
        br.submit()

        br.open('https://bramka.play.pl/composer/public/editableSmsCompose.do?SMS_SEND_CONFIRMED=Wy%9Clij')
        return 1

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],debug=False)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
