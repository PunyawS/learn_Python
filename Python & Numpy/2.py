#การสร้าง Array 1 มิติ

import numpy as np #np ชื่อย่อไว้สำหรับเรียกใช้ numpy
'''
x=np.array(1) # Array 0 มิติ มีสมาชิก 1 ตัว
print(x)    #แสดงค่า Array
x=x.ndim    #ตรวจสอบว่า Array มีกี่มิติ
print(x)    #แสดงค่า มิติ Array
'''
x=np.array([1,2,3])
print(x)
x=x.ndim
print(x)