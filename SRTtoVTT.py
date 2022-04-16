import sys

try:
    SRTfile_name = sys.argv[1]
    print("ok i got file name ")
    if(sys.argv[1][-4:] != '.srt'):
        raise Exception() 
except:
    print("you must enter a filename")
    sys.exit()


try:
    SRTfile = open(SRTfile_name)
    SRTfile_list = SRTfile.readlines()
    SRTfile.close()

except:
    print("Your file name isn't correct")
    sys.exit()


with open(SRTfile_name[:-4]+".vtt", 'w') as VTTfile:
    VTTfile.write("WEBVTT\n \n")
    i = 0
    for idx, SRTfile_line in enumerate(SRTfile_list):
        if(SRTfile_line[0] != "0" and SRTfile_line[0] != "1" and SRTfile_line[0] != "2" and SRTfile_line[0] != "3" and SRTfile_line[0] != "4" and SRTfile_line[0] != "5" and
           SRTfile_line[0] != "6" and SRTfile_line[0] != "7" and SRTfile_line[0] != "8" and SRTfile_line[0] != "9" and SRTfile_line[0] != "\n"):

            VTTfile.write((str(i))+'\n')
            timeconvert = SRTfile_list[idx-1].replace(',', '.')
            VTTfile.write(timeconvert)
            VTTfile.write((SRTfile_line)+'\n')

            i += 1

    print("\n     Your file converted successfully :)")
