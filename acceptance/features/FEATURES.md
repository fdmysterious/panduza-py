# API Specifications

This documentation describes Panduza Features.

## First definitions

Panduza is based on MQTT, in this protocol there is the MQTT brokers and the MQTT clients.

Todo: image here

The Panduza clients and drivers are both MQTT clients and communicate through the MQTT brokers.

- Panduza **driver** expose interface control part of the API. It is connected to the interface and wait for clients to send commands.
- Panduza **client** is the interface user part of the API. The user can send command and monitor answers from the client.

Todo: image here

When multiple drivers are gathered into a common package it is called a **class**.
For example the class PSU can gather driver to manage different types of power supplies.

## Panduza MQTT topic levels

Panduza levels are defined as follow

INTERFACE_PREFIX is the identifier of the interface on the MQTT Broker.

```
INTERFACE_PREFIX: pza/[machine]/[group]/[interface]
```

- **pza**       : to tag all the topics matching the Panduza specification
- **machine**   : defines the host on which the interface is located. It should be the name of the physical device that support the interface.
- **group**     : defines the name of the group that support this interface. By default it is the name of the driver running the interface.
- **interface** : defines the interface name.

```
{INTERFACE_PREFIX}/[specifier]/[property]/[action]
```

- **specifier** : [atts|cmds|info]
- **property**  : defines the specific element of the interface to monitor.
- **action**    : if specifier is cmds, action to perform

Specificers definitions

- **atts**
- **cmds**
- **info**


## Symmetrical & Asymmetric Properties

<!--
Work here on general concept behind cmds and atts




Some attributes are defined as Symmetrical

The Specificers

| Topic                                   | QOS   | Retain   |
| :-------------------------------------- | :---: | :------: |
| {INTERFACE_PREFIX}/cmds/state/set       | 0     | false    |
| {INTERFACE_PREFIX}/atts/state           | 0     | true     |
-->


## Test Scenarios

The test scenarios are designed using the fake drivers. The goal of those scenarios is to cover 100% of the client en platform sources.
