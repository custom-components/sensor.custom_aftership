# sensor.custom_aftership [![Build Status](https://travis-ci.com/custom-components/sensor.aftership.svg?branch=master)](https://travis-ci.com/custom-components/sensor.aftership)

A platform which allows you to get information about pending parcels.
  
To get started put `/custom_components/sensor/custom_aftership.py` here:  
`<config directory>/custom_components/sensor/custom_aftership.py`  
  
**Example configuration.yaml:**

```yaml
sensor:
  platform: custom_aftership
  api_key: '9781915b342514bf0dede6e3d058a'
```

**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The platform name.  
**api_key (Required)** | Your Aftership API key.

**Serice Calls:**

`sensor.aftership_new_tracking`

Example JSON data format. **All fields are required**

```json
{
  "title":"HA Shirt",
  "slug":"usps",
  "tracking_number":"123456789"
}
```

***

[There is an official platform for Aftership in Home Assistant](https://www.home-assistant.io/components/sensor.aftership/)

***

Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.