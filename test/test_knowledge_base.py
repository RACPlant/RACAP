import unittest
from os import path
from database.knowledge_base import KnowledgeBase, DB_PATH
from unittest import mock
from freezegun import freeze_time


class TestKnowledgeBase(unittest.TestCase):

    @mock.patch('database.knowledge_base.Sensor')
    def test_add_metric_fact_should_create_one_Sensor(self, mock_sensor):
        kb = KnowledgeBase()
        sensor_instance = mock_sensor.return_value
        kb.add_metric_fact("a1", "s1", 10)
        kb.add_metric_fact("a1", "s1", 10)

        mock_sensor.assert_called_once_with("a1", "s1")
        assert sensor_instance.value == 10

    @mock.patch('database.knowledge_base.Sensor')
    def test_add_metric_fact_should_create_more_than_one_Sensor(self, mock_sensor):
        kb = KnowledgeBase()
        s1 = mock.Mock()
        s2 = mock.Mock()

        mock_sensor.side_effect = [s1, s2]
        kb.add_metric_fact("a1", "s1", 10)
        kb.add_metric_fact("a1", "s2", 20)

        mock_sensor.assert_has_calls(
            [mock.call("a1", "s1"), mock.call("a1", "s2")])

        assert s1.value == 10
        assert s2.value == 20

    @freeze_time("2012-01-14")
    @mock.patch('database.knowledge_base.Sensor')
    def test_update_metrics_file(self, mock_sensor):
        kb = KnowledgeBase()
        s1 = mock.Mock()

        mock_sensor.return_value = s1

        s1.get_fact.return_value = "sensor(a1,s1,1,1,1,1)."

        kb.add_metric_fact("a1", "s1", 1)

        with mock.patch("builtins.open", mock.mock_open()) as mock_file:

            kb.update_metrics_file()

            mock_file.assert_called_once_with(path.join(DB_PATH, "metrics.pl"), "+w")

            mock_file().write.assert_called_with(
                "sensor(a1,s1,1,1,1,1).\n%% log processed at 2012-01-14 00:00:00")
