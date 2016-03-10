from django.db import models

from ..core.models import UUIDModel


class FleaOwner(UUIDModel):
    name = models.CharField(max_length=128)
    url = models.URLField(unique=True)
    reddit_username = models.CharField(blank=True, null=True, max_length=128)
    active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or '--Unowned--'


class FleaTeam(UUIDModel):
    name = models.CharField(max_length=128)
    url = models.URLField(unique=True)
    owner = models.ForeignKey('FleaOwner', null=True)
    league = models.ForeignKey('leagues.FleaLeague', related_name='teams')
    stat_fgpct100 = models.PositiveIntegerField(default=0)
    stat_ftpct100 = models.PositiveIntegerField(default=0)
    stat_3pt = models.PositiveIntegerField(default=0)
    stat_reb = models.PositiveIntegerField(default=0)
    stat_stl = models.PositiveIntegerField(default=0)
    stat_blk = models.PositiveIntegerField(default=0)
    stat_ast = models.PositiveIntegerField(default=0)
    stat_to = models.PositiveIntegerField(default=0)
    stat_pts = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name