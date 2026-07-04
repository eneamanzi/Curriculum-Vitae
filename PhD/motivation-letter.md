# Motivation Letter — Intersectoral Innovation PhD (v15)

> **Nota:** Codice tabella Modello 1: **2**. Lunghezza: 6525 caratteri (+57% vs Luzzara, ~4150 caratteri). 8 paragrafi (P3 e il vecchio P4 sono ora fusi in un solo paragrafo).
> Controlli superati: grammatica, ortografia (britannico coerente), riferimenti pronominali, conformità ai 4 punti del bando.
> Le intestazioni `##` sotto sono solo per tua navigazione — NON vanno nel Modello 1, solo il testo in prosa.

**Legenda:**
- **Grassetto** = termini che riecheggiano il testo ufficiale del bando/proposta TIM (verificati uno per uno contro il testo esatto)
- *Corsivo* = vocabolario tecnico della letteratura, richiesto esplicitamente da Anisetti (guardrails, constrained decoding, ecc.)

---

## P1 — Apertura

*(348 caratteri)*

My name is Enea Manzi, and I am writing to express my strong motivation to join the "Intersectoral Innovation" industrial PhD programme, with reference to Research Theme 2, "Trusted Agentic Generative AI for Intent-Driven Deployment, Observability and Troubleshooting in Telco Edge–Cloud Continuum Systems", developed in collaboration with TIM S.p.A.

## P2 — Background: le 4 aree indicate da Anisetti (punto 1)

*(1900 caratteri)*

Network operations in a Telco context are **mission-critical**, and any automated decision has to be **reliable, verifiable, explainable, and compliant** with policies and constraints, an area where current systems still lack robust mechanisms for **trustworthiness, grounding, evaluation, and governance**. Across both my Bachelor's and Master's theses at the SESAR Lab, I have worked on different pieces of that same problem. My Bachelor's thesis laid the groundwork, evaluating distributed systems against evidence-based contracts rather than direct inspection. It is also where I engaged, more tangentially, with **intent-driven, non-functional-property deployment**, formalising contracts to jointly evaluate reliability, scalability and performance on a Kubernetes testbed. The same thesis is built around **observability** too, the triad of logs, traces and metrics and the architectural choices behind collecting them at scale, and around **Edge-Cloud Continuum** architectures, the paradigm whose heterogeneity and geographic distribution make monitoring genuinely hard to get right, a background I later put to further, more hands-on use building a cloud-native microservices infrastructure on Kubernetes with Kafka and Kong. My Master's thesis then took **trust** as its central concern: an automated tool that evaluates REST APIs through specified oracles, criteria declared in advance from the domain knowledge of each control, so that a verdict on whether a behaviour violates a guarantee is reached without ad-hoc judgement, orchestrated deterministically so the same verdict can be reproduced and audited, while staying general enough to apply across heterogeneous targets. It also returned to **observability** from a different angle, treating it as one of eight distinct security domains to verify. Taken together, this is why I believe my background is well aligned with the goals of this specific research theme.

## P3 — Cosa voglio acquisire: agentic Gen AI, guardrails/constrained decoding, troubleshooting come decision-support (punto 2)

*(1863 caratteri)*

With reference to the same research theme, what I want to learn from this PhD is how to make agentic Generative AI **trustworthy** enough to act as a **foundational layer** for **Telco Edge-Cloud Continuum systems**: deploying services under explicit **non-functional requirements and operational constraints**, keeping **observability** adaptive as risks change, and supporting **AI-assisted troubleshooting**, all while remaining **reliable, verifiable, explainable and compliant**. Where my own oracles rely on a domain that is closed and known in advance, an agentic system has to reason over **intents** it must translate into deployment decisions, and the literature I have looked into converges on not letting that reasoning act unchecked. *Guardrails* and *constrained decoding* keep a non-deterministic model's output within a deterministic, typed boundary, so a decision stays accountable even when the intent behind it is genuinely new; the same literature also tends to split this work across *specialised roles*, planning, validating and executing separately, rather than trusting one generalist agent to do all three at once. I want to learn how the same discipline extends to **troubleshooting**, where generative AI is increasingly used not as an autonomous fixer but as a *decision-support system*: correlating telemetry, configuration and domain knowledge to propose a diagnosis a human can still verify, rather than a black-box verdict to be trusted outright. This is only a first, partial reading of a much broader body of work, but it is enough to convince me the direction is the right one to pursue. More importantly, I want to develop the competences of a researcher: writing with the precision and economy a scientific publication demands, discussing and defending ideas with other researchers, and building the kind of critical judgement, grounded in real knowledge and competence.

## P4 — Perché un PhD: frontiera + curiosità personale + etimologia (punto 3, parte 1)

*(535 caratteri)*

Problems still not fully understood are the ones that push competence and determination the furthest, the kind that demands patience on a single goal, and a PhD is what gives access to them, together with the people and knowledge that surround them. This has a more personal root, too: I have always needed to investigate what I do not understand and to share what I do, and the word PhD itself stands for Doctor of Philosophy, philosophy meaning, at its root, love of knowledge. It is, quite simply, a fitting description of who I am.

## P5 — Il connubio ricerca/sviluppo (punto 3, parte 2)

*(378 caratteri)*

To me, this PhD is the convergence of research and development: the freedom to chase an idea that does not yet have an answer, paired with the discipline of building it and watching it actually work. That is the level I want to reach, the kind that would let me join an organisation working on something genuinely significant and contribute to it in a way that actually matters.

## P6 — TIM dedicato

*(744 caratteri)*

What makes this opportunity stand out is the combination of an academic community and an industrial partner working on a topic I am genuinely passionate about. With TIM S.p.A. involved, the research would not stay confined to a controlled setting. I would have a real environment to test it against, and see whether it actually holds up. Being guided by both an academic and an industrial supervisor matters to me for the same reason, since it gives holistic guidance to the work: one inclined to push toward what is new, even when far ahead of what is practical, the other keeping a closer eye on what an operational system can actually sustain. I value this dual perspective; standing between both worlds allows me to understand how each distinctively conceptualises and frames a problem prior to solving it.

## P7 — ITADATA + continuità SESAR Lab (punto 4)

*(421 caratteri)*

Both my Bachelor's and Master's theses were carried out within that same research group at SESAR Lab. That continuity led to my first scientific publication, written together with my supervisors and submitted as a contribution to the ITADATA 2026 conference. I see this research theme as a natural continuation of that trajectory, extended into a domain where the questions become genuinely harder and more consequential.

## P8 — Conclusione

*(334 caratteri)*

In conclusion, I am convinced that this PhD aligns with both my background and my personal, academic and professional goals, and that it would give me access to exactly the kind of industrial scenarios I am looking for, bringing the rigour of the scientific method into an industrial setting. Thank you for considering my application.
















# Riferimenti P3 — da dove viene ciascun pezzo

Promemoria rapido per sapere dove riprendere ciascun concetto in caso di domande al colloquio. Ogni voce spiegata in modo concreto, non solo con l'etichetta tecnica.

> **Aggiornamento importante:** dopo il feedback di Anisetti, P3 è stato riscritto per includere vocabolario preciso (guardrails, constrained decoding) e il tema del troubleshooting come decision-support. In questo processo, **le sezioni 3 e 4 qui sotto (confidenza non binaria, blockchain) sono state tagliate dal testo della lettera**. Le lascio comunque nel documento, chiaramente marcate come "non più nella lettera", perché restano materiale utile se al colloquio ti viene chiesto di allargare il discorso oltre quello scritto.

---

## ✅ NELLA LETTERA — 1. Grounding offline → online

**Concetto:** invece di ancorare una decisione una volta sola, in anticipo, contro una specifica fissa, l'approccio più recente ancora la decisione continuamente, a runtime, affiancando il ragionamento non deterministico a un livello di verifica deterministico. *(Questo principio, con vocabolario "guardrails" e "constrained decoding", è nella prima parte di P3.)*

**Paper di riferimento (tutti già in project knowledge):**

- **Symbiotic Agents** — Chatzistefanidis, Nikaein — *Computer Networks* 2025 — l'LLM decide come regolare la rete radio, ma prima di agire un modulo matematico gli dà un intervallo numerico preciso entro cui restare, così la decisione finale ha un errore garantito e non è lasciata al giudizio libero del modello.
- **MAESTRO** — Chatzistefanidis, Leone, Nikaein — *IEEE Networking Letters* 2024 — testano cosa succede se l'LLM negozia da solo, senza nessun aiuto matematico: il risultato finale si allontana in media di 8 Mbps da quello che sarebbe corretto, dimostrando che il ragionamento libero del modello, senza vincoli, è impreciso.
- **A1GENT** — Li, Xu, Chen, Liu — arXiv 2026 — separa nettamente chi "pensa" (un modulo LLM lento) da chi "agisce" (un livello di esecuzione veloce e deterministico), e chi agisce non si ferma mai ad aspettare chi pensa — continua con l'ultimo valore valido. È il parallelo più diretto con come hai separato pianificazione/validazione da esecuzione nella tua tesi.
- **AgentEdge** — Gort, Kibalya, Antonopoulos — TechRxiv (non peer-reviewed) — prima di eseguire un'azione sull'infrastruttura, il sistema la simula e la fa valutare da un secondo modello indipendente che può accettarla o respingerla, così l'errore viene individuato prima di diventare reale.
- **MX-AI** — Chatzistefanidis et al. — arXiv 2025 — se un componente della rete non ha risorse disponibili, il sistema non permette nemmeno all'agente di *proporre* di aggiungerci qualcosa — l'opzione sbagliata è esclusa in anticipo, non corretta dopo.
- **IntentContinuum** — Akbari, Grundy, Cheema, Toosi — arXiv 2025 — quando il modello deve diagnosticare perché qualcosa non va, non può inventare liberamente una spiegazione: deve scegliere da un elenco chiuso di cause possibili definito in anticipo (es. "CPU troppo alta", "problema di rete"), più una categoria di fallback per i casi non previsti.
- **ARM** — Avgerinos, Ramantas, Alonso, Verikoukis — *IEEE IoT Journal* 2025-2026 — l'agente non può intervenire su un problema finché non ha raccolto prove sufficienti a giustificare l'azione — è vietato agire "a naso".

---

## ✅ NELLA LETTERA — 2. Specializzazione dei ruoli

**Concetto:** invece di un unico agente generalista, il lavoro viene diviso tra ruoli specializzati (uno pianifica, uno esegue, uno osserva, uno valida) — e questo rivela anche quali compiti restano più difficili da rendere affidabili di altri. *(Presente in P3 come "the same literature also tends to split this work across specialised roles, planning, validating and executing separately".)*

**Paper di riferimento:**

- **MX-AI** — 5 agenti distinti: uno smista le richieste, uno monitora lo stato della rete, uno pianifica i cambiamenti, uno valida che siano corretti, uno li esegue davvero. Il dato interessante: quando testato, il ruolo di "controllo" (azioni con uno schema fisso) raggiunge il 100% di accuratezza, mentre il ruolo di "osservabilità" (rispondere a domande aperte sullo stato della rete) non arriva mai alla perfezione, con nessun modello — perché un compito ha regole rigide da rispettare, l'altro richiede di sintetizzare informazioni sparse.
- **OSS-GPT** — Mekrache, Ksentini, Verikoukis — *IEEE NetSoft* 2025 — un Planner decide la sequenza di azioni tecniche da fare, un Executor le esegue materialmente, un Reporter riassume alla fine cosa è successo in linguaggio comprensibile — tre compiti tenuti separati invece che affidati a un unico agente che fa tutto.
- **MAESTRO** — dentro ogni agente ci sono sette componenti diverse, ciascuna con un compito preciso (una estrae il valore proposto, una controlla se qualcuno sta barando nella negoziazione, una consulta le regole esterne da rispettare, e così via) — nessuna di queste fa tutto da sola.
- **TN-AutoRCA** — Wu, Yu, Mei et al. — ZTE + China Mobile, arXiv 2025 — il sistema che migliora la diagnosi dei guasti è diviso in un componente che coordina, uno che valuta i risultati, uno che analizza dove si sbaglia più spesso, uno che riscrive il codice di soluzione, uno che ripulisce l'output finale.
- **AgentEdge** — un componente gestisce l'intento dell'operatore, uno osserva lo stato della rete, uno pianifica le azioni, uno le traduce in comandi tecnici reali — quattro compiti separati anziché uno unico.

---

## ✅ NELLA LETTERA — Troubleshooting come decision-support

**Concetto:** generative AI usata non come autonomous fixer ma come sistema di supporto alla decisione — correla telemetria, configurazione e conoscenza di dominio per proporre una diagnosi che un umano verifica, invece di un verdetto a scatola nera. *(È la terza parte di P3, quella che ha colmato il buco segnalato da Anisetti: "tutta la parte... troubleshooting con GenAI come decision support system".)*

**Paper di riferimento principali:** ARM (RCA + remediation con GenAI come decisore, IEEE IoT Journal), TN-AutoRCA (ZTE + China Mobile).

---

## ⚠️ NON PIÙ NELLA LETTERA — 3. Confidenza non binaria

**Tagliata da P3 durante la riscrittura per il feedback di Anisetti** — non compare più nel testo attuale. La lascio qui solo come possibile materiale da discutere se emerge in un colloquio più aperto sulla letteratura.

**Concetto:** alcuni approcci non trattano un risultato come solo "corretto/sbagliato", ma esprimono la fiducia in modo quantificato/graduato.

**Paper di riferimento (uso concreto, non teorico):**

- **ARM** — inietta un guasto artificiale, poi valuta se l'agente riporta il sistema al comportamento che aveva prima del guasto: succede pienamente solo nel 55% dei casi, ma in media viene comunque recuperato l'80.4% del degrado — un giudizio binario avrebbe nascosto quel recupero parziale dietro un semplice "fallito".
- **OSS-GPT** — per ogni richiesta calcolano il numero minimo di passaggi tecnici necessari per soddisfarla (il "percorso ideale"), poi misurano quanto il sistema si allontana da quel percorso ideale invece di dire solo se alla fine ha avuto successo o no.
- **MX-AI** — invece di dire solo se una risposta sullo stato della rete è giusta o sbagliata, la valutano su una scala da 0 a 5 per quanto è coerente e completa.

**Fonte teorica/formale (se vuoi approfondire il lato matematico):**

- **Ristic, Gilliam, Byrne, Benavoli**, "A tutorial on uncertainty modeling for machine reasoning", *Information Fusion*, 2020 — RMIT University + University of Limerick — invece di dire "questo è vero" o "questo è falso", propongono di dire "questo è vero con questo grado di certezza", calcolato con un metodo matematico esplicito (teoria bayesiana, funzioni di credenza) invece che con un giudizio secco.

---

## ⚠️ NON PIÙ NELLA LETTERA — 4. Blockchain / audit nel tempo

**Tagliata da P3 durante la riscrittura per il feedback di Anisetti** — non compare più nel testo attuale. La lascio qui solo come possibile materiale da discutere se emerge in un colloquio più aperto sulla letteratura, in particolare se si parla di RQ7/RQ8 (governance, trust lifecycle).

**Concetto:** la fiducia, una volta stabilita, va mantenuta nel tempo — un registro delle decisioni a prova di manomissione (blockchain) è già usato altrove ma non ancora nel Telco.

**Fonte primaria (il gap):**

- **Mekrache, Ksentini, Verikoukis**, "Machine Reasoning in FCAPS: Towards Enhanced Beyond 5G Network Management", *IEEE Communications Surveys & Tutorials*, 2024 — **è in project knowledge** — nella sezione finale sulle direzioni future, gli autori stessi scrivono esplicitamente che combinare ragionamento automatico e blockchain per la sicurezza delle reti è "un'area di ricerca emergente che merita ulteriore indagine".

**Prova che il meccanismo esiste già altrove (verificato via web, non in project knowledge):**

- **"A Blockchain-Monitored Agentic AI Architecture for Trusted Perception–Reasoning–Action Pipelines"** — presentato a IEEE ICCA 2025 (Bahrain) — un sistema reale dove ogni decisione di un agente AI viene registrata su una blockchain. Testato su gestione di magazzino, controllo di semafori, monitoraggio sanitario — non nel Telco, ma dimostra che il meccanismo funziona davvero.

---

## Nota su cosa NON è nella project knowledge

I paper di **Ristic et al.** (incertezza) e sul **blockchain applicato (ICCA 2025)** li ho trovati e verificati tramite ricerca web, ma non li hai caricati come PDF — se ti servono per il colloquio, vanno recuperati separatamente (riferimenti bibliografici completi sopra).