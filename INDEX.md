# SuperInstance Technical Repository - Knowledge Index

This index provides a comprehensive knowledge tree and navigation system for finding specific functionality, concepts, and documentation across the repository.

## Quick Navigation by Purpose

### I want to...
- [Deploy to AWS Lambda](#aws-deployment)
- [Set up multi-agent orchestration](#multi-agent-orchestration)
- [Generate code automatically](#code-generation)
- [Build a logging application](#logging-applications)
- [Understand the architecture](#architecture--design)
- [Get started with development](#getting-started)
- [Contribute to the project](#contributing)
- [Find configuration examples](#configuration)

## Knowledge Tree by Domain

### 1. Multi-Agent Systems & AI Orchestration

**Core Concept**: Hierarchical agent coordination where a Master agent orchestrates multiple Worker agents

**Entry Points:**
- 📄 [Main Documentation](projects/multibot/orchestrator-master/README.md)
- 📄 [Architecture Overview](docs/architecture/ARCHITECTURE.md)
- 📄 [Communication Protocol](projects/multibot/orchestrator-master/COMMUNICATION_PROTOCOL.md)

**Key Components:**

#### Master Agent Coordination
| Component | File | Purpose |
|-----------|------|---------|
| Orchestrator | `orchestrator_master.py` | Main master agent logic |
| Worker Manager | `worker_manager.py` | Spawning and lifecycle management |
| Task Queue | `task_queue.py` | Task prioritization and assignment |
| Message Queue | `message_queue.py` | Inter-agent messaging |

#### Worker Agent Intelligence
| Component | File | Purpose |
|-----------|------|---------|
| Worker Intelligence | `worker_intelligence.py` | AI decision-making for workers |
| Worker Lifecycle | `worker_lifecycle.py` | State management |
| Worker MCP Server | `worker_mcp_server.py` | MCP integration |
| Launch Worker | `launch_worker.py` | Worker spawning logic |

#### Task Management
| Component | File | Purpose |
|-----------|------|---------|
| Task Decomposition | `task_decomposition.py` | Breaking down complex tasks |
| Task Orchestration | `task_orchestration_tools.py` | Coordinating task execution |
| Priority Handler | `priority_timeout_handler.py` | Priority and timeout management |

#### Communication & Coordination
| Component | File | Purpose |
|-----------|------|---------|
| Communication Layer | `communication.py` | Base communication protocols |
| Master Communication | `master_communication.py` | Master-specific messaging |
| Merge Coordination | `merge_coordination.py` | Git merge orchestration |

#### Memory & Knowledge
| Component | File | Purpose |
|-----------|------|---------|
| Memory Management | `memory_management.py` | Worker memory systems |
| Shared Knowledge | `shared_knowledge.py` | Knowledge sharing between agents |
| Context Management | Via memory tools | Maintaining agent context |

#### Monitoring & Observability
| Component | File | Purpose |
|-----------|------|---------|
| Monitoring Dashboard | `monitoring_dashboard.py` | Real-time monitoring UI |
| Monitoring GUI | `monitoring_gui.py` | GUI components |
| Web Dashboard | `web_dashboard_server.py` | Web-based monitoring |
| Advanced Dashboard | `advanced_web_dashboard.py` | Enhanced features |

**Documentation:**
- [Installation Guide](projects/multibot/orchestrator-master/INSTALLATION.md)
- [Worker Intelligence](projects/multibot/orchestrator-master/WORKER_INTELLIGENCE.md)
- [Worker Lifecycle](projects/multibot/orchestrator-master/WORKER_LIFECYCLE.md)
- [Task Orchestration](projects/multibot/orchestrator-master/TASK_ORCHESTRATION.md)
- [Monitoring Dashboard](projects/multibot/orchestrator-master/MONITORING_DASHBOARD.md)
- [Web Dashboard](projects/multibot/orchestrator-master/WEB_DASHBOARD.md)

---

### 2. Automated Code Generation

**Core Concept**: Template-based code generation for multiple languages and architectural patterns

**Entry Points:**
- 📄 [AutoCoder Documentation](projects/autocoder/autocoder/README.md)
- 📂 [Example Projects](projects/autocoder/autocoder/example/)
- 📂 [Benchmarks](projects/autocoder/autocoder/benchmark/)

**Key Components:**

#### Code Generation Engines
| Component | File | Purpose |
|-----------|------|---------|
| Controller Generator | `autocode/controller.py` | API controller generation |
| Model Generator | `autocode/model.py` | Data model generation |
| Gateway Generator | `autocode/gateway.py` | API gateway scaffolding |
| Router Generator | `autocode/router.py` | Route generation |
| Datastore Generator | `autocode/datastore.py` | Database layer generation |

#### Support Systems
| Component | File | Purpose |
|-----------|------|---------|
| Container | `autocode/container.py` | Dependency injection |
| Dashboard | `autocode/dashboard.py` | Dashboard generation |
| Use Cases | `autocode/use_case.py` | Business logic generation |
| Settings | `autocode/setting.py` | Configuration management |

#### Examples & Templates
| Type | Location | Languages |
|------|----------|-----------|
| Python Examples | `example/controller.py` | Python |
| Go Account Service | `example/client/app_account/` | Go |
| Go Gateway Service | `example/client/app_gateway/` | Go |
| Go Product Service | `example/client/app_product/` | Go |
| Jupyter Notebooks | `example/*.ipynb` | Python |

#### Optimization & Benchmarking
| Type | File | Purpose |
|------|------|---------|
| Algorithm Optimization | `benchmark/optimization_algorithm.ipynb` | Algorithm tuning |
| Bayesian Optimization | `benchmark/optimization_bayesian.ipynb` | Hyperparameter optimization |
| Genetic Algorithms | `benchmark/optimization_genetic.ipynb` | Evolutionary optimization |

**Supported Patterns:**
- Clean Architecture
- Microservices
- API Gateway Pattern
- Repository Pattern
- Dependency Injection

---

### 3. Logging & Data Collection Applications

**Core Concept**: Specialized logging applications for voice, industrial BLE devices, and business processes

**Entry Points:**
- 📂 [Logging Apps Directory](projects/logging-apps/)
- 📄 [Voice Note App README](projects/logging-apps/voice-note-logger/voice-note-app/)
- 📄 [Deckboss App README](projects/logging-apps/voice-note-logger/deckboss-app/README.md)

#### Voice Note Logger
**Purpose**: Audio recording with transcription and AWS storage

| Component | Location | Technology |
|-----------|----------|------------|
| Main App | `voice-note-app/App.js` | React Native |
| Backend Schema | `voice-note-app/amplify/schema.graphql` | GraphQL |
| Auth | `voice-note-app/amplify/auth/` | AWS Amplify Auth |
| Assets | `voice-note-app/assets/` | Images/Icons |

**Features:**
- Audio recording and playback
- AWS S3 storage integration
- Transcription services
- Metadata tagging
- Offline support

#### Deckboss Logger
**Purpose**: Industrial-grade BLE device logging for fishing/marine operations

| Component | Location | Technology |
|-----------|----------|------------|
| App Screens | `deckboss-app/app/` | React Native/TypeScript |
| GraphQL Queries | `deckboss-app/graphql/` | GraphQL |
| Components | `deckboss-app/components/` | React Components |
| Navigation | `deckboss-app/app/(tabs)/` | Tab Navigation |

**Features:**
- BLE device discovery and connection
- Real-time telemetry logging
- Data synchronization
- Custom characteristics handling
- Low-power management

#### Business Log App
**Purpose**: Business process logging and automation

| Component | File | Technology |
|-----------|------|------------|
| GUI Automation | `autoGUI.py` | Python |
| Commands | `commands.txt` | Configuration |

---

### 4. AWS Deployment & Infrastructure

**Core Concept**: Serverless deployment automation with Infrastructure-as-Code

**Entry Points:**
- 📂 [Deployment Directory](projects/deployment/activelog-deploy/)
- 📄 [Backend Architecture](docs/architecture/ActiveLog-Backend-Architecture.txt)

#### Deployment Scripts
| Script | Platform | Purpose |
|--------|----------|---------|
| `activelog-fire.ps1` | Windows PowerShell | Automated deployment |
| `activelog-fire.cmd` | Windows CMD | Legacy deployment |

#### Lambda Functions
| Component | File | Purpose |
|-----------|------|---------|
| Main Handler | `lambda/app.py` | Lambda entry point |
| Logger | `lambda/dm_logger.py` | Logging implementation |
| Configuration | `lambda/config.json` | Lambda settings |

**AWS Services Used:**
- Lambda - Serverless compute
- DynamoDB - NoSQL database
- S3 - Object storage
- CloudWatch - Monitoring and logs
- EventBridge - Event routing
- Amplify - Mobile backend

**Architecture Patterns:**
- Event-driven architecture
- CQRS (Command Query Responsibility Segregation)
- Event sourcing
- Microservices
- API Gateway pattern

---

### 5. Architecture & Design

**Core Concept**: Modern, scalable system design with event-driven patterns

**Documentation:**
- 📄 [Multi-Agent Architecture](docs/architecture/ARCHITECTURE.md)
- 📄 [Backend Architecture](docs/architecture/ActiveLog-Backend-Architecture.txt)

#### Key Architectural Patterns

**1. Microservices Architecture**
- Service decoupling and autonomy
- Independent deployment
- Technology diversity
- Fault isolation

**2. Event-Driven Design**
- Asynchronous communication
- Event buses and pub-sub
- Event sourcing for auditability
- Eventual consistency

**3. CQRS Pattern**
- Separate read and write models
- Optimized query paths
- Scalable writes
- Event-driven updates

**4. Multi-Agent Coordination**
- Hierarchical orchestration
- Distributed state management
- File-based communication
- Git worktree isolation

**5. Serverless Architecture**
- AWS Lambda functions
- Pay-per-use pricing
- Auto-scaling
- Managed services

#### System Components Map

```
┌─────────────────────────────────────────────────┐
│           User Applications Layer                │
│  (Voice Logger, Deckboss, Business Log)         │
└────────────────┬────────────────────────────────┘
                 │
        ┌────────▼────────┐
        │   API Gateway    │
        └────────┬────────┘
                 │
     ┌───────────┴───────────┐
     │                       │
┌────▼──────┐       ┌───────▼────────┐
│  Lambda   │       │   Multi-Agent  │
│ Functions │       │  Orchestrator  │
└────┬──────┘       └───────┬────────┘
     │                      │
     │         ┌────────────┴──────────┐
     │         │                       │
     │    ┌────▼──────┐         ┌─────▼─────┐
     │    │  Worker   │         │  Worker   │
     │    │  Agent 1  │         │  Agent 2  │
     │    └────┬──────┘         └─────┬─────┘
     │         │                      │
  ┌──▼─────────▼──────────────────────▼──┐
  │        Event Bus / Message Queue      │
  └──┬────────┬──────────────┬──────────┬┘
     │        │              │          │
 ┌───▼──┐ ┌──▼───┐  ┌──────▼─────┐ ┌─▼──┐
 │ S3   │ │ Dyna │  │ CloudWatch │ │Git │
 │      │ │ moDB │  │    Logs    │ │    │
 └──────┘ └──────┘  └────────────┘ └────┘
```

---

### 6. Configuration Management

**Entry Points:**
- 📂 [Config Directory](config/)
- 📂 [Multibot Config](projects/multibot/orchestrator-master/config/)

#### Configuration Files by Project

**Multibot:**
- `master_config.yaml` - Master agent settings
- `worker_config_template.yaml` - Worker template
- Environment variables (`.env`)

**AutoCoder:**
- `.env` - API keys and settings
- `goals.json` - Generation goals
- `pyproject.toml` - Python project config

**Logging Apps:**
- `amplify_outputs.json` - AWS Amplify config
- `app.json` - React Native app config
- `package.json` - Dependencies and scripts

**Deployment:**
- `lambda/config.json` - Lambda function config
- AWS credentials (via AWS CLI)

---

### 7. Testing & Quality Assurance

**Entry Points:**
- 📂 [Multibot Tests](projects/multibot/orchestrator-master/tests/)

#### Test Types

| Type | Location | Purpose |
|------|----------|---------|
| Unit Tests | `tests/test_unit.py` | Individual component testing |
| Integration Tests | `tests/test_integration.py` | Component interaction testing |
| End-to-End Tests | `tests/test_e2e.py` | Full workflow testing |
| Stress Tests | `tests/test_stress.py` | Load and performance testing |

#### Running Tests

```bash
# Python projects
pytest
pytest tests/test_unit.py      # Specific test file
pytest -v                       # Verbose output
pytest --cov                    # With coverage

# Node.js projects
npm test
npm run test:watch             # Watch mode
npm run test:coverage          # With coverage
```

---

## Getting Started

### New to the Repository?
1. 📄 Read [README.md](README.md) - Project overview
2. 📄 Follow [SETUP.md](docs/guides/SETUP.md) - Environment setup
3. 📄 Review [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Repository layout
4. 📄 Check [CONTRIBUTING.md](CONTRIBUTING.md) - Development standards

### Want to Deploy Something?
1. **AWS Lambda**: [Deployment Scripts](#aws-deployment)
2. **Multi-Agent System**: [Multibot Setup](projects/multibot/orchestrator-master/INSTALLATION.md)
3. **Mobile Apps**: [Logging Apps Setup](docs/guides/SETUP.md#logging-applications)

### Want to Generate Code?
1. [AutoCoder Documentation](projects/autocoder/autocoder/README.md)
2. [Code Examples](projects/autocoder/autocoder/example/)
3. [Setup Guide](docs/guides/SETUP.md#autocoder)

### Want to Contribute?
1. [Contributing Guidelines](CONTRIBUTING.md)
2. [Code Style Standards](CONTRIBUTING.md#style-guidelines)
3. [PR Process](CONTRIBUTING.md#pull-request-process)

---

## Cross-Reference Index

### By Technology

**Python Projects:**
- Multi-Agent Orchestrator
- AutoCoder
- Lambda Functions
- Business Log App

**TypeScript/JavaScript Projects:**
- Voice Note Logger
- Deckboss Logger
- Web Dashboards

**Go Projects:**
- AutoCoder Examples (Client services)

### By AWS Service

**Lambda:**
- [Deployment Scripts](projects/deployment/activelog-deploy/)
- [Lambda Functions](projects/deployment/activelog-deploy/lambda/)

**Amplify:**
- [Voice Note App](projects/logging-apps/voice-note-logger/voice-note-app/)
- [Deckboss App](projects/logging-apps/voice-note-logger/deckboss-app/)

**DynamoDB:**
- Lambda integration
- Event sourcing

**S3:**
- Audio file storage
- Deployment packages

### By Architectural Pattern

**Event-Driven:**
- Multi-Agent Communication
- Lambda Functions
- Message Queues

**Microservices:**
- AutoCoder Examples
- Logging Services
- Lambda Functions

**CQRS:**
- Multi-Agent State Management
- Event Sourcing

**Clean Architecture:**
- AutoCoder Generated Code
- Structured Project Layout

---

## Troubleshooting Index

### Setup Issues
- [Common Setup Problems](docs/guides/SETUP.md#troubleshooting)
- [Python Module Not Found](docs/guides/SETUP.md#python-module-not-found)
- [Node Modules Issues](docs/guides/SETUP.md#node-modules-issues)
- [AWS Credentials Error](docs/guides/SETUP.md#aws-credentials-error)

### Deployment Issues
- [Lambda Deployment Failures](projects/deployment/activelog-deploy/)
- [Amplify Configuration](projects/logging-apps/)

### Development Issues
- [Git Conflicts](CONTRIBUTING.md#merge-requirements)
- [Test Failures](CONTRIBUTING.md#running-tests)
- [Linting Errors](CONTRIBUTING.md#code-quality-standards)

---

## Documentation Map

```
📚 Documentation Hierarchy
│
├── 📄 README.md (Start here)
│   └── Overview, features, quick start
│
├── 📄 INDEX.md (This file)
│   └── Knowledge tree and navigation
│
├── 📄 PROJECT_STRUCTURE.md
│   └── Detailed folder structure
│
├── 📄 CONTRIBUTING.md
│   └── Development guidelines
│
├── 📁 docs/
│   ├── 📁 architecture/
│   │   ├── ARCHITECTURE.md (Multi-agent design)
│   │   └── ActiveLog-Backend-Architecture.txt
│   │
│   ├── 📁 guides/
│   │   └── SETUP.md (Complete setup guide)
│   │
│   └── 📁 research/
│       └── (Research materials)
│
└── 📁 projects/
    ├── 📁 multibot/
    │   └── 📁 orchestrator-master/
    │       ├── README.md
    │       ├── INSTALLATION.md
    │       ├── COMMUNICATION_PROTOCOL.md
    │       ├── MONITORING_DASHBOARD.md
    │       ├── TASK_ORCHESTRATION.md
    │       ├── WEB_DASHBOARD.md
    │       ├── WORKER_INTELLIGENCE.md
    │       └── WORKER_LIFECYCLE.md
    │
    └── 📁 autocoder/
        └── 📁 autocoder/
            └── README.md
```

---

## Quick Command Reference

### Setup Commands
```bash
# Clone repository
git clone https://github.com/ctothed/SuperInstance.git

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install

# Configure AWS
aws configure
```

### Running Projects
```bash
# Multibot orchestrator
python projects/multibot/orchestrator-master/orchestrator_master.py

# Multibot dashboard
python projects/multibot/orchestrator-master/run_dashboard.py

# AutoCoder
python projects/autocoder/autocoder/main.py

# Voice Note App
cd projects/logging-apps/voice-note-logger/voice-note-app
npm start
```

### Testing
```bash
# Python tests
pytest

# JavaScript tests
npm test
```

### Deployment
```bash
# Lambda deployment (PowerShell)
./activelog-fire.ps1

# Amplify deployment
amplify push
```

---

## Version Information

- **Repository Version**: 1.0
- **Last Updated**: October 2025
- **Python**: 3.9+
- **Node.js**: 18+
- **Supported Platforms**: Linux, macOS, Windows (WSL2)

---

## Support & Resources

- **Main Documentation**: [README.md](README.md)
- **Setup Guide**: [SETUP.md](docs/guides/SETUP.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **GitHub**: [ctothed/SuperInstance](https://github.com/ctothed/SuperInstance)
