# @action.platform_start.psu_tree.json
Feature: API_LACE

    Panduza provides a way to perform Linux Arbitrary Command Execution.

    API_LACE does not manage stdin, it is not the purpose of this interface.

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_LACE must be comptabile with the discovery process

        Discovery requests are sent by the client on the topic *pza*.

        The driver must respond on its own topic {INTERFACE_PREFIX}/info.

        The payload exposed by the interface
        ```json
        {
            "type": "lace",
            "version": "1.0"
        }
        ```

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_LACE must be able to

        2 topics are defined to this purpose:

        | Suffix                                  | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        
        | {INTERFACE_PREFIX}/atts/queue           | 0     | true     |
        
        | {INTERFACE_PREFIX}/cmds/queue/push      | 0     | false    |
        | {INTERFACE_PREFIX}/cmds/queue/reset     | 0     | false    |

        | {INTERFACE_PREFIX}/atts/status          | 0     | true     |
        | {INTERFACE_PREFIX}/atts/stdout          | 0     | true     |
        | {INTERFACE_PREFIX}/atts/stderr          | 0     | true     |



