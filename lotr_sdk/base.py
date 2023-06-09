"""Base script used across defined."""

import requests
import lotr_sdk as api


class Borg:
    """Borg class making class attributes global"""

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class LotrBase(Borg):
    """Base Class used across defined."""

    def __init__(self, **kwargs):
        """Initialize SDK with secret key."""
        Borg.__init__(self)
        headers = {}
        api_key = kwargs.get("api_key", api.API_KEY)
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"

        arguments = dict(api_url=api.API_URL, headers=headers)
        if not hasattr(self, "requests"):
            req = LotrRequests(**arguments)
            self._shared_state.update(requests=req)


class LotrRequests(object):
    def __init__(self, api_url=api.API_URL, headers=None):
        """Initialize SDK Request object for browsing resource.
        Args:
                api_url: str
                headers: dict
        """
        self.API_BASE_URL = f"{api_url}"
        self.headers = headers

    def _request(self, method, resource_uri, **kwargs):
        """Perform a method on a resource.
        Args:
                method: requests.`method`
                resource_uri: resource endpoint
        Raises:
                HTTPError
        Returns:
                JSON Response
        """
        data = kwargs.get("data")
        qs = kwargs.get("qs")

        response = method(
            self.API_BASE_URL + resource_uri, json=data, headers=self.headers, params=qs
        )
        return response.json()

    def get(self, endpoint, **kwargs):
        """Get a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.get, endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """Create a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.post, endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """Update a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.put, endpoint, **kwargs)
