def sumNumber():
    pass

# สร้าง Class ใน python ค่าคงที่ใช้ตัวใหญ่หมด ส่วนชื่อ class ต้องขึ้นต้นด้วยตัวใหญ่
class IoTSAU :
    # data/attribute/filed/property member เหมือนตัวแปร
    info1 = 20
    info2 = ''

    # method member เหมือนฟังก์ชัน
    def showHi(self):
        print('Hi...')

    def showInfo(self):
        print(self.info1, self.info1)
        self.showHi()

# สร้าง Object
obA = IoTSAU()
obB = IoTSAU()
obC = IoTSAU()

obA.info1 = 100
print(obA.info1 + obB.info1) #120
obC.showInfo()
obA.showInfo()