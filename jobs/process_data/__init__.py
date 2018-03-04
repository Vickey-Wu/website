from threading import Thread
msg_l=[]
format_l=[]
def get_info():
    while True:
        msg=input('>>: ').strip()
        if not msg:continue
        msg_l.append(msg)

def format_info():
    while True:
        if msg_l:
            res=msg_l.pop()
            format_l.append(res.upper())

def save_info():
    while True:
        if format_l:
            with open('db.txt','a',encoding='utf-8') as f:
                res=format_l.pop()
                f.write('%s\n' %res)

if __name__ == '__main__':
    # multi threads
    t1=Thread(target=get_info)
    t2=Thread(target=format)
    t3=Thread(target=save_info)
    t1.start()
    t2.start()
    t3.start()