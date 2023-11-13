import os
from supabase import create_client, Client
import supabase.gotrue
from supabase.gotrue.types import AuthChangeEvent

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

response = supabase.table("prompt_results").select("*").execute()
response.data
