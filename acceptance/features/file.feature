@action.platform_start.file_tree.json
Feature: API_FILE

    Panduza provides a way to transfert small files

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_FILE must be comptabile with the discovery process

        Discovery requests are sent by the client on the topic *pza*.

        The driver must respond on its own topic {INTERFACE_PREFIX}/info.

        The payload exposed by the interface
        ```json
            {
                "type": "file", 
                "version": "1.0"
            }
        ```

        @fixture.client.test
        Scenario: Check scan information
            Given core aliases loaded with file "file_alias.json"
            Given a client "test" initialized with the mqtt test broker alias:"local_test"
            When  the client "test" start the connection
            And   the client "test" scan the interfaces
            Then  interface "pza/test/file_fake/file_test" contains information type == "file" and version == "1.0"

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_FILE must be able to transfert the file content

        2 topics are defined to this purpose:

        | Topic                                 | QOS | Retain |
        |:--------------------------------------|:---:|:------:|
        | {INTERFACE_PREFIX}/atts/content       | 0   | true   |
        | {INTERFACE_PREFIX}/cmds/content/set   | 0   | false  |

        The payload of those topics must be a json payload:

        | Key       | Type          | Description                                   |
        |:-------- :|:-------------:|:---------------------------------------------:|
        | data      | string        | Content of the file encoding in base64        |
        | mime      | string        | A mime type https://mimetype.io/all-types/    |

        ```json
            {
                "data": "SKGKFGD ... JGBEIGDFGPD"
                "mime": "text/plain"
            }
        ```

        @fixture.interface.file.test
        Scenario Outline: Transfert simple file
            Given core aliases loaded with file "file_alias.json"
            And   file interface "test" initialized with alias "file_test"
            When  file interface "test" is set with content from file "<rsc_file>"
            Then  atts/content data of the file interface "test" is filled with file "<rsc_file>" content encoded in base64
            And   atts/content mime of the file interface "test" is filled "<mime>"

        Examples:
            | rsc_file          | mime          |
            | file/2bytes.txt   | text/plain    |

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    Rule: API_FILE must provide a way to manage errors

        It is the client responsability to timeout if the interface does not respond.

        @fixture.interface.file.test
        Scenario: Test that the client timeout when the interface does not exist
            Given core aliases loaded with file "file_alias.json"
            And   file interface "test" initialized with alias "not_exist"
            When  file interface "test" is set with content from file "file/2bytes.txt"
            Then  an ensure exception must have occured

