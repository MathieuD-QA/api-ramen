from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


def get_show():
    show = supabase.table('Ramen-Reviews').select('*').execute()
    return show

def get_index(payload = ""):
    pass


def post_created(payload = ""):
    pass

def delete_index(payload = ""):
    pass










