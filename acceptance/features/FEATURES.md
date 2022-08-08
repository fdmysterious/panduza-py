# API Specifications

This documentation describes Panduza Features.

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

