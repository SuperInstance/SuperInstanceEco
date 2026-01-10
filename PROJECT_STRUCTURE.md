# SuperInstance Technical Repository - Project Structure

This document provides a comprehensive overview of the repository structure, explaining the purpose and contents of each directory and key files.

## Repository Root

```
ActiveLog-TechnicalRepo/
├── .gitignore                 # Git ignore rules for dependencies, secrets, models
├── README.md                  # Main repository documentation
├── CONTRIBUTING.md            # Contribution guidelines and standards
├── PROJECT_STRUCTURE.md       # This file - repository structure documentation
├── config/                    # Configuration templates and examples
├── docs/                      # Documentation and guides
├── projects/                  # Main project source code
├── research/                  # Research materials and findings
└── scripts/                   # Utility and automation scripts
```

## Directory Structure

### `/projects/` - Main Project Code

All source code and applications are organized under this directory.

```
projects/
├── multibot/                   # Multi-agent orchestration system
├── autocoder/                  # Automated code generation tools
├── logging-apps/               # Logging application suite
├── deployment/                 # Deployment infrastructure and scripts
└── ai-tools/                   # AI and machine learning tools
```

#### `/projects/multibot/` - Multi-Agent Orchestration

```
multibot/
├── .claude/                    # Claude Code configuration
│   └── settings.local.json    # Local Claude settings
├── ARCHITECTURE.md             # High-level multibot architecture
└── orchestrator-master/        # Master orchestrator implementation
    ├── README.md              # Project documentation
    ├── INSTALLATION.md        # Installation guide
    ├── COMMUNICATION_PROTOCOL.md  # Inter-agent communication specs
    ├── MONITORING_DASHBOARD.md    # Dashboard documentation
    ├── TASK_ORCHESTRATION.md      # Task management documentation
    ├── WEB_DASHBOARD.md           # Web interface documentation
    ├── WORKER_INTELLIGENCE.md     # Worker AI capabilities
    ├── WORKER_LIFECYCLE.md        # Worker management docs
    │
    ├── orchestrator_master.py     # Main orchestrator logic
    ├── worker_manager.py          # Worker lifecycle management
    ├── task_queue.py              # Task queue implementation
    ├── message_queue.py           # Message passing system
    ├── communication.py           # Communication protocols
    │
    ├── config.py                  # Configuration management
    ├── config_manager.py          # Advanced config handling
    ├── config_examples.py         # Configuration examples
    ├── config_tools.py            # Config utilities
    │
    ├── memory_management.py       # Worker memory system
    ├── memory_examples.py         # Memory usage examples
    ├── memory_tools.py            # Memory utilities
    │
    ├── merge_coordination.py      # Git merge coordination
    ├── merge_coordination_examples.py  # Merge examples
    ├── merge_coordination_tools.py     # Merge utilities
    │
    ├── shared_knowledge.py        # Shared knowledge base
    ├── shared_knowledge_examples.py    # Knowledge sharing examples
    ├── shared_knowledge_tools.py       # Knowledge utilities
    │
    ├── task_decomposition.py      # Task breakdown logic
    ├── task_orchestration_tools.py     # Orchestration utilities
    ├── task_orchestration_examples.py  # Usage examples
    │
    ├── monitoring_dashboard.py    # Monitoring UI
    ├── monitoring_gui.py          # GUI components
    ├── dashboard_config.py        # Dashboard configuration
    ├── dashboard_integration.py   # Dashboard integrations
    │
    ├── web_dashboard_server.py    # Web dashboard backend
    ├── advanced_web_dashboard.py  # Advanced web features
    ├── run_dashboard.py           # Dashboard launcher
    ├── run_web_dashboard.py       # Web dashboard launcher
    │
    ├── worker_intelligence.py     # Worker AI logic
    ├── worker_lifecycle.py        # Worker state management
    ├── worker_mcp_server.py       # MCP server for workers
    ├── launch_worker.py           # Worker spawning
    │
    ├── repo_manager.py            # Git repository management
    ├── terminal_manager.py        # Terminal window management
    ├── master_communication.py    # Master communication layer
    │
    ├── setup.py                   # Installation script
    ├── setup.sh                   # Shell setup script
    ├── setup_dashboard.py         # Dashboard setup
    ├── setup_examples.py          # Example configurations
    ├── setup_web_dashboard.py     # Web dashboard setup
    │
    ├── requirements.txt           # Python dependencies
    ├── web_requirements.txt       # Web dashboard dependencies
    │
    ├── config/                    # Configuration files
    │   ├── master_config.yaml    # Master agent config
    │   └── worker_config_template.yaml  # Worker template
    │
    └── tests/                     # Test suite
        ├── __init__.py
        ├── conftest.py           # Pytest configuration
        ├── test_unit.py          # Unit tests
        ├── test_integration.py   # Integration tests
        ├── test_e2e.py           # End-to-end tests
        └── test_stress.py        # Stress tests
```

