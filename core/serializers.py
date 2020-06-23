from django.contrib.auth.models import User, Group
from rest_framework import serializers
from clinical.models import Clinical
from company.models import Company
from driver.models import Driver
from student.models import Student
from schedule.models import Schedule
from service.models import Service, Itinerary
from sede.models import Sede
from transport.models import Transport
from trip.models import Travels, Route, Passenger, Planningpre
from vehicle.models import Vehicle

class SedeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sede
        fields = ('id','name','city','commune','address','latitude','length')
class ClinicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinical
        fields = ('id','name','encargado','address','latitude','length')
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','rut', 'email')
class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('id','first_name', 'last_name','rut','state','company_id')
class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','patent', 'brand','kind','state','state')        
class OtherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinical
        fields = ('day_cut','trip')
class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = ('id','student_id','student_rut','student_name','student_profession','destination','destination_id','state')
class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('travels_id','service_id','name_service','id_point','name_point','orden','kind','latitude','length')
class RouteSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('service_id','travels_id','name_service','id_point','name_point','orden','kind','latitude','length')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('date','departure','mon_trip','tue_trip','wed_trip','thu_trip','fri_trip','sat_trip','sun_trip','service_id')
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name','name_itinerary','type_service','departure','mon_trip','tue_trip','wed_trip','thu_trip','fri_trip','sat_trip','sun_trip','clinical_id')
class ServiceClinicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Itinerary
        fields = ('id','name','service_id','clinical_id')
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name', 'last_name','campus','profession','state','state_card')
class TransportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transport
        fields = ('id','date','vehicle_id','patent','service_id','travels_id','travel_name','company_id','kind','departure','state')
class TravelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Travels
        fields = ('id','name','type_trip','date','departure','arribal','state','clinical_id','sede_id','service_id')
class TravelsProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Travels
        fields = ('id','name','type_trip','date','departure','clinical_id','sede_id')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email',)
class PlanningpreSerializer(serializers.HyperlinkedModelSerializer):
    driver = DriverSerializer(read_only=True)
    driverId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Driver.objects.all(),source='driver')
    vehicle = VehicleSerializer(read_only=True)
    vehicleId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vehicle.objects.all(),source='vehicle')
    class Meta:
        model = Planningpre
        fields = ('id','state','kind','cost','capacity','travels_id','driver','driverId','vehicle','vehicleId')

class ItinerarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Itinerary
        fields = ('id','name','service_id','clinical_id')

'''
class PlanningpreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planningpre
        fields = ('id','state','kind','cost','capacity','travels_id')
'''