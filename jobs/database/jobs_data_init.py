#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2018/1/23 22:58 
# @name: jobs_data_init
# @author：vickey-wu

import pymysql

jobs_list = []
with open("jobs_data.txt", "r") as f:
    for j in f:
        # job_title, job_salary, job_requirement, job_addr, job_exp, job_edu, job_tags, company_name, company_employee_num, company_type = j.strip().split(",")
        jobs_list.append(j.strip().split(","))
    print(jobs_list)

sql = '''INSERT INTO website.jobs_jobsinfo (job_title, job_salary, job_requirement, job_addr, job_exp, job_edu, job_tags, company_name, company_employee_num, company_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

conn = pymysql.connect(host="localhost", user="root", password="vickey123$",
                       database="website", port=3306)
cur = conn.cursor()
cur.executemany(sql, jobs_list)
conn.commit()
