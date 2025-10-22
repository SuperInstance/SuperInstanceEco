# Contributing to SuperInstance Technical Repository

Thank you for your interest in contributing to the SuperInstance project. This document provides guidelines and standards for professional development collaboration.

## Code of Conduct

### Professional Standards

- Be respectful and constructive in all interactions
- Focus on technical merit and project goals
- Provide thoughtful, actionable feedback
- Respect different perspectives and approaches
- Maintain confidentiality of sensitive information

## Getting Started

### Before You Begin

1. **Review Documentation**
   - Read the main [README.md](README.md)
   - Review [SETUP.md](docs/guides/SETUP.md) for environment configuration
   - Study relevant architecture documents in `docs/architecture/`

2. **Set Up Development Environment**
   - Follow setup instructions for the project you're working on
   - Ensure all tests pass before making changes
   - Configure your IDE with project formatting rules

3. **Understand the Architecture**
   - Review the multi-agent orchestration design
   - Understand event-driven patterns
   - Familiarize yourself with the technology stack

## Development Workflow

### 1. Creating Issues

Before starting work, create or find an existing issue:

**Good Issue Example:**
```
Title: Add retry logic to Lambda deployment script

Description:
Current behavior: Lambda deployment fails on network timeout without retry
Expected behavior: Retry up to 3 times with exponential backoff
Impact: Reduces deployment failures in unstable network conditions

Proposed solution:
- Add retry decorator to deployment function
- Implement exponential backoff (1s, 2s, 4s)
- Log each retry attempt
- Fail after 3 attempts with detailed error

Environment: AWS Lambda, Python 3.9
Related files: projects/deployment/activelog-deploy/lambda/app.py
```

### 2. Branching Strategy

We use a feature branch workflow:

```bash
# Create feature branch from main
git checkout main
git pull origin main
git checkout -b feature/descriptive-name

# Or for bug fixes
git checkout -b fix/issue-description

# Or for documentation
git checkout -b docs/what-you-are-documenting
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions/updates
- `chore/` - Maintenance tasks

### 3. Making Changes

#### Code Quality Standards

**Python:**
```bash
# Format code
black your_file.py

# Check linting
flake8 your_file.py

# Type checking
mypy your_file.py

# Run tests
pytest tests/
```

**JavaScript/TypeScript:**
```bash
# Format code
npm run format

# Lint
npm run lint

# Type check
npm run type-check

# Run tests
npm test
```

#### Style Guidelines

**Python:**
- Follow PEP 8
- Use type hints
- Write docstrings for all public functions/classes
- Maximum line length: 100 characters
- Use Black formatting

```python
def process_message(
    message: dict[str, Any],
    timeout: int = 30
) -> ProcessResult:
    """
    Process incoming message with timeout.

    Args:
        message: Message dictionary containing type and payload
        timeout: Maximum processing time in seconds

    Returns:
        ProcessResult with status and optional data

    Raises:
        TimeoutError: If processing exceeds timeout
        ValueError: If message format is invalid
    """
    # Implementation
    pass
```

**JavaScript/TypeScript:**
- Use TypeScript for new code
- Prefer functional components (React)
- Use async/await over promises
- Document with JSDoc or TSDoc

```typescript
/**
 * Uploads voice recording to S3 with metadata
 * @param audioBlob - The audio data to upload
 * @param metadata - Recording metadata (timestamp, location, etc.)
 * @returns Promise with upload result and S3 URL
 * @throws UploadError if upload fails after retries
 */
async function uploadVoiceRecording(
  audioBlob: Blob,
  metadata: RecordingMetadata
): Promise<UploadResult> {
  // Implementation
}
```

### 4. Writing Tests

All new features must include tests:

**Unit Tests:**
```python
# tests/test_orchestrator.py
import pytest
from orchestrator_master import TaskManager

def test_task_decomposition():
    """Test task is correctly decomposed into subtasks."""
    manager = TaskManager()
    task = {
        "description": "Add user authentication",
        "complexity": "high"
    }

    subtasks = manager.decompose_task(task)

    assert len(subtasks) > 1
    assert all(st["complexity"] == "low" for st in subtasks)
