class APIKeyError(Exception):
    """Custom exception for issues related to API keys."""
    pass

class NoMetadataError(Exception):
    """Custom exception for no Metadata from gemini response."""
    pass

class NoContentFunctionResponse(Exception):
    """Custom exception for lack of types.Content.function_response"""
    pass
