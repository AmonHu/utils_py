from suds.client import Client


def call_wcf_api(url: str, method_name: str, *args):
    client = Client(url)
    method = getattr(client.service, method_name)
    return method(args)
