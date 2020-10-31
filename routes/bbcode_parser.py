import bbcode
parser = bbcode.Parser()
parser.add_simple_formatter(
    'q',
    """
        <a href="#%(value)s"
            id="cite"
            onclick="openReply(%(value)s)"
            class="btn btn-secondary btn-sm">#%(value)s</a>
        <div style="overflow: visible;" id="quote-%(value)s"></div>
    """
)
