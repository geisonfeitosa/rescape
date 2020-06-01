def unescapeXml(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt", ">")
    s = s.replace("&amp", "&")
    s = s.replace("&nbsp;", " ")
    return s

def unescapeString(s):
    s = s.replace('\\r', '')
    s = s.replace('\\t', '')
    s = s.replace('\\n', '')
    return s