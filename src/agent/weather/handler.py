import boto3
from strands import Agent
from strands.models import BedrockModel
from strands_tools import http_request
from typing import Dict, Any

# Define a weather-focused system prompt
WEATHER_SYSTEM_PROMPT_US = """You are a weather assistant with HTTP capabilities for US. You can:

1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:
1. First get the coordinates or grid information using https://api.weather.gov/points/{latitude},{longitude} or https://api.weather.gov/points/{zipcode}
2. Then use the returned forecast URL to get the actual forecast
"""

WEATHER_SYSTEM_PROMPT_IT = """You are a weather assistant with HTTP capabilities for Italy.

You can:
1. Make HTTP requests to APIs like https://nominatim.openstreetmap.org/search and https://api.open-meteo.com/v1/forecast
2. Process and display weather forecast data
3. Provide weather information for locations in Italy

When using Nominatim API:
- You must set a valid User-Agent header
- You must respect usage policy: make max 1 request per second (or you risk being blocked)

If you are blocked by Nominatim API please print the exact error.

When retrieving weather information:
1. Use this API endpoint to get city latitude and longitude: https://nominatim.openstreetmap.org/search?q={city},Italia&format=json
2. Use this API endpoint to get forecast based on latitude and longitude: https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true
3. Then use the returned forecast URL to get the actual forecast
"""

WEATHER_SYSTEM_PROMPT = """
When displaying responses:
- Display a json with this format {"city":..., "region":..., "latitude":..., "longitude":..., "temperature": ..., "weather_description"...}
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language
- Always explain the weather conditions clearly and provide context for the forecast.
"""

WEATHER_SYSTEM_PROMPT_US = WEATHER_SYSTEM_PROMPT_US + WEATHER_SYSTEM_PROMPT
WEATHER_SYSTEM_PROMPT_IT = WEATHER_SYSTEM_PROMPT_IT + WEATHER_SYSTEM_PROMPT

# Create a BedrockModel
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-micro-v1:0",
    region_name='us-east-1'
)

# The handler function signature `def handler(event, context)` is what Lambda
# looks for when invoking your function.
def weather(event: Dict[str, Any], _context) -> str:
    prompt = event.get('prompt')
    if not prompt:
        return str("Missing required parameter: 'prompt'")

    region = event.get('region', 'US').upper()

    if region == 'US':
        system_prompt = WEATHER_SYSTEM_PROMPT_US
    elif region == 'IT':
        system_prompt = WEATHER_SYSTEM_PROMPT_IT
    else:
        return str("Unsupported region. Must be 'US' or 'IT'")

    weather_agent = Agent(
        model=bedrock_model,
        system_prompt=system_prompt,
        tools=[http_request],
    )

    response = weather_agent(prompt)
    return str(response)