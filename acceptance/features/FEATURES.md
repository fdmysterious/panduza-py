# API Specifications

This documentation describes Panduza Features.

## First definitions

Panduza is based on MQTT, in this protocol there is the MQTT brokers and the MQTT clients.

Todo: image here

The Panduza clients and drivers are both MQTT clients and communicate through the MQTT brokers.

- Panduza **driver** expose interface control part of the API. It is connected to the interface and wait for clients to send commands.
- Panduza **client** is the interface user part of the API. The user can send command and monitor answers from the client.

Todo: image here

When multiple driver are gathered into a common package it is called a **class**. For example the class psu can gather driver to manage different types of power supply 


## Panduza MQTT levels

Panduza levels are defined as follow

```
INTERFACE_PREFIX: pza/[machine]/[group]/[interface]
```

- **pza**       : to tag all the topics matching the Panduza specification
- **machine**   : defines the host on which the interface is located. It should be the name of the physical device that support the interface.
- **group**     : defines the name of the group that support this interface. By default it is the name of the driver running the interface.
- **interface** : defines the interface name.

```
{INTERFACE_PREFIX}/[specifier]/[attribut]
```

- **specifier** : [atts|cmds|info]
- **attribut**  : defines the specific element of the interface to monitor.





