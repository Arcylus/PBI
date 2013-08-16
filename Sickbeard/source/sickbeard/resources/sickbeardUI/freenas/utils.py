from subprocess import Popen, PIPE
import os
import platform

sickbeard_pbi_path = "/usr/pbi/sickbeard-" + platform.machine()
sickbeard_etc_path = os.path.join(sickbeard_pbi_path, "etc")
sickbeard_fcgi_pidfile = "/var/run/fcgi_sickbeard.pid"
sickbeard_control = "/usr/local/etc/rc.d/sickbeard"
sickbeard_icon = os.path.join(sickbeard_pbi_path, "default.png")
sickbeard_oauth_file = os.path.join(sickbeard_pbi_path, ".oauth")

def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_sickbeard_oauth_creds():
    f = open(sickbeard_oauth_file)
    lines = f.readlines()
    f.close()

    key = secret = None
    for l in lines:
        l = l.strip()

        if l.startswith("key"):
            pair = l.split("=")
            if len(pair) > 1:
                key = pair[1].strip()

        elif l.startswith("secret"):
            pair = l.split("=")
            if len(pair) > 1:
                secret = pair[1].strip()

    return key, secret
