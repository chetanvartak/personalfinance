# API Contract (minimal)

POST /api/v1/auth/login
  - body: { username, password }
  - response: { access_token, token_type }

GET /api/v1/
  - response: placeholder

# Other endpoints
Refer to `app/api/v1/api.py` for registered routers.
