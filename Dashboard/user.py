from msgimport os
from msgraph import GraphServiceClient
from msgraph.generated.me.me_request_builder import MeRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration

graph_client = GraphServiceClient(credentials, scopes)

request_configuration = RequestConfiguration()
request_configuration.headers.add("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY"))
request_configuration.headers.add("ID", os.environ.get("USER_ID"))
request_configuration.headers.add("OPENAI_API_KEY", os.environ.get("OPENAI_API_KEY"))

result = await graph_client.me.get(request_configuration = request_configuration)
raph import GraphServiceClient
from msgraph.generated.me.me_request_builder import MeRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration

graph_client = GraphServiceClient(credentials, scopes)


request_configuration = RequestConfiguration()
request_configuration.headers.add("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY"))
request_configuration.headers.add("ID", os.environ.get("USER_ID"))
request_configuration.headers.add("OPENAI_API_KEY", os.environ.get("OPENAI_API_KEY"))


result = await graph_client.me.get(request_configuration = request_configuration)
