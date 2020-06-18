
import re
from django import template

from django.utils.safestring import mark_safe

register = template.Library()

regex_speciale = re.compile(r"(\[speciale\])(?P<sp>(.)*)(\[/speciale\])", re.DOTALL)
# t => tag => <span> ... </span>
regex_tag = re.compile(r"(\[t\])(?P<tg>(.)*)(\[/t\])", re.I)


@register.filter(name='reformate', is_safe=True)
def reformatage_contenu(content):
    '''
        [speciale]
            ...content...
        [/speciale]

        # remplacer par:

        <div class='quote-wrapper'>
            <div class='quotes'>
                ...content...
            </div>
        </div>
    '''

    content = regex_speciale.sub('<div class="quote-wrapper"><div class="quotes">\g<sp></div></div>', content)
    content = regex_tag.sub("<span>\g<tg></span>", content)

    return mark_safe(content)
