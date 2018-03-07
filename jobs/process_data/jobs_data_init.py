#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2018/1/23 22:58
# @name: jobs_data_init
# @author：vickey-wu

#!/usr/bin/python
# -*- coding:utf-8 -*-

# @filename: search
# @author：wwx399777 wuweiji
# @date: 2018/1/25 9:35

import pymysql
import pyecharts
from datetime import datetime
import numpy as np
import pandas as pd
# import matplotlib as mpl
import re
# cut word
import jieba
from wordcloud import WordCloud
# import matplotlib.pyplot as plt
from collections import Counter
from scipy.misc import imread


def connect_mysql(sql, oper_type="select", data_l=None):
    conn = pymysql.connect(host='localhost', user="root", password="123",
                           database="website", port=3306, charset="utf8")
    cur = conn.cursor()
    if oper_type == "insert":
        cur.executemany(sql, data_l)
        conn.commit()
    else:
        cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result


def create_list(file_name):
    ls = []
    if not re.findall(file_name, r".txt"):
        file_name += ".txt"
    with open(file_name) as f:
        for i in f:
            job_title, job_salary, job_requirement, job_addr, job_exp, job_edu, job_tags, company_name, company_employee_num, company_type = i.strip().split(
                ",")
            ls.append([job_title, job_salary, job_requirement, job_addr, job_exp, job_edu, job_tags, company_name, company_employee_num, company_type])
    return ls


def data_insert():
    sql = '''INSERT INTO website.jobs_jobsinfo (job_title, job_salary, job_requirement, job_addr, job_exp, job_edu, job_tags, company_name, company_employee_num, company_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    data_l = create_list("jobs_data")
    connect_mysql(sql, oper_type="insert", data_l=data_l)

# data_insert()


# def data_analysis():
#     sql = """
#     SELECT p.name, p.email, p.memo from personal_userinfo p
#     """
#     x = connect_mysql(sql)
#     print(type(x), x)
#     x = list(x[2])
#     print(x)
#     return x

# data_analysis()
# version 1.1


def count_times(all_list):
    count_list = []
    item_list = list(set(all_list))
    for item in item_list:
        times = all_list.count(item)
        count_list.append([item, times])
    return count_list


def process_field(field_name):
    sql = "select " + field_name + " from jobs_jobsinfo where job_exp = '1-3年';"
    column_name = connect_mysql(sql, oper_type="select")
    # sort salary order
    row_category = list(set(column_name))
    general_min, general_avg, general_max = [], [], []
    # cal_num = 0
    for sal in row_category:
        # calculate category amount
        # for cat in column_name:
        #     if cat == sal:
        #         cal_num += 1
        # process salary
        if field_name == "job_salary":
            sal_tmp = str(sal).strip("('").strip("K',)").split("K-")
            general_min.append(int(sal_tmp[0]))
            general_max.append(int(sal_tmp[1]))

        # process experience
        # if field_name == "job_exp":
        #     print(column_name)

        # initial again
        # cal_num = 0

    # calculate min sal
    min_sal = count_times(general_min)
    for m1 in min_sal:
        min_s = str(m1[0]) + "K"
        m1[0] = min_s

    # calculate max sal
    max_sal = count_times(general_max)
    for m2 in max_sal:
        max_s = str(m2[0]) + "K"
        m2[0] = max_s

    # calculate avg sal
    avg_sal = count_times(column_name)
    # print("original", avg_sal)
    for a1 in avg_sal:
        sal_tmp_1 = str(a1[0]).strip("('").strip("K',)").split("K-")
        a1[0] = (int(sal_tmp_1[0]) + int(sal_tmp_1[1])) / 2.0
    avg_sal = sorted(avg_sal)

    for a2 in avg_sal:
        a2[0] = str(a2[0]) + "K"
    # debug
    # print(len(min_sal), min_sal)
    # print(len(avg_sal), avg_sal)
    # print(len(max_sal), max_sal)
    return min_sal, avg_sal, max_sal

# process_field("job_salary")


def process_reqirement(field_name):
    sql_all_req = "select " + field_name + " from jobs_jobsinfo"
    sql = "select " + field_name + " from jobs_jobsinfo where job_exp = '1年以内' or job_exp = '经验不限';"
    original_req = connect_mysql(sql)
    original_all_req = connect_mysql(sql_all_req)
    user_list = ["C", "C#", "C++", "Go", "Linux", "MongoDB", "Mysql", "PostgreSQL", "Ajax", "Bootstrap", "CSS", "Django", "Docker", "Flask", "Git", "http", "tcp", "Java", "JavaScript", "Jquery", "Oracle", "Python", "Redis", "Ruby", "Scrapy", "shell", "Tornado", "Web", "Zabbix", "RESTful", "云计算", "分布式", "前端", "后端", "大数据", "高并发", "数据分析", "数据挖掘", "机器学习", "爬虫", "算法", "自动化", "运维", "集群"]

    jieba.load_userdict(user_list)
    # print(type(original_req), str(original_req))
    text0 = Counter(jieba.cut(str(original_req)))
    text1 = " ".join(jieba.cut(str(original_req)))
    [item for item in sorted(text0.values())]
    # print(text0.keys(), text0.values())


    # find requirement item what we really need
    req_list, req_mention_list = [], []
    # print(len(text0.keys()), text0)
    for k, v in text0.items():
        for kk, vv in text0.items():
            if str(k).lower() == str(kk).lower():
                # print(k, v)
                req_list.append([k, (v + vv)])
                # print(k, v)
                break
    # print(len(req_list), req_list)
    for kw in user_list:
        for k, v in text0.items():
            if kw.lower() == str(k).lower():
                req_list.append([kw, v])
                break
    # print(req_list)
    for rkw in req_list:
        for ukw in user_list:
            if rkw[0].lower() == ukw.lower():
                req_mention_list.append(rkw)
                break
    print(req_mention_list)

    # create word cloud
    # wordcloud = WordCloud(font_path=r"E:\pythonProcess\website\jobs\database\simhei.ttf",
    #                       background_color="white", mask=imread("python.jpg")).generate(text1)
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.show()

    return req_mention_list
# process_reqirement("job_requirement")

def user_defined(file_name):
    user_list = []
    with open(file_name, "r", encoding="utf8") as f:
        for i in f:
            user_list.append(i.strip())
    return user_list

def process_company(field_name):
    sql = "select " + field_name + " from website.jobs_jobsinfo;"
    company = [list(i) for i in connect_mysql(sql)]
    # user_list = user_defined("t.txt")
    user_list = ['C','C#','C++','Go','Linux','MongoDB','Mysql','PostgreSQL','Ajax','Bootstrap','CSS','Django','Docker','Flask','Git','http','tcp','Java','JavaScript','Jquery','Oracle','Python','Redis','Ruby','Scrapy','shell','Tornado','Web','RESTful','云计算','分布式','前端','后端','大数据','高并发','数据分析','数据挖掘','机器学习','爬虫','算法','自动化','测试','运维','集群']
    jieba.load_userdict(user_list)
    me_list = ['python', 'django', 'linux', '运维', '自动化', '爬虫', '数据分析', 'shell', 'mysql', 'oracle']
    req_list, suit_list = [], []
    for req in company:
        req_dict = Counter(jieba.cut(req[1]))
        req_list.append([req[0], [k for k in req_dict.keys() if k in user_list]])
    for r in req_list:
        if len(r[1]) > 0:
            # print(r[1])
            own = [item for item in me_list if item in r[1]]
            if len(own) > 0:
                suit_list.append([r[0], int(len(own) * 100/len(r[1]))])
    # print(sorted(suit_list, key=lambda x: x[1]))
    return sorted(suit_list, key=lambda x: x[1])
# process_company("company_name, job_requirement")