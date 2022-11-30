import xlsxwriter

data = [
    ['3d61125', '1.02 TB'], 
    [
        [6.152, 6.15, 1265.86, 1254.0, 1401.0, 6849.0, 18744.0, 19268.0, 19530.0, 19530.0], 
        [27.3, 27.0, 290.1, 297.0, 322.0, 408.0, 441.0, 465.0, 1074.0, 1106.0], 
        [136.0, 13.0, 232.73, 93.0, 215.0, 1156.0, 17695.0, 20317.0, 27132.0, 27395.0], 
        [275.0, 27.0, 114.77, 101.0, 133.0, 273.0, 367.0, 461.0, 832.0, 922.0], 
        [6.924, 6.92, 1123.03, 1237.0, 1385.0, 3916.0, 7111.0, 7635.0, 7767.0, 7767.0], 
        [27.5, 27.0, 287.41, 297.0, 322.0, 396.0, 498.0, 750.0, 1106.0, 1156.0], 
        [88.6, 88.0, 10.04978, 10.0, 10.0, 54.0, 127.0, 1811.0, 5735.0, 11207.0], 
        [12.3, 12.0, 80.15, 89.0, 90.0, 93.0, 102.0, 188.0, 594.0, 816.0]
    ], 
    [
        ['1GB', '128KB', '8', '1'], 
        ['1GB', '128KB', '8', '1'], 
        ['1GB', '4KB', '2', '6'], 
        ['1GB', '4KB', '2', '6'], 
        ['1GB', '4KB', '1', '1'], 
        ['1GB', '4KB', '1', '1'], 
        ['100%', '128KB', '8', '1'], 
        ['100%', '128KB', '8', '1']
    ]
    ]


workbook = xlsxwriter.Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet()

# Drive Standard Configuration.
worksheet.write("A1", "Standard Device Config.")
worksheet.write("A2", "Firware Rev.")  
worksheet.write("A3", "Drive Capacity")
worksheet.write("B2", data[0][0])
worksheet.write("B3", data[0][1])

# Standard FIO Scripts
worksheet.write("A6", "Standard Device Config.")
worksheet.write("A7", "Standard Device Config.")
worksheet.write("A8", "Standard Device Config.")
worksheet.write("A9", "Standard Device Config.")
worksheet.write("A10", "Standard Device Config.")
worksheet.write("A11", "Standard Device Config.")
worksheet.write("A12", "Standard Device Config.")
worksheet.write("A13", "Standard Device Config.")


workbook.close()
