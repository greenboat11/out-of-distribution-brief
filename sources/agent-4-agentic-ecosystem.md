# Agent 4 — Agentic Ecosystem & Distributed AI: Source List

**This is the priority lane — give it deeper coverage than other lanes (20+ searches if time permits).**

Cover new protocols, infrastructure developments, agentic deployment risks, and the expanding attack surface created by autonomous AI systems.

## Primary focus areas

- MCP (Model Context Protocol): adoption trajectory, security implications, prompt injection via tool results, new vulnerabilities or abuse patterns
- A2A (Agent-to-Agent protocol): federation risks, authentication gaps, early security findings
- Other emerging protocols: OpenAI's Realtime API, ACP, AGNTCY, ANP, agent orchestration frameworks (CrewAI, AutoGen, LangGraph, LlamaIndex)
- Computer use / OS-level agents: attack surfaces when agents control GUIs, exfiltration via clipboard or screen
- Observability tooling (Langfuse, Helicone, Braintrust, OTel agent semantic conventions) and observability failures
- Prompt injection as a network attack vector: injections propagating across tool calls, poisoning agent memory
- Agent memory and persistent state attacks: vector DB corruption, TOCTOU issues
- Malicious agent architectures: adversarial agents exploiting MCP/A2A, authority laundering, permission laundering
- Supply chain attacks on agent tooling: poisoned MCP servers, malicious tool definitions, typosquatting in agent registries
- Agent identity and authentication: NHI (non-human identity) standards, OAuth/OIDC for agents
- Sandboxing and capability restriction: least-privilege architectures for agents, circuit breakers
- Agent-to-agent payment rails and the attack surfaces they open

## Sources to check every run

### Protocol & framework documentation
- Anthropic MCP (modelcontextprotocol.io, github.com/modelcontextprotocol)
- Google A2A (github.com/google/A2A)
- OpenAI platform changelog (platform.openai.com/docs/changelog)
- LangChain blog (blog.langchain.dev)
- AutoGen GitHub (github.com/microsoft/autogen)

### Security research
- Simon Willison's blog (simonwillison.net) — MCP security, prompt injection
- Embrace The Red (embracethered.com) — agentic attack research
- Trail of Bits blog (blog.trailofbits.com)
- PortSwigger Web Security Blog (portswigger.net/research) — for prompt injection
- NCC Group Research (research.nccgroup.com)

### Community & news
- The Register (theregister.com) — infrastructure and protocol news
- Hacker News (news.ycombinator.com) — MCP and agent ecosystem discussions
- GitHub Security Advisories for MCP-related repos

### Academic research
- arXiv: cs.CR, cs.MA (multi-agent systems), cs.AI
- Search terms: "MCP security", "agentic AI security", "prompt injection agent", "multi-agent protocol", "agent orchestration attack", "tool poisoning", "indirect prompt injection", "agent authentication", "non-human identity"
- NeurIPS, ICML, ICLR proceedings for multi-agent systems papers

### Observability & infrastructure
- OTel (opentelemetry.io) — agent semantic conventions updates
- Langfuse (langfuse.com/blog)
- Helicone (helicone.ai/blog)

## Twitter/X accounts to check
- @simonw (Simon Willison — leading voice on LLM/agent security)
- @wunderwuzzi23 (Johann Rehberger — prompt injection and agent attack research)
- @lbeurerkellner (Luca Beurer-Kellner — agentic AI security)
- @anthropicai (MCP announcements)
- @LangChainAI
- @hwchase17 (Harrison Chase — LangChain)

## Key questions
1. New MCP or A2A vulnerabilities, abuse patterns, or security advisories in the last 24h?
2. Prompt injection or context poisoning techniques effective in production agentic systems?
3. Supply chain attacks on agent plugins, MCP servers, or tool registries?
4. New academic research on multi-agent security, cascading failures, or authority laundering?
5. Observability and monitoring developments — are gaps in agent visibility being addressed?
6. Agent identity and authentication standards progress — NHI, OAuth for agents?
