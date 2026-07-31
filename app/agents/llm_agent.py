def route_query(query):

    if "summary" in query.lower():
        return "summarization"

    elif "score" in query.lower():
        return "evaluation"

    else:
        return "retrieval"