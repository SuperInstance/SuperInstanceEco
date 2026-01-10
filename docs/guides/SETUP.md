# Setup Guide - SuperInstance Technical Repository

This guide walks you through setting up the development environment for all projects in this repository.

## System Requirements

### Minimum Requirements
- **OS**: Linux, macOS, or Windows with WSL2
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 10GB free space
- **Internet**: Stable connection for dependency downloads

### Required Software

1. **Git** (2.30+)
   ```bash
   git --version
   ```

2. **Node.js** (18+) and npm/yarn
   ```bash
   node --version  # Should be v18 or higher
   npm --version
   ```

3. **Python** (3.9+)
   ```bash
   python --version  # Should be 3.9 or higher
   pip --version
   ```

4. **AWS CLI** (Optional, for deployment projects)
   ```bash
   aws --version
   ```

5. **Docker** (Optional, for containerization)
   ```bash
   docker --version
   ```

## Project-Specific Setup

### 1. Multi-Agent Orchestration System

**Location**: `projects/multibot/orchestrator-master/`

#### Setup Steps

1. Navigate to the project directory:
   ```bash
   cd projects/multibot/orchestrator-master
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the system:
   ```bash
   cp config/worker_config_template.yaml config/worker_config.yaml
   # Edit config files as needed
   ```

5. Run setup script:
   ```bash
   python setup.py
   # OR
   bash setup.sh
   ```

#### Configuration

Edit `config/master_config.yaml` to set:
- Worker pool size
- GitHub credentials (for MCP)
- Shared filesystem paths
- Terminal management settings

#### Running the System

```bash
# Start the master orchestrator
python orchestrator_master.py

# Run the monitoring dashboard
python run_dashboard.py

# Run the web dashboard
python run_web_dashboard.py
```

### 2. AutoCoder

**Location**: `projects/autocoder/autocoder/`

#### Setup Steps

1. Navigate to the project directory:
   ```bash
   cd projects/autocoder/autocoder
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and settings
   ```

4. Run the autocoder:
   ```bash
   python main.py
   ```

#### Optional: Go Examples

To run the Go client examples:

```bash
cd example/client/app_account
go mod download
go run main.go
```

### 3. Logging Applications

#### Voice Note Logger

**Location**: `projects/logging-apps/voice-note-logger/voice-note-app/`

1. Navigate to the project:
   ```bash
   cd projects/logging-apps/voice-note-logger/voice-note-app
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Configure Amplify:
   ```bash
   # Ensure amplify_outputs.json exists
   # If not, initialize Amplify:
   amplify init
   amplify push
   ```

4. Run the app:
   ```bash
   # For web
   npm run web

   # For iOS (requires macOS and Xcode)
   npm run ios

   # For Android (requires Android Studio)
   npm run android
   ```

#### Deckboss Logger

**Location**: `projects/logging-apps/voice-note-logger/deckboss-app/`

Similar setup to Voice Note Logger:

```bash
cd projects/logging-apps/voice-note-logger/deckboss-app
npm install
npm run web  # or ios/android
```

#### Business Log App

**Location**: `projects/logging-apps/businesslog-app/`

1. Navigate to the project:
   ```bash
   cd projects/logging-apps/businesslog-app
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt  # if requirements.txt exists
   ```

3. Run the application:
   ```bash
   python autoGUI.py
   ```

### 4. Deployment Infrastructure

**Location**: `projects/deployment/activelog-deploy/`

#### Prerequisites

- AWS CLI configured with credentials
- Appropriate IAM permissions
- Lambda deployment package prepared

#### Setup Steps

1. Navigate to the lambda directory:
   ```bash
   cd projects/deployment/activelog-deploy/lambda
   ```

2. Install Lambda dependencies:
   ```bash
   pip install -r requirements.txt -t .
   ```

3. Configure the Lambda function:
   ```bash
   # Edit config.json with your settings
   vim config.json
   ```

4. Deploy using provided scripts:
   ```bash
   # Windows PowerShell
   ..\activelog-fire.ps1

   # Windows CMD
   ..\activelog-fire.cmd
   ```

#### AWS Configuration

Ensure your AWS credentials are configured:

```bash
aws configure
```

Required IAM permissions:
- Lambda function creation/update
- DynamoDB table access
- S3 bucket access
- CloudWatch Logs

## Common Development Tasks

### Running Tests

For Python projects:
```bash
pytest
# or
python -m pytest tests/
```

For Node.js projects:
```bash
npm test
# or
yarn test
```

### Linting and Formatting

Python:
```bash
black .
flake8 .
mypy .
```

JavaScript/TypeScript:
```bash
npm run lint
npm run format
```

### Building for Production

Multibot:
```bash
# No build step required for Python
```

AutoCoder:
```bash
# Build package
python -m build
```

Logging Apps:
```bash
# Build optimized version
npm run build
# or for mobile
eas build --platform ios  # Requires Expo account
```

## Troubleshooting

### Common Issues

#### 1. Python Module Not Found

**Error**: `ModuleNotFoundError: No module named 'xxx'`

**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### 2. Node Modules Issues

**Error**: Various npm/yarn errors

**Solution**:
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

#### 3. AWS Credentials Error

**Error**: `Unable to locate credentials`

**Solution**:
```bash
# Configure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

#### 4. Permission Denied (Scripts)

**Error**: `Permission denied` when running scripts

**Solution**:
```bash
# Make script executable
chmod +x script_name.sh

# Or run with explicit interpreter
bash script_name.sh
python script_name.py
```

### Getting Help

1. Check project-specific README files
2. Review architecture documentation in `docs/architecture/`
3. Search for similar issues in project history
4. Create a detailed issue report with:
   - Error message
   - Steps to reproduce
   - Environment details (OS, versions, etc.)

## Environment Variables

### Multibot

Create `.env` file in `projects/multibot/orchestrator-master/`:

```env
GITHUB_TOKEN=your_github_token
WORKSPACE_PATH=/path/to/workspace
LOG_LEVEL=INFO
```

### AutoCoder

Create `.env` file in `projects/autocoder/autocoder/`:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
MODEL=gpt-4
```

### Logging Apps

Amplify handles most configuration through `amplify_outputs.json`, but you may need:

```env
REACT_APP_API_ENDPOINT=https://your-api.com
REACT_APP_REGION=us-east-1
```

## Next Steps

After completing setup:

1. Review the main [README.md](../../README.md)
2. Explore the [Architecture Documentation](../architecture/)
3. Try running example projects
4. Review [CONTRIBUTING.md](../../CONTRIBUTING.md) if you plan to contribute

## Support

For setup issues or questions:
- Check project documentation
- Review troubleshooting section
- Contact the development team
