# API Design Conventions

## URL Structure

```
GET    /api/v1/users          # List users
POST   /api/v1/users          # Create user
GET    /api/v1/users/:id      # Get user by ID
PUT    /api/v1/users/:id      # Update user (full)
PATCH  /api/v1/users/:id      # Update user (partial)
DELETE /api/v1/users/:id      # Delete user
```

## Naming

- Use plural nouns for resources: `/users`, `/orders`
- Use kebab-case for multi-word resources: `/order-items`
- Use camelCase for JSON fields: `firstName`, `createdAt`
- Nest related resources: `/users/:id/orders`

## Response Format

### Success

```json
{
  "data": { ... },
  "meta": {
    "page": 1,
    "pageSize": 20,
    "total": 100
  }
}
```

### Error

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable description",
    "details": [
      { "field": "email", "message": "Invalid email format" }
    ]
  }
}
```

## HTTP Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate resource |
| 422 | Unprocessable Entity | Semantic validation error |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Unexpected server error |

## Pagination

Use cursor-based pagination for large datasets:

```
GET /api/v1/users?cursor=abc123&limit=20
```

Or offset-based for simpler cases:

```
GET /api/v1/users?page=2&pageSize=20
```

## Filtering & Sorting

```
GET /api/v1/users?status=active&role=admin&sort=-createdAt,name
```

- Prefix with `-` for descending order

## Authentication

- Use Bearer tokens in the `Authorization` header
- Short-lived access tokens + refresh tokens
- Never pass tokens in URL query parameters
