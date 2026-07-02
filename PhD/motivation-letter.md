# Motivation Letter — Intersectoral Innovation PhD (v14)

> **Nota:** Codice tabella Modello 1: **2**. Lunghezza: 6494 caratteri (+57% vs Luzzara, ~4150 caratteri). 9 paragrafi.
> P4 è il nuovo paragrafo dedicato al materiale di ricerca, ora separato da P3 con apertura e chiusura proprie.
> Le intestazioni `##` sotto sono solo per tua navigazione — NON vanno nel Modello 1, solo il testo in prosa.

---

## P1 — Apertura

*(348 caratteri)*

My name is Enea Manzi, and I am writing to express my strong motivation to join the "Intersectoral Innovation" industrial PhD programme, with reference to Research Theme 2, "Trusted Agentic Generative AI for Intent-Driven Deployment, Observability and Troubleshooting in Telco Edge–Cloud Continuum Systems", developed in collaboration with TIM S.p.A.

## P2 — Background (punto 1)

*(1213 caratteri)*

Across five years at the University of Milan, including both my Bachelor's and Master's theses carried out at the SESAR Lab (Secure Service-oriented Architectures Research Lab), I have developed a deep interest in automated assurance for distributed systems, particularly exploring how evaluation criteria can be made explicit and verifiable rather than left to implicit heuristics, and how a system can stay general enough to apply across heterogeneous targets while remaining grounded enough to produce auditable, trustworthy verdicts. Through this continuous hands-on research, building tools that evaluate REST APIs and distributed systems against formally declared security and non-functional contracts, I have built up a solid understanding of what it means to treat trustworthiness as a primary design objective rather than an emergent property, to orchestrate verification deterministically, and to keep every decision traceable to the evidence behind it. This experience, together with an independent project building a cloud-native microservices infrastructure on Kubernetes with Kafka and Kong, has reinforced my belief that my background is well aligned with the goals of this specific research theme.

## P3 — Cosa voglio acquisire (punto 2)

*(1069 caratteri)*

With reference to the same research theme, what draws me to this PhD is the kind of problem it deals with: not yet well understood, still at the edge of what is known, the kind I am genuinely curious about. So far, the problems I have worked on have always started from something formally given: a contract, a specification, a declared objective. What I want from this PhD is to learn how that same approach can hold once that starting point is no longer there: translating high-level intents into deployment decisions bound by explicit non-functional constraints, grounding an agent's decisions in verifiable evidence rather than blind trust, keeping multi-agent planning, validation and execution accountable to policy and auditable, and letting observability adapt as risks change. More importantly, I want to develop the competences of a researcher: writing with the precision and economy a scientific publication demands, discussing and defending ideas with other researchers, and building the kind of critical judgement, grounded in real knowledge and competence.

## P4 — Cosa dice la letteratura recente — grounding offline/online, specializzazione dei ruoli, confidenza non binaria, blockchain/audit nel tempo

*(1411 caratteri)*

Having looked into recent work on this shift, I notice a recurring architectural answer: instead of grounding a decision once, in advance, against a fixed specification, the more recent approach grounds it continuously, at runtime, pairing the non-deterministic reasoning step with a deterministic verification layer, a numerical bound, a typed policy, an explicit constraint, so the output stays accountable even when the input is genuinely new. That same literature usually achieves this by splitting the work across specialised roles instead of one generalist agent, each bounded to a narrower task it can be checked against. My own oracles, in my Master's thesis, are in this sense a limit case of the same principle, one where that grounding could be fixed once because the domain itself was closed, and the same pipeline already separated discovery, scheduling and execution into distinct stages, each checked before the next could begin. Separately, I noticed some of it stops treating confidence as binary altogether, expressing it instead as an explicit, quantified degree rather than a pass-or-fail verdict. Trust, once established, still has to be maintained over time, and one way to do that - a blockchain-based, tamper-evident ledger of every decision - is already used elsewhere but not yet in this domain. This is, admittedly, only a first pass at what is actually a much broader body of work, but it is enough to tell me the direction is worth pursuing.

## P5 — Perché un PhD: frontiera + curiosità personale + etimologia (punto 3, parte 1)

*(496 caratteri)*

These are the kinds of problems that push competence and determination the furthest, the kind that demands patience on a single goal, and a PhD is what gives access to them, together with the people and knowledge that surround them. This has a more personal root, too: I have always needed to investigate what I do not understand and to share what I do, and the word PhD itself stands for Doctor of Philosophy, philosophy meaning, at its root, love of knowledge. It is, quite simply, a fitting description of who I am.

## P6 — Il connubio ricerca/sviluppo (punto 3, parte 2)

*(378 caratteri)*

To me, this PhD is the convergence of research and development: the freedom to chase an idea that does not yet have an answer, paired with the discipline of building it and watching it actually work. That is the level I want to reach, the kind that would let me join an organisation working on something genuinely significant and contribute to it in a way that actually matters.

