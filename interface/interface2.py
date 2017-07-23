from datatype import datatype1
import time

def write_log(logtype, loginfo):
    logfile = datatype1.LOGFILE[logtype]
    info = str(time.strftime('%c')) + "| " + loginfo + "\n"
    try:
        f = open(logfile, 'a')
        f.write(info)
        f.flush()
    except :
        pass
    finally:
        f.close()
