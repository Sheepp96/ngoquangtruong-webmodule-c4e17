from models.service import Service
import mlab

mlab.connect()

delete_service = Service.objects()

if delete_service is not None:
    delete_service.delete()
else:
    print("Service not found")
