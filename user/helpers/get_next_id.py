from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist

from user.models import CustomUser


def get_next_id(role):
    try:
        last_id = CustomUser.objects.exclude(role=role).aggregate(Max('id'))['id__max']
        if last_id is not None:
            return last_id + 1
    except ObjectDoesNotExist:
        pass

    return 1
