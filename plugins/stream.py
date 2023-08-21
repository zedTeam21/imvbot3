import shortzy 

from info import STREAM_API, STREAM_SITE, STREAM_URL, STREAM_LONG



#stream link shortner

shortz = shortzy.Shortzy(STREAM_API, STREAM_SITE)
async def stream_short_link(link):
    if STREAM_URL:
        if  STREAM_LONG =="True" or STREAM_LONG is True:
            return await shortz.get_quick_link(link)
        else:
            return await shortz.convert(link, silently_fail=False)
    return link
