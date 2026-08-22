# Agent 2 — AI-Enabled Offensive Security & SOC Pressure: Source List

Cover how AI is being weaponized for offense, new attack techniques involving LLMs, and the operational stress this puts on defenders.

## Primary focus areas

- Agentic AI used for offense (automated recon, exploitation, lateral movement)
- New malware or attack tooling that leverages LLMs
- Adversarial ML attacks: new techniques, evasion, model inversion, membership inference
- Prompt injection research — indirect injection via tool use, data exfiltration through agents
- Supply chain attacks on model weights, HuggingFace repositories, AI/ML packages
- Dataset poisoning, sleeper agents, RAG poisoning
- SOC operational stress: vuln discovery backlogs, alert fatigue under AI-amplified discovery, TTE/TTD/TTR trends
- AI-augmented defender tooling and its failure modes

## Sources to check every run

### Threat intelligence & security research
- The Record by Recorded Future (therecord.media)
- CISA advisories (cisa.gov/news-events/cybersecurity-advisories)
- NIST NVD (nvd.nist.gov) — new CVEs in AI/ML frameworks
- Krebs on Security (krebsonsecurity.com)
- Schneier on Security (schneier.com)
- 404 Media (404media.co)

### Vendor threat intel (use for leads, verify with primaries)
- CrowdStrike blog (crowdstrike.com/blog/)
- Mandiant / Google Threat Intelligence (cloud.google.com/blog/topics/threat-intelligence)
- Microsoft Threat Intelligence (microsoft.com/security/blog/)
- Palo Alto Unit 42 (unit42.paloaltonetworks.com)
- Secureworks (secureworks.com/research)

### Academic & conference research
- arXiv: cs.CR (cryptography and security), cs.LG (for adversarial ML)
- USENIX Security proceedings (usenix.org/conferences/byname/108)
- IEEE S&P (IEEE Security & Privacy)
- ACM CCS
- Black Hat and DEF CON published materials

### AI-specific security research
- Simon Willison's blog (simonwillison.net) — prompt injection, LLM security
- LLM Security (llmsecurity.net)
- Embrace The Red (embracethered.com) — prompt injection research

### HuggingFace & supply chain
- HuggingFace blog (huggingface.co/blog)
- PyPI security advisories
- GitHub Security Lab (securitylab.github.com)

## Twitter/X accounts to check
- @simonw (Simon Willison — LLM security, prompt injection, practical agentic AI)
- @schneierblog (Bruce Schneier — cybersecurity policy, AI security)
- @random_walker (Arvind Narayanan — AI hype criticism, security)
- @taviso (Tavis Ormandy — Google Project Zero, vuln research)
- @thegrugq (operational security, threat intelligence)
- @MalwareTechBlog (malware analysis, threat intelligence)

## Key questions
1. Any new LLM-enabled attack tooling or malware observed in the wild?
2. New prompt injection techniques or documented exploitation chains?
3. Supply chain incidents involving AI/ML packages or model weights?
4. Evidence that AI is compressing time-to-exploit for newly disclosed CVEs?
5. SOC tooling announcements — are AI defensive tools keeping pace with offensive use?
