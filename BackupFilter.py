import os, time, sys,calendar
from datetime import date

def last_5_days_backup_file(path,x,now,NumberofDays):#checks if the file is from last 5 days.
    j=os.path.getmtime(path+'/'+x)
    if j>(now-5*86400):
        del(j)
        return(x)
    else:
        return(0)

def last_4_sat():
    today=date.today()
    d= today.toordinal()#Number of days passed since 1/1/1
    saturdays_date=[]
    last_sat= d-(d%7)-1
    for n in range(0,4):
        saturdays_date.append(str(date.fromordinal(last_sat)))
        last_sat=last_sat-7
    del(last_sat)
    del(today)
    return(saturdays_date)

def last_date_month(x):#Checks if the date is the last dtae of the month.
    temp=x.split("-")
    real_last_date=calendar.monthrange(int(temp[0]),int(temp[1]))
    if int(temp[2])==real_last_date[1]:
        del(temp)
        return(True)
    del(temp)
    return(False)
    
def file_removal(fsave,f,path):#Removes the files which are not present in fsave i.e does not satisfies the conditions. 
    fsave='_'.join(fsave)
    for x in f:
        if fsave.find(str(x))==-1:
            os.remove(path+'/'+x)
        else:
            pass
    del(f)
    del(fsave)
    del(path)
    
def filter(path,NumberofDays):
    
    now = time.time()
    file=os.listdir(path)
    
    files_saved=last_4_sat()
    
    for x in file:

        temp=last_5_days_backup_file(path,x,now,NumberofDays)
        
        if temp!=0:
            files_saved.append(str(temp))

        elif last_date_month(x[10:-4]):
            files_saved.append(str(temp))

        else:
            pass
    del(now)
    file_removal(files_saved,file,path)
   
'''path="C:/Users/HP/Desktop/Python Data Backup Task/bucket1"
filter(path,5)'''
