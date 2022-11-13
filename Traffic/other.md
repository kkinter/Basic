## Django
- python web Framework
- 다루는 것
  - URL 매핑
  - 객체 관계 매퍼
  - 관리자 사이트

## DRF 
- Django add- on
- API 만듦

## Postgre SQL

## DOCKER
- 개발 환경 
- 배포

## Swagger 
- API 문서
- Brouweble api ? 

## Github Actions 
- 자동화
  - 테스팅 and Linting

## Apps 
- app/ - django project
- app/core/ - code shared between mulpiple apps
- app/user/ - User related code
- app/recipe/ - Recipe related code

## TDD 란 ?
- Unit Tests
  - Sets up conditions / inputs
  - Runs a piece of code
  - Checks outputs with "assertions"
- Many benefits
  - Ensures code runs as expected
  - Catches bugs
  - improves reliabiliity
  - Provieds confidence
- Development pratice

  - Wrtie Test > Write code
  - Write Test > Run Test > Add feature > Run Test > Re-factor
## 왜 TDD를 사용하는가 ?
- Better understanding of code
- Make changes with confidence
- Reduces bugs

## 왜 Docker를 사용하는가?
- Consistent dev and prod environment
- Easier collaboration 디펜던시로 발생하는 문제가 해소됨
  - diff ver python
  - diff ver db
  - diff ver SDK
- Capture all dependencies as code
  - Python requirements
  - Operationg system dependencies -->
- Easier cleanup

## 어떻게 Docker를 사용할 것인가 ?
- Define Dockerfile
- Create Docker Compose config
- Run all commands via Docker Compose

## Docker GitHub Actions
- Doker Hub introduced rate limit:
  - 100 pulls/6hr for unauthenticated users
  - 200 pulls/6hr for unauthenticated users
- GitHub Actions is a shared service
  - 100 pulls/6hr applied for all users
- Authenticate with Docker Hub
  - create account
  - setup credentials
  - Login before running job
  - Get 200 pulls/6hr for free

## Using Docker with Django

- Many benefits
  - Consistent dev and prod environment
  - Easier collaboration
  - Capture all dependencies as code
  - Easier cleanup
  - Save a lot of time

- Drawbacks
  - VSCode unable to access interpreter
  - More difficult to use integrated features 
    - Lintin tools, interactive debugger

- configure Docker
  - create a dockerfile
  - lists steps for creating image
    - choose a base image(python)
    - install dependencies
    - Setup users

## Docker compose
- How our docker image(s) should be used
- Define our "services"
  - Name
  - Port mappings
  - Volume mappings

## Using Docker Compose
- Run all commands through Docker Compose
 `docker-compose run --rm app sh -c "python manage.py collectstatic`
 - `docker-compose` runs a Docker Compose command
 - `run` will start a specific containser defined in config
 - `--rm` removes the container
 - `app` is the name of the service
 - `sh -c` passes in a shell command
 - Command to run inside container

## What is Linting ?
- Tool to check code formmating
- Highlights errors, typos, formatting issues

## How we'll handling Linting
- install `flake8` package
- Run it througn Docker Compose

## what is GitHub Actions ?
- automation tool
- Similar to Travis-CI , GitLab CI/CD, Jenkins
- Run jobs when code changes
- Automate tasks

### Common uses
- Deployment
- Code linting
- Unit tests

### How it works
Trigger(Push to GitHub) > Job(Run unit tests) > Result (Success/fail)

### Pricing
- Charged per miuntes
- 2000 free miuntes
- Various plans available

### Configure GitHub Actions
- Create a config file at `.github/workflows/checks.yml
  - Set trigger
  - Add steps for running testing and linting
- Configure Docker Hub auth

### Docker Hub
- Needed to pull base images
- Rate limits
  - Anonymous : 100/6h
  - Authenticated : 200/6h
- GitHub Actions uses shared IP addresses
  - Limit applied to all users
- Authenticate with Docker Hub
  - 200 pulls per 6h all to ourselves
  - more than enough for most projects

## QUIZ GitHub Actions
### GitHub 작업의 일반적인 용도는 무엇입니까?
Deploy, Lint, Unittest
### GitHub Action 언어
YML, YAML
### Docker Hub로 인증해야 하는 이유는 무엇입니까?
pull 의 제한이 있기 때문에


## Django test Framework
- Based on the `unittest` library
- Django adds features
  - Test client - dummy web browser
  - Simulate authentication
  - Temporary database
- Django REST Framework adds features
  - API test client

### Where do you put tests ?
- Placeholder tests.py added to each app
- Or, create tests/ subdir to split tests up
- Keep in mind:
  - Only use `tests.py` or `tests/` dir(not both)
  - Test modules must start with `test_`
  - Test directories must contain `__init__.py`
-app/
-`__init__.py`
-tests.py
--tests/
--- `__init__.py`
--- `test_module_one.py`
### Test Database
- Test code that uses the DB
- Specific db for tests
  Runs test > Clears data 
- Happens for every test(default)

### Test classes
- SimpleTestCase
  - No DB integration
  - Userful if no database is required for your test
  - Save time exectuing tests
- TestCase
  - DB integration
  - Useful for testing code that uses the DB

`docker-compose run --rm app sh -c "python manage.py test"`

### TDD
- Create test
- Add Functionality

1. Write test for behaviour expected to see in code
2. Test fails
3. Write code so test passes


### What is Mocking ?
- Override or change behaviour of dependencies
- Avoid unintended side effects
- Isolate code being tested
### Why use mocking ?
- Avoid relying on external services
  - Can't guarantee they will be available
  - Makes test unpredictable and inconsistent

- Avoid unintended consequences
  - Accidentally sending emails
  - Overloading external services

### Example
register_user() > create_in_db() > send_welcome_email()
- Prevent email being send
- Ensure `send_welcome_email()` called correctly
### Another benefit
- Speed up tests

### How to mock code?
- Use `unittest.mock`
  - `MagicMock/Mock` - Replace real objects
  - `patch` - Overrides code for tests

### Testing web requests
- Make actual requests
- Check result

### Django REST Framework APIClient
- Based on the Django's TestClient
- Make requests
- Check result
- Override authentication

## Common testing problems
### Common Issues
- Tests not running

- Ran less test than you have

### Possible reasons for test not running 
- Missing `__init__.py` in `tests/` dir
- Indentation of test cases
- Missing `test` prefix for method
- `ImportError` when running tests
- Both `test/` dir and `tests.py` exist.

### Quiz: TDD with Django
`Django pjt 에서 테스트를 찾는 방법`
Django 테스트 실행은 "test"로 시작하는 모듈을 찾습니다. 예를 들어, 이것은 test.py 파일 또는 tests/test_something.py일 수 있습니다.
`단위 테스트 작성과 관련하여 Mocking이란 무엇입니까?`
이는 테스트 중인 코드를 격리하고 의도하지 않은 부작용을 방지하는 데 도움이 됩니다.


## Databse
- PostgreSQL
  - Popular open sourve DB
  - Integrates well with Django
- Docker Compose
  - Defined with project (re-usable)
  - Persistent data using volumes
  - Handles network configuraiton
  - Environment variable configuration
### Architecture

### Network connectivity
- Set `depends_on` on `app` service to start `db` first
- Docker Compose creates a network
- The `app` service can use `db` hostname

### Volumes
- Persistent data
- Maps directory in container to local machine
