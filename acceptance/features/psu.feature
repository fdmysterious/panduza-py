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

        @fixture.client.test
        Scenario: Check scan information
            Given core aliases loaded with file "io_alias.json"
            Given a client "test" initialized with the mqtt test broker alias:"local_test"
            When  the client "test" start the connection
            And   the client "test" scan the interfaces
            Then  interface "pza/test/psu_fake/Pikachu" contains information type == "psu" and version == "1.0"

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_PSU must be able to control and monitor the state of the power supply

        The power supply state management is done through 2 topics.

        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/state/set       | 0     | false    |
        | {INTERFACE_PREFIX}/atts/state           | 0     | true     |

        ```json
            {
                "state": "off"
            }
        ```

        # When set off
        # Then it is off
        # When set on
        # Then is on

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_PSU must be able to control the amps of the power supply

        The power supply amps management is done through 2 topics that have asymmetric payloads.

        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/amps/set        | 0     | false    |

        | Key       | Type   | Description                           |
        |:-------- :|:------:|:-------------------------------------:|
        | amps      | number | amps value to set on the power supply |

        ```json
            {
                "amps": 5
            }
        ```

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_PSU must be able to monitor the amps parameters of the power supply

        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/atts/amps            | 0     | true     |


        The driver provides more information from the power supply that depend of the driven hardware.
        atts/amps

        ```json
            {
                "min":  0,
                "max": 50,
                "scale": 0.01
            }
        ```


    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_PSU must be able to control and monitor the voltage of the power supply


        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/volts/set       | 0     | false    |
        | {INTERFACE_PREFIX}/atts/volts           | 0     | true     |

        ```json
            {
                "volts": 3.3
                "min":  0
                "max": 50,
                "scale": 0.01
            }
        ```





#        | Topic                                   | QOS   | Retain   |
#        | :-------------------------------------- | :---: | :------: |
#        | {INTERFACE_PREFIX}/cmds/settings/set    | 0     | false    |
#        | {INTERFACE_PREFIX}/atts/settings        | 0     | true     |



