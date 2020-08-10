import smsCodeTask,smsCallTask,mesCallTask,config
import random

'''
入口
'''

def main():
    users = config.users
    settings = config.settings
    # 留言板
    # mesCallTask.liuxue(users)
    # mesCallTask.schoolsbak(users)

    # 短信验证码
    smsCodeTask.disneyphotopass(users)

    # 短信语音



if __name__ == "__main__":
    main()