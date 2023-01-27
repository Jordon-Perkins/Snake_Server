import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import (get_all_snakes, get_single_snake, create_snake, update_snake,
                    get_all_species, get_single_specie,
                    get_all_owners, get_single_owner, delete_snake,
                    get_snakes_by_species_id)



class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """




    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/') 
        resource = path_params[1]
        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)
        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)


    def do_GET(self):
        """Handles GET requests to the server """
        status_code = 200
        response = {}
        parsed = self.parse_url(self.path)
        ( resource, _ ) = parsed
        if resource is not ["snakes", "species", "owners"]:
            status_code = 404
            if '?' not in self.path:
                ( resource, id ) = parsed
                if resource == "species":
                    if id is not None:
                        response = get_single_specie(id)
                        if response is None:
                            status_code = 404
                    else: response = get_all_species()
                elif resource == "owners":
                    if id is not None:
                        response = get_single_owner(id)
                        if response is None:
                            status_code = 404
                    else: response = get_all_owners()
                elif resource == "snakes":
                    if id is not None:
                        response = get_single_snake(id)
                        if response is None:
                            status_code = 404
                    else: response = get_all_snakes()
            else:
                (resource, query) = parsed
                if query.get('species') and resource == 'snakes':
                    response = get_snakes_by_species_id(query['species'][0])
            self._set_headers(status_code)
            self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        status_code = 201
        response = {}
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        if resource == "snakes":
            name_does_exist = "name" in post_body.keys()
            owner_id_does_exist = "owner_id" in post_body.keys()
            species_id_does_exist = "species_id" in post_body.keys()
            gender_does_exist = "gender" in post_body.keys()
            color_does_exist = "color" in post_body.keys()
            if not name_does_exist:
                response = {"message": "name is required"}
                status_code = 400
            elif not owner_id_does_exist:
                response = {"message": "owner_id is required"}
                status_code = 400
            elif not species_id_does_exist:
                response = {"message": "species_id is required"}
                status_code = 400
            elif not gender_does_exist:
                response = {"message": "gender is required"}
                status_code = 400
            elif not color_does_exist:
                response = {"message": "color is required"}
                status_code = 400
            else:
                response = create_snake(post_body)
        else:
            status_code = 404
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode())


    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        response = {}
        if resource == "snakes":
            response = update_snake(id, post_body)
        if response:
            self._set_headers(204)
        else:
            self._set_headers(404)
        self.wfile.write(json.dumps(response).encode())


    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response
        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    def do_DELETE(self):
        response = {}
        status_code = 204
        (resource, id) = self.parse_url(self.path)
        if resource == "snakes":
            delete_snake(id)
        else:
            response = {"message" : "this table doesn't exist"}
            status_code = 404
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
