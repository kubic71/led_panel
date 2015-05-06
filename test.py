import time, math

def test1(count=1000):
    """writing into video memory"""
    
    #ser = serial.Serial('/dev/ttyACM3', 115200, timeout=0.1)
    # time.sleep(1)
    r = 0.5
    g = 0
    b = 0
    #j = ser.readlines()
    
    data_pattern = '\x00\x00\x00\x10\x10\x10   @@@'
    count_of_pixels = 40
    begin_time = time.time()
    for change_number in range(count):
        for memblock in range(4):
            command = "m{} {}".format(memblock * count_of_pixels, count_of_pixels)
            #print command
            #m = ser.write(prikaz + "\n")
            #while ser.inWaiting() < len(prikaz) + 2:
            #    pass
            #j = ser.read(len(prikaz) + 2)
            
            # apply rgb modifying
            r = max(math.sin(change_number/50.), 0)
            g = max(math.sin(change_number/50. + math.pi * 2 / 3), 0)
            b = max(math.sin(change_number/50. + math.pi * 4 / 3), 0)
            modif_data_pattern = ""
            for i in range(len(data_pattern)):
                modif_data_pattern += chr(int(ord(data_pattern[i]) * \
                    (r * (i % 3 == 0) + g * (i % 3 == 1) + b * (i % 3 == 2))))
            # data writing
            data = rotate(modif_data_pattern, (change_number * 3) % len(data_pattern)) \
                   * (count_of_pixels * 3 / len(data_pattern))

            print (list(data))
            
            #print len(data)
            #print data
            
        command = "show"



 
    end_time = time.time()
    print "{} changes".format(count)
    print "total time {} seconds".format(end_time - begin_time)
    print "one change period {} seconds".format((end_time - begin_time) / count)
        
    return #ser

def rotate(l,n):
    """ list rotation """
    return l[n:] + l[:n]



test1()