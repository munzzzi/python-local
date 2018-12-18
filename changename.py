import os 

os.chdir(r'C:\Users\student\change\SSAFY지원자')

for filename in os.listdir("."):
    #os.rename(filename, "SSAFY_"+filename[13:])
   after_name = filename.replace("SSAFY","S"))
   os.rename(filename, after_name)