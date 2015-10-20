#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

from satosa.backends.openid_connect import OpenIdBackend
from satosa.plugin_base.endpoint import BackendModulePlugin

XMLSEC_PATH = '/usr/local/bin/xmlsec1'


def full_path(local_file):
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, local_file)


PROVIDER = "google"
MODULE = OpenIdBackend


class OpenidPlugin(BackendModulePlugin):
    def __init__(self, base_url):
        module_base = "%s/%s" % (base_url, PROVIDER)
        config = RpConfig(module_base, PROVIDER)
        super(OpenidPlugin, self).__init__(OpenIdBackend, PROVIDER, config)


class RpConfig(object):
    def __init__(self, module_base, PROVIDER):
        self.CLIENTS = {
            PROVIDER: {
                "srv_discovery_url": "https://accounts.google.com/",
                "client_registration": {
                    "client_id": "492986585079-oon1lphrlblru781m9ojcitt7ud8tf7n.apps.googleusercontent.com",
                    "client_secret": "INqwvhksluxA79v1tV1cqEG0",
                    "redirect_uris": ["%s" % module_base],
                },
                "behaviour": {
                    "response_type": "code",
                    "scope": ["openid", "profile", "email"]
                },
                "userinfo_request_method": "GET",
                "allow": {
                    "issuer_mismatch": True,
                    "userinfo_request_method": "GET"
                }
            }
        }
        self.ACR_VALUES = ["PASSWORD"]
        self.VERIFY_SSL = False
        self.OP_URL = "https://accounts.google.com"
        self.STATE_ENCRYPTION_KEY = "Qrn9IQ5hr9uUnIdNQe2e0KxsmR3CusyARs3RKLjp"
        self.STATE_ID = "OpenID_Qrn9R3Cus"
