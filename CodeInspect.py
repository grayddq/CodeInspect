# -*- coding: utf-8 -*-
import os, logging

#代码路径
CODE_DIR_LIST = ['/root/tool/PubilcAssetInfo']
#代码同步方式
TYPE = 'git'
#是否执行代码恢复，
ACTION = 'checkout'



def loging():
    log_file = '/var/log/codeinspect.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(message)s'
    )
    logger = logging.getLogger('LogInfo')
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    logger = loging()
    if TYPE == 'git':
        for path in CODE_DIR_LIST:
            exception_list = os.popen("cd %s && git status -s | awk '{print $2}'" % path).readlines()
            if len(exception_list) >0:
                for file in exception_list:
                    file = file.strip().strip('\n')
                    os.system("cd %s && cp -r %s /tmp/%s" % (path, file, file))
                    logger.info("Find Exception File : %s" % file)
                    logger.info(" ")
                if ACTION == 'checkout':
                    os.system("cd %s && git checkout . && git clean -df" % path)


