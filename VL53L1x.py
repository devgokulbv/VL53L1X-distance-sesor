# from PiicoDev_VL53L1X import PiicoDev_VL53L1X
# from time import sleep
# 
# 
# distSensor = PiicoDev_VL53L1X(freq=0.1)
# #regId=distSensor.read_model_id()
# #distSensor.SetIntermeasurementInMs(1000)
# #distSensor.writeReg(regId,1)
# while True:
#     dist = distSensor.read()
#     print(str(dist)+" mm")
#     sleep(0.1)
#----------

#----------------------
# import qwiic
# import time
#  
# print("VL53L1X Qwiic Test\n")

# 
# ToF.set_timing_budget_in_ms(40)
# ToF.set_signal_threshold(10)
# print("time:",ToF.get_inter_measurement_in_ms())
# ToF.set_inter_measurement_in_ms(100)
# print("time:",ToF.get_inter_measurement_in_ms())
# print("xy:",ToF.get_roi_xy())
# ToF.set_roi(4,4)
# print("xy:",ToF.get_roi_xy())
# print("Inter Measurement Period (ms): %s \n", ToF.get_inter_measurement_in_ms())
# while True:
#     try:
#         ToF.start_ranging() # Write configuration bytes to initiate measurement
#         time.sleep(.005)
#         distance = ToF.get_distance() # Get the result of the measurement from the sensor
#         time.sleep(.005)
#         ToF.stop_ranging()
#         distanceInches = distance / 25.4
#         distanceFeet = distanceInches / 12.0
#         print("Distance(mm):", distance)
#  
#     except Exception as e:
#         print(e)
#         
#----------------
import qwiic_vl53l1x
import time
import datetime
import statistics as sts
import sys
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,GPIO.HIGH)
time.sleep(1)
def run():
    arr=[]
    
    mySensor = qwiic_vl53l1x.QwiicVL53L1X()
    # = Qwiic.QwiicVL53L1X()
    

    mySensor.sensor_init()
    mySensor.set_inter_measurement_in_ms(500)
    mySensor.set_timing_budget_in_ms(500)
    mySensor.set_roi(4,4)
    mySensor.set_distance_mode(2)

    print("time",mySensor.get_timing_budget_in_ms())
    print("inter_measurement",mySensor.get_inter_measurement_in_ms())
    i=1
    while i<11:
        try:
            mySensor.clear_interrupt()
            ty=time.time()
            time.sleep(0.5)
            mySensor.start_ranging()  # Write configuration bytes to initiate measurement
            #time.sleep(0.5)
            distance = mySensor.get_distance()  # Get the result of the measurement from the sensor
            #time.sleep(0.143)
            mySensor.stop_ranging()
            
            td=time.time()
            #print(distance,td-ty)
            if i>2:
                print(distance,td-ty)
                arr.append(distance)
        except Exception as e:
            print(e)
            
        #if len(arr)<32:
        #    avgdist=sts.mean(arr)
        #else:
          #  arr.remove(arr[0])
         #   sts.mean(arr[len(arr)-32:len(arr)+1])
        #print("Distance(mm):",distance,"avgsitance",avgdist)
        i+=1
    return arr

arr=run()
# print(arr)
print("acutal distance+/-5mm: ",sts.mean(arr))
print("range:",min(arr),",",max(arr))
GPIO.output(13,GPIO.LOW)
