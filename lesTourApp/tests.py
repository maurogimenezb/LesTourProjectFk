from django.test import TestCase
from .models import Ciudades, Hoteles, Areas, Cargo, Empleados, Clientes, Tipo_Habitacion, Habitacion, Reservas, Reserva_Huesped

class ModelTests(TestCase):
    def setUp(self):
        ciudad = Ciudades.objects.create(nombre='Asuncion')
        area = Areas.objects.create(nombre='Recepción')
        cargo = Cargo.objects.create(nombre='Recepcionista', id_area=area)
        hotel = Hoteles.objects.create(
            nombre='Hotel iturbe',
            ciudad=ciudad,
            barrio='san juan',
            direccion='iturbe',
            telefono=123456789,
            email='hola@hotel.com',
            pisos=3,
            habitaciones=50
        )
        empleado = Empleados.objects.create(
            ci_numero=1234567,
            nombre='Juan Gonzalez',
            email='juan@hotel.com',
            direccion='villarrica',
            ciudad=ciudad,
            telefono=987654321,
            cargo=cargo,
            hotel=hotel
        )
        cliente = Clientes.objects.create(
            ci_numero=9876543,
            nombre='Mauro Gimenez',
            email='mauro@hola.com',
            direccion='Iturbe',
            telefono=555666777
        )
        tipo_habitacion = Tipo_Habitacion.objects.create(
            nombre='Suite',
            capacidad=2,
            costo=150
        )
        habitacion = Habitacion.objects.create(
            numero=101,
            piso=1,
            id_tipo_habitacion=tipo_habitacion,
            id_hotel=hotel
        )
        reserva = Reservas.objects.create(
            id_cliente=cliente,
            fecha_entrada='2023-11-10 12:00:00',
            fecha_salida='2023-11-12 12:00:00',
            precio=200,
            numero_personas=2,
            estado='Activa',
            id_habitacion=habitacion
        )
        Reserva_Huesped.objects.create(
            id_cliente=cliente,
            id_reserva=reserva
        )

    def test_hoteles_model(self):
        hotel = Hoteles.objects.get(nombre='Hotel Iturbe')

        self.assertEqual(hotel.ciudad.nombre, 'Asuncion')
        self.assertEqual(hotel.barrio, 'San Juan')
        self.assertEqual(hotel.direccion, 'Iturbe')
        self.assertEqual(hotel.telefono, 123456789)
        self.assertEqual(hotel.email, 'iturbe@hotel.com')
        self.assertEqual(hotel.pisos, 3)
        self.assertEqual(hotel.habitaciones, 50)

