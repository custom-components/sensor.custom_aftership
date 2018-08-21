"""
A component which allows you to get information about pending parcels.

For more details about this component, please refer to the documentation at
https://github.com/HalfDecent/HA-Custom_components/ruter
"""
import logging
import voluptuous as vol
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)

__version__ = '0.1.0'

REQUIREMENTS = ['pyaftership==0.0.1']

CONF_API_KEY = 'api_key'
CONF_NAME = 'name'

DATA = 'aftership_data'


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_NAME, default='AfterShip'): cv.string,
})

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the sensor platform"""
    api_key = config.get(CONF_API_KEY)
    name = config.get(CONF_NAME)
    add_devices([AftershipSensor(hass, api_key, name)])

class AftershipSensor(Entity):
    """The sensor class"""
    def __init__(self, hass, api_key, name):
        from pyaftership import AfterShip
        self._aftership = AfterShip()
        self.hass = hass
        self._name = name
        self._api_key = api_key
        self._state = 0
        self.hass.data[DATA] = {}
        self.update()


    def update(self):
        """Update the sensor"""
        base_link = 'https://track.aftership.com/'
        result = self._aftership.get_trackings(self._api_key)
        if not result['sucess']:
            return False
        else:
            self.hass.data[DATA] = {}
            data = result['data']
            self._state = data['count']
            for parcel in data['trackings']:
                parcel_data = {}
                if not parcel['title']:
                    title = parcel['tracking_number']
                else:
                    title = parcel['title']
                parcel_data['title'] = title
                if parcel['tag'] == 'InTransit':
                    parcel_data['status'] = 'In transit'
                else:
                    parcel_data['status'] = parcel['tag']
                parcel_data['slug'] = parcel['slug']
                parcel_data['last_update'] = parcel['updated_at']
                parcel_data['tracking_number'] = [parcel['tracking_number']
                parcel_data['link'] = base_link + parcel['slug'] + '/' + [parcel['tracking_number']
                self.hass.data[DATA][parcel['tracking_number']] = parcel_data

    @property
    def name(self):
        """Return the name of the sensor"""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor"""
        return 'mdi:package'

    @property
    def device_state_attributes(self):
        """Return the attributes of the sensor"""
        return self.hass.data[DATA]
