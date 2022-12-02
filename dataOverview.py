import xlsxwriter

# data_a = [Firmware, capacity]
# data_b = [Iops, Bandwidth, AVg. latecy, 50th-99.9999th ]
# data_c = [Size, Block size, IO-DEPTH, Thread]

data_X = [
    ['3d61125', '1.02 TB'],
    [
        [23.3, 3060.0, 336.04, 269.0, 310.0, 1369.0, 5276.0, 5473.0, 6390.0, 6456.0],
        [27.3, 3576.0, 290.1, 297.0, 322.0, 408.0, 441.0, 465.0, 1074.0, 1106.0],
        [6.924, 908.0, 1123.03, 1237.0, 1385.0,
            3916.0, 7111.0, 7635.0, 7767.0, 7767.0],
        [27.5, 3610.0, 287.41, 297.0, 322.0, 396.0, 498.0, 750.0, 1106.0, 1156.0],
        [136.0, 556.0, 232.73, 93.0, 215.0, 1156.0,
            17695.0, 20317.0, 27132.0, 27395.0],
        [275.0, 1127.0, 114.77, 101.0, 133.0, 273.0, 367.0, 461.0, 832.0, 922.0],
        [88.6, 363.0, 10.04978, 10.0, 10.0, 54.0, 127.0, 1811.0, 5735.0, 11207.0],
        [12.3, 50.4, 80.15, 89.0, 90.0, 93.0, 102.0, 188.0, 594.0, 816.0]
    ],
    [
        ['1GB', '128KB', '8', '1'],
        ['1GB', '128KB', '8', '1'],
        ['100%', '128KB', '8', '1'],
        ['100%', '128KB', '8', '1'],
        ['1GB', '4KB', '2', '6'],
        ['1GB', '4KB', '2', '6'],
        ['1GB', '4KB', '1', '1'],
        ['1GB', '4KB', '1', '1']
    ]
]

