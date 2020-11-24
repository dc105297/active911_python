"""The active911 module is made to allow developers easily integrate the active911 api into their applications"""
import urllib3
import json
import datetime
import os

#Pool Manager for urllib3
http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED')

class Active911Client(object):
    """You can provide an active911 access token to the constructor or set a ACTIVE911_ACCESS_TOKEN enviroment variable."""
    BASE_URL = 'https://access.active911.com/interface/open_api/api/'

    def __init__(self, access_token=None):
        if not access_token:
            access_token = os.getenv('ACTIVE911_ACCESS_TOKEN')
        if not access_token:
            raise Exception("No access token has been passed or set.")

        self.access_token = access_token


    def get_agency(self):
        """This will return the authorized agency also this is the root of the api."""
        req = http.request('GET', self.BASE_URL, headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_device_info(self, device_id=None):
        """This will return detailed device information by passing device_id."""
        req = http.request('GET', self.BASE_URL + "devices/%s" %device_id , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_device_alerts(self, device_id=None, alert_days="", alert_minutes=""):
        """Returns agency alerts by device.
           Number of alerts can be set by alert_days(default:10 Max:30) or alert_minutes, alert_minutes supersedes alert_days if set.
        """
        req = http.request('GET', self.BASE_URL + "devices/%s/" %device_id + "alerts/" + "&alert_days=%s" %alert_days + "&alert_minutes=%s" %alert_minutes , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_alerts(self, alert_days="", alert_minutes=""):
        """Returns agency alerts.
           Number of alerts can be set by alert_days(default:10 Max:30) or alert_minutes, alert_minutes supersedes alert_days if set.
        """
        req = http.request('GET', self.BASE_URL + "alerts/" + "&alert_days=%s" %alert_days + "&alert_minutes=%s" %alert_minutes , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_alert_detail(self, alert_id=None):
        """Returns alert detail by alert_id"""
        req = http.request('GET', self.BASE_URL + "alerts/" + "%s" %alert_id , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_locations(self, locations_page=1, locations_per_page=10):
        """Returns all mapdata locations"""
        req = http.request('GET', self.BASE_URL + "locations/" + "&locations_page%s" %locations_page + "&locations_per_page%s" %locations_per_page , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_location_detail(self, location_id=None):
        """Returns all mapdata location detail"""
        req = http.request('GET', self.BASE_URL + "locations/" + "%s" %location_id , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response


    def get_resource_detail(self, resource_id=None):
        """Returns all mapdata location resource detail"""
        req = http.request('GET', self.BASE_URL + "resources/" + "%s" %resource_id , headers={"Authorization": "Bearer %s" %self.access_token})
        response = json.loads(req.data.decode('utf-8'))
        return response
