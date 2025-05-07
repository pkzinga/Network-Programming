
# the webserver has been adapted from Oddette Windsor Python Network Programming 101 section: web server with aiohttp
# the paths.get("/assets/ {filename}") route and the implementation of 
# the handle_image function has been implemented with the help of deepseek ai

from aiohttp import web
from pathlib import Path
import argparse

# added just for testing purposes
def parse_args():
    parser =    argparse.ArgumentParser()

    parser.add_argument("--host", type=str, default= "localhost",help="THE ADDRESS OF THE WEBSERVER")
    
    parser.add_argument("--port", type= int, default=8088,help="THE PORT NUMBER ON WHICH IT IS BOUND ON")

    return parser.parse_args()


def main():
    pass 

    paths = web.RouteTableDef()

    @paths.get("/")
    async def handle_index(request):
        try:
        
            index_file_path = Path(__file__).parent / "templates/index.html"
            index_file_handle = open(file= index_file_path,mode= "r")
            index_data = index_file_handle.read()
            index_file_handle.close()

            return web.Response(text=index_data,content_type="html")
        except FileNotFoundError as e:
            return web.Response(text="the was an error openng the inde.htmll file", status=404)
    

    @paths.get("/register")
    async def handle_register(request):
        try:

            register_file_path = Path(__file__).parent / "templates/register.html"
            register_file_handle = open(file= register_file_path,mode= "r")
            register_data = register_file_handle.read()
            register_file_handle.close()

            return web.Response(text=register_data,content_type="html")
        except FileNotFoundError as e:
            return web.Response(text="file not found", status= 404 , type='text/html')
 
        

    @paths.post("/submit")
    async def handle_submit(request):
        try:
            submit_data =  await request.post()
            username = submit_data.get("username","").strip()
            email = submit_data.get("email", "").strip()

            db_path = Path(__file__).parent / "db.txt"
            db_handle = open(db_path,"a")
            database_data = db_handle.write(f"{username} : {email} \n")
            db_handle.close()

            return web.Response(text="Form has been submitted succesfully")
        except FileExistsError as e:
            return web.Response(text="There was an error parsing the entry to db.txt", status=404)

    
    @paths.get("/assets/{filename}")
    async def handle_image(request):
        try:
            filename = request.match_info['filename']
            image_path = Path(__file__).parent / "assets" / filename
            if not image_path.is_file():
                raise FileNotFoundError
        
            return web.FileResponse(image_path)
        
        except FileNotFoundError as e:
            return web.Response(text="file not found", status=404)

   
    
    args = parse_args()
    HOST = args.host
    PORT = args.port

    web_server = web.Application()
    web_server.add_routes(paths)
    web.run_app(web_server,host=HOST, port=PORT)
    

if __name__ == "__main__":
     main()

