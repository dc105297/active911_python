Active911 Python Bindings
========================

## Install

**via pip**

pip install active911-python

**Manual Installation**

download release and install by:

**python setup.py install**

## Setup / Initialize

**Import Package**

**from** active911_python **import** active911

**Initialize class**

client = active_911.active911Client(access_token='Enter Access Token Here')

**Environment Variable Support**

If access_token is not passed you can set **ACTIVE911_ACCESS_TOKEN** as the environment variable.

## Available Methods:

**get_agency()**

This function will return the authorized agency and is considered the root of the API.

**get_device_info(device_id=None)**

This function will return detailed device information.

**get_device_alerts(device_id=None, alert_days=None, alert_minutes=None)**

This function will return agency alerts by device.
Number of alerts can be set by alert_days(default:10 Max:30) or alert_minutes, alert_minutes supersedes alert_days if set.

**get_alerts(alert_days=None, alert_minutes=None)**

Returns agency alerts.
Number of alerts can be set by alert_days(default:10 Max:30) or alert_minutes, alert_minutes supersedes alert_days if set.

**get_alert_detail(alert_id=None)**

Returns alert detail by alert_id.

**get_locations(locations_page=None, locations_per_page=None)**

Returns all map data locations.

**get_location_detail(location_id)**

Returns location point detail

**get_resource_detail**

Returns location point resource detail

## TODOS:

* Add POST request support for mapping locations.
* Support locations_coordinate_window
