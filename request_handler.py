import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from views import (get_all_snakes, get_single_snake, create_snake, update_snake,
                    get_all_species, get_single_specie, create_specie, update_specie,
                    get_all_owners, get_single_owner, create_owner, update_owner)

import logging
logging.basicConfig(level=logging.DEBUG)


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """


    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        try:
            id = int(path_params[2])
        except IndexError:
            pass 
        except ValueError:
            pass  
        return (resource, id)  


    def do_GET(self):
        """Handles GET requests to the server """
        status_code = 200
        response = {}
        (resource, id) = self.parse_url(self.path)
        logging.debug(f"Inside the `do_GET`: {resource}, {id}")
        if resource == "species":
            if id is not None:
                response = get_single_specie(id)
                if response is None:
                    status_code = 404
                    response = {"message": f"{id} is currently in hibernation."}
            else: response = get_all_species()
        elif resource == "owners":
            if id is not None:
                response = get_single_owner(id)
                if response is None:
                    status_code = 404
                    response = {"message": f"{id} is currently not available for questions."}
            else: response = get_all_owners()
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        status_code = 201
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        logging.debug(f"Inside the `do_POST`: {resource}, {id}")
        if resource == "metals":
            new_metal = None
            new_metal = create_metal(post_body)
            response = new_metal
        elif resource == "orders":
            metal_does_exist = "metal_id" in post_body.keys()
            style_does_exist = "style_id" in post_body.keys()
            size_does_exist = "size_id" in post_body.keys()
            if not metal_does_exist:
                response = {"message": "metal_id is required"}
                status_code = 400
            elif not style_does_exist:
                response = {"message": "style_id is required"}
                status_code = 400
            elif not size_does_exist:
                response ={"message": "size_id is required"}
                status_code = 400
            else:
                response = create_order(post_body)
        elif resource == "styles":
            new_style= None
            new_style = create_style(post_body)
            response = new_style
        elif resource == "sizes":
            new_size= None
            new_size = create_size(post_body)
            response = new_size
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode())


    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        logging.debug(f"Inside the `do_PUT`: {resource}, {id}")
        response = {}
        if resource == "orders":
            if id:
                response = { "message" : "Your order has been placed and is in production, no changes can be made at this time, Thank you!" }
        elif resource == "metals":
            response = update_metal(id, post_body)
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
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        logging.debug(f"Inside the `do_DELETE`: {resource}, {id}")
        if resource == "orders":
            delete_order(id)
        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
