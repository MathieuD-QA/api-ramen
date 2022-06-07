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


def get_index(payload):
    index = supabase.table('Ramen-Reviews').select('*').eq('Review', payload).execute()
    return index


def post_created(payload):
    created = supabase.table('Ramen-Reviews').insert([payload]).execute()
    return created


def delete_index(payload):
    deleted = supabase.table('Ramen-Reviews').delete().eq('Review', payload).execute()
    return deleted
