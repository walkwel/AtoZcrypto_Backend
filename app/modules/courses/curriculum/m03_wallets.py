"""Module 3 — Wallets, Custody & Key Management."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="wallets-and-custody",
    title="Wallets, Custody & Key Management",
    summary=(
        "Holding your own assets without losing them: wallet types, seed phrase discipline, "
        "transaction safety, and a storage plan that survives your own mistakes."
    ),
    level=CourseLevel.BEGINNER,
    phase=CoursePhase.FOUNDATIONS,
    lessons=[
        LessonSpec(
            title="What a wallet is and is not",
            minutes=7,
            body=(
                "A wallet does not hold your coins. Your coins are entries on a blockchain; the "
                "wallet holds the keys that let you move them, and shows you a balance it reads "
                "from the network. Losing a wallet is not losing your assets — losing the keys is. "
                "Understanding that distinction is what makes backups make sense.\n\n"
                "Every wallet does three things: it stores a private key, it derives addresses "
                "from it, and it signs transactions on your instruction. Everything else — token "
                "lists, portfolio charts, swap buttons — is convenience layered on top, and none "
                "of it is stored on the blockchain.\n\n"
                "The critical property is custody. In a custodial wallet, someone else holds the "
                "key: an exchange account is the obvious case. You get password resets and support "
                "at the cost of depending on that company's solvency and honesty. In a "
                "non-custodial wallet you hold the key, which means nobody can freeze or lose your "
                "funds, and nobody can help you if you lose them yourself.\n\n"
                "One more distinction that confuses beginners: your addresses are derived from "
                "your seed phrase, not from the app. If a wallet app disappears tomorrow, you "
                "restore the same phrase into a different wallet and every address and balance "
                "reappears. The phrase is the asset; the app is a viewer. This is why the standard "
                "for seed phrases exists across vendors, and why 'my wallet company shut down' is "
                "not, by itself, a loss event.\n\n"
                "Finally: a wallet is per-key, not per-coin. One seed phrase generates addresses "
                "across many networks. When someone says 'I need a separate wallet for that "
                "chain', they usually mean a separate app or a separate account within the same "
                "seed — not a new backup to protect."
            ),
        ),
        LessonSpec(
            title="Hot, cold and hardware wallets",
            minutes=8,
            body=(
                "Wallets differ mainly in where the key lives and whether that device touches the "
                "internet.\n\n"
                "A hot wallet keeps keys on an internet-connected device — a browser extension or "
                "a phone app. It is fast and convenient, and it is exactly as secure as the device "
                "it runs on. Malware on the machine can, in principle, reach the key. Hot wallets "
                "are appropriate for amounts you would carry in a physical wallet: enough to "
                "transact with, not enough to hurt.\n\n"
                "A hardware wallet keeps the key on a dedicated device that never exposes it. "
                "Transactions are constructed on your computer, sent to the device, signed inside "
                "it, and returned signed. Even a fully compromised computer cannot extract the "
                "key. Crucially, the device has its own screen: you verify the destination address "
                "and amount on hardware the malware does not control. That screen is the actual "
                "security feature, and ignoring it defeats the whole purpose.\n\n"
                "Cold storage means keys generated and kept entirely offline. A hardware wallet "
                "used carefully is cold storage for practical purposes.\n\n"
                "Two more types worth knowing. Multisig wallets require several keys to approve a "
                "transaction — two of three, say — so a single compromised or lost key is not "
                "fatal. They are the standard for shared funds and for large individual holdings. "
                "Smart contract wallets add recovery and spending rules in code, letting you "
                "nominate trusted parties who can help you recover access without ever holding "
                "your funds.\n\n"
                "A reasonable structure for most people: a hardware wallet for long-term holdings, "
                "a hot wallet with a small balance for day-to-day activity, and an exchange "
                "account for converting currency. Three tiers, each sized to the risk it carries."
            ),
        ),
        LessonSpec(
            title="Seed phrases: the one thing you cannot get wrong",
            minutes=9,
            body=(
                "Your seed phrase is twelve or twenty-four words that encode every key your wallet "
                "will ever generate. Anyone who has it has everything, permanently, from anywhere. "
                "Nothing else in crypto is this unforgiving, so it deserves a procedure rather "
                "than a habit.\n\n"
                "Generate it on the device itself. A hardware wallet creates the phrase using its "
                "own randomness and shows it only on its own screen. A phrase that arrived by "
                "email, was printed on a card in the box, or was displayed by a website is already "
                "compromised — pre-loaded 'ready to use' devices are a known scam.\n\n"
                "Record it physically. Paper is acceptable; stamped or engraved steel is better, "
                "because it survives fire and water. Write clearly, number the words, and note "
                "which wallet and which network family it belongs to.\n\n"
                "Never let it become digital. No photographs, no cloud notes, no password manager "
                "that syncs, no email to yourself, no text file 'temporarily'. Every one of these "
                "has produced real, large losses. A phrase that touches an internet-connected "
                "device should be considered burned: move the funds to a freshly generated "
                "wallet.\n\n"
                "Store copies in more than one place. One copy is a single point of failure — a "
                "house fire ends you. Two or three copies in separate physical locations balances "
                "theft risk against loss risk. If someone else could plausibly find a copy, "
                "consider a passphrase (below).\n\n"
                "Verify the backup before funding. Restore the phrase into a fresh wallet and "
                "confirm the first address matches. Untested backups fail exactly when they are "
                "needed.\n\n"
                "Two advanced options, briefly. A passphrase — sometimes called a 25th word — "
                "creates an entirely separate wallet from the same phrase, so a found backup alone "
                "reveals nothing. It must also be backed up, and forgetting it is unrecoverable. "
                "Splitting a phrase across locations sounds clever and usually is not: naive "
                "splitting weakens it, and proper schemes are easy to get wrong. Prefer multisig "
                "if you need that level of protection."
            ),
        ),
        LessonSpec(
            title="Sending safely: addresses, networks and test transactions",
            minutes=8,
            body=(
                "Transfers are final. There is no reversal, no support line, and no mechanism that "
                "can help — which means the checking has to happen before you press send.\n\n"
                "Always copy and paste addresses; never retype them. Then verify. Malware that "
                "swaps a copied address for the attacker's is common and effective precisely "
                "because addresses look like noise. Check the first and last several characters "
                "against the source, and if you are using a hardware wallet, check them on the "
                "device's own screen — that is the only display an attacker cannot alter.\n\n"
                "Match the network exactly. The same asset exists on many chains, and an address "
                "can be valid on several. Sending on a network the recipient does not support "
                "usually means the funds are stranded; sometimes an exchange can recover them for "
                "a fee, often they cannot. Read the network name on the deposit page rather than "
                "assuming.\n\n"
                "Send a test transaction whenever the destination is new. A few dollars, confirmed "
                "arrived, then the rest. The cost is trivial and it has saved an enormous number "
                "of people.\n\n"
                "Understand fees before you are in a hurry. Network fees vary with congestion; "
                "underpaying can leave a transaction pending for a long time. Some networks let "
                "you replace a stuck transaction with a higher-fee version. Keep a small balance "
                "of the native coin on every network you use — without it you cannot move "
                "anything, including to safety.\n\n"
                "Finally, save destinations you use repeatedly in your wallet's address book and "
                "in your exchange's allowlist. Recognising a saved label is far more reliable than "
                "re-verifying a random string every time, and it removes the moment of "
                "inattention that most losses depend on."
            ),
        ),
        LessonSpec(
            title="Approvals, signatures and drainer attacks",
            minutes=9,
            body=(
                "Using decentralised applications means signing things, and signatures are where "
                "self-custodied funds are most often lost — not through broken cryptography, but "
                "through people approving exactly what the attacker asked for.\n\n"
                "There are two categories. A transaction changes state on-chain and costs gas — "
                "sending funds, swapping, approving a token. A message signature costs nothing and "
                "produces a signed statement; some are harmless logins, and some grant sweeping "
                "permissions off-chain that a contract can act on later. The dangerous ones look "
                "identical to the harmless ones in a careless interface.\n\n"
                "Token approvals are the mechanism that makes decentralised exchanges work: you "
                "permit a contract to move a token on your behalf. Interfaces frequently request "
                "an unlimited allowance for convenience. That permission persists indefinitely, so "
                "a contract compromised a year from now can still drain the token today's "
                "approval covered. Approve the amount you need where the interface allows it, and "
                "periodically review and revoke approvals you no longer use.\n\n"
                "Drainer sites are the industrial version of this. A fake airdrop, mint or "
                "'wallet validation' page asks you to connect and sign. The request may be a batch "
                "approval covering every valuable token you hold. The defences are practical:\n\n"
                "- Read what the wallet is telling you. Modern wallets simulate transactions and "
                "show expected balance changes. If it says an unknown address gains your tokens, "
                "stop.\n"
                "- Reject anything you do not understand. There is no cost to declining and no "
                "opportunity that requires an instant signature.\n"
                "- Use a separate 'burner' wallet for experimenting, holding only what you can "
                "afford to lose, and never connect the wallet holding your long-term positions to "
                "an unfamiliar site.\n\n"
                "That last habit alone converts most drainer incidents from a disaster into an "
                "annoyance."
            ),
        ),
        LessonSpec(
            title="Building a storage plan by tier",
            minutes=8,
            body=(
                "Security advice fails when it is uniform, because people abandon procedures that "
                "are inconvenient for everyday amounts. The fix is tiering: match the protection "
                "to the value, so the strict rules only apply where they are worth it.\n\n"
                "Tier one — spending. A hot wallet on your phone with a small, defined balance. "
                "Used for swaps, fees, and experimenting with applications. Treat it as "
                "expendable: if it were drained tomorrow it would be irritating, not damaging.\n\n"
                "Tier two — active. Exchange balances you are actually trading, plus a hot wallet "
                "for positions you expect to move within weeks. Protected by the account hardening "
                "from Module 2 and kept deliberately smaller than your total.\n\n"
                "Tier three — vault. Long-term holdings on a hardware wallet, with a seed phrase "
                "backed up on steel in two locations. This wallet connects to nothing "
                "experimental. Ideally it has never signed anything except plain transfers.\n\n"
                "Decide the split as percentages and write them down. A common shape is a few "
                "percent in tier one, the amount you are genuinely trading in tier two, and "
                "everything else in tier three. Then rebalance on a schedule rather than by "
                "impulse.\n\n"
                "Two refinements worth considering as balances grow. Use separate wallets for "
                "separate purposes rather than one wallet doing everything, so a compromise is "
                "contained. And consider multisig once the vault holds an amount whose loss would "
                "be materially damaging — requiring two of three keys removes the single point of "
                "failure that a lone seed phrase represents.\n\n"
                "Write the plan down as a document, not a memory. Which wallet holds what, where "
                "the backups are, and what to do if a device is lost. You are writing it for "
                "yourself under stress, which is a different and much less capable reader than you "
                "are right now."
            ),
        ),
        LessonSpec(
            title="Inheritance and the plan you hope nobody needs",
            minutes=7,
            body=(
                "Self-custody has a failure mode people avoid thinking about: if something happens "
                "to you, assets protected by a secret only you know are gone. Not tied up in "
                "probate — gone. A meaningful amount of crypto has already been lost this way, and "
                "the fix is straightforward if you do it deliberately.\n\n"
                "The problem to solve is genuinely awkward: your heirs need access eventually, but "
                "not now, and the instructions must survive years of you not thinking about "
                "them.\n\n"
                "A workable approach has three parts.\n\n"
                "First, an inventory. A document listing what exists and where — which exchanges, "
                "which wallets, which devices, and roughly what is held. It contains no secrets, "
                "so it can live with your other important papers. Without it, heirs do not know "
                "what to look for, and unfound assets are indistinguishable from assets that never "
                "existed.\n\n"
                "Second, an access mechanism. Options range from a sealed backup with a trusted "
                "party or a solicitor, to a safe deposit box, to a multisig where an heir holds "
                "one key and a professional holds another. Multisig is the most robust because no "
                "single party can act alone and no single loss is fatal.\n\n"
                "Third, instructions written for someone who knows nothing. Assume the reader has "
                "never used a wallet. Explain what the words are, what device to use them with, "
                "and what not to do — specifically, never to type the phrase into a website or "
                "accept help from anyone who contacts them.\n\n"
                "Review it annually, and whenever you change wallets. Also check how your "
                "jurisdiction treats crypto in a will: naming assets without disclosing keys in "
                "the will itself is usually the right structure, since wills can become public "
                "documents."
            ),
        ),
        LessonSpec(
            title="Recovering from a mistake",
            minutes=7,
            body=(
                "Things go wrong. Knowing what is recoverable and what is not — and acting in the "
                "right order — is the difference between an incident and a catastrophe.\n\n"
                "If you believe a seed phrase is exposed, act immediately. Do not investigate "
                "first. Generate a new wallet on a clean device, move everything to it, starting "
                "with the highest-value assets, and accept the fees. An exposed phrase can be "
                "drained by an automated bot within seconds of funds arriving, so partial urgency "
                "is not urgency.\n\n"
                "If you sent to a wrong address: if it belongs to an exchange, contact their "
                "support immediately with the transaction hash — recovery is sometimes possible. "
                "If it is a random address, it is gone. Nobody can help, and anyone offering to is "
                "running a recovery scam.\n\n"
                "If you sent on the wrong network, the funds usually still exist at your address "
                "on that other chain. Adding the network to your wallet and importing the address "
                "often reveals them. If they went to an exchange, ask support — many can recover "
                "common cases for a fee.\n\n"
                "If a transaction is stuck pending, check whether the network is congested and "
                "whether your wallet supports replacing it with a higher fee. Do not send a second "
                "transaction hoping to override the first.\n\n"
                "If you signed a malicious approval, revoke it immediately and move remaining "
                "assets to a fresh wallet. Revoking does not undo a transfer that already "
                "happened, but it stops the next one.\n\n"
                "Two rules for every scenario. Never engage with anyone who contacts you offering "
                "to recover funds — that industry is entirely fraudulent, and the second loss is "
                "usually larger than the first. And write down what happened afterwards while it "
                "is fresh. The incident that teaches you the most is the one you are least "
                "inclined to record."
            ),
        ),
        homework(
            title="Week 3 homework — set up and test your vault",
            minutes=15,
            body=(
                "This is the most important homework in the Foundations phase. Do it before you "
                "hold an amount that would hurt to lose.\n\n"
                "1. Set up a non-custodial wallet.\n\n"
                "If you can, use a hardware wallet bought directly from the manufacturer — never "
                "second-hand, never from a marketplace listing. Generate the seed phrase on the "
                "device. If you are not ready to buy hardware, set up a reputable software wallet "
                "and treat this as tier one only.\n\n"
                "2. Back up the phrase properly.\n\n"
                "Write it on paper or steel, numbered, with the wallet type noted. Make a second "
                "copy and store it in a different physical location. Nothing digital — no photo, "
                "no cloud, no password manager.\n\n"
                "3. Test the restore. Do not skip this.\n\n"
                "Wipe the device (or use a second wallet app) and restore from your written "
                "backup. Confirm the first receiving address matches exactly what it was before. "
                "An untested backup is not a backup.\n\n"
                "4. Do a round trip.\n\n"
                "Send a small test amount from your exchange to the wallet. Confirm arrival. Send "
                "it back. Note the fees and the time taken at each step.\n\n"
                "5. Write your storage plan.\n\n"
                "One page: your three tiers, the target percentage in each, where each backup "
                "lives, and what you would do if a device were lost tomorrow. Add an inventory "
                "section listing what exists and where — no secrets in it. Date it, and put a "
                "reminder in your calendar to review it in six months."
            ),
        ),
    ],
)
