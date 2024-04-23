import os
from time import sleep


import win32com.client

xl = win32com.client.DispatchEx("Excel.Application")

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range("A%s" % (i+1)).Value = "group %s" % i
    sleep(0.5)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()


