# v0.2.4
- Introduced `Spa.id` property

# v0.2.3
- Implemented error messages instead of returning a HTTPStatus object.
- `testpypi` workarounds removed. (The `arcticspas` library is now deployed.)

# v0.2.2
- Added pylint and fixed its concerns
- Fixed tox calling setup.py directly.
- Fixed all tests.

# v0.2.1
- Removed AsyncSpa class and created `async_` functions in the Spa class instead. Async calls are untested.

# v0.2.0
- AsyncSpa class for asynchronous calls
- Developer scripts (lint, test) moved to `tox`

# v0.1.0
- Initial release
- arcticspa API v2.0
- Spa class for synchronous calls
