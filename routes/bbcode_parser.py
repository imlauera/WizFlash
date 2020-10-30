import bbcode
parser = bbcode.Parser()
parser.add_simple_formatter(
    'q',
    """
        <a href="javascript:void(0)"
            id="cite"
            class="btn btn-secondary btn-sm"
            onmouseover="openReply(%(value)s)"
            onmouseout="closeReply(%(value)s)">
                #%(value)s
        </a>
        <div style="overflow: visible;" id="quote-%(value)s"></div>
    """
)
