import re

pattern ="was"

text = """This wiki was is in the process of being archived due to lack of usage and the resources necessary to serve it — predominately to bots, crawlers, and LLM companies. Edits are discouraged.
Pages are preserved as they were at the time of archival. For current information, please visit python.org.
If a change to this archive is absolutely needed, requests can be made via the infrastructure@python.org mailing list."""

match =re.search(pattern,text)
print(match)