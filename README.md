# SuperInstance - ActiveLog Technical Repository

A comprehensive suite of event-driven backend systems, multi-agent orchestration tools, and intelligent logging applications designed for scalable, production-ready deployments.

## Overview

This repository contains the technical components of the SuperInstance project, including:

- **Multi-Agent Orchestration System**: Advanced Claude Code orchestration with master-worker architecture
- **AutoCoder**: Automated code generation and development tools
- **Logging Applications**: Voice-note logger, deckboss logger, and business logging solutions
- **Deployment Infrastructure**: AWS Lambda deployment scripts and Infrastructure-as-Code

## Repository Structure

```
ActiveLog-TechnicalRepo/
├── projects/
│   ├── multibot/              # Multi-agent orchestration system
│   ├── autocoder/             # Automated coding tools
│   ├── logging-apps/          # Voice, deckboss, and business logging
│   └── deployment/            # AWS deployment scripts and IaC
├── docs/
│   ├── architecture/          # Architecture documents and design specs
│   ├── guides/                # Implementation and usage guides
│   └── research/              # Research materials and technical papers
├── scripts/                   # Utility and automation scripts
├── config/                    # Configuration templates and examples
└── research/                  # Research documentation and findings
```

## Key Projects

### 1. Multi-Agent Orchestration System (`projects/multibot/`)

A hierarchical multi-agent system where a Master Claude Code instance (Opus) coordinates multiple Worker instances (Sonnet/Haiku) working in parallel on the same Git repository using different branches/worktrees.

**Key Features:**
- Master-Worker architecture for parallel task execution
- Task decomposition and intelligent assignment
- Git worktree management for isolated development
- Real-time monitoring and coordination
- MCP server integration for enhanced capabilities

**Documentation:** See `projects/multibot/orchestrator-master/README.md` and `docs/architecture/ARCHITECTURE.md`

### 2. AutoCoder (`projects/autocoder/`)

Automated code generation system supporting multiple programming languages and architectural patterns.

**Key Features:**
- Template-based code generation
- Support for Python, Go, and more
- Clean architecture patterns
- API gateway and microservices scaffolding
- Benchmark and optimization tools

**Documentation:** See `projects/autocoder/autocoder/README.md`

### 3. Logging Applications (`projects/logging-apps/`)

Suite of specialized logging applications for various use cases:

- **Voice Note Logger**: Audio recording and transcription with AWS integration
- **Deckboss Logger**: Industrial-grade BLE device logging
- **Business Log App**: Business process logging and automation

**Key Technologies:**
- React Native / Expo
- AWS Amplify
- GraphQL APIs
- BLE device integration

### 4. Deployment Infrastructure (`projects/deployment/`)

AWS-based deployment automation and Infrastructure-as-Code for serverless architectures.

**Key Features:**
- Lambda function deployment
- PowerShell/Python automation scripts
- Event-driven architecture setup
- DynamoDB integration
- CloudWatch monitoring

## Architecture Highlights

### Event-Driven Microservices

The ActiveLog backend follows modern scalable system design principles:

- **Service Decoupling**: Independent microservices for each domain
- **API Gateway**: Unified request handling with authentication
- **Event-Driven Messaging**: Pub-sub channels for async communication
- **CQRS & Event Sourcing**: Scalable reads/writes with full auditability
- **Containerization**: Docker + Kubernetes/Fargate orchestration

### Multi-Agent Orchestration

The multibot system implements:

- **Hierarchical Coordination**: Master delegates to specialized workers
- **Git Worktree Management**: Isolated development environments
- **File-Based Communication**: JSON message passing between agents
- **State Synchronization**: Distributed state with atomic updates
- **MCP Integration**: GitHub, filesystem, and custom MCP servers

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.9+
- Git
- AWS CLI (for deployment projects)
- Docker (optional, for containerization)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/ctothed/SuperInstance.git
   cd ActiveLog-TechnicalRepo
   ```

2. **Install dependencies for a specific project**
   ```bash
   # For multibot
   cd projects/multibot/orchestrator-master
   pip install -r requirements.txt

   # For logging apps
   cd projects/logging-apps/voice-note-logger
   npm install
   ```

3. **Review project-specific README files** for detailed setup instructions

## Configuration

Each project has its own configuration requirements. See individual project README files for details:

- Multibot: `projects/multibot/orchestrator-master/config/`
- AutoCoder: `projects/autocoder/autocoder/` settings
- Logging Apps: `amplify_outputs.json` and environment variables
- Deployment: `projects/deployment/activelog-deploy/lambda/config.json`

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **Architecture**: System design and architectural patterns
- **Guides**: Implementation and usage documentation
- **Research**: Technical papers and research findings

Key documents:
- [Multi-Agent Architecture](docs/architecture/ARCHITECTURE.md)
- [ActiveLog Backend Design](docs/architecture/ActiveLog-Backend-Architecture.txt)

## Development Workflow

### Multi-Agent Development

The multibot system supports parallel development:

1. Master agent decomposes tasks
2. Workers execute in isolated worktrees
3. Changes are coordinated and merged
4. Continuous monitoring and recovery

### CI/CD

Projects use Infrastructure-as-Code and automated deployment:

- Terraform for AWS resources
- GitHub Actions / AWS CodePipeline
- Automated testing and validation
- Rollback capabilities

## Contributing

This is a professional development repository. When contributing:

1. Follow the existing code style and architecture
2. Write comprehensive tests
3. Update documentation
4. Use meaningful commit messages
5. Request code review before merging

## Technology Stack

- **Languages**: Python, TypeScript/JavaScript, Go
- **Frameworks**: React Native, Expo, FastAPI
- **Cloud**: AWS (Lambda, DynamoDB, S3, Amplify)
- **AI/ML**: Claude Code, OpenAI APIs
- **Infrastructure**: Terraform, Docker, Kubernetes
- **Messaging**: Event buses, SQS, Kafka
- **Monitoring**: OpenTelemetry, Prometheus, Grafana

## Project Status

This repository is actively maintained and under continuous development. Individual projects are at various stages:

- **Multibot**: Beta - Active development
- **AutoCoder**: Stable - Production ready
- **Logging Apps**: Alpha - Early testing
- **Deployment**: Stable - Production ready

## License

[License information to be added]

## Contact & Support

For professional development inquiries:
- GitHub: [@ctothed](https://github.com/ctothed)
- Repository: [SuperInstance](https://github.com/ctothed/SuperInstance)

## Acknowledgments

Built with Claude Code and modern development practices. Special thanks to the open-source community for tools and frameworks that make this possible.

---

**Note**: This repository excludes creative works, models, and large re-downloadable dependencies. See `.gitignore` for complete exclusions.
