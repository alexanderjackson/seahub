# Copyright (c) 2012-2016 Seafile Ltd.
import re

from django.conf import settings

from seahub.utils import is_valid_email

def validate_accepter(accepter):
    if not is_valid_email(accepter):
        return False

    for pattern in settings.INVITATION_ACCEPTER_BLACKLIST:
        if pattern.startswith('*'):
            if accepter.endswith(pattern[1:]):
                return False
        elif accepter == pattern:
            return False
        else:
            compiled_pattern = re.compile(pattern)
            if compiled_pattern.search(accepter) is not None:
                return False

    return True