```

**Integration Tests:**
```python
# tests/test_integration.py
def test_master_worker_communication(test_workspace):
    """Test master can spawn worker and receive response."""
    master = MasterOrchestrator(workspace=test_workspace)

    # Spawn worker
    worker_id = master.spawn_worker(task="simple-task")

    # Wait for response
    response = master.wait_for_worker(worker_id, timeout=30)

    assert response["status"] == "completed"
    assert "result" in response
```

### 5. Committing Changes

#### Commit Message Format

Use conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting (no code change)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**

```
feat(multibot): add worker health check monitoring

Implement periodic health checks for worker agents to detect
unresponsive workers and trigger automatic restart.

- Add heartbeat mechanism (30s interval)
- Monitor last heartbeat timestamp
- Auto-restart on 3 missed heartbeats
- Log health check events

Closes #123
```

```
fix(lambda): handle DynamoDB throttling errors

Add exponential backoff retry logic for DynamoDB operations
to handle ProvisionedThroughputExceededException.

- Retry up to 3 times
- Exponential backoff: 1s, 2s, 4s
- Log each retry attempt

Fixes #456
```

### 6. Pull Request Process

#### Before Opening PR

1. **Ensure all tests pass**
   ```bash
   pytest
   npm test
   ```

2. **Update documentation**
   - Update README if behavior changed
   - Add/update docstrings
   - Update architecture docs if needed

3. **Rebase on latest main**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

4. **Review your own changes**
   - Read through the diff
   - Remove debug code
   - Check for sensitive information

#### Opening the PR

**PR Template:**

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Changes Made
- Detailed list of changes
- Why each change was necessary

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added and passing
- [ ] No new warnings introduced
- [ ] Related issues linked

## Related Issues
Closes #123
Relates to #456
```

#### PR Review Process

**As Author:**
- Respond to all comments
- Make requested changes promptly
- Mark conversations as resolved when addressed
- Re-request review after changes

**As Reviewer:**
- Review within 2 business days
- Be constructive and specific
- Approve when satisfied
- Request changes if issues found

#### Merge Requirements

- [ ] At least one approval from maintainer
- [ ] All CI checks passing
- [ ] No merge conflicts
- [ ] Documentation updated
- [ ] Tests covering new code

## Project-Specific Guidelines

### Multi-Agent Orchestration System

- Always test with multiple workers
- Verify file-based communication works
- Check for race conditions
- Test recovery scenarios
- Monitor resource usage

### AutoCoder

- Test generated code compiles/runs
- Verify multiple language support
- Check template rendering
- Validate against examples

### Logging Applications

- Test on iOS and Android
- Verify Amplify integration
- Check offline functionality
- Test with real BLE devices (if available)

### Deployment Infrastructure

- Test in sandbox AWS account first
- Verify rollback procedures
- Check IAM permissions
- Monitor CloudWatch logs

## Documentation Standards

### README Files

Each project must have a README with:
- Project description
- Installation instructions
- Usage examples
- Configuration options
- Troubleshooting

### Code Documentation

- All public APIs must be documented
- Include examples in docstrings
- Document edge cases and limitations
- Explain complex algorithms

### Architecture Docs

Update architecture docs when:
- Adding new components
- Changing communication patterns
- Modifying data flows
- Updating deployment strategy

## Security

### Sensitive Information

**Never commit:**
- API keys or credentials
- Private keys or certificates
- Personal identifiable information
- Internal URLs or IPs
- AWS credentials

**Use instead:**
- Environment variables
- AWS Secrets Manager
- Configuration templates
- .env.example files

### Reporting Security Issues

For security vulnerabilities:
1. **Do not** open a public issue
2. Email security concerns privately
3. Include detailed description
4. Provide reproduction steps
5. Allow time for fix before disclosure

## Getting Help

### Resources

- Review existing documentation
- Search closed issues and PRs
- Check architecture diagrams
- Read setup guides

### Asking Questions

When asking for help:
1. Describe what you're trying to do
2. Show what you've tried
3. Include error messages
4. Specify your environment
5. Link to relevant code

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to SuperInstance!
