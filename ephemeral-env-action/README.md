# Ephemeral Environment GitHub Action

A reusable **GitHub Action** that orchestrates the full lifecycle of **ephemeral (preview) environments** for Pull Requests.

This action provisions isolated environments on demand, exposes a unique preview URL, automatically destroys resources when the PR closes, and provides a mocked cost estimate based on uptime. This action provides:

- Spin up preview environments from PR events
- Automatic unique URL per environment
- Automatic teardown and cleanup
- Environment uptime cost estimation
- Docker Compose orchestration
- Traefik dynamic routing
- Reusable across repositories

---

## Project setup

Previous to any interaction please ensure the following:

- Node.js LTS version (24.x)
- NPM LTS version (11.x)

These requirements are fixed into [package.json](./package.json) engine configuration.

This action uses NCC, so it is not recomendable to dockerize the project to have full manage of running environment, instead delegating it to Docker sock.

---

## Architecture Overview

```markdown
┌─────────────────────────────┐
│       GitHub Workflow       │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│          Ephemeral          │
│      Environment Action     │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│         Environment         │
│         Orchestrator        │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│       Docker Compose +      │
│           Traefik           │
└─────────────────────────────┘
```

Repositories only call one action with parameters.

### Workflow

```
PR Event (simulated or real)
          │
          ▼
 GitHub Action Runner
          │
          ▼
 Ephemeral Environment Action
          │
          ├── Create Environment
          ├── Route via Traefik
          ├── Track Uptime
          └── Destroy Environment
```

Each Pull Request gets:

```
http://pr-<number>.localhost
```

Example:

```
http://pr-42.localhost
```

---

## How It Works

### Environment Creation

1. PR opened event received
2. Action executes `docker compose up`
3. Environment labeled for Traefik routing
4. Preview URL generated
5. Start time recorded

---

### Environment Destruction

1. PR closed event received
2. Containers stopped and removed
3. Volumes cleaned
4. Uptime calculated
5. Cost estimate printed

---

## Example Usage

```yaml
name: Preview Environment

on:
  repository_dispatch:
    types: [preview]

jobs:
  preview:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: your-org/ephemeral-environment-action@v1
        with:
          action: ${{ github.event.client_payload.action }}
          pr-number: ${{ github.event.client_payload.pr }}
```

---

## Inputs

| Input       | Description                                      |
| ----------- | ------------------------------------------------ |
| `action`    | `up` or `down`                                   |
| `pr-number` | Pull Request identifier                          |
| `app-path`  | Application directory (Optional. Default to `.`) |

---

## Outputs

| Output        | Description                       |
| ------------- | --------------------------------- |
| `preview-url` | Generated preview environment URL |

---

## Simulating PR Events

### Create Preview Environment

```bash
curl -X POST \
  https://api.github.com/repos/<org>/<repo>/dispatches \
  -d '{
    "event_type": "preview",
    "client_payload": {
      "action": "up",
      "pr": "42"
    }
  }'
```

---

### Destroy Preview Environment

```bash
curl -X POST \
  https://api.github.com/repos/<org>/<repo>/dispatches \
  -d '{
    "event_type": "preview",
    "client_payload": {
      "action": "down",
      "pr": "42"
    }
  }'
```

---

## Cost Estimation

A mocked pricing model estimates runtime cost:

```
Cost = uptime_minutes × rate
```

Default rate:

```
$0.002 / minute
```
More info at [Github actions pricing refence](https://docs.github.com/en/billing/reference/actions-runner-pricing)

Example output:

```
Preview Cost Report
PR: 42
Uptime: 18 minutes
Estimated Cost: $0.036
```

---

## 🛠 Development

### Install Dependencies

```bash
npm install
```

### Build Action

```bash
npm run build
```

Or execute the following to exec build/lint processes

```bash
npm run all
```

This performs:

1. TypeScript compilation
2. NCC bundling into a single executable action

Output:

```
dist/index.js
```

This file is required for action utilization.

---

### Lint

```bash
npm run lint
```

---

## Technology Stack

- **TypeScript**
- **GitHub Actions Toolkit**
- **Docker Compose**
- **Traefik**
- **@vercel/ncc**
- **ESLint (Flat Config)**

---

## Possible Next Steps

- Kubernetes namespace backend
- TTL auto-cleanup controller
- Preview database cloning
- PR comment integration
- Resource quotas
- Real cloud cost APIs
- Git SHA image tagging

> **Important!**
>> A better option for this implementation can be mounting an ephemeral environment on an external instance with more robust infrastructure instead an integral mount in GitHub Actions (e.g. EC2 instance or EKS node), but this is not suitable at all for a local and easily reproducible implementation and can generate real costs.
