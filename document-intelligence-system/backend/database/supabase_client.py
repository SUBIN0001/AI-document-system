from supabase import create_client
from config.settings import SUPABASE_URL, SUPABASE_KEY

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "Missing Supabase credentials. "
        "Ensure SUPABASE_URL and SUPABASE_KEY are set in your .env file."
    )

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)