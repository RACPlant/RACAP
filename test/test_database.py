from database import DatabaseMetric, DatabasePlant, DatabaseArduino
from controller.plants import Plants
from social.arduino import Devices
import unittest
from unittest import mock


class DatabaseArduinoTestCase(unittest.TestCase):

    @mock.patch("social.arduino.requests")
    def test_add_arduino_factr(self, mock_request):
        api_response_mock = [
            {
                "id": "arduino_1",
                "port": "/dev/ttyACM0",
                "radiation": "r",
                "temperature": "t"
            }
        ]

        mock_response = mock.Mock()
        mock_response.json.return_value = api_response_mock
        mock_request.get.return_value = mock_response

        db_arduino = DatabaseArduino()
        db_arduino.add_arduino_fact(Devices("test_url"))
        facts = db_arduino._get_facts()
        expected_facts = [
            'is_radiation(arduino_1,r).',
            'is_temperature(arduino_1,t).'
        ]
        mock_request.get.assert_called_once_with("test_url")
        self.assertListEqual(expected_facts, facts)

    def test_add_metric_fact_without_atenuator(self):
        db_metrics = DatabaseMetric()
        for i in range(20):
            db_metrics.add_metric_fact("a1", "t", 10)
            db_metrics.add_metric_fact("a1", "r", 10)
            db_metrics.add_metric_fact("a2", "t", 10)

        expected_facts = [
            "sensor(a1,r,10.0,10.0,10.0,10.0).",
            "sensor(a1,t,10.0,10.0,10.0,10.0).",
            "sensor(a2,t,10.0,10.0,10.0,10.0)."
        ]

        self.assertListEqual(expected_facts, db_metrics._get_facts())


class DatabasePlantTestCase(unittest.TestCase):

    def test_add_plant_fact_without_ETo_data(self):
        slots = {
            "0": {
                "botanical_name": "botanical_name_does_not_exist",
                "humidity": "h1",
                "pump": "p1"
            }
        }
        slots = mock.Mock(arduino_id="a1", all=slots)
        plants = Plants(slots)
        plants.set_info()
        db_plants = DatabasePlant()

        db_plants.add_plants_fact("a1", plants)

        facts = db_plants._get_facts()

        expected_facts = [
            "plant(a1,0,botanical_name_does_not_exist).",
            "slot(a1,0,h1,p1)."
        ]

        self.assertListEqual(expected_facts, facts)

    def test_add_plant_fact_with_ETo_data(self):
        slots = {
            "0": {
                "botanical_name": "Abies pinsapo",
                "humidity": "h1",
                "pump": "p1"
            }
        }
        slots = mock.Mock(arduino_id="a1", all=slots)
        plants = Plants(slots)
        plants.set_info()
        db_plants = DatabasePlant()

        db_plants.add_plants_fact("a1", plants)

        facts = db_plants._get_facts()
        expected_facts = [
            "eto_water(abies_pinsapo,1,0,2).",
            "eto_water(abies_pinsapo,1,0,2).",
            "eto_water(abies_pinsapo,12,0,2).",
            "eto_water(abies_pinsapo,14,0,0).",
            "eto_water(abies_pinsapo,14,0,2).",
            "eto_water(abies_pinsapo,15,0,2).",
            "eto_water(abies_pinsapo,16,0,2).",
            "eto_water(abies_pinsapo,17,0,0).",
            "eto_water(abies_pinsapo,18,0,0).",
            "eto_water(abies_pinsapo,2,0,2).",
            "eto_water(abies_pinsapo,2,0,2).",
            "eto_water(abies_pinsapo,3,0,2).",
            "eto_water(abies_pinsapo,4,0,2).",
            "eto_water(abies_pinsapo,4,0,2).",
            "eto_water(abies_pinsapo,6,0,2).",
            "eto_water(abies_pinsapo,6,0,2).",
            "eto_water(abies_pinsapo,8,0,2).",
            "eto_water(abies_pinsapo,9,0,0).",
            "plant(a1,0,abies_pinsapo).",
            "slot(a1,0,h1,p1)."
        ]

        self.assertListEqual(expected_facts, facts)


class DatabaseMetricTestCase(unittest.TestCase):

    def test_add_metric_fact_with_atenuator(self):
        db_metrics = DatabaseMetric()
        db_metrics.add_metric_fact("a1", "t", 10)
        db_metrics.add_metric_fact("a1", "r", 10)
        db_metrics.add_metric_fact("a2", "t", 10)

        expected_facts = [
        ]

        self.assertListEqual(expected_facts, db_metrics._get_facts())

    def test_add_metric_fact_without_atenuator(self):
        db_metrics = DatabaseMetric()
        for i in range(20):
            db_metrics.add_metric_fact("a1", "t", 10)
            db_metrics.add_metric_fact("a1", "r", 10)
            db_metrics.add_metric_fact("a2", "t", 10)

        expected_facts = [
            "sensor(a1,r,10.0,10.0,10.0,10.0).",
            "sensor(a1,t,10.0,10.0,10.0,10.0).",
            "sensor(a2,t,10.0,10.0,10.0,10.0)."
        ]

        self.assertListEqual(expected_facts, db_metrics._get_facts())
