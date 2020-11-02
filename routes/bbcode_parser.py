import bbcode
parser = bbcode.Parser()
parser.add_simple_formatter(
    'q',
    """
        <span href="javascript:void(0)"
            onmouseover="openReply(%(value)s)"
            onmouseout="closeReply(%(value)s)"
            class="btn btn-outline-info btn-sm">%(value)s</span>
    """
)
