class APIKeyError(Exception):
    """Custom exception for issues related to API keys."""
    pass

class NoMetadataError(Exception):
    """Custom exception for no Metadata from gemini response."""
    pass
