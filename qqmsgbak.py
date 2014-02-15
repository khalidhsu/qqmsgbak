#!/usr/bin/env python  
#-*-coding:utf-8-*-
  
import sys,os  

from os.path import join as pj
from datetime import datetime, date, timedelta
from calendar import timegm
from lsession import *

ls=LSession()

def md_recursive(path):
    _parent = os.path.dirname(path)
    if not os.path.exists(_parent):
        md_recursive(_parent)
    if not os.path.exists(path):
        os.mkdir(path)

def savedaymsg(sid,q,d,_path): # d is how many day before
    startday = date.today() - timedelta(d)
    _f = ('0' + str(startday.day) + '.html')[-7:]
    _nf = pj(_path, _f)
    md_recursive(_path)
    if  os.path.isfile(_nf) :
        print "File already exists: %s" % _nf
        return

    print 'start retrieving: %s' % _nf
    endday = date.today() - timedelta( d - 1)
    _stm = timegm(startday.timetuple()) - 28800
    _etm = timegm(endday.timetuple()) -1 - 28800
    #http://sqq.3g.qq.com/roam/read.jsp?sid=%s&q=%s&from=mqq&cmd=1&ltm=%s&rnd=%s
    _url='http://sqq.3g.qq.com/roam/read.jsp'
    print '%s?sid=%s&q=%s&from=mqq&cmd=1&ltm=%d&rnd=%d'%(_url,sid,q,_stm,_etm)
    ls.get('%s?sid=%s&q=%s&from=mqq&cmd=1&ltm=%d&rnd=%d'%(_url,sid,q,_stm,_etm))
    open(_nf,'w+').write(ls.text('utf8'))

def msgbakloop(_dir,q,sid):
    _now = datetime.now()
    _sdir = str(_now.month)
    _np = pj(pj(_dir,q),_sdir)
    for i in range(2,8): #
        savedaymsg(sid,q,i,_np)
    print ' ----------------\nDone!'

def main(argv):
    #example
    #備份和Q號爲123456的對話，放在`/tmp`下
    #msgbakloop('/tmp','123456','sid')

def back_script_dir():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #print(os.getcwd())


if __name__=="__main__":  
    back_script_dir()
    main(sys.argv[1:])  








