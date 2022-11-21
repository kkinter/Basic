### Various ways to deploy Django
- Directly on a server
	- Run directly on server
	- Docker
- Serverless Cloud
	- Google Cloud Run / Google App Engine
	- AWS Elastic Beanstalk / ECS Fargate

### How we'll deploy
- Single VPS on AWS(EC22)
- Docker / Docker Compose

### Why this approach?
- Simple solution
- Great for testing during development
- Low cost

### Steps we'll take

1. Config pjt for deploy
2. Create server on AWS
3. Deploy app


### Deploying Django
1. Setup a proxy
2. Handle static / media files
3. Configuratiion

### Components 
![[Pasted image 20221120064055.png]]

### Why use a reverse proxy ?
- Best practice when deploy Django
- WSGI server great at executing Python
	- Not great at serving data
- Web servers
	- Serve data really efficiently

### Applications we'll use
- nginx
	- Open source, fast, secure, production grade
- uWSGI
	- Open source, fast, lightweight, simple to use
- Docker Compose
	- Pulls it all together

### Docker Compose setup
![[Pasted image 20221120064440.png]]

### Handling configuration
- How do we configure deployed app?
	- Can't put everything into Git
- Various approaches
	- Environment variables
	- Secret managers
- We'll use environment variables
	- Popular approach
	- Simple to use
### How config works
- Create `.env` file on server
- Set values in Docker Compose

### Using AWS
- We'll host our app on AWS
	- Popular platform
- Students responsible for security and costs
- Must keep your account secure!
	- Use MFA
	- Use strong passwords
	- Don't share your account details
	- Keep your machine secure and update to date
	- Delete unused accounts

![[Pasted image 20221120160943.png]]