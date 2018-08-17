# sensor.aftership

A platform which allows you to get information about pending parcels.
  
To get started put `/custom_components/sensor/aftership.py` here:  
`<config directory>/custom_components/sensor/aftership.py`  
  
**Example configuration.yaml:**

```yaml
sensor:
  platform: aftership
  api_key: '9781915b342514bf0dede6e3d058a'
```

**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The platform name.  
**api_key (Required)** | Your Aftership API key.

***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.