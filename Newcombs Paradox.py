import newcombfuncs as nfc
import pandas as pd
import sqlite3 as sq
conn=sq.connect("E:\\transfer\\Parth notes\\11th standard\\Informatics Practices\\SQL\\sqlite-tools-win32-x86-3270100\\Newcombparadox.db")

for prob in range(1,101):
    earnM=nfc.newcomb("M",prob)
    earnB=nfc.newcomb("B",prob)
    if earnM>earnB:
        win="M"
    elif earnM<earnB:
        win="B"
    else:
        win="T"
    dic={"Accuracy":prob,"Mystery_Box":earnM,"Both_Box":earnB,"Winner":win}
    earn=pd.DataFrame(dic,index=[0])
    earn.to_sql("earning",conn,if_exists="append")
    
    
    
    
    
