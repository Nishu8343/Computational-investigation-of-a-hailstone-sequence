import xlsxwriter
    # Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('test20.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0 , "For Power m")
worksheet.write(0,1,"base3")
worksheet.write(0,2,"ratio")
worksheet.write(0,3,"base5")
worksheet.write(0,4, "ratio")
worksheet.write(0,5,"base7")
worksheet.write(0,6, "ratio")
worksheet.write(0,7,"base2")
worksheet.write(0,8, "ratio")
worksheet.write(0,9,"base6")
worksheet.write(0,10, "ratio")
worksheet.write(0,11,"base10")
worksheet.write(0,12, "ratio")
worksheet.write(0,13,"base12")
worksheet.write(0,14,"ratio")
worksheet.write(0,15,"base14")
worksheet.write(0,16, "ratio")
worksheet.write(0,17,"base18")
worksheet.write(0,18, "ratio")





m = 1

base2 = pow(2, m)-1
base3 = pow(3, m)-1
base5 = pow(5, m)-1
base6 = pow(6, m)-1
base7 = pow(7, m)-1
base10 = pow(10, m)-1
base12 = pow(12, m)-1
base14 = pow(14,m)-1
base18 = pow(18,m)-1

diff2 = 0
diff3 = 0
diff5 = 0
diff6 = 0
diff7 = 0
diff10 = 0
diff12 = 0
diff14 = 0
diff18 = 0

ratio2 = 0
ratio3 = 0
ratio5 = 0
ratio6 = 0
ratio7 = 0
ratio10 = 0
ratio12 = 0
ratio14 = 0
ratio18 = 0



m1 = int(input("Enter a number for m: "))


