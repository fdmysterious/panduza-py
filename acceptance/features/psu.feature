@action.platform_start.psu_tree.json
Feature: API_PSU

    Panduza provides a way to control power supplies

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_PSU must be comptabile with the discovery process

        Discovery requests are sent by the client on the topic *pza*.

        The driver must respond on its own topic {INTERFACE_PREFIX}/info.

        The payload exposed by the interface
        ```json
            {
                "type": "psu",
                "version": "1.0"
            }
        ```



        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/state/set       | 0     | false    |
        | {INTERFACE_PREFIX}/atts/state           | 0     | true     |



        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/amps/set        | 0     | false    |
        | {INTERFACE_PREFIX}/atts/amps            | 0     | true     |


        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/volts/set       | 0     | false    |
        | {INTERFACE_PREFIX}/atts/volts           | 0     | true     |


        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/settings/set    | 0     | false    |
        | {INTERFACE_PREFIX}/atts/settings        | 0     | true     |



