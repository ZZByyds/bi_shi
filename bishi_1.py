
# 编程题二：

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
outputObject = {}

paragraphs = long_text.split('\n')
print(paragraphs)

# sub_fund -> 字典的List
# Keys:
# Title -> 字符串
# isin -> List

sub_fund = []
sub_fund_object = {}
isin_list = []

# Key 'name'
name = paragraphs[1]
outputObject["name"] = name

# Key 'lei'
lei = paragraphs[2]
outputObject["lei"] = lei

# 循环剩下段落
for i in range(3, len(paragraphs)):
    # 检测是否为TITLE行
    if (paragraphs[i].find('.') != -1):  # 是
        # 处理非空的 sub_fund
        if (len(isin_list) != 0):
            sub_fund_object["isin"] = isin_list  # 设置List为上一个关键字
            sub_fund.append(sub_fund_object)  # Append进sub_fund列表

            sub_fund_object = {}  # 残留处理
            isin_list = []

        # 设置字典
        sub_fund_object["title"] = paragraphs[i]
    else:  # 是isin行
        isin_list.append(paragraphs[i])

# 由于最后一行没有处理sub_fund, 在这边再处理一次
if (len(isin_list) != 0):
    sub_fund_object["isin"] = isin_list  # 设置List为上一个关键字
    sub_fund.append(sub_fund_object)  # Append进sub_fund列表

    sub_fund_object = {}  # 残留处理
    isin_list = []

# sub_fund处理完成，给sub_fund送进Object
outputObject["sub_fund"] = sub_fund

print(outputObject)