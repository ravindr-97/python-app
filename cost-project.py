from azure.identity import ClientSecretCredential
from azure.mgmt.costmanagement import CostManagementClient

SUBSCRIPTION_ID = "f5ccd026-1c6d-42d9-9854-392865023846"
RESOURCE_GROUP_NAME = "Hawkeye-east-us"
TENANT_ID = "fbe11e7f-2426-4591-bff5-d5bb22bfeb36"
CLIENT_ID = "ed610304-b486-4727-942c-490d98b7610e"
CLIENT_SECRET = "TLnWh8pZK18Ejck-qrIa.~G1tYA0Lh5o.I"

CREDENTIAL = ClientSecretCredential(
    tenant_id = TENANT_ID,
    client_id= CLIENT_ID,
    client_secret= CLIENT_SECRET
)

COST_CLIENT = CostManagementClient(CREDENTIAL)

TEST = COST_CLIENT.query.usage("/subscriptions/f5ccd026-1c6d-42d9-9854-392865023846/", )

print(TEST)