


def topic_join(*sections):
    """join mqtt topic sections
    """
    topic=""
    for s in sections:
        if topic and not topic.endswith("/"):
            topic+="/"
        topic+=s
    return topic


