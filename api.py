import json
import urllib.error
import urllib.request


class CaddyApi:
    def __init__(self, base_url=None, server='server0'):
        self.data = None
        self.server = server

        if not base_url:
            self.base_url = 'http://localhost:2019/'

    def add_route(self, data=None, route_id=None):
        self.data = data

        if route_id and self.is_idexists(route_id):
            path = f"id/{route_id}/"
            return self._api(path=path, method='PATCH', data=data)
        else:
            path = f'config/apps/http/servers/{self.server}/routes'
            return self._api(path=path, method='POST', data=data)

    def is_idexists(self, element_id) -> bool:
        response = self._api(path=f"id/{element_id}/", method='GET')

        if response["status"] == 200:
            return True
        else:
            return False

    def _api(self, path='', method='GET', data=None) -> dict:
        result = dict({
            "status": None,
            "path": path,
            "response": None,
            "message": None
        })

        if data:
            data = json.dumps(data, indent=2).encode('utf-8')

        req = urllib.request.Request(self.base_url + path, data=data, method=method)
        req.add_header('Content-Type', f'application/json')

        try:
            with urllib.request.urlopen(req) as response:
                result["status"] = response.status
                r = response.read().decode('utf-8')

                if response.status != 200:
                    result["message"] = 'An Error Occurred!'

                if len(r) == 0:
                    result["message"] = response.msg
                else:
                    result["response"] = json.loads(r)
        except urllib.error.HTTPError as e:
            result["message"] = str(e)
        except json.decoder.JSONDecodeError as e:
            result["message"] = str(e)
        except:
            result["message"] = "Unknown error!"
        finally:
            return result
