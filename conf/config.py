# 强烈建议修改
LAST_NAME = '郑'  # 姓氏
SEX = '男'  # 孩子性别，男 或者 女
year = 1999  # 出生的时间：年
month = 5  # 出生的时间：月
date = 16  # 出生的时间：日
hour = 2  # 出生的时间：小时
minute = None  # 出生的时间： 分钟

# 选择性修改
MIN_SINGLE_NUM = 2  # 单个字最少笔画过滤
MAX_SINGLE_NUM = 20  # 单个字最多笔画过滤
THRESHOLD_SCORE = 80  # 三才五格测试最低能接受的得分，结果记录在RESULT_FILE
SELECTED_XITONGSHEN = None  # 已知的喜用神，或者次喜用神。None表示没关系。这个喜用神自己在网站查查，选填，填了可能没有最佳匹配结果

# 尽量别改，除非你知道是什么意思
debug = False
my_write_num_list = [(6, 7),(11, 7),(12, 4),(13, 17),(18, 12)]  # 经过第一轮测试后笔画的结果， 自己记录下来
true_request = True  # 真实请求测试
# 名字固定要的字
fix_write_word = None
SELECTED_SANCAI = ['大吉', '中吉']  # 三才中，如果为None就不特意选最好的

# 首先在http://www.qimingzi.net/ 网站提交基本信息，点击开始起名，F12查看请求信息把Cookie复制下来
headers = {"Cookie": "bdshare_firstime=1559048183377; Hm_lvt_4baf75bdd37d2c14c33b580be5423f7f=1559048184,1559118050; "
                     "__tins__5033285=%7B%22sid%22%3A%201559118050258%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A"
                     "%201559119879909%7D; __51cke__=; __51laig__=2; "
                     "Hm_lpvt_4baf75bdd37d2c14c33b580be5423f7f=1559118080; userSurname=%e9%83%91; userSex=1; "
                     "searchType=report; otherPara=%e4%b8%8a%e6%b5%b7%e5%b8%82%e4%b8%8a%e6%b5%b7%7c%e9%87%91%7c%3cb"
                     "%3e%e4%ba%94%e8%a1%8c%e5%88%86%e6%9e%90%3c%2fb%3e%ef%bc%9a%e5%85%ab%e5%ad%97%e8%bf%87%e7%a1%ac"
                     "%ef%bc%8c%e5%85%ab%e5%ad%97%e5%96%9c%e9%87%91%ef%bc%8c%e8%b5%b7%e5%90%8d%e6%9c%80%e5%a5%bd%e"
                     "7%94%a8%e4%ba%94%e8%a1%8c%e5%b1%9e%e6%80%a7%e4%b8%ba%e3%80%8c%3cfont+color%3d0033FF%3e%3cb%3e%"
                     "e9%87%91%3c%2fb%3e%3c%2ffont%3e%e3%80%8d%e7%9a%84%e5%ad%97%3cbr%3e; year=1999; month=5; "
                     "date=16; hour=2; minute=-1",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
