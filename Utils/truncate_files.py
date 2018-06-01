import os
d = {}
d["w02_z00.mp4"]=  95040670
d["w02_z01.mp4"]=   122116749
d["w02_z02.mp4"]=   125734963
d["w02_z03.mp4"]=   126154867
d["w02_z04.mp4"]=   117733868
d["w02_z05.mp4"]=   115494313
d["w02_z99.mp4"]=   103283854
d["w02_z06.mp4"]=   115715754
d["w02_z07.mp4"]=   117248014
d["w05_z00.mp4"]=  91778123
d["w05_z01.mp4"]=   119302456
d["w05_z03.mp4"]=   116107717
d["w05_z02.mp4"]=   115847723
d["w05_z04.mp4"]=   116556067
d["w05_z05.mp4"]=   116253493
d["w05_z07.mp4"]=   114675142
d["w05_z06.mp4"]=   115534575
d["w05_z99.mp4"]=   104478125
d["w07_z00.mp4"]=  80602320
d["w07_z01.mp4"]=   121325487
d["w07_z02.mp4"]=   124683378
d["w07_z03.mp4"]=   128381577
d["w07_z04.mp4"]=   128898505
d["w07_z05.mp4"]=   128077726
d["w07_z06.mp4"]=   123565278
d["w07_z07.mp4"]=   118486376
d["w07_z99.mp4"]=  99738286


root = "C:\\Users\\sss\\Desktop\\Example_Patient_Work\\video-trucated"

i = 1

for key, value in d.items():
    print i, " - truncating ", key

    fo = open(os.path.join(root,key), 'r+')
    fo.truncate(value+1)
    fo.close()


while True:
    pass