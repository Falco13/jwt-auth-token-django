# jwt-auth-token-django
# Django application with token authentication, refresh & access tokens, registration and logout

- User model with usernamefield = email, and without username field.
- Implemented the ability to authentication with jwt-token, access_token refresh with refresh_token from cookies, logout with clearing cookies.
- Fixed authentication error code 401 instead of 403.


__API end-points:__
- api/register/
- api/login/
- api/logout/
- api/user/
- api/refresh/


__Used tools:__    
:heavy_check_mark: Python     
:heavy_check_mark: Django REST Framework    
:heavy_check_mark: PyJWT      
:heavy_check_mark: SQLite database    
