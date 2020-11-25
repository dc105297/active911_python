[![Downloads](https://pepy.tech/badge/active911-python)](https://pepy.tech/project/active911-python)

[![Build Status](https://travis-ci.com/dc105297/active911_python.svg?branch=master)](https://travis-ci.com/dc105297/active911_python)

Active911 Python Bindings
========================


## Install

**via pip**

`pip install active911-python`

**Manual Installation**

Download release and install by:

`python setup.py install`

## Setup / Initialize

**Import Package**

`import active_911`

**Initialize class**

`client = active_911.Active911Client(access_token='Enter Access Token' refresh_token = 'Enter Refresh Token')`

## Authentication


**Environment Variable Support**

If access_token is not passed you can set **ACTIVE911_ACCESS_TOKEN** as an environment variable.

If refresh_token is not passed you can set **ACTIVE911_REFRESH_TOKEN** as an environment variable.

#### Access Token Refresh Method:

`access_token_refresh()`

Adding the `access_token_refresh()` method before any other API call will automagically check if the access_token is expired, create a new access_token , and set it to the `ACTIVE911_ACCESS_TOKEN`Env.


## Available Methods:

`get_agency()`

This function will return the authorized agency and is considered the root of the API.

`get_device_info(device_id=None)`

This function will return detailed device information.

`get_device_alerts(device_id=None, alert_days=None, alert_minutes=None)`

This function will return agency alerts by device.
Number of alerts can be set by alert_days(default:10 Max:30) or alert_minutes, alert_minutes supersedes alert_days if set.

`get_alerts(alert_days=None, alert_minutes=None)`

Returns agency alerts.
Number of alerts can be set by alert_days(default:10 Max:30) or alert_minutes, alert_minutes supersedes alert_days if set.

`get_alert_detail(alert_id=None)`

Returns alert detail by alert_id.

`get_locations(locations_page=None, locations_per_page=None)`

Returns all map data locations.

`get_location_detail(location_id)`

Returns location point detail

`get_resource_detail(resource_id)`

Returns location point resource detail

## Important Notes:

Full OAUTH scope is required for proper functionality.

* read_agency	Allows read-only access to this agency's information (Name, Address etc).
* read_alert	Allows read-only access to all alerts in the agency.
* read_response	Allows read-only access to responses to all alerts in the agency.0
* read_device	Allows read-only access to all device information in the agency.
* read_mapdata	Allows read-only access to all locations and resources in the agency.
* write_mapdata	Allows creation of locations and resources for the agency.


## TODOS:

* Add POST request support for mapping locations.
* Support locations_coordinate_window
