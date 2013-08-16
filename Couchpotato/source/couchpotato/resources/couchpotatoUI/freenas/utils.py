from subprocess import Popen, PIPE
import os
import platform

couchpotato_pbi_path = "/usr/pbi/couchpotato-" + platform.machine()
couchpotato_etc_path = os.path.join(couchpotato_pbi_path, "etc")
couchpotato_fcgi_pidfile = "/var/run/fcgi_couchpotato.pid"
couchpotato_control = "/usr/local/etc/rc.d/couchpotato"
couchpotato_icon = os.path.join(couchpotato_pbi_path, "default.png")
couchpotato_oauth_file = os.path.join(couchpotato_pbi_path, ".oauth")

def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_couchpotato_oauth_creds():
    f = open(couchpotato_oauth_file)
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
