import os
import platform
import pwd

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from sabnzbdUI.freenas import models, utils


class SabnzbdForm(forms.ModelForm):

    class Meta:
        model = models.Sabnzbd

        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SabnzbdForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(SabnzbdForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.sabnzbd_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('sabnzbd_enable="YES"\n')

        os.system(os.path.join(utils.sabnzbd_pbi_path, "tweak-rcconf"))