## P7 — TIM dedicato

*(709 caratteri)*

What makes this opportunity stand out is the combination of an academic community and an industrial partner working on a topic I am genuinely passionate about. With TIM S.p.A. involved, the research would not stay confined to a controlled setting. I would have a real environment to test it against, and see whether it actually holds up. Being guided by both an academic and an industrial supervisor matters to me for the same reason, since it gives holistic guidance to the work: one inclined to push toward what is new, even when far ahead of what is practical, the other keeping a closer eye on what an operational system can actually sustain. I like having both, since it means seeing both worlds at once and standing right in between them.

## P8 — ITADATA + continuità SESAR Lab (punto 4)

*(421 caratteri)*

Both my Bachelor's and Master's theses were carried out within that same research group at SESAR Lab. That continuity led to my first scientific publication, written together with my supervisors and submitted as a contribution to the ITADATA 2026 conference. I see this research theme as a natural continuation of that trajectory, extended into a domain where the questions become genuinely harder and more consequential.

## P9 — Conclusione

*(334 caratteri)*

In conclusion, I am convinced that this PhD aligns with both my background and my personal, academic and professional goals, and that it would give me access to exactly the kind of industrial scenarios I am looking for, bringing the rigour of the scientific method into an industrial setting. Thank you for considering my application.
















# Riferimenti P4 — da dove viene ciascun pezzo

Promemoria rapido per sapere dove riprendere ciascun concetto in caso di domande al colloquio. Ogni voce spiegata in modo concreto, non solo con l'etichetta tecnica.

---

## 1. Grounding offline → online (frase di apertura di P4)

**Concetto:** invece di ancorare una decisione una volta sola, in anticipo, contro una specifica fissa, l'approccio più recente ancora la decisione continuamente, a runtime, affiancando il ragionamento non deterministico a un livello di verifica deterministico.

**Paper di riferimento (tutti già in project knowledge):**

- **Symbiotic Agents** — Chatzistefanidis, Nikaein — *Computer Networks* 2025 — l'LLM decide come regolare la rete radio, ma prima di agire un modulo matematico gli dà un intervallo numerico preciso entro cui restare, così la decisione finale ha un errore garantito e non è lasciata al giudizio libero del modello.
- **MAESTRO** — Chatzistefanidis, Leone, Nikaein — *IEEE Networking Letters* 2024 — testano cosa succede se l'LLM negozia da solo, senza nessun aiuto matematico: il risultato finale si allontana in media di 8 Mbps da quello che sarebbe corretto, dimostrando che il ragionamento libero del modello, senza vincoli, è impreciso.
- **A1GENT** — Li, Xu, Chen, Liu — arXiv 2026 — separa nettamente chi "pensa" (un modulo LLM lento) da chi "agisce" (un livello di esecuzione veloce e deterministico), e chi agisce non si ferma mai ad aspettare chi pensa — continua con l'ultimo valore valido. È il parallelo più diretto con come hai separato pianificazione/validazione da esecuzione nella tua tesi.
- **AgentEdge** — Gort, Kibalya, Antonopoulos — TechRxiv (non peer-reviewed) — prima di eseguire un'azione sull'infrastruttura, il sistema la simula e la fa valutare da un secondo modello indipendente che può accettarla o respingerla, così l'errore viene individuato prima di diventare reale.
- **MX-AI** — Chatzistefanidis et al. — arXiv 2025 — se un componente della rete non ha risorse disponibili, il sistema non permette nemmeno all'agente di *proporre* di aggiungerci qualcosa — l'opzione sbagliata è esclusa in anticipo, non corretta dopo.
- **IntentContinuum** — Akbari, Grundy, Cheema, Toosi — arXiv 2025 — quando il modello deve diagnosticare perché qualcosa non va, non può inventare liberamente una spiegazione: deve scegliere da un elenco chiuso di cause possibili definito in anticipo (es. "CPU troppo alta", "problema di rete"), più una categoria di fallback per i casi non previsti.
- **ARM** — Avgerinos, Ramantas, Alonso, Verikoukis — *IEEE IoT Journal* 2025-2026 — l'agente non può intervenire su un problema finché non ha raccolto prove sufficienti a giustificare l'azione — è vietato agire "a naso".

---

## 2. Specializzazione dei ruoli (seconda frase di P4)

**Concetto:** invece di un unico agente generalista, il lavoro viene diviso tra ruoli specializzati (uno pianifica, uno esegue, uno osserva, uno valida) — e questo rivela anche quali compiti restano più difficili da rendere affidabili di altri.

**Paper di riferimento:**

- **MX-AI** — 5 agenti distinti: uno smista le richieste, uno monitora lo stato della rete, uno pianifica i cambiamenti, uno valida che siano corretti, uno li esegue davvero. Il dato interessante: quando testato, il ruolo di "controllo" (azioni con uno schema fisso) raggiunge il 100% di accuratezza, mentre il ruolo di "osservabilità" (rispondere a domande aperte sullo stato della rete) non arriva mai alla perfezione, con nessun modello — perché un compito ha regole rigide da rispettare, l'altro richiede di sintetizzare informazioni sparse.
- **OSS-GPT** — Mekrache, Ksentini, Verikoukis — *IEEE NetSoft* 2025 — un Planner decide la sequenza di azioni tecniche da fare, un Executor le esegue materialmente, un Reporter riassume alla fine cosa è successo in linguaggio comprensibile — tre compiti tenuti separati invece che affidati a un unico agente che fa tutto.
- **MAESTRO** — dentro ogni agente ci sono sette componenti diverse, ciascuna con un compito preciso (una estrae il valore proposto, una controlla se qualcuno sta barando nella negoziazione, una consulta le regole esterne da rispettare, e così via) — nessuna di queste fa tutto da sola.
- **TN-AutoRCA** — Wu, Yu, Mei et al. — ZTE + China Mobile, arXiv 2025 — il sistema che migliora la diagnosi dei guasti è diviso in un componente che coordina, uno che valuta i risultati, uno che analizza dove si sbaglia più spesso, uno che riscrive il codice di soluzione, uno che ripulisce l'output finale.
- **AgentEdge** — un componente gestisce l'intento dell'operatore, uno osserva lo stato della rete, uno pianifica le azioni, uno le traduce in comandi tecnici reali — quattro compiti separati anziché uno unico.

---

## 3. Confidenza non binaria (terza frase di P4)

**Concetto:** alcuni approcci non trattano un risultato come solo "corretto/sbagliato", ma esprimono la fiducia in modo quantificato/graduato.

**Paper di riferimento (uso concreto, non teorico):**

- **ARM** — inietta un guasto artificiale, poi valuta se l'agente riporta il sistema al comportamento che aveva prima del guasto: succede pienamente solo nel 55% dei casi, ma in media viene comunque recuperato l'80.4% del degrado — un giudizio binario avrebbe nascosto quel recupero parziale dietro un semplice "fallito".
- **OSS-GPT** — per ogni richiesta calcolano il numero minimo di passaggi tecnici necessari per soddisfarla (il "percorso ideale"), poi misurano quanto il sistema si allontana da quel percorso ideale invece di dire solo se alla fine ha avuto successo o no — anche un successo "sporco", con passaggi in più del necessario, viene registrato come tale.
- **MX-AI** — invece di dire solo se una risposta sullo stato della rete è giusta o sbagliata, la valutano su una scala da 0 a 5 per quanto è coerente e completa.

**Fonte teorica/formale (se vuoi approfondire il lato matematico):**

- **Ristic, Gilliam, Byrne, Benavoli**, "A tutorial on uncertainty modeling for machine reasoning", *Information Fusion*, 2020 — RMIT University + University of Limerick — invece di dire "questo è vero" o "questo è falso", propongono di dire "questo è vero con questo grado di certezza", calcolato con un metodo matematico esplicito (teoria bayesiana, funzioni di credenza) invece che con un giudizio secco.

---

## 4. Blockchain / audit nel tempo (quarta frase di P4)

**Concetto:** la fiducia, una volta stabilita, va mantenuta nel tempo — un registro delle decisioni a prova di manomissione (blockchain) è già usato altrove ma non ancora nel Telco.

**Fonte primaria (il gap):**

- **Mekrache, Ksentini, Verikoukis**, "Machine Reasoning in FCAPS: Towards Enhanced Beyond 5G Network Management", *IEEE Communications Surveys & Tutorials*, 2024 — **è in project knowledge** — nella sezione finale sulle direzioni future, gli autori stessi scrivono esplicitamente che combinare ragionamento automatico e blockchain per la sicurezza delle reti è "un'area di ricerca emergente che merita ulteriore indagine" — cioè lo dicono loro che non è ancora stato fatto, non lo sto dicendo io.

**Prova che il meccanismo esiste già altrove (verificato via web, non in project knowledge):**

- **"A Blockchain-Monitored Agentic AI Architecture for Trusted Perception–Reasoning–Action Pipelines"** — presentato a IEEE ICCA 2025 (Bahrain) — un sistema reale (non solo un'idea) dove ogni decisione di un agente AI viene registrata su una blockchain, così nessuno può modificare la cronologia delle decisioni dopo il fatto. Testato su gestione di magazzino, controllo di semafori, monitoraggio sanitario — **non nel Telco**, ma dimostra che il meccanismo funziona davvero, non è solo teoria.

---

## Nota su cosa NON è nella project knowledge

I paper di **Ristic et al.** (incertezza) e sul **blockchain applicato (ICCA 2025)** li ho trovati e verificati tramite ricerca web, ma non li hai caricati come PDF — se ti servono per il colloquio, vanno recuperati separatamente (riferimenti bibliografici completi sopra).