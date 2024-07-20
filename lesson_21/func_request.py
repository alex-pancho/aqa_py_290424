import requests


# GET-requests
def make_get_request(url=None, endpoint=None, params=None, full_url=None):
    if full_url:
        uri = full_url
    elif url and endpoint:
        uri = url + endpoint
    else:
        raise ValueError('Either full_url or url and endpoint must be provided')

    response = requests.get(url=uri, params=params)
    if response.status_code != 200:
        raise requests.HTTPError(f'Not ok status code: {response.status_code}')
    return response.json()


# POST-requests
def make_post_request(url, endpoint, body):
    uri = url + endpoint
    response = requests.post(url=uri, json=body)
    if response.status_code != 200:
        raise requests.HTTPError(f'Not ok status code: {response.status_code}')
    return response.json()


# DELETE-requests
def make_delete_request(full_url=None):
    uri = full_url
    response = requests.delete(url=uri)
    if response.status_code != 200:
        raise requests.HTTPError(f'Not ok status code: {response.status_code}')
    return response.json()
