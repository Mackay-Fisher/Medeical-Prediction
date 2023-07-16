#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:08:34 2023

@author: mackayfisher
"""

import pandas as pd

df = pd.read_csv('Appointmentpython.csv',usecols=["Provider/Resource","OverBk"])

count_BeachRobertE = 0
count_BeachRobertE_booked = 0

count_Provider_Stv_Dermatology = 0
count_Provider_Stv_Dermatology_booked = 0

count_Provider_Stv_Endocrine = 0
count_Provider_Stv_Endocrine_booked  = 0

count_Provider_Stv_Ent = 0
count_Provider_Stv_Ent_booked  = 0

count_Provider_Stv_Medicine = 0
count_Provider_Stv_Medicine_booked  = 0

count_Provider_Stv_Neurology = 0
count_Provider_Stv_Neurology_booked  = 0

count_Provider_Stv_Ob_Gyn= 0
count_Provider_Stv_Ob_Gyn_booked  = 0

count_Provider_Stv_Ophthalmology= 0
count_Provider_Stv_Ophthalmology_booked  = 0

count_Provider_Stv_Psychiatry= 0
count_Provider_Stv_Psychiatry_booked  = 0

count_Provider_Stv_Rheumatology= 0
count_Provider_Stv_Rheumatology_booked  = 0

count_Provider_Stv_Telehealth = 0
count_Provider_Stv_Telehealth_booked  = 0

for index, row in df.iterrows():
    if row['Provider/Resource'] == "Beach, Robert E":
        count_BeachRobertE= count_BeachRobertE + 1
        if row['OverBk'] == 1.0:
           count_BeachRobertE_booked = count_BeachRobertE_booked +1 
    if row['Provider/Resource'] == "Provider-Stv, Dermatology":
        count_Provider_Stv_Dermatology =count_Provider_Stv_Dermatology +1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Dermatology_booked  =count_Provider_Stv_Dermatology_booked  +1   
    if row['Provider/Resource'] == "Provider-Stv, Endocrine":
        count_Provider_Stv_Endocrine = count_Provider_Stv_Endocrine + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Endocrine_booked  = count_Provider_Stv_Endocrine_booked  + 1   
    if row['Provider/Resource'] == "Provider-Stv, Ent":
        count_Provider_Stv_Ent = count_Provider_Stv_Ent + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Ent_booked  = count_Provider_Stv_Ent_booked  + 1   
    if row['Provider/Resource'] == "Provider-Stv, Medicine":
        count_Provider_Stv_Medicine = count_Provider_Stv_Medicine + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Medicine_booked  = count_Provider_Stv_Medicine_booked  + 1   
    if row['Provider/Resource'] == "Provider-Stv, Neurology":
        count_Provider_Stv_Neurology = count_Provider_Stv_Neurology + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Neurology_booked  = count_Provider_Stv_Neurology_booked  + 1   
    if row['Provider/Resource'] == "Provider-Stv, Ob/Gyn":
        count_Provider_Stv_Ob_Gyn = count_Provider_Stv_Ob_Gyn + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Ob_Gyn_booked  = count_Provider_Stv_Ob_Gyn_booked  + 1 
    if row['Provider/Resource'] == "Provider-Stv, Ophthalmology":
        count_Provider_Stv_Ophthalmology = count_Provider_Stv_Ophthalmology + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Ophthalmology_booked  = count_Provider_Stv_Ophthalmology_booked  + 1   
    if row['Provider/Resource'] == "Provider-Stv, Psychiatry":
        count_Provider_Stv_Psychiatry = count_Provider_Stv_Psychiatry + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Psychiatry_booked  = count_Provider_Stv_Psychiatry_booked  + 1  
    if row['Provider/Resource'] == "Provider-Stv, Rheumatology":
        count_Provider_Stv_Rheumatology = count_Provider_Stv_Rheumatology + 1
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Rheumatology_booked  = count_Provider_Stv_Rheumatology_booked  + 1   
    if row['Provider/Resource'] == "Provider-Stv, Telehealth":
        count_Provider_Stv_Telehealth = count_Provider_Stv_Telehealth + 1 
        if row['OverBk'] == 1.0:
            count_Provider_Stv_Telehealth_booked  = count_Provider_Stv_Telehealth_booked  + 1    

count_BeachRobertE_overbooked = count_BeachRobertE - count_BeachRobertE_booked
count_Provider_Stv_Dermatology_overbooked = count_Provider_Stv_Dermatology - count_Provider_Stv_Dermatology_booked
count_Provider_Stv_Endocrine_overbooked = count_Provider_Stv_Endocrine - count_Provider_Stv_Endocrine_booked
count_Provider_Stv_Ent_overbooked = count_Provider_Stv_Ent - count_Provider_Stv_Ent_booked
count_Provider_Stv_Medicine_overbooked = count_Provider_Stv_Medicine - count_Provider_Stv_Medicine_booked 
count_Provider_Stv_Neurology_overbooked = count_Provider_Stv_Neurology - count_Provider_Stv_Neurology_booked
count_Provider_Stv_Ob_Gyn_overbooked = count_Provider_Stv_Ob_Gyn - count_Provider_Stv_Ob_Gyn_booked
count_Provider_Stv_Ophthalmology_overbooked = count_Provider_Stv_Ophthalmology - count_Provider_Stv_Ophthalmology_booked
count_Provider_Stv_Psychiatry_overbooked = count_Provider_Stv_Psychiatry - count_Provider_Stv_Psychiatry_booked
count_Provider_Stv_Rheumatology_overbooked = count_Provider_Stv_Rheumatology - count_Provider_Stv_Rheumatology_booked
count_Provider_Stv_Telehealth_overbooked = count_Provider_Stv_Telehealth - count_Provider_Stv_Telehealth_booked

total = count_BeachRobertE + count_Provider_Stv_Dermatology + count_Provider_Stv_Endocrine + count_Provider_Stv_Ent + count_Provider_Stv_Medicine + count_Provider_Stv_Neurology + count_Provider_Stv_Ob_Gyn + count_Provider_Stv_Ophthalmology + count_Provider_Stv_Psychiatry + count_Provider_Stv_Rheumatology  + count_Provider_Stv_Telehealth
total_booked = count_BeachRobertE_booked+count_Provider_Stv_Dermatology_booked+count_Provider_Stv_Endocrine_booked+count_Provider_Stv_Ent_booked+count_Provider_Stv_Medicine_booked+count_Provider_Stv_Neurology_booked+count_Provider_Stv_Ob_Gyn_booked+count_Provider_Stv_Ophthalmology_booked+count_Provider_Stv_Psychiatry_booked + count_Provider_Stv_Rheumatology_booked + count_Provider_Stv_Telehealth_booked
total_overbooked = total - total_booked

dbl_count_BeachRobertE_overbooked = float(count_BeachRobertE_booked/count_BeachRobertE)  * 100
dbl_count_Provider_Stv_Dermatology_overbooked = float (count_Provider_Stv_Dermatology_booked/count_Provider_Stv_Dermatology)* 100
dbl_count_Provider_Stv_Endocrine_overbooked = float ( count_Provider_Stv_Endocrine_booked/count_Provider_Stv_Endocrine )* 100
dbl_count_Provider_Stv_Ent_overbooked = float ( count_Provider_Stv_Ent_booked/count_Provider_Stv_Ent)* 100
dbl_count_Provider_Stv_Medicine_overbooked = float ( count_Provider_Stv_Medicine_booked/count_Provider_Stv_Medicine )* 100
dbl_count_Provider_Stv_Neurology_overbooked = float ( count_Provider_Stv_Neurology_booked/count_Provider_Stv_Neurology)* 100
dbl_count_Provider_Stv_Ob_Gyn_overbooked = float ( count_Provider_Stv_Ob_Gyn_booked/count_Provider_Stv_Ob_Gyn)* 100
dbl_count_Provider_Stv_Ophthalmology_overbooked = float ( count_Provider_Stv_Ophthalmology_booked/count_Provider_Stv_Ophthalmology)* 100
dbl_count_Provider_Stv_Psychiatry_overbooked = float ( count_Provider_Stv_Psychiatry_booked/count_Provider_Stv_Psychiatry)* 100
dbl_count_Provider_Stv_Rheumatology_overbooked = float ( count_Provider_Stv_Rheumatology_booked/count_Provider_Stv_Rheumatology)* 100
dbl_count_Provider_Stv_Telehealth_overbooked = float ( count_Provider_Stv_Telehealth_booked/count_Provider_Stv_Telehealth) * 100
dbl_total_overbooked = float ( total_booked/total) * 100

dbl_count_BeachRobertE_booked = 100 - dbl_count_BeachRobertE_overbooked
dbl_count_Provider_Stv_Dermatology_booked = 100 - dbl_count_Provider_Stv_Dermatology_overbooked
dbl_count_Provider_Stv_Endocrine_booked = 100 - dbl_count_Provider_Stv_Endocrine_overbooked
dbl_count_Provider_Stv_Ent_booked = 100 - dbl_count_Provider_Stv_Ent_overbooked 
dbl_count_Provider_Stv_Medicine_booked = 100 - dbl_count_Provider_Stv_Medicine_overbooked
dbl_count_Provider_Stv_Neurology_booked = 100 - dbl_count_Provider_Stv_Neurology_overbooked
dbl_count_Provider_Stv_Ob_Gyn_booked = 100 - dbl_count_Provider_Stv_Ob_Gyn_overbooked
dbl_count_Provider_Stv_Ophthalmology_booked = 100 - dbl_count_Provider_Stv_Ophthalmology_overbooked
dbl_count_Provider_Stv_Psychiatry_booked = 100 - dbl_count_Provider_Stv_Psychiatry_overbooked
dbl_count_Provider_Stv_Rheumatology_booked = 100 - dbl_count_Provider_Stv_Rheumatology_overbooked
dbl_count_Provider_Stv_Telehealth_booked = 100 - dbl_count_Provider_Stv_Telehealth_overbooked
dbl_total_booked = 100 - dbl_total_overbooked


print(total)
d={'Names': ["Beach, Robert E","Provider-Stv, Dermatology","Provider-Stv, Endocrine","Provider-Stv, Ent","Provider-Stv, Medicine","Provider-Stv, Neurology","Provider-Stv, Ob/Gyn","Provider-Stv, Ophthalmology","Provider-Stv, Psychiatry","Provider-Stv, Rheumatology","Provider-Stv, Telehealth","Total"]
   , 'Over-Booked' : [count_BeachRobertE_booked,count_Provider_Stv_Dermatology_booked,count_Provider_Stv_Endocrine_booked,count_Provider_Stv_Ent_booked,count_Provider_Stv_Medicine_booked,count_Provider_Stv_Neurology_booked,count_Provider_Stv_Ob_Gyn_booked,count_Provider_Stv_Ophthalmology_booked,count_Provider_Stv_Psychiatry_booked,count_Provider_Stv_Rheumatology_booked,count_Provider_Stv_Telehealth_booked,total_booked]
   , 'Booked' : [count_BeachRobertE_overbooked,count_Provider_Stv_Dermatology_overbooked,count_Provider_Stv_Endocrine_overbooked,count_Provider_Stv_Ent_overbooked,count_Provider_Stv_Medicine_overbooked,count_Provider_Stv_Neurology_overbooked,count_Provider_Stv_Ob_Gyn_overbooked,count_Provider_Stv_Ophthalmology_overbooked,count_Provider_Stv_Psychiatry_overbooked,count_Provider_Stv_Rheumatology_overbooked,count_Provider_Stv_Telehealth_overbooked,total_overbooked]
   , 'Total': [count_BeachRobertE,count_Provider_Stv_Dermatology,count_Provider_Stv_Endocrine,count_Provider_Stv_Ent,count_Provider_Stv_Medicine,count_Provider_Stv_Neurology,count_Provider_Stv_Ob_Gyn,count_Provider_Stv_Ophthalmology,count_Provider_Stv_Psychiatry,count_Provider_Stv_Rheumatology,count_Provider_Stv_Telehealth,total]
   , 'DBL(OB)' : [dbl_count_BeachRobertE_overbooked,dbl_count_Provider_Stv_Dermatology_overbooked,dbl_count_Provider_Stv_Endocrine_overbooked,dbl_count_Provider_Stv_Ent_overbooked,dbl_count_Provider_Stv_Medicine_overbooked,dbl_count_Provider_Stv_Neurology_overbooked,dbl_count_Provider_Stv_Ob_Gyn_overbooked,dbl_count_Provider_Stv_Ophthalmology_overbooked,dbl_count_Provider_Stv_Psychiatry_overbooked,dbl_count_Provider_Stv_Rheumatology_overbooked,dbl_count_Provider_Stv_Telehealth_overbooked,dbl_total_overbooked]
   , 'DBL(B)' : [dbl_count_BeachRobertE_booked,dbl_count_Provider_Stv_Dermatology_booked,dbl_count_Provider_Stv_Endocrine_booked,dbl_count_Provider_Stv_Ent_booked,dbl_count_Provider_Stv_Medicine_booked,dbl_count_Provider_Stv_Neurology_booked,dbl_count_Provider_Stv_Ob_Gyn_booked,dbl_count_Provider_Stv_Ophthalmology_booked,dbl_count_Provider_Stv_Psychiatry_booked,dbl_count_Provider_Stv_Rheumatology_booked,dbl_count_Provider_Stv_Telehealth_booked,dbl_total_booked]
   }

Lucy_data = pd.DataFrame(data=d)
print(Lucy_data)