**Key Features:**
- Master-worker orchestration architecture
- File-based inter-agent communication
- Git worktree management
- Real-time monitoring dashboards
- Comprehensive testing suite

#### `/projects/autocoder/` - Automated Code Generation

```
autocoder/
└── autocoder/
    ├── README.md              # Project documentation
    ├── .env.example           # Environment template
    ├── .gitignore             # Autocoder-specific ignores
    ├── main.py                # Entry point
    ├── pyproject.toml         # Python project configuration
    ├── requirements.txt       # Python dependencies
    ├── goals.json             # Generation goals
    ├── agent_prompt.txt       # AI agent instructions
    ├── loop.log               # Execution logs
    │
    ├── autocode/              # Core autocoder package
    │   ├── __init__.py
    │   ├── container.py       # Dependency injection
    │   ├── controller.py      # Controller generation
    │   ├── dashboard.py       # Dashboard creation
    │   ├── database.db        # Local database
    │   ├── datastore.py       # Data layer generation
    │   ├── gateway.py         # API gateway generation
    │   ├── model.py           # Model generation
    │   ├── router.py          # Route generation
    │   ├── setting.py         # Settings management
    │   └── use_case.py        # Use case generation
    │
    ├── benchmark/             # Performance benchmarks
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   ├── requirements.txt
    │   ├── optimization_algorithm.ipynb
    │   ├── optimization_bayesian.ipynb
    │   └── optimization_genetic.ipynb
    │
    ├── example/               # Usage examples
    │   ├── controller.ipynb   # Jupyter examples
    │   ├── controller.py
    │   ├── controller2.py
    │   └── client/            # Client implementations
    │       ├── docker-compose.yml
    │       ├── app_account/   # Account service (Go)
    │       ├── app_gateway/   # Gateway service (Go)
    │       └── app_product/   # Product service (Go)
    │
    └── src/                   # Generated source files
        └── autogen_*.py       # Auto-generated modules
```

**Key Features:**
- Multi-language code generation (Python, Go)
- Clean architecture patterns
- Microservices scaffolding
- Benchmark and optimization tools

#### `/projects/logging-apps/` - Logging Application Suite

```
logging-apps/
├── voice-note-logger/         # Voice recording and logging
│   ├── cd                     # Change directory helper
│   ├── package.json
│   ├── package-lock.json
│   │
│   ├── voice-note-app/        # Main voice note application
│   │   ├── README.md
│   │   ├── .gitignore
│   │   ├── App.js             # Main app component
│   │   ├── index.js           # Entry point
│   │   ├── app.json           # App configuration
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── amplify_outputs.json  # AWS Amplify config
│   │   │
│   │   ├── .expo/             # Expo configuration
│   │   ├── amplify/           # Backend definitions
│   │   │   ├── backend.ts
│   │   │   ├── schema.graphql
│   │   │   └── auth/
│   │   │       └── resource.js
│   │   │
│   │   ├── assets/            # App assets
│   │   │   ├── adaptive-icon.png
│   │   │   ├── favicon.png
│   │   │   ├── icon.png
│   │   │   └── splash-icon.png
│   │   │
│   │   └── src/               # Source code
│   │       ├── amplify_outputs.json
│   │       └── test-voice-note.ts
│   │
│   └── deckboss-app/          # Deckboss logging application
│       ├── README.md
│       ├── .gitignore
│       ├── amplify_outputs.json
│       ├── app.json
│       ├── package.json
│       ├── tsconfig.json
│       ├── codegen.yml
│       ├── eslint.config.js
│       │
│       ├── app/               # App screens and navigation
│       │   ├── _layout.tsx
│       │   ├── +not-found.tsx
│       │   └── (tabs)/
│       │       ├── _layout.tsx
│       │       ├── index.tsx
│       │       └── explore.tsx
│       │
│       ├── assets/            # Images and fonts
│       ├── components/        # React components
│       ├── constants/         # App constants
│       ├── graphql/           # GraphQL queries/mutations
│       ├── hooks/             # Custom React hooks
│       ├── scripts/           # Build scripts
│       └── src/               # Additional source
│
├── deckboss-logger/           # Deckboss logger backend
│   ├── package.json
│   ├── package-lock.json
│   └── amplify/
│       ├── package.json
│       └── package-lock.json
│
└── businesslog-app/           # Business logging application
    ├── 25.2
    ├── interpreter
    ├── commands.txt
    └── autoGUI.py             # GUI automation script
```

**Key Features:**
- Voice recording with transcription
- BLE device integration
- AWS Amplify backend
- React Native / Expo mobile apps
- GraphQL APIs

#### `/projects/deployment/` - Deployment Infrastructure

```
deployment/
└── activelog-deploy/
    ├── activelog-fire.cmd     # Windows deployment script
    ├── activelog-fire.ps1     # PowerShell deployment script
    ├── dm_logger.zip          # Logger package
    ├── firelog-history.txt    # Deployment history
    ├── response.json          # Last deployment response
    │
    └── lambda/                # AWS Lambda functions
        ├── app.py             # Main Lambda handler
        ├── app.pyecho         # Echo test
        ├── config.json        # Lambda configuration
        ├── dm_logger.py       # Logger implementation
        ├── dm_logger.zip      # Packaged Lambda
        ├── requirements.txt   # Python dependencies
        └── response.json      # Lambda response
```

**Key Features:**
- AWS Lambda deployment automation
- PowerShell and CMD scripts
- DynamoDB integration
- Event-driven architecture

### `/docs/` - Documentation

```
docs/
├── architecture/              # Architecture documentation
│   ├── ARCHITECTURE.md       # Multi-agent system architecture
│   └── ActiveLog-Backend-Architecture.txt  # Backend design
│
├── guides/                    # User and developer guides
│   └── SETUP.md              # Comprehensive setup guide
│
└── research/                  # Research materials
    └── (research documents)
```

**Contents:**
- System architecture and design patterns
- Setup and installation guides
- API documentation
- Research papers and findings

### `/config/` - Configuration Templates

```
config/
└── (configuration templates and examples)
```

**Purpose:**
- Shared configuration templates
- Environment-specific configs
- API endpoint configurations

### `/scripts/` - Utility Scripts

```
scripts/
└── (automation and utility scripts)
```

**Purpose:**
- Build automation
- Testing utilities
- Deployment helpers
- Data migration scripts

### `/research/` - Research Materials

```
research/
└── (research documents and technical papers)
```

**Purpose:**
- Technical research
- Algorithm documentation
- Performance studies
- Comparative analysis

## Key File Types

### Python Files (`.py`)
- Application logic and business code
- Test files (`test_*.py`)
- Configuration scripts
- Setup and installation scripts

### JavaScript/TypeScript Files (`.js`, `.ts`, `.tsx`)
- React Native components
- Node.js services
- Frontend logic
- Mobile app screens

### Configuration Files
- `package.json` - Node.js dependencies and scripts
- `requirements.txt` - Python dependencies
- `config.yaml` / `config.json` - Application configuration
- `amplify_outputs.json` - AWS Amplify configuration
- `.env.example` - Environment variable templates

### Documentation Files (`.md`)
- `README.md` - Project documentation
- Architecture and design docs
- Setup and usage guides
- API documentation

## Dependencies and Re-downloadable Content

The following are excluded from the repository (see `.gitignore`):

### Excluded Directories
- `node_modules/` - Node.js packages (reinstall with `npm install`)
- `venv/`, `env/` - Python virtual environments
- `__pycache__/` - Python bytecode cache
- `.git/` - Git metadata (removed from copied projects)
- `models/` - Machine learning models (too large)

### Excluded Files
- `*.pyc`, `*.pyo` - Compiled Python
- `*.log` - Log files
- `.env` - Environment secrets
- `*.db`, `*.sqlite` - Local databases
- `*.key`, `*.pem` - Private keys and certificates

## Restoration Instructions

To restore dependencies after cloning:

### For Node.js Projects
```bash
cd project-directory
npm install
```

### For Python Projects
```bash
cd project-directory
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### For AWS Amplify Projects
```bash
cd project-directory
npm install
amplify pull  # If needed
```

## Repository Statistics

- **Total Projects**: 4 major projects + utilities
- **Languages**: Python, TypeScript/JavaScript, Go
- **Frameworks**: React Native, Expo, FastAPI
- **Cloud Platform**: AWS (Lambda, Amplify, DynamoDB, S3)
- **Documentation Files**: 16+ markdown files
- **Test Coverage**: Unit, integration, and E2E tests

## Getting Started

1. Read the main [README.md](README.md)
2. Follow the [SETUP.md](docs/guides/SETUP.md) guide
3. Review project-specific README files
4. Check [CONTRIBUTING.md](CONTRIBUTING.md) for development standards

## Support

For questions or issues:
- Check project-specific documentation
- Review architecture documents
- Consult setup guides
- Contact the development team
