import os
import random
def autofile_path(keyword, inside_fold, folder_nm):
    try:
        no = random.random()
        xno = round(no, 2)
        rno = str(xno)
        x = os.getcwd()
        y = folder_nm
        parent = os.path.join(x, y, inside_fold)
        child = keyword + "data" + rno + ".jpg"
        file_path = os.path.join(parent, child)
        return file_path
        print("filecreated succesfully")
    except Exception as e:
        print("error due to ___",e)

"""keyword  = 'modiji'
folder_nm = "imagemy"
inside_fold = "modiji"
x = autofile_path(keyword, inside_fold, folder_nm)
f = open(x,'wb')"""