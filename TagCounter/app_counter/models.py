from django.db import models


class TagCounter(models.Model):
    PERFORMED = 'performed'
    DONE = 'done'
    ERROR = 'error'

    STATUS_SELECTIONS = (
        (PERFORMED, 'Performed'),
        (DONE, 'Done'),
        (ERROR, 'Error')
    )

    url = models.CharField(verbose_name='URL', max_length=2048)
    status = models.CharField(verbose_name='Parse status', choices=STATUS_SELECTIONS, default=PERFORMED, max_length=9)
    tags = models.JSONField(default=dict, verbose_name='URL Tags', null=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Counter'
        verbose_name_plural = 'Counters'
