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
    Rule: API_LACE must manage a queue of commands to execute

        API_LACE interface can execute only one command at a time.

        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/queue/push      | 0     | false    |
        | {INTERFACE_PREFIX}/atts/queue           | 0     | true     |
        | {INTERFACE_PREFIX}/atts/cmd/status      | 0     | true     |

        The client can push a command with the topic **cmds/queue/push**.

        The payload is composed of the command string and its environnement parameters

        | Key         | Type     | Description                         |
        | :-------- : | :------: | :---------------------------------: |
        | command     | string   | Command to exectue                  |
        | workdir     | string   | Path to working dir                 |
        | env         | dict     | Dict of env variables               |

        ```json
        {
            "command": "ls -la",
            "workdir": "/path/to/workdir",
            "env": {
                "key": "value",
                "key": "value",
                "key": "value"
            }
        }
        ```

        Each command will be queued by the driver.
        The client can see the current content of the queue on **atts/queue**.

        ```json
        {
            "commands": [ { "command": ... }, ... ],
        }
        ```





        | Topic                                   | QOS   | Retain   |
        | :-------------------------------------- | :---: | :------: |
        | {INTERFACE_PREFIX}/cmds/queue/reset     | 0     | false    |
        | {INTERFACE_PREFIX}/atts/cmd/stdout      | 0     | true     |
        | {INTERFACE_PREFIX}/atts/cmd/stderr      | 0     | true     |



