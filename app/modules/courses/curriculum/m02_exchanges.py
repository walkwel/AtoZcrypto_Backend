"""Module 2 — Exchanges, Onboarding & Account Security."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="exchanges-and-account-security",
    title="Exchanges, Onboarding & Account Security",
    summary=(
        "Choosing a venue, getting money in and out, understanding what you actually pay, and "
        "hardening your accounts before there is anything worth stealing."
    ),
    level=CourseLevel.BEGINNER,
    phase=CoursePhase.FOUNDATIONS,
    lessons=[
        LessonSpec(
            title="Centralised and decentralised venues",
            minutes=8,
            body=(
                "There are two ways to trade, and they fail in different ways — which is the real "
                "reason to understand both.\n\n"
                "A centralised exchange is a company. You send it money, it credits an internal "
                "balance, and it matches your orders against other customers on its own order "
                "book. Your 'balance' is a database entry — a claim on the company, not an asset "
                "you hold. In exchange you get deep liquidity, fiat on-ramps, customer support, "
                "and an interface that does not require you to understand gas fees.\n\n"
                "A decentralised exchange is a smart contract. You keep custody of your assets and "
                "connect a wallet; the swap executes on-chain against a pool of assets other users "
                "have deposited. Nobody can freeze your funds or lose them in a bankruptcy, and "
                "there is no sign-up. In exchange you pay network fees, you get no support, and "
                "every mistake is final.\n\n"
                "For most people the sensible answer is both, used for different jobs: a "
                "reputable centralised exchange for converting currency and building core "
                "positions, and self-custody for anything held long term. Decentralised venues "
                "matter when you want an asset before it is listed anywhere, or you specifically "
                "want to avoid holding a balance at a company.\n\n"
                "When choosing a centralised venue, weigh these in order:\n\n"
                "- Regulatory standing in your country, and whether you can legally use it.\n"
                "- Whether it supports your local currency directly. Converting through a third "
                "currency costs you twice.\n"
                "- Liquidity in the pairs you actually want. Thin books cost more in slippage than "
                "any headline fee difference.\n"
                "- Security history — not just whether it has been hacked, but whether customers "
                "were made whole.\n"
                "- Withdrawal reliability. An exchange you cannot leave quickly during stress is a "
                "risk regardless of its fees.\n\n"
                "Headline trading fees should be near the bottom of that list. The difference "
                "between 0.1% and 0.2% is trivial next to being unable to withdraw for a week."
            ),
        ),
        LessonSpec(
            title="KYC, verification and what to expect",
            minutes=6,
            body=(
                "Any exchange that touches conventional banking has to identify its customers. "
                "Know Your Customer checks exist because regulated financial institutions are "
                "legally obliged to know who they are transacting with, and exchanges that skip "
                "them lose their banking relationships.\n\n"
                "Expect to supply a government photo ID, a selfie or short video for liveness, "
                "proof of address, and sometimes a declaration of the source of your funds for "
                "larger deposits. Verification usually takes minutes and occasionally days.\n\n"
                "A few practical points that save real trouble:\n\n"
                "- Complete verification before you need it, not on the day you want to withdraw. "
                "Accounts are frequently frozen mid-withdrawal pending checks, and the timing is "
                "never convenient.\n"
                "- Names must match exactly across your ID, your bank account and your exchange "
                "account. Most rejected transfers are a mismatch, not fraud.\n"
                "- Deposit only from an account in your own name. Third-party transfers are the "
                "single most common reason for a frozen balance.\n"
                "- Expect higher limits at higher verification tiers. Complete the tier you will "
                "eventually need.\n\n"
                "It is also worth being clear-eyed about the trade-off. Verification means your "
                "identity is linked to your trading history and, in many jurisdictions, reported "
                "to tax authorities. That is a genuine privacy cost. It is not, however, avoidable "
                "at any venue you would want to hold meaningful money at, and services promising "
                "otherwise carry risks that dwarf the privacy benefit.\n\n"
                "Keep copies of everything you submit and note the date. If an account is ever "
                "restricted, a clean record of what you provided and when is the fastest route "
                "through support."
            ),
        ),
        LessonSpec(
            title="Funding your account: rails, fees and limits",
            minutes=8,
            body=(
                "How you get money onto an exchange affects what you pay, how fast it arrives, and "
                "how easily it can be reversed against you.\n\n"
                "Bank transfer is almost always the cheapest route, often free, and settles within "
                "a day or two depending on your country's payment rails. It is the default for any "
                "amount you care about.\n\n"
                "Card payments are instant and expensive — commonly 2–4%, sometimes more once the "
                "spread is included. Worse, many banks classify them as cash advances, adding "
                "interest from day one. Use them only for small amounts where speed genuinely "
                "matters.\n\n"
                "Stablecoin deposits move value from another venue quickly and cheaply, but you "
                "must match the network exactly. Sending on a network the receiving venue does not "
                "credit is one of the most common ways funds are lost. Always check the deposit "
                "page's network name, and always send a small test first.\n\n"
                "Three things to check before your first deposit:\n\n"
                "- The minimum deposit. Sending less than the minimum can mean the funds are "
                "simply not credited.\n"
                "- The withdrawal limits at your verification tier. Discovering these on the way "
                "out is the wrong time.\n"
                "- Whether deposits are locked for a holding period. Many venues freeze newly "
                "deposited fiat against chargeback fraud, and you may be unable to withdraw for "
                "several days even though you can trade.\n\n"
                "Finally, plan the round trip before you make it. Know how you will get money back "
                "out, what it will cost, and how long it takes. A position you cannot exit into "
                "your own bank account is not really liquid, whatever the order book says."
            ),
        ),
        LessonSpec(
            title="What you actually pay: fees, spread and slippage",
            minutes=8,
            body=(
                "The advertised trading fee is rarely the largest cost of a trade. There are four "
                "components, and beginners routinely optimise the smallest one.\n\n"
                "Trading fees. Exchanges use a maker–taker model. A maker adds liquidity by "
                "placing a limit order that rests on the book; a taker removes liquidity by "
                "executing against an existing order. Makers pay less — sometimes nothing — "
                "because they make the market work. Simply using limit orders instead of market "
                "orders can halve your fee.\n\n"
                "The spread. The gap between the best bid and the best ask. If the best buy price "
                "is 100.00 and the best sell is 100.10, you lose that 0.10 the moment you cross "
                "the spread. On liquid majors this is negligible; on thin altcoins it can exceed "
                "1% per trade.\n\n"
                "Slippage. If your order is larger than the size available at the best price, the "
                "remainder fills at progressively worse prices. A market order in a thin book can "
                "fill several percent away from where you thought you were buying. This is the "
                "cost that surprises people, and it is entirely avoidable with limit orders.\n\n"
                "Withdrawal and network fees. Flat charges per withdrawal, plus the blockchain's "
                "own fee. On some networks this is cents; on others it can be tens of dollars at "
                "busy times. Batching withdrawals rather than making many small ones matters.\n\n"
                "The compounding effect is what to keep in view. A round trip that costs 0.6% in "
                "total is a 0.6% headwind you must overcome before you have made anything. Trade "
                "twenty times and you have given away 12% of your capital to friction. This is "
                "why frequency is a risk parameter, not just a style choice — a point Module 12 "
                "returns to."
            ),
        ),
        LessonSpec(
            title="Hardening your account",
            minutes=9,
            body=(
                "Exchange accounts are attacked constantly, mostly through the account recovery "
                "path rather than the password. Set these up before you deposit anything.\n\n"
                "Use a unique password from a password manager. Reused passwords are the single "
                "largest cause of account takeover, because credentials leaked from an unrelated "
                "site get replayed against every exchange automatically.\n\n"
                "Turn off SMS two-factor authentication and use an authenticator app or, better, a "
                "hardware security key. SIM swapping — where an attacker persuades your mobile "
                "carrier to move your number to their device — is common, targeted, and defeats "
                "SMS codes entirely. A hardware key defeats it and phishing at the same time, "
                "because the key will not authenticate to a lookalike domain.\n\n"
                "Then configure the controls that limit damage even if someone does get in:\n\n"
                "- A withdrawal address allowlist, so funds can only leave to addresses you have "
                "pre-approved.\n"
                "- A time lock on adding new addresses — usually 24 hours. This is the single most "
                "valuable setting on any exchange, because it converts a silent theft into an "
                "alert you have a day to act on.\n"
                "- Withdrawal confirmation by email plus 2FA.\n"
                "- Login and withdrawal notifications, and anti-phishing codes where offered, so "
                "genuine emails from the exchange carry a phrase only you know.\n\n"
                "Two more habits. Secure the email account behind the exchange with equal care — "
                "it is the recovery path for everything, and an attacker who owns your email "
                "usually owns everything else eventually. And back up your 2FA recovery codes "
                "offline, because losing your phone without them means an identity-verification "
                "process measured in weeks."
            ),
        ),
        LessonSpec(
            title="Phishing, impersonation and manufactured urgency",
            minutes=8,
            body=(
                "Most crypto losses are not sophisticated. Someone is persuaded to approve "
                "something themselves, and the persuasion follows a small number of patterns you "
                "can learn to recognise instantly.\n\n"
                "Fake support. You post a problem publicly and a helpful account messages you "
                "within minutes. Real support never initiates contact, never operates by direct "
                "message, and never asks for a seed phrase, a password, a 2FA code, or remote "
                "access to your screen. Anyone who does is stealing from you, without "
                "exception.\n\n"
                "Lookalike domains and search ads. A single changed character, or a paid ad "
                "sitting above the real result. Reach exchanges and wallets through your own "
                "bookmarks only, and be particularly careful on mobile where the address bar "
                "truncates.\n\n"
                "Wallet drainers. A site asks you to connect and sign a message. The signature "
                "grants a contract permission to move your tokens, and the interface describing it "
                "is written by the attacker. Read what you are signing; if a request is opaque, "
                "reject it. Airdrop claims and 'wallet validation' pages are almost always "
                "this.\n\n"
                "Malicious approvals that sit dormant. A token approval you granted months ago can "
                "be used later. Periodically review and revoke approvals you no longer need.\n\n"
                "Manufactured urgency. Limited windows, accounts about to be suspended, "
                "opportunities closing tonight. Urgency exists to prevent you from checking, which "
                "is precisely why it is the reliable tell.\n\n"
                "Adopt one rule that covers nearly all of it: never act inside the channel that "
                "contacted you. Close the message, open your own bookmark, and verify from there. "
                "If the problem is real it will still be there in five minutes; if it evaporates, "
                "it was never real."
            ),
        ),
        LessonSpec(
            title="Exchange risk and what proof of reserves proves",
            minutes=8,
            body=(
                "'Not your keys, not your coins' is a slogan, but it describes a legal reality. An "
                "exchange balance is an unsecured claim on a company. If that company becomes "
                "insolvent, you are a creditor in a bankruptcy, and creditors have historically "
                "waited years and recovered a fraction.\n\n"
                "This has happened repeatedly and at scale: Mt. Gox in 2014, and in 2022 a chain "
                "of failures — Celsius, Voyager, FTX — that took customer assets with them. The "
                "common thread was not exotic technology. It was customer assets being lent, "
                "rehypothecated or simply moved, while the interface kept showing a balance.\n\n"
                "Proof of reserves emerged in response. An exchange publishes a cryptographic "
                "commitment to customer balances and demonstrates control of on-chain addresses "
                "holding at least that much. It is a genuine improvement, and it is important to "
                "understand its limits:\n\n"
                "- It shows assets, not liabilities. An exchange that has borrowed the assets for "
                "the snapshot passes.\n"
                "- It is a point in time, not a continuous guarantee.\n"
                "- It says nothing about off-chain obligations, loans against the assets, or "
                "affiliated entities.\n\n"
                "Treat it as one input, not a safety certificate. The practical protections are "
                "behavioural: keep on exchange only what you are actively trading, move long-term "
                "holdings to self-custody, spread balances across more than one venue, and "
                "withdraw promptly when a venue starts showing stress — delayed withdrawals, "
                "unusual promotions to attract deposits, or executives loudly denying rumours. In "
                "practice the warning signs have always been visible for days before the freeze."
            ),
        ),
        LessonSpec(
            title="How a decentralised swap works",
            minutes=9,
            body=(
                "Decentralised exchanges mostly do not use order books. They use automated market "
                "makers: pools of two assets, with a formula that sets the price from the ratio "
                "between them.\n\n"
                "In the classic design the product of the two balances is held constant. Buying "
                "one asset out of the pool reduces its supply and raises its price along a curve. "
                "This has two consequences worth internalising. First, price impact is a function "
                "of your trade size relative to pool depth — a large trade against a small pool "
                "moves the price against you dramatically. Second, the pool always quotes a price, "
                "even when that price is nonsense, so there is no protection from thin liquidity "
                "except your own slippage setting.\n\n"
                "The mechanics of a swap:\n\n"
                "- Connect a wallet. You are not depositing; the contract only ever moves what you "
                "authorise.\n"
                "- Approve the token. A one-time transaction permitting the contract to move that "
                "token. Approve the amount you need, not an unlimited allowance.\n"
                "- Set slippage tolerance — the worst price you will accept. Too tight and the "
                "transaction fails and you still pay gas; too loose and you invite sandwich "
                "attacks, where a bot buys ahead of you, lets your order push the price up, and "
                "sells into it.\n"
                "- Execute, and pay the network fee in the chain's native coin.\n\n"
                "Two risks are specific to this venue. Anyone can create a pool for any token, "
                "including one named identically to a real asset — always paste the contract "
                "address from an authoritative source rather than searching by ticker. And "
                "liquidity can be withdrawn by whoever provided it, which is the mechanism behind "
                "a 'rug pull': the pool empties and the token becomes unsellable at any price."
            ),
        ),
        LessonSpec(
            title="Your first purchase, done properly",
            minutes=8,
            body=(
                "Make your first trade small enough that the outcome does not matter. Its purpose "
                "is to prove your process works end to end, not to make money.\n\n"
                "Walk the whole path deliberately:\n\n"
                "- Deposit a modest amount by bank transfer and note exactly how long it took to "
                "become tradeable.\n"
                "- Choose a liquid major pair. Look at the order book: note the spread, and note "
                "how much size sits within 0.5% of the mid price. This is what liquidity looks "
                "like, and you will want the comparison when you later look at something thin.\n"
                "- Place a limit order slightly inside the spread rather than a market order. "
                "Watch whether it fills. If it does not, you have learned something real about "
                "the trade-off between price and certainty.\n"
                "- Record the trade: date, asset, quantity, price, fee, and one sentence on why. "
                "That last field will be worth more than the rest combined when you review it in "
                "Module 14.\n"
                "- Withdraw a small amount to a wallet you control, and then back again. Confirm "
                "you can complete the round trip before you rely on it.\n\n"
                "Do not skip the withdrawal step. The most common failure mode is discovering "
                "months later — with a much larger balance and under time pressure — that the "
                "withdrawal path requires verification you never completed.\n\n"
                "One more thing to notice: how you felt. Watching a small position move is the "
                "cheapest possible sample of your own temperament, and it is genuine data for "
                "Module 13. If a trivial amount produces a strong reaction, that is important "
                "information about position sizing, not a character flaw."
            ),
        ),
        homework(
            title="Week 2 homework — harden and document",
            minutes=12,
            body=(
                "This week's work is operational. It takes about half an hour and removes most of "
                "the ways beginners lose money.\n\n"
                "1. Security pass on your exchange account.\n\n"
                "Set a unique password from a password manager. Replace SMS 2FA with an "
                "authenticator app or hardware key. Enable a withdrawal address allowlist and, if "
                "offered, a time lock on new addresses. Turn on login and withdrawal alerts. Store "
                "your 2FA recovery codes offline. Then do the same for the email account behind "
                "it — it is the recovery path for everything.\n\n"
                "2. Cost audit.\n\n"
                "Find your exchange's fee schedule and write down four numbers: maker fee, taker "
                "fee, withdrawal fee for the asset you hold, and the deposit method fee you used. "
                "Then calculate the total cost of one round trip on a $1,000 position. Keep the "
                "number visible — it is the hurdle every trade has to clear.\n\n"
                "3. Liquidity comparison.\n\n"
                "Open the order book for a major pair and for a small-cap pair. For each, write "
                "down the spread as a percentage and roughly how much size sits within 0.5% of "
                "mid. The difference is what 'thin' means in practice.\n\n"
                "4. Start your trade journal.\n\n"
                "Create a spreadsheet with columns: date, asset, side, quantity, price, fee, "
                "reason, and how you felt. Log your test purchase from this module. Every later "
                "module assumes this file exists."
            ),
        ),
    ],
)
