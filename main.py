import time
import hcsr04
ultrasonic = hcsr04.HCSR04(trigger_pin=6, echo_pin=7, echo_timeout_us=1000000)
from machine import Pin,PWM
from lcd import*

if __name__=='__main__':
   
    LCD = LCD_init()
    store = 0 
    while(1):
        LCD.fill(LCD.white)
        time.sleep(0.1)

        distance = ultrasonic.distance_mm()
        if (distance > 200 ):
            distance = 200
        if (store < 0 ):
            store = 0    
        print(store)
       
        if (distance == store ):
           LCD.fill(LCD.green)
           LCD.fill_rect(110,35,40,40,LCD.green)
        else :
           LCD.fill_rect(110,35,40,40,LCD.red)

        LCD.text( str(distance),120,50,LCD.white)
       
        if(keyA.value() == 0):
            store = distance
            LCD.fill_rect(208,12,20,20,LCD.red)
        else :
            LCD.fill_rect(208,12,20,20,LCD.white)
            LCD.rect(208,12,20,20,LCD.red)
            #saved value 
            LCD.fill_rect(110,40+35,40,40,LCD.green)
            LCD.text( str(store),120,40+50,LCD.white)
                 
        if(keyB.value() == 0):
            LCD.fill_rect(208,103,20,20,LCD.red)
            store = 0 
        else :
            LCD.fill_rect(208,103,20,20,LCD.white)
            LCD.rect(208,103,20,20,LCD.red)
    
        if(key2.value() == 0):#up
            LCD.fill_rect(37,35,20,20,LCD.red)
            time.sleep(0.2)
            store = store + 1 
        else :
            LCD.fill_rect(37,35,20,20,LCD.white)
            LCD.rect(37,35,20,20,LCD.red)
            
        if(key3.value() == 0):#middle
            LCD.fill_rect(37,60,20,20,LCD.red)
        else :
            LCD.fill_rect(37,60,20,20,LCD.white)
            LCD.rect(37,60,20,20,LCD.red)

        if(key4.value() == 0):#left
            LCD.fill_rect(12,60,20,20,LCD.red)
        else :
            LCD.fill_rect(12,60,20,20,LCD.white)
            LCD.rect(12,60,20,20,LCD.red)
              
        if(key5.value() == 0):#down
            LCD.fill_rect(37,85,20,20,LCD.red)
            time.sleep(0.2)
            store = store - 1
           

        else :
            LCD.fill_rect(37,85,20,20,LCD.white)
            LCD.rect(37,85,20,20,LCD.red)
            
        if(key6.value() == 0):#right
            LCD.fill_rect(62,60,20,20,LCD.red)
        else :
            LCD.fill_rect(62,60,20,20,LCD.white)
            LCD.rect(62,60,20,20,LCD.red)

        #rfresh  
        LCD.show()
    time.sleep(1)
    LCD.fill(0xFFFF)





