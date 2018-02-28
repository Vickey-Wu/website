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
import pandas as pd
import numpy as np
import matplotlib as mpl
import re


def connect_mysql(sql, oper_type="select", data_l=None):
    conn = pymysql.connect(host='localhost', user="root", password="123",
                           database="website", port=3306)
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

data_insert()



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
def process_jobs(field_name):
    sql = "select j." + field_name + " from jobs_jobsinfo j"
    column_name = connect_mysql(sql, oper_type="select")
    row_total = (len(column_name))
    row_category = set(column_name)

    # init category dict
    category_dict = {}
    for k in row_category:
        category_dict[k] = 0

    # calculate amount
    cal_nmu = 0
    for k in row_category:
        for r in column_name:
            if r == k:
                cal_nmu += 1
        category_dict[k] = cal_nmu
        cal_nmu = 0
    print(type(category_dict.items()), category_dict.items())
    print(row_total, len(category_dict.items()))
    return row_total, category_dict

# process_jobs("job_salary")