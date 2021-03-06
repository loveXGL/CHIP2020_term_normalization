from rule_base import load_icd_v2
x_list, y_clean_list, y_list, y_clean_icd10_list, y_icd10_list = load_icd_v2.load_train_icd()

def get_ngram(des, n=2):
    if n==1:
        return list(des)
    if n > 1:
        tmp = [des[idx:idx+n] for idx in range(len(des) - n + 1)]
    return tmp

def get_c_ngram(des, n=3):
    res = []
    for i in range(n):
        res.extend(get_ngram(des, i + 1))
    return res

result = {}
for i in range(7000):
    x = get_c_ngram(x_list[i], 4)
    y = []
    for yy in y_list[i]:
        y.extend(get_c_ngram(yy, 4))
    for ch in y:
        if not ch in result:
            result[ch] = [0, 0, 0]
        if ch in x:
            result[ch][0] += 1
        result[ch][1] += 1

for ch in result:
    result[ch] = [result[ch][0], result[ch][1], result[ch][0] / result[ch][1]]

outer_dict = ["头","头皮","脑","颅","面","脸","颊","额","颧","颌","上颌","下颌","颞","颏","颚","腭","眉","耳","眼","眶","鼻","嘴","口","唇","腮","喉","牙","舌","颈","脊","肩","肩胛","肩峰","胸","背","腰","肘","肋","臂","上臂","前臂","腕","手","掌","指","上肢","髋","臀","股","下肢","腿","大腿","小腿","指","膝","踝","足","脚"]

loc_dict = ["上","下","前","后","内","外","近","远","尺","桡","胫","腓","浅","深"]

bone_dict = ["颅骨","顶骨","额骨","蝶骨","鼻骨","颧骨","上颌骨","下颌骨","颞骨","枕骨","乳突","泪骨","筛骨","颧弓","犁骨","舌骨","胸骨","颈椎","锁骨","肩胛骨","肱骨","肋骨","肋弓","剑突","腰椎","上髁","桡骨","桡骨头","髋骨","髂骨","髂嵴","骶骨","骶椎","鹰嘴","坐骨","耻骨","尺骨","髋骨","桡骨茎突","尺骨茎突","掌骨","指骨","股骨","髌骨","胫骨","腓骨","腓骨头","足骨","髋骨","腕骨","距骨","骰骨","跟骨","跖骨","趾骨","坐骨结节","坐骨棘","耻骨结节","跗骨","尾骨","尾椎","钩骨","豆骨","月骨","髋骨","籽骨","舟骨","三角骨","头状骨","楔骨","骨端","骨膜","骨质","骨干","骨髓","骨髓腔","骨密质","骨松质","骨骺"]

inner_dict = ["口腔","牙龈","唾液腺","腮腺","下颌下腺","舌下腺","咽","食管","胃","肠","大肠","盲肠","阑尾","结肠","直肠","肛管","胰","肝","肝总管","胆囊","胆总管","腹膜","网膜","系膜","关节","韧带","腱","牙齿","口部","舌","唾腺","下颌腺","食道","小肠","十二指肠","空肠","回肠","大肠","肝脏","胆囊","肠系膜","胰脏","鼻腔","喉","气管","支气管","肺","左肺","右肺","横膈膜","肾","输尿管","膀胱","尿道","卵巢","输卵管","子宫","阴道","女阴","阴蒂","胎盘","睾丸","附睾","输精管","精囊","前列腺","尿道球腺","阴茎","阴囊","脑下垂体","松果体","甲状腺","副甲状腺","胸腺","肾上腺","胰岛","性腺","心","心脏","动脉","静脉","微血管","淋巴","淋巴管","淋巴结","骨髓","胸腺","脾","脾脏","扁桃腺","大脑","间脑","脑干","中脑","桥脑","延髓","小脑","脊髓","脑室","脉络丛","神经","角膜","虹膜","睫状体","晶状体","视网膜","外耳","耳垂","鼓膜","中耳","听小骨","内耳","耳蜗","半规管","耳前庭","鼻","外鼻","鼻腔","鼻旁窦","上颌窦","额窦","蝶窦","筛窦","甲状软骨","环状软骨","勺状软骨","会厌软骨","胸膜","肾盂","纤维囊","脂肪囊","筋膜","毛细血管","大动脉","中动脉","小动脉","大静脉","中静脉","小静脉","心壁","心肌膜","心内膜","心外膜","肺动脉瓣","主动脉瓣","二尖瓣","三尖瓣","房间隔","室间隔","右心房","右心室","左心房","左心室","窦房结","房室结","左冠状动脉","右冠状动脉","冠状窦","左肺动脉","右肺动脉","主动脉","颈动脉","颈总动脉","颈外动脉","颈内动脉"]

pre_dict = outer_dict + loc_dict + bone_dict + inner_dict

m = [ch for ch in result if result[ch][2] > 0.9 and (result[ch][1] > 5 or ch in pre_dict)]
print(m)
