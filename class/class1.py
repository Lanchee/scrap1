
class TimeoutError(Exception):
    def __str__(self, cmd, timeout):
        '''
        打印超时错误信息
        :param cmd: 命令
        :param timeout: 超时
        '''
        print("error")
        tmpcmd = ''
        print(cmd)
        for tmpstr in cmd:
            tmpcmd = tmpcmd + " " + str(tmpstr)
            print("tmpstr=%s"%str(tmpstr))