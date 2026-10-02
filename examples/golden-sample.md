# Golden Sample: Disney Architect Execution

Use this exact input-to-output pattern as a few-shot reference when processing any user request.

---

## 1. User Input
> "Build a lightweight CLI tool in Rust that monitors disk usage and sends an alert when available space drops below 10%."

---

## 2. Stage 1: The Dreamer Output
```xml
<DREAMER_STAGE>
### 1. Core Value Proposition
Zero-latency, battery-friendly terminal sentry that predicts storage exhaustion before emergency kernel out-of-space crashes occur.

### 2. The 3 Killer Differentiators
- **Predictive Burn-Rate Telemetry**: Calculates GB consumed per hour and projects exact hours until disk failure.
- **Panic Mitigation Hook**: Automatically triggers a user-defined shell command (e.g. `docker system prune` or log truncate) upon threshold breach.
- **Terminal Micro-Sparkline**: Renders an ASCII mini-graph of 24-hour disk consumption directly inside terminal notifications.

### 3. The Ideal User Journey
1. User installs via single curl/cargo binary: `sentry watch --threshold 10%`.
2. Tool prints a sleek, silent daemon acknowledgment and detaches into the background.
3. System disk hits 9% `→` Sentry fires an OS desktop notification with sparkline + prompt to auto-clean cache.

### 4. Aesthetic & Sensory Tone
Ultra-clean Unix ergonomics. High-contrast terminal output, silent when healthy, bold and unambiguous when alerting.
</DREAMER_STAGE>
```

---

## 3. Stage 2: The Realist Output
```xml
<REALIST_STAGE>
### 1. Archetype & Language Selection
- **Domain Archetype**: CLI & Systems Utility
- **Target Language & Runtime**: Rust (Edition 2021)
- **Build Tool**: Cargo

### 2. Scope Pruning Matrix
| Dreamer Feature | MVP Status | Technical Justification |
| :--- | :--- | :--- |
| Core threshold monitor | `IN_SCOPE` | Essential functional requirement |
| Panic Mitigation Hook | `IN_SCOPE` | Simple `std::process::Command` execution |
| Predictive Burn-Rate (ML) | `DEFERRED_V2` | High memory footprint; replace with simple linear delta in MVP |
| ASCII Micro-Sparkline | `DEFERRED_V2` | Terminal rendering bloat; stick to standard tabular output in MVP |

### 3. Core Technical Specifications
- **CLI Commands**:
  - `sentry run --path <PATH> --threshold <PERCENT> [--hook <COMMAND>]`
- **Dependencies (`Cargo.toml`)**:
  - `clap = { version = "4.4", features = ["derive"] }`
  - `sysinfo = "0.30"`
  - `notify-rust = "4.10"`

### 4. Physical Project Directory Tree
```text
disk-sentry/
├── Cargo.toml
├── README.md
└── src/
    ├── main.rs
    ├── monitor.rs
    └── alert.rs
```
</REALIST_STAGE>
```

---

## 4. Stage 3: The Critic Output
```xml
<CRITIC_STAGE>
### 1. Domain Audit Findings
| Severity | Subsystem | Failure Vector / Vulnerability | Concrete Remediation |
| :--- | :--- | :--- | :--- |
| High | `alert.rs` | Shell injection via unescaped string in `--hook` execution | Use `std::process::Command::new` with explicit arg arrays instead of `sh -c` |
| Med | `monitor.rs` | Infinite blocking if queried mount path is an unresponsive NFS drive | Set timeout flag on filesystem stat calls |
| Low | `main.rs` | Missing graceful shutdown on `Ctrl+C` | Register `tokio::signal::ctrl_c()` or `ctrlc` crate handler |

### 2. Dimension Scores
- **Safety/Security**: 88/100 (Clean memory safety, shell injection risk remediated)
- **Feasibility**: 95/100 (Single binary, minimal dependencies)
- **Simplicity**: 90/100 (Standard idiomatic Rust, zero runtime daemons)
- **Composite Score**: **91 / 100**

### 3. Final Verdict
- **Status**: `APPROVED`
- **Scaffold Authorization**: Granted. Proceed directly to code generation.
</CRITIC_STAGE>
```
