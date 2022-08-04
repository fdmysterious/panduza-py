@action.platform_start.psu_tree.json
Feature: API_PSU

    Panduza provides a way to control power supplies


    Rule: API_PSU must be comptabile with the discovery process

        Discovery requests are sent by the client on the topic *pza*.

        To respond to those requests the driver must respond on {INTERFACE_PREFIX}/info

        ```json
            {
                "type": "psu", 
                "version": "1.0"
            }
        ```
     