def excelPlot(data):

    workbook = xlsxwriter.Workbook('write_data.xlsx')
    worksheet = workbook.add_worksheet()    

    # Drive Standard Configuration.
    worksheet.write("A1", "Standard Device Config.")
    worksheet.write("A2", "Firware Rev.")
    worksheet.write("A3", "Drive Capacity")
    worksheet.write("B2", data[0][0])
    worksheet.write("B3", data[0][1])   

    # Standard FIO Scripts
    worksheet.write("A6", "BURST SEQUENTIAL WRITE")
    worksheet.write("A7", "BURST SEQUENTIAL READ")
    worksheet.write("A8", "SUBSTAIN SEQUENTIAL WRITE")
    worksheet.write("A9", "SUBSTAIN SEQUENTIAL READ")
    worksheet.write("A10", "BURST RANDOM WRITE")
    worksheet.write("A11", "BURST RANDOM READ")
    worksheet.write("A12", "BURST RANDOM WRITE OIO")
    worksheet.write("A13", "BURST RANDOM READ OIO") 

    # Table column name
    worksheet.write("B5", "SIZE")
    worksheet.write("C5", "BLOCK SIZE")
    worksheet.write("D5", "IO-DEPTHS")
    worksheet.write("E5", "THREADS")
    worksheet.write("F5", "PRECONDITION")
    worksheet.write("G5", "IOPS")
    worksheet.write("H5", "BANDWIDTH")
    worksheet.write("I5", "AVG. LATENCY")
    worksheet.write("J5", "50th")
    worksheet.write("K5", "75th")
    worksheet.write("L5", "99th")
    worksheet.write("M5", "99.9th")
    worksheet.write("N5", "99.99th")
    worksheet.write("O5", "99.999th")
    worksheet.write("P5", "99.9999th")  

    # cell = ["B6","C6","D6","E6","F6","G6","H6","I6","J6","K6","L6","M6","N6","O6","P6"]
    fileIndex = 0
    # BURST SEQUENTIAL WRITE
    worksheet.write("B6", data[2][fileIndex][0])
    worksheet.write("C6", data[2][fileIndex][1])
    worksheet.write("D6", data[2][fileIndex][2])
    worksheet.write("E6", data[2][fileIndex][3])
    worksheet.write("F6", "BPC1")
    worksheet.write("G6", data[1][fileIndex][0])
    worksheet.write("H6", data[1][fileIndex][1])
    worksheet.write("I6", data[1][fileIndex][2])
    worksheet.write("J6", data[1][fileIndex][3])
    worksheet.write("K6", data[1][fileIndex][4])
    worksheet.write("L6", data[1][fileIndex][5])
    worksheet.write("M6", data[1][fileIndex][6])
    worksheet.write("N6", data[1][fileIndex][7])
    worksheet.write("O6", data[1][fileIndex][8])
    worksheet.write("P6", data[1][fileIndex][9])    

    fileIndex = fileIndex + 1
    # BURST SEQUENTIAL READ
    worksheet.write("B7", data[2][fileIndex][0])
    worksheet.write("C7", data[2][fileIndex][1])
    worksheet.write("D7", data[2][fileIndex][2])
    worksheet.write("E7", data[2][fileIndex][3])
    worksheet.write("F7", "BPC1")
    worksheet.write("G7", data[1][fileIndex][0])
    worksheet.write("H7", data[1][fileIndex][1])
    worksheet.write("I7", data[1][fileIndex][2])
    worksheet.write("J7", data[1][fileIndex][3])
    worksheet.write("K7", data[1][fileIndex][4])
    worksheet.write("L7", data[1][fileIndex][5])
    worksheet.write("M7", data[1][fileIndex][6])
    worksheet.write("N7", data[1][fileIndex][7])
    worksheet.write("O7", data[1][fileIndex][8])
    worksheet.write("P7", data[1][fileIndex][9])    

    fileIndex = fileIndex + 1
    # SUBSTAIN SEQUENTIAL WRITE
    worksheet.write("B8", data[2][fileIndex][0])
    worksheet.write("C8", data[2][fileIndex][1])
    worksheet.write("D8", data[2][fileIndex][2])
    worksheet.write("E8", data[2][fileIndex][3])
    worksheet.write("F8", "BPC1")
    worksheet.write("G8", data[1][fileIndex][0])
    worksheet.write("H8", data[1][fileIndex][1])
    worksheet.write("I8", data[1][fileIndex][2])
    worksheet.write("J8", data[1][fileIndex][3])
    worksheet.write("K8", data[1][fileIndex][4])
    worksheet.write("L8", data[1][fileIndex][5])
    worksheet.write("M8", data[1][fileIndex][6])
    worksheet.write("N8", data[1][fileIndex][7])
    worksheet.write("O8", data[1][fileIndex][8])
    worksheet.write("P8", data[1][fileIndex][9])    

    fileIndex = fileIndex + 1
    # SUBSTAIN SEQUENTIAL READ
    worksheet.write("B9", data[2][fileIndex][0])
    worksheet.write("C9", data[2][fileIndex][1])
    worksheet.write("D9", data[2][fileIndex][2])
    worksheet.write("E9", data[2][fileIndex][3])
    worksheet.write("F9", "BPC1")
    worksheet.write("G9", data[1][fileIndex][0])
    worksheet.write("H9", data[1][fileIndex][1])
    worksheet.write("I9", data[1][fileIndex][2])
    worksheet.write("J9", data[1][fileIndex][3])
    worksheet.write("K9", data[1][fileIndex][4])
    worksheet.write("L9", data[1][fileIndex][5])
    worksheet.write("M9", data[1][fileIndex][6])
    worksheet.write("N9", data[1][fileIndex][7])
    worksheet.write("O9", data[1][fileIndex][8])
    worksheet.write("P9", data[1][fileIndex][9])    

    fileIndex = fileIndex + 1
    # BURST RANDOM WRITE
    worksheet.write("B10", data[2][fileIndex][0])
    worksheet.write("C10", data[2][fileIndex][1])
    worksheet.write("D10", data[2][fileIndex][2])
    worksheet.write("E10", data[2][fileIndex][3])
    worksheet.write("F10", "BPC1")
    worksheet.write("G10", data[1][fileIndex][0])
    worksheet.write("H10", data[1][fileIndex][1])
    worksheet.write("I10", data[1][fileIndex][2])
    worksheet.write("J10", data[1][fileIndex][3])
    worksheet.write("K10", data[1][fileIndex][4])
    worksheet.write("L10", data[1][fileIndex][5])
    worksheet.write("M10", data[1][fileIndex][6])
    worksheet.write("N10", data[1][fileIndex][7])
    worksheet.write("O10", data[1][fileIndex][8])
    worksheet.write("P10", data[1][fileIndex][9])   

    fileIndex = fileIndex + 1
    # BURST RANDOM READ
    worksheet.write("B11", data[2][fileIndex][0])
    worksheet.write("C11", data[2][fileIndex][1])
    worksheet.write("D11", data[2][fileIndex][2])
    worksheet.write("E11", data[2][fileIndex][3])
    worksheet.write("F11", "BPC1")
    worksheet.write("G11", data[1][fileIndex][0])
    worksheet.write("H11", data[1][fileIndex][1])
    worksheet.write("I11", data[1][fileIndex][2])
    worksheet.write("J11", data[1][fileIndex][3])
    worksheet.write("K11", data[1][fileIndex][4])
    worksheet.write("L11", data[1][fileIndex][5])
    worksheet.write("M11", data[1][fileIndex][6])
    worksheet.write("N11", data[1][fileIndex][7])
    worksheet.write("O11", data[1][fileIndex][8])
    worksheet.write("P11", data[1][fileIndex][9])   

    fileIndex = fileIndex + 1
    # BURST RANDOM WRITE OIO
    worksheet.write("B12", data[2][fileIndex][0])
    worksheet.write("C12", data[2][fileIndex][1])
    worksheet.write("D12", data[2][fileIndex][2])
    worksheet.write("E12", data[2][fileIndex][3])
    worksheet.write("F12", "BPC1")
    worksheet.write("G12", data[1][fileIndex][0])
    worksheet.write("H12", data[1][fileIndex][1])
    worksheet.write("I12", data[1][fileIndex][2])
    worksheet.write("J12", data[1][fileIndex][3])
    worksheet.write("K12", data[1][fileIndex][4])
    worksheet.write("L12", data[1][fileIndex][5])
    worksheet.write("M12", data[1][fileIndex][6])
    worksheet.write("N12", data[1][fileIndex][7])
    worksheet.write("O12", data[1][fileIndex][8])
    worksheet.write("P12", data[1][fileIndex][9])   

    fileIndex = fileIndex + 1
    # BURST RANDOM READ OIO
    worksheet.write("B13", data[2][fileIndex][0])
    worksheet.write("C13", data[2][fileIndex][1])
    worksheet.write("D13", data[2][fileIndex][2])
    worksheet.write("E13", data[2][fileIndex][3])
    worksheet.write("F13", "BPC1")
    worksheet.write("G13", data[1][fileIndex][0])
    worksheet.write("H13", data[1][fileIndex][1])
    worksheet.write("I13", data[1][fileIndex][2])
    worksheet.write("J13", data[1][fileIndex][3])
    worksheet.write("K13", data[1][fileIndex][4])
    worksheet.write("L13", data[1][fileIndex][5])
    worksheet.write("M13", data[1][fileIndex][6])
    worksheet.write("N13", data[1][fileIndex][7])
    worksheet.write("O13", data[1][fileIndex][8])
    worksheet.write("P13", data[1][fileIndex][9])   


    workbook.close()
