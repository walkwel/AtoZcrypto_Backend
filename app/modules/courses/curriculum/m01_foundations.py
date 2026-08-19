"""Module 1 — Getting Started & How Blockchains Work."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="getting-started-and-blockchains",
    title="Getting Started & How Blockchains Work",
    summary=(
        "How this programme is structured, what a blockchain actually is, and the vocabulary "
        "every later module assumes you already have."
    ),
    level=CourseLevel.BEGINNER,
    phase=CoursePhase.FOUNDATIONS,
    lessons=[
        LessonSpec(
            title="How this programme works",
            minutes=6,
            body=(
                "This is a fifteen-module programme designed to take you from no prior knowledge "
                "to running your own research and risk process. It is built for people with jobs: "
                "each lesson is short enough to finish in a sitting, and each module closes with "
                "a homework exercise that turns what you read into something you have actually "
                "done.\n\n"
                "The five phases build on each other. Foundations covers what crypto is and how "
                "to hold it safely. Market Mechanics covers how exchanges, order books and charts "
                "work. Analysis covers the three research disciplines — technical, fundamental "
                "and on-chain — plus the macro backdrop they sit inside. Risk & Strategy covers "
                "position sizing, psychology and how to write a plan you can follow. Practice "
                "closes with portfolio construction, tax record-keeping and a ninety-day plan.\n\n"
                "Two habits matter more than reading speed:\n\n"
                "- Do the homework. Reading about position sizing does not change behaviour; "
                "sizing a real position does.\n"
                "- Keep a notes file from lesson one. Every strategy you eventually run will be "
                "assembled from observations you made along the way, and you will not remember "
                "them otherwise.\n\n"
                "Mark each lesson complete as you finish it. Your progress is saved to your "
                "account, so you can move between devices and pick up where you left off. There "
                "is no time limit and no penalty for repeating a module — the analysis modules in "
                "particular reward a second pass once you have watched a market for a few "
                "weeks.\n\n"
                "One thing this programme will not do is tell you what to buy. It teaches you how "
                "to evaluate an asset, size a position and manage the risk, which is the part that "
                "transfers to every market and every cycle."
            ),
        ),
        LessonSpec(
            title="What a blockchain actually is",
            minutes=8,
            body=(
                "A blockchain is a database with two unusual properties: many independent parties "
                "hold a full copy of it, and entries can be added but never quietly edited. "
                "Everything else — mining, wallets, tokens, smart contracts — is machinery built "
                "to serve those two properties.\n\n"
                "Transactions are collected into batches called blocks. Each block contains a "
                "cryptographic hash of the block before it: a short fingerprint that changes "
                "completely if even one character of the earlier block changes. Because every "
                "block commits to its predecessor, the chain of hashes ties the whole history "
                "together. Altering a transaction from last year would change that block's hash, "
                "which would break the next block's reference, and the next, all the way to the "
                "present.\n\n"
                "That is what makes tampering impractical rather than merely illegal. To rewrite "
                "history you would have to redo the work for every block since, faster than the "
                "rest of the network is extending the honest chain, and convince the majority to "
                "accept your version. On a large network that costs more than the theft is "
                "usually worth — the security is economic as much as it is cryptographic.\n\n"
                "The word that trips people up is 'ledger'. A blockchain does not store your coins "
                "in a folder with your name on it. It stores a record of transfers, and your "
                "balance is simply what that record implies: everything sent to your address minus "
                "everything sent from it. There is no account object to hack, which is why "
                "security in crypto is almost entirely about protecting the key that authorises "
                "outgoing transfers.\n\n"
                "It is worth being clear about what a blockchain is bad at, too. It is slow and "
                "expensive compared with a normal database, it cannot verify anything that "
                "happens off the chain, and it cannot undo a mistake. Those costs buy you one "
                "thing — a shared record no single participant controls — and that trade is only "
                "worth making when nobody in the system fully trusts anybody else."
            ),
        ),
        LessonSpec(
            title="What Bitcoin solved",
            minutes=8,
            body=(
                "Digital cash was attempted repeatedly through the 1990s and always failed on the "
                "same problem: double spending. A digital file can be copied perfectly, so what "
                "stops someone spending the same coin twice? Every earlier system answered with a "
                "trusted issuer who kept the master ledger — which meant a single company that "
                "could be shut down, pressured or simply go out of business.\n\n"
                "Bitcoin's 2008 white paper proposed an answer with no issuer. Anyone could join "
                "the network, and the version of history everyone agreed on would be the chain "
                "with the most computational work behind it. To add a block you had to find a "
                "number that made the block's hash fall below a target — hard to find, trivial to "
                "verify. That is proof of work. Miners spend real electricity competing for the "
                "right to add the next block, and are paid in newly issued bitcoin plus the fees "
                "of the transactions they include.\n\n"
                "The elegance is in the incentives. An attacker with enough hardware to rewrite "
                "history could instead point that hardware at mining honestly and earn the reward. "
                "Attacking the network also devalues the asset the attacker would be paid in. "
                "Security does not rest on participants being honest; it rests on honesty being "
                "the more profitable option.\n\n"
                "Bitcoin also fixed its issuance schedule in code: 21 million coins, with the "
                "block reward halving roughly every four years. Nobody can vote to print more "
                "without persuading the entire network to run different software. Whether a fixed "
                "supply is good monetary policy is genuinely debated — but its predictability is "
                "the property people are buying.\n\n"
                "Understanding this matters beyond Bitcoin itself. Every asset you will look at "
                "later in the programme is, in some sense, a variation on these choices: who is "
                "allowed to add to the record, what they are paid, and who can change the rules. "
                "When you evaluate a new chain, those are the three questions worth asking first."
            ),
        ),
        LessonSpec(
            title="Coins, tokens and the networks beneath them",
            minutes=7,
            body=(
                "A coin is the native asset of its own blockchain. Bitcoin on the Bitcoin network, "
                "Ether on Ethereum, SOL on Solana. Coins pay the network's transaction fees and "
                "usually pay the participants who secure it.\n\n"
                "A token is issued on top of an existing blockchain using a smart contract — a "
                "program deployed to that chain. USDC, UNI and thousands of others are tokens on "
                "Ethereum and elsewhere. A token does not have its own validators; it inherits the "
                "security of the chain it lives on, and you pay fees in that chain's coin to move "
                "it. This is why you can hold a token and still be unable to send it: you have the "
                "token but no ETH for gas.\n\n"
                "Layer 1 and Layer 2 are the next distinction. A Layer 1 is a base chain that "
                "settles its own transactions — Bitcoin, Ethereum, Solana. A Layer 2 is a separate "
                "system that processes transactions cheaply and periodically posts proofs or data "
                "back to a Layer 1 for final settlement. Arbitrum, Base and Optimism are Layer 2s "
                "on Ethereum. The practical consequence is that the same asset can exist on many "
                "networks, and sending to the wrong one is one of the most common ways people lose "
                "funds.\n\n"
                "Categories worth knowing by name:\n\n"
                "- Stablecoins, designed to hold a fixed value, usually a dollar. Some are backed "
                "by reserves held by a company (USDC, USDT); others are backed by crypto "
                "collateral. They differ enormously in what happens if the backing fails.\n"
                "- Governance tokens, which grant votes over a protocol's parameters.\n"
                "- Utility tokens, which pay for something specific inside an application.\n"
                "- Meme coins, which have no mechanism connecting price to activity and trade "
                "purely on attention.\n\n"
                "When you look at any asset, the first two questions are: what network is this on, "
                "and what, if anything, connects its price to something happening?"
            ),
        ),
        LessonSpec(
            title="What decentralisation actually buys you",
            minutes=7,
            body=(
                "Decentralisation is the most overused word in the industry, and treating it as an "
                "unqualified virtue is a reliable way to get separated from money. It is a "
                "trade-off, and it is worth being precise about what you get and what you pay.\n\n"
                "What you get is censorship resistance and continuity. No single party can freeze "
                "your assets, reverse your transaction, or switch the system off. For someone "
                "moving value out of a collapsing currency or operating where banking access is "
                "political, that is not an abstraction. You also get verifiability: you can check "
                "the rules and the state of the ledger yourself rather than trusting a "
                "statement.\n\n"
                "What you pay is convenience and recourse. There is no password reset, no fraud "
                "department, no chargeback. Throughput is lower and fees are higher than a "
                "centralised system doing the same job. Upgrades are slow because they require "
                "broad agreement.\n\n"
                "It is also a spectrum, not a switch. Ask concrete questions instead: How many "
                "independent parties produce blocks, and could a handful of them collude? Who can "
                "upgrade the smart contract, and can they do it instantly? Is there an admin key "
                "that can pause transfers or mint new supply? Is the front-end you use the only "
                "way to reach the protocol? Many projects describing themselves as decentralised "
                "have a multisig held by the founding team that can change everything.\n\n"
                "The practical rule: the further a system sits toward the decentralised end, the "
                "more the responsibility for security sits with you. That is not a reason to avoid "
                "it — it is a reason to learn key management before you move size, which is "
                "exactly what Module 3 does."
            ),
        ),
        LessonSpec(
            title="Mining, staking and how blocks get made",
            minutes=8,
            body=(
                "Someone has to decide which transactions go into the next block, and the network "
                "has to agree they played fair. The two dominant answers are proof of work and "
                "proof of stake.\n\n"
                "Under proof of work, miners race to find a hash below a difficulty target. It "
                "requires specialised hardware and a great deal of electricity, and the winner "
                "collects the block reward and fees. The cost is the point: attacking the chain "
                "means out-spending everyone else's hardware and power indefinitely. Bitcoin uses "
                "this, and its difficulty adjusts automatically so blocks keep arriving roughly "
                "every ten minutes regardless of how much hardware joins.\n\n"
                "Under proof of stake, validators lock up the network's own coin as collateral. "
                "The protocol selects who proposes the next block, and a validator who signs "
                "conflicting or invalid blocks can have part of their stake destroyed — "
                "'slashing'. "
                "Ethereum moved to this in 2022, cutting its energy use by more than 99%. "
                "Attacking "
                "the chain here means acquiring a large fraction of the staked supply and then "
                "watching it get burned.\n\n"
                "For an investor the differences that matter are practical:\n\n"
                "- Proof of stake usually offers a yield for participating, either by running a "
                "validator or by delegating to one. That yield is issuance, not profit from "
                "nowhere — it partly dilutes holders who do not stake.\n"
                "- Staked assets often have an unbonding period during which you cannot sell. That "
                "is a real risk in a fast decline.\n"
                "- Liquid staking tokens let you hold a tradeable claim on staked assets, at the "
                "cost of trusting the protocol that issued them.\n"
                "- Proof of work assets have a persistent seller: miners with electricity "
                "bills.\n\n"
                "Neither model is universally better. What matters when you evaluate a chain is "
                "how concentrated block production actually is, and what it would cost someone to "
                "control it."
            ),
        ),
        LessonSpec(
            title="Keys, addresses and what ownership means",
            minutes=8,
            body=(
                "Ownership in crypto is the ability to produce a valid signature. That is the "
                "whole of it, and internalising it early prevents most catastrophic mistakes.\n\n"
                "A private key is an enormous random number. From it, mathematics derives a public "
                "key, and from that an address — the string you share to receive funds. The "
                "derivation runs one way only: an address reveals nothing useful about the private "
                "key behind it. When you send funds, your wallet uses the private key to sign the "
                "transaction. Every node can verify the signature matches the address without ever "
                "seeing the key.\n\n"
                "Modern wallets do not ask you to store keys directly. They generate a seed phrase "
                "— typically twelve or twenty-four ordinary words — from which every key in that "
                "wallet is derived deterministically. This is why the phrase is so dangerous to "
                "mishandle: it is not a password to an account, it is the account. Anyone who "
                "reads it can regenerate every key and take everything, from anywhere, forever. "
                "There is no revocation.\n\n"
                "Three consequences follow, and they are absolute:\n\n"
                "- Never type a seed phrase into a website, a chat, a support ticket or a phone. "
                "No legitimate service will ever ask for it. This single rule prevents the "
                "majority of retail losses.\n"
                "- Never photograph it or store it in cloud notes, email or a password manager "
                "that syncs. Write it on paper or steel, and keep it somewhere a fire or a flood "
                "will not reach.\n"
                "- Test your backup before it matters. Restore the phrase into a fresh wallet with "
                "a trivial balance and confirm the addresses match.\n\n"
                "Addresses themselves are worth a moment of care. They are network-specific and "
                "unforgiving: a transfer to a valid address on the wrong network, or to a "
                "mistyped one, is generally unrecoverable. Send a small test amount first when the "
                "destination is new. The fee is a rounding error against the alternative."
            ),
        ),
        LessonSpec(
            title="Where crypto's value comes from",
            minutes=8,
            body=(
                "'It isn't backed by anything' is the most common objection and the least useful, "
                "because it is equally true of every fiat currency and most equity valuations. The "
                "better question is: what would make demand for this asset persist?\n\n"
                "There are only a few honest answers, and it is worth being able to name which one "
                "applies to anything you hold.\n\n"
                "Monetary premium. Some assets are held because other people hold them and expect "
                "to keep doing so — a shared belief that something is a reasonable store of value. "
                "This sounds circular because it is; gold works the same way. What supports it is "
                "durability, verifiable scarcity, liquidity and a long track record of surviving "
                "stress. Bitcoin's case rests almost entirely here.\n\n"
                "Fee demand. A chain that people use generates fees paid in its native coin, and "
                "some chains destroy a portion of those fees, reducing supply. That is a real, "
                "measurable link between activity and the asset. When you hear 'this chain has "
                "real revenue', this is what is meant — and it can be checked rather than "
                "believed.\n\n"
                "Productive claims. Staking or protocol revenue distributions make an asset "
                "resemble a yield-bearing instrument. Here you can build something like a "
                "conventional valuation, provided you are honest about whether the yield is real "
                "revenue or newly printed supply.\n\n"
                "Collateral demand. Assets used as collateral across lending and derivatives "
                "markets accrue demand from that use, independent of speculation.\n\n"
                "And then there is attention: assets with no mechanism at all, whose price is a "
                "pure function of how many people are talking about them. These can rise "
                "spectacularly. They can also go to nothing in a week, because nothing underneath "
                "resists the fall.\n\n"
                "Most assets are a blend. The exercise that makes this practical is to write, in "
                "one sentence, why demand for a given asset should exist in three years. If you "
                "cannot, you are not investing in it — you are trading its attention, which is a "
                "legitimate activity but requires completely different risk management."
            ),
        ),
        LessonSpec(
            title="The risks nobody should skip",
            minutes=8,
            body=(
                "Every risk below has separated large numbers of competent people from their "
                "money. Read this lesson as a checklist rather than a warning.\n\n"
                "Volatility. Drawdowns of 70–85% have happened in every major cycle, to the "
                "largest assets, not just the speculative ones. Any position must be sized so that "
                "outcome is survivable — financially and psychologically. This is covered properly "
                "in Module 12, and it is the module that matters most.\n\n"
                "Self-custody error. Lost seed phrases, mistyped addresses, wrong networks. These "
                "losses are permanent and there is no counterparty to appeal to.\n\n"
                "Counterparty failure. Exchanges and lenders have failed, taking customer assets "
                "with them — repeatedly, including firms that looked institutional. An exchange "
                "balance is a claim on a company, not ownership of an asset.\n\n"
                "Smart contract risk. Code holding funds can contain bugs. Audits reduce the "
                "probability but do not eliminate it, and audited protocols have been drained.\n\n"
                "Fraud. Rug pulls, fake tokens, impersonated support accounts, wallet-draining "
                "signature requests, romance and investment scams routed through crypto. Assume "
                "anyone who contacts you first about an opportunity is running one.\n\n"
                "Regulatory change. Rules on custody, taxation and access are still moving in most "
                "jurisdictions, and a change can affect what you can hold or how it is taxed.\n\n"
                "Concentration. Holding one asset, on one exchange, in one country, is several "
                "correlated bets at once.\n\n"
                "The point is not to be frightened out of the market. It is that most of these are "
                "avoidable with process: size positions deliberately, hold long-term assets in "
                "self-custody, spread counterparty exposure, verify before signing, and never act "
                "on urgency someone else manufactured."
            ),
        ),
        homework(
            title="Week 1 homework — your why, your ceiling and your schedule",
            minutes=12,
            body=(
                "Three short written exercises. Keep them in the notes file you will use for the "
                "rest of the programme — you will be asked to revisit all three in Module 15.\n\n"
                "1. Write your objective in one sentence.\n\n"
                "Be specific and finite. 'Grow a long-term position in two or three assets I have "
                "researched, over five years' is an objective. 'Make money' is not, because it "
                "does not tell you what to do on any given day. Include the time horizon — almost "
                "every bad decision later traces back to a horizon that was never stated.\n\n"
                "2. Write your maximum loss, as a number.\n\n"
                "Not a percentage, and not a feeling: the actual sum of money that could go to "
                "zero without changing how you live or how you sleep. Then halve it for your first "
                "six months, while you are still learning. This number is the ceiling on "
                "everything "
                "you will do in this programme.\n\n"
                "3. Write your study schedule.\n\n"
                "Pick specific days and a specific length — twenty minutes, four evenings a week, "
                "is enough to finish this programme comfortably. Write down when, not how much. A "
                "schedule tied to time survives busy weeks; one tied to volume does not.\n\n"
                "Finally, one practical task: create a dedicated folder or note for this course "
                "and paste all three answers into it, with today's date at the top. In Module 15 "
                "you will compare what you wrote today with what you believe by then, and the gap "
                "is genuinely instructive."
            ),
        ),
    ],
)
