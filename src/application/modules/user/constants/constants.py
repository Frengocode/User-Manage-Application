ACCOUNT_CONFIRMATION_CACHE_KEY: str = "account.{token}.confirmation"
ACCOUNT_CONFIRMATION_BODY = "You should confirim your account {token}"

# Constants for rabbitmq
USERS_EXCHANGE = "users"
USER_CREATED_ROUTING_KEY = "users.created"