while m <= m1:    
           
    base2 = pow(2, m)-1
    Max2 = base2

    while base2 !=4:

        if base2 % 2 == 0:
            base2 = base2/2
        else:
            base2 = 3*base2 +1

        num2 = int(base2)


        if Max2 <= num2:
            Max2 = num2
             
        
            
    base3 = pow(3, m)-1
    Max3 = base3

    while base3 !=4:
        

        if base3 % 2 == 0:
            base3 = base3/2
        else:
            base3 = 3*base3 +1

        num3 = int(base3)


        if Max3 <= num3:
            Max3 = num3
        
        
    base5 = pow(5, m)-1
    Max5 = base5

    while base5 !=4:
        if base5 % 2 == 0:
            base5 = base5/2
        else:
            base5 = 3*base5 +1
    
        num5 = int(base5)


        if Max5 <= num5:
            Max5 = num5
        
            
    base6 = pow(6, m)-1
    Max6 = base6
    while base6 !=4:
        

        if base6 % 2 == 0:
            base6 = base6/2
        else:
            base6 = 3*base6 +1

        num6 = int(base6)


        if Max6 <= num6:
            Max6 = num6
        
           
    base7 = pow(7, m)-1
    Max7 = base7
    while base7 !=4:
        

        if base7 % 2 == 0:
            base7 = base7/2
        else:
            base7 = 3*base7 +1

        num7 = int(base7)


        if Max7 <= num7:
            Max7 = num7
        
    

    base10 = pow(10, m)-1
    Max10 = base10
    while base10 !=4:
        

        if base10 % 2 == 0:
            base10 = base10/2
        else:
            base10 = 3*base10 +1

        num10 = int(base10)


        if Max10 <= num10:
            Max10 = num10
        

    base12 = pow(12, m)-1
    Max12 = base12
    while base12 !=4:
        if base12 % 2 == 0:
            base12 = base12/2
        else:
            base12 = 3*base12 +1

        num12 = int(base12)

        if Max12 <= num12:
            Max12 = num12
        
        
           
    base14 = pow(14, m)-1
    Max14 = base14
    while base14 !=4:

        if base14 % 2 == 0:
            base14 = base14/2
        else:
            base14 = 3*base14 +1

        num14 = int(base14)


        if Max14 <= num14:
            Max14 = num14
             
        


    base18 = pow(18, m)-1
    Max18 = base18
    while base18 !=4:

        if base18 % 2 == 0:
            base18 = base18/2
        else:
            base18 = 3*base18 +1

        num18 = int(base18)


        if Max18 <= num18:
            Max18 = num18
             
        

        

    base2 = pow(2, m)-1
    base3 = pow(3, m)-1
    base5 = pow(5, m)-1
    base6 = pow(6, m)-1
    base7 = pow(7, m)-1
    base10 = pow(10, m)-1
    base12 = pow(12, m)-1
    base14 = pow(14,m)-1
    base18 = pow(18,m)-1


    diff2 = Max2 - base2
    ratio2 = diff2 / base2
    ratio2 = round(ratio2, 2)

    diff3 = Max3 - base3
    ratio3 = diff3 / base3
    ratio3 = round(ratio3, 2)

    diff5 = Max5 - base5
    ratio5 = diff5 / base5
    ratio5 = round(ratio5, 2)

    diff6 = Max6 - base6
    ratio6 = diff6 / base6
    ratio6 = round(ratio6, 2)

    diff7 = Max7 - base7
    ratio7 = diff7 / base7
    ratio7 = round(ratio7, 2)

    
    diff10 = Max10 - base10
    ratio10 = diff10 / base10
    ratio10 = round(ratio10, 2)

    diff12 = Max12 - base12
    ratio12 = diff12 / base12
    ratio12 = round(ratio12, 2)

        
    diff14 = Max14 - base14
    ratio14 = diff14 / base14
    ratio14 = round(ratio14, 2)

    
    diff18 =  Max18 - base18
    ratio18 = diff18 / base18
    ratio18 = round(ratio18, 2)
    
    worksheet.write(m,0, m)
    worksheet.write(m, 1,base3)
    worksheet.write(m, 2,ratio3)
    worksheet.write(m, 3,base5)
    worksheet.write(m, 4,ratio5)
    worksheet.write(m, 5,base7)
    worksheet.write(m, 6,ratio7)
    worksheet.write(m, 7,base2)
    worksheet.write(m, 8,ratio2)
    worksheet.write(m, 9,base6)
    worksheet.write(m, 10,ratio6)
    worksheet.write(m, 11,base10)
    worksheet.write(m, 12,ratio10)
    worksheet.write(m, 13,base12)
    worksheet.write(m, 14,ratio12)
    worksheet.write(m, 15,base14)
    worksheet.write(m, 16,ratio14)
    worksheet.write(m, 17,base18)
    worksheet.write(m, 18,ratio18)
    

    ## print("FOR m =" , m)
    m += 1

    """print()
    print("FOR ODD NUMBERS base = 3,5,7")
    ## print( base3, "=", Max3 ," | " , base5,"=", Max5 , " | " ,  base7, "=",Max7, )
    print("Difference: ", base3 , "=", diff3, "|", base5 , "=", diff5, "|", base7 , "=", diff7, "|")
    print("Ratio: ", base3 , "=", ratio3, "|", base5 , "=", ratio5, "|", base7 , "=", ratio7, "|")
        
    print()
    print("FOR EVEN NUMBER base = 2,6,10,12,14,18")
    ## print(base2, "=", Max2, "|" ,base6, "=", Max6 ,"|" ,base10,"=", Max10, " | " , base12, "=",Max12 , "|", base14 , "=", Max14 ,"|", base18 ,"=", Max18)
    print()
    print("Difference: ", base2 , "=", diff2, "|", base6 , "=", diff6, "|", base10 , "=", diff10, "|",base12 , "=", diff12, "|",base14 , "=", diff14, "|",base18 , "=", diff18, "|")
    print("Ratio:" , base2 , "=", ratio2, "|", base6 , "=", ratio6, "|", base10 , "=", ratio10  , "|",base12 , "=", ratio12, "|",base14 , "=", ratio14, "|",base18 , "=", ratio18, "|")
    print() """


    
workbook.close()