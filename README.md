# Raspberry Pi System CI/CD

This repository contains the system configuration and application code for Raspberry Pi devices in the IoT Reconfiguration project.

## Project Structure

``` plaintext
raspi-repo/
├── app/                 # Application code
├── docs/                    
├── Dockerfile           # Docker build configuration
└── .github/workflows/   # CI/CD workflows
```

## Development Setup

1. Install Docker
2. Clone this repository
3. Build the Docker image:

```bash
docker build -t raspi-system .
```

## Running Locally

```bash
docker run -d --name raspi-system -p 8050:8050 raspi-system 
```

## Testing

```bash
docker run --rm raspi-system python -m pytest
```

## CI/CD Pipeline

The CI/CD pipeline automatically:

1. Builds the Docker image
2. Runs tests
3. Pushes to Docker Hub if tests pass
4. Tags releases

## Versioning

We use semantic versioning (MAJOR.MINOR.PATCH)

- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes, backward compatible

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
