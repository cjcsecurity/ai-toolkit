# Tool catalog

**69 reviewed tools and collections**, grouped by their main use. Categories are navigation aids; many tools span several areas. Each tool page includes requirements, setup alternatives, skill counts, and links to its exact upstream source revision.

Catalog membership does not imply downloaded source or a configured runtime. Global recommendations are optional adoption choices, never automatic installation.

## Engineering and code intelligence

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [agent-skills](tools/agent-skills.md) | skill-bundle | 25 | Twenty-five engineering skills and lifecycle commands covering requirements, implementation, testing, review, UI, APIs, performance and shipping. |
| [ast-grep](tools/ast-grep.md) | cli | 0 | Tree-sitter based structural code search, YAML lint rules and AST-aware rewrites, with Rust CLI and Node.js/Python programmatic bindings. |
| [codebase-memory-mcp](tools/codebase-memory-mcp.md) | mcp | 0 | Native local code knowledge-graph indexer with structural/semantic search, call tracing, architecture and change-impact queries through MCP or one-shot CLI. |
| [context7](tools/context7.md) | cli | 9 | Context7 CLI, MCP server, SDKs and agent skills retrieve version-specific library documentation and code snippets from the hosted Context7 index. |
| [ecc](tools/ecc.md) | skill-bundle | 293 | Cross-agent engineering collection with 293 canonical skills for language and framework patterns, reviews, LLM pipelines, evaluation and agent memory; optional ECC CLI, hooks, rules and client adapters have a separate integration footprint. |
| [gh-aw](tools/gh-aw.md) | cli | 5 | GitHub CLI extension for defining AI repository automation in Markdown and compiling it to GitHub Actions with scoped permissions and validated safe outputs. |
| [loop-engineering](tools/loop-engineering.md) | reference | 40 | Patterns, templates, skills and a Node CLI for recurring repository triage, PR maintenance and verification loops. |
| [matt-pocock-skills](tools/matt-pocock-skills.md) | skill-bundle | 31 | Engineering and productivity skills for domain glossaries, architecture decisions, requirements interviews, specifications, ticket planning, TDD, debugging, reviews, teaching and writing agent instructions. |
| [open-code-review](tools/open-code-review.md) | cli | 2 | Go-based code review CLI combining deterministic Git diff selection, file grouping and review rules with model-backed line-level findings, full-file scans and host-agent delegation without a separate OCR LLM endpoint. |
| [ponytail](tools/ponytail.md) | skill-bundle | 6 | Coding simplification skills for reuse-first implementation, over-engineering review, repository audits and deferred-shortcut tracking, with optional multi-agent-host plugins, lifecycle hooks and an MCP instruction server. |
| [serena](tools/serena.md) | mcp | 0 | MCP coding toolkit with language-server-backed symbol lookup, reference navigation, semantic editing, refactoring and project memories. |
| [rea](tools/rea.md) | cli + mcp + skill | 1 | CLI, MCP server and investigation skill for evidence-based analysis of native binaries, Electron/JavaScript applications, .NET assemblies and websites. |
| [e2e](tools/e2e.md) | framework + cli + skill | 1 | TypeScript end-to-end test runner combining natural-language agent actions with deterministic assertions for web and mobile applications. |

## Design and interfaces

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [animate-ui](tools/animate-ui.md) | reference | 0 | React/TypeScript/Tailwind/Motion animated component source and shadcn-compatible registry, with documentation and optional shadcn Registry MCP setup. |
| [archify](tools/archify.md) | skill-bundle | 1 | Diagram-authoring skill and Node.js renderer producing validated standalone interactive HTML/SVG for architecture, workflows, sequences, data flow and lifecycles from typed JSON, with repository evidence and image/video exports. |
| [awesome-claude-design](tools/awesome-claude-design.md) | reference | 0 | Curated reference directory linking brand design-system DESIGN.md documents and prototypes for use in design prompts. |
| [huashu-design](tools/huashu-design.md) | skill-bundle | 1 | Chinese-language design skill for HTML prototypes, slide decks, animation, data visualization, critique, and local PDF/PPTX/video export, with bundled templates and scripts. |
| [impeccable](tools/impeccable.md) | skill-bundle | 20 | One frontend design router skill with 24 commands, detailed UX and visual design references, optional live browser workflows, and a deterministic design detector engine. |
| [open-design](tools/open-design.md) | application | 338 | Local design studio and daemon for prototypes, decks, images, videos, design systems, plugin catalogs, and integration with coding-agent CLIs; includes a stdio MCP interface. |
| [taste-skill](tools/taste-skill.md) | skill-bundle | 13 | Portable frontend design and redesign guidance, including experimental v2 taste, minimalist, brutalist, image-to-code, and image-generation reference workflows. |
| [photocraft](tools/photocraft.md) | desktop application + cli + mcp | 0 | Rust image editor with layered PSD workflows, masks, adjustments and automation through a headless CLI, MCP server and authenticated desktop control channel. |
| [text-to-cad](tools/text-to-cad.md) | skills + plugin + cli + mcp | 12 | Agent skills and local cadgen runtime for parametric CAD, STEP/STL/GLB/3MF exports, engineering drawings, manufacturing checks and robot descriptions. |

## Browsers, research, and web data

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [agent-reach](tools/agent-reach.md) | cli | 1 | CLI and skill that select, configure, and check upstream tools for web pages, video transcripts, RSS, GitHub, search, and social-platform research. |
| [autocli](tools/autocli.md) | cli | 0 | Rust CLI offering declarative website adapters, authenticated browser-session reuse, public API retrieval and external CLI passthrough. |
| [browser-harness](tools/browser-harness.md) | cli | 1 | CLI, agent skill, and optional stdio MCP server for controlling a real Chrome browser over CDP, with reusable local helper functions. |
| [chrome-devtools-mcp](tools/chrome-devtools-mcp.md) | mcp | 7 | Chrome automation and debugging MCP server plus CLI for DOM/browser interaction, screenshots, network/console inspection and performance traces. |
| [cloakbrowser](tools/cloakbrowser.md) | cli | 0 | Python/JavaScript wrappers and CLI around a separately downloaded patched Chromium browser, compatible with Playwright/Puppeteer workflows and persistent profiles. |
| [crucix](tools/crucix.md) | application | 0 | Local OSINT dashboard and data-collection application aggregating geopolitical, economic, environmental, transport, and market sources, with optional LLM analysis and messaging bots. |
| [firecrawl](tools/firecrawl.md) | application | 5 | Web-data API and SDKs for search, URL scraping, crawling, mapping, browser interactions, and structured extraction; includes self-hosted server source and agent skills. |
| [opencli](tools/opencli.md) | cli | 6 | TypeScript CLI with website/Electron adapters and browser primitives using a Chrome extension and local bridge daemon. |
| [playwright](tools/playwright.md) | framework | 3 | Browser automation and end-to-end tests across Chromium, Firefox and WebKit, with locators, web-first assertions, screenshots, network mocking, tracing and production CLI/trace/component-testing skills. |
| [public-apis](tools/public-apis.md) | reference | 0 | Curated catalog of public APIs organized by topic, with descriptions and authentication, HTTPS, and CORS information. |
| [free-for-dev](tools/free-for-dev.md) | reference | 0 | Find free hosting platforms for web apps, static websites and React/Vite projects. Compare free tiers for hosting, databases, authentication, storage, email, monitoring, CI/CD, APIs and cloud services. Community-maintained reference includes Cloudflare Pages, Netlify and Vercel; verify current official provider limits before choosing. |
| [scrapling](tools/scrapling.md) | cli | 1 | Python HTML parser, HTTP/browser fetchers, adaptive selectors, spider framework, scraping CLI, and optional MCP server. |
| [moli](tools/moli.md) | cli + skills | 3 | Rust headless browser for JavaScript-rendered page extraction, web search and automation through CLI, CDP and WebDriver, with optional layout and screenshots. |

## Security and assessment

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [agentic-bug-hunter](tools/agentic-bug-hunter.md) | cli | 16 | Bug-bounty CLI, skill collection, and agent integrations for reconnaissance, vulnerability investigation, finding validation, and report generation. |
| [anthropic-cybersecurity-skills](tools/anthropic-cybersecurity-skills.md) | skill-bundle | 818 | Independent community collection of 818 structured skills spanning defensive security, incident response, forensics, cloud security, and authorized offensive testing. |
| [cyberstrike](tools/cyberstrike.md) | application | 7,689 | AI security-assessment harness with terminal/web interfaces, specialized agents, a large on-demand skill collection including CIS/NIST/MITRE controls, integrated browser testing, and optional remote/MCP tools. |
| [hackingtool](tools/hackingtool.md) | cli | 0 | Python security-tool catalog, installer and launcher with category/tag search, optional AI recommendations and guided workflows; includes a documented catalog of 215 active tools across 21 categories. |
| [hexstrike-ai](tools/hexstrike-ai.md) | mcp | 0 | Python API service and MCP bridge that expose external reconnaissance, web-security, binary-analysis, forensics, and cloud-security tools to AI clients. |
| [pentagi](tools/pentagi.md) | application | 0 | Containerized autonomous penetration-testing application with agent workflows, security tools, browser/search integrations, persistent memory, reports, and a web UI. |
| [security-audit-skill](tools/security-audit-skill.md) | skill-bundle | 1 | Source-first security audit guidance with trust-boundary analysis, coverage-led hunting, independent finding verification, structured verdicts and machine-readable audit reports. |
| [semgrep](tools/semgrep.md) | cli | 0 | Local multi-language static analysis with code-like rules, bug/security searches, custom YAML rules and CI scanning; optional bundled MCP server integrates findings with coding agents. |
| [shannon](tools/shannon.md) | application | 0 | Autonomous security-testing application that analyzes source-available web applications/APIs and attempts exploit validation in containerized worker sessions. |
| [skillspector](tools/skillspector.md) | cli | 1 | Static and optional LLM-based scanner for agent skill bundles, with vulnerability-pattern analysis, dependency checks and JSON/SARIF reports. |
| [strix](tools/strix.md) | application | 9 | AI application-security assessment CLI and agent skills for source, web and API testing, remediation and CI workflows, with Docker sandboxes, model-provider configuration and separate managed-cloud integrations. |

## AI infrastructure and retrieval

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [agentmemory](tools/agentmemory.md) | application | 17 | Persistent agent memory service using the iii engine, BM25/optional embeddings, knowledge graphs, MCP/REST APIs, native skills and agent lifecycle integrations. |
| [arcbox](tools/arcbox.md) | application | 0 | Rust container and virtual-machine runtime for macOS with Docker compatibility, Kubernetes, Linux/macOS guests and disposable agent sandboxes. |
| [docling](tools/docling.md) | framework | 1 | Local document conversion and extraction for PDF, Office files, HTML, images and audio into Markdown or structured DoclingDocument JSON, with OCR, tables and RAG chunking. |
| [langfuse](tools/langfuse.md) | application | 0 | Self-hosted LLM observability, tracing, prompt management, evaluation datasets and experiments platform. |
| [laya](tools/laya.md) | mcp | 0 | Local non-autoregressive decision model SDK and CLI for typed choices, scores, triage, routing, and moderation, with optional HTTP and stdio MCP servers. |
| [litellm](tools/litellm.md) | framework | 0 | Unified OpenAI-compatible Python SDK and self-hosted AI gateway for multiple LLM providers with routing, budgets, virtual keys, guardrails and spend tracking. |
| [opensandbox](tools/opensandbox.md) | framework | 1 | Self-hosted isolated execution environments for AI agents, code, files, browsers and desktops with Docker/Kubernetes runtimes, SDKs, CLI and MCP. |
| [promptfoo](tools/promptfoo.md) | cli | 4 | CLI/library for LLM prompt and agent evaluations, model comparisons, assertions, CI gates, authorized red teaming and optional MCP evaluation tools; includes four production setup/run skills. |
| [rag-anything](tools/rag-anything.md) | application | 0 | Python framework built on LightRAG for parsing and indexing documents, images, tables, equations, audio, and video for multimodal retrieval and question answering. |
| [ruflo](tools/ruflo.md) | application | 373 | Agent orchestration meta-harness with CLI/MCP, agent teams, workflow plugins, memory, hooks and background coordination. |

## Finance and markets

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [finance-skills](tools/finance-skills.md) | skill-bundle | 26 | Agent Skills for market data, company valuation, earnings, options, stock research, read-only social research, startup analysis, and optional external market-data providers. |
| [financial-services](tools/financial-services.md) | skill-bundle | 112 | Claude financial-services plugin marketplace containing financial modeling, banking, equity research, private-equity, fund-admin, operations, and advisor workflows plus data connectors. |
| [openalice](tools/openalice.md) | application | 15 | Local trading-research orchestrator with agent workspaces, market tools, recurring research, inbox, quantitative projects, and optional broker integration. |

## Writing, video, and audio

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [brag](tools/brag.md) | skill-bundle | 2 | Agent skills that turn a project or website into a short launch video with motion, music and share copy; classic Brag uses Hyperframes and the slim variant uses available local rendering tools. |
| [humanizer](tools/humanizer.md) | skill-bundle | 1 | Prose editing skill that removes common AI writing patterns, matches an author voice, and preserves facts, citations and non-prose file content. |
| [hyperframes](tools/hyperframes.md) | cli | 40 | HTML/CSS/media video framework with seekable animations, deterministic MP4 rendering, a preview CLI, reusable blocks, and task-specific agent skills. |
| [hypit](tools/hypit.md) | application | 1 | Agent-oriented video creation system with SVML compositions, captions, reusable assets, local rendering and optional generation/model services. |
| [pixelle-video](tools/pixelle-video.md) | application | 0 | Python/Streamlit short-video creation platform combining LLM scripts, image/video workflows, speech, templates, background music, and FFmpeg composition. |
| [recordly](tools/recordly.md) | application | 0 | Electron desktop screen recorder and editor with automatic zooms, cursor effects, webcam overlays, timeline editing, and video/GIF export. |
| [voicestudio](tools/voicestudio.md) | application | 2 | Local speech studio with Electron desktop, voice cloning and design, transcription, dubbing, audiobooks, a REST API and an optional MCP connection to its running backend. |
| [filmcraft](tools/filmcraft.md) | desktop application + cli + mcp | 0 | Rust non-linear video editor with timeline editing, color grading, audio mixing, captions and export, exposed through desktop, CLI and MCP interfaces. |
| [openmontage](tools/openmontage.md) | agent workflow + tool library | 90 | Agent-directed video production workspace with staged pipelines, provider routing, production knowledge, rendering tools and a local storyboard dashboard. |

## Games and modding

| Tool | Type | Skills | Purpose |
| --- | --- | ---: | --- |
| [universal-modder](tools/universal-modder.md) | cli-and-skill-bundle | 10 | Game-modding skills and Python CLI for engine recon, reverse engineering, sprite and 3D-to-sprite pipelines, Windows capture, video editing, packaging checks and shared field notes. |
