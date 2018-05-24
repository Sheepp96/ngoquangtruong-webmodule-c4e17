from models.service import Service
import mlab

mlab.connect()

id_to_find = "5afad2cc533daa1c1c72b592"

# hera = Service.objects(id = id_to_find) #nó ra 1 list
# hera = Service.objects.get(id = id_to_find)

berry = Service.objects.with_id(id_to_find) #nên dùng cái này

if berry is not None:
    # berry.delete()
    print(berry.address,",", berry.height)
    berry.update(set__address = "Nguyễn Khánh Toàn",
                 set__height = 420)

    berry.reload()
    print(berry.address,",", berry.height)
    # print("Deleted")

else:
    print("Service not found")
# print(berry.to_mongo()) #lấy tất cả các phần tử của nó


# all_service = Service.objects(gender = 1) #lấy ra tất cả các objects của class Service
#
# # firt_service = all_service[0]
# # print(firt_service['name'])
#
# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index == 9:
#         break
