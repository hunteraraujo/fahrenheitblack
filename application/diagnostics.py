from typing import List
from entities.alert import Alert
from entities.activity import Activity
from entities.confirmation import Confirmation

# ? Owner: TradingSystem
# TODO: Implement this class
class Diagnostics:
    def __init__(self, alerts: List[Alert]):
        self.alerts = alerts

    def send_alert(self, alert: Alert) -> Confirmation:
        # Code to send real-time alerts via SMS or email
        pass

    def log_activity(self, activity: Activity):
        # Code to log system activities and performance
        pass