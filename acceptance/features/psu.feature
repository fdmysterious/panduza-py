Feature: API_PSU

    Panduza provides a way to control power supplies

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_PSU must be comptabile with the discovery process

        # @fixture.client.test
        Scenario: Check scan information
            Given core aliases loaded with file "io_alias.json"
            # Given a client "test" initialized with the mqtt test broker alias:"local_test"
            # When  the client "test" start the connection
            # And   the client "test" scan the interfaces
            # Then  interface "pza/test/psu_fake/Pikachu" contains information type == "psu" and version == "1.0"

    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # Rule: API_PSU must be able to manage the state of the power supply

    #     The power supply state management is done through 2 symmetrical topics.

    #     @fixture.interface.psu.test
    #     Scenario: Try to change and read back the state
    #         Given core aliases loaded with file "psu_alias.json"
    #         And   psu interface "test" initialized with alias "Pikachu"
    #         When  psu interface "test" change power supply state to "on"
    #         Then  psu interface "test" state is "on"
    #         When  psu interface "test" change power supply state to "off"
    #         Then  psu interface "test" state is "off"

    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # Rule: API_PSU must be able to manage the amps value of the power supply

    #     The power supply amps management is done through 2 topics that have asymmetric payloads.


    #     @fixture.interface.psu.test
    #     Scenario: Try to change and read back the amps
    #         Given core aliases loaded with file "psu_alias.json"
    #         And   psu interface "test" initialized with alias "Pikachu"
    #         When  psu interface "test" change power supply amps value to "8"
    #         Then  psu interface "test" amps value is "8"
    #         When  psu interface "test" change power supply amps value to "2"
    #         Then  psu interface "test" amps value is "2"

    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # Rule: API_PSU must be able to monitor the amps parameters of the power supply



    #     @fixture.interface.psu.test
    #     Scenario: Try to read amps parameters
    #         Given core aliases loaded with file "psu_alias.json"
    #         And   psu interface "test" initialized with alias "Pikachu"
    #         Then  psu interface "test" amps min is "0"
    #         And   psu interface "test" amps max is "50"
    #         And   psu interface "test" amps scale is "0.01"


    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # Rule: API_PSU must be able to manage the volts value of the power supply

    #     The power supply volts management is done through 2 topics that have asymmetric payloads.


    #     @fixture.interface.psu.test
    #     Scenario: Try to change and read back the volts
    #         Given core aliases loaded with file "psu_alias.json"
    #         And   psu interface "test" initialized with alias "Pikachu"
    #         When  psu interface "test" change power supply volts value to "8"
    #         Then  psu interface "test" volts value is "8"
    #         When  psu interface "test" change power supply volts value to "2"
    #         Then  psu interface "test" volts value is "2"

    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # Rule: API_PSU must be able to monitor the volts parameters of the power supply

  
    #     @fixture.interface.psu.test
    #     Scenario: Try to read volts parameters
    #         Given core aliases loaded with file "psu_alias.json"
    #         And   psu interface "test" initialized with alias "Pikachu"
    #         Then  psu interface "test" volts min is "0"
    #         And   psu interface "test" volts max is "50"
    #         And   psu interface "test" volts scale is "0.01"


    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # Rule: API_PSU must be able to control and monitor extra settings

    #     Power supplies often have specifics functions. Those functions depends on hardware capacity and are not standart.
    #     The extras property provides a way to cover those functions.

    #     | Topic                                    | QOS   | Retain   |
    #     | :--------------------------------------- | :---: | :------: |
    #     | {INTERFACE_PREFIX}/cmds/extras/set       | 0     | false    |
    #     | {INTERFACE_PREFIX}/atts/extras           | 0     | true     |

    #     ```json
    #         {
    #             "ovp": true
    #         }
    #     ```



