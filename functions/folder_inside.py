import os

def folderIn(folder_nm, inside_folder):
    try:
        x = os.getcwd()
        parent = x
        child1 = folder_nm
        child2 = inside_folder
        path = os.path.join(parent, child1, child2)
        if not os.path.exists(path):
            os.makedirs(path)
            print(path)
            print("foldercreated succesfully")


    except Exception as e:
        print("error due to ___",e)

"""folder_nm = "manish"
inside_folder = '5negi'
folderIn(folder_nm, inside_foldernm)"""