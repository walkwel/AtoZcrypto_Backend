"""Module 10 — On-Chain Analysis & Research Tooling."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="on-chain-analysis",
    title="On-Chain Analysis & Research Tooling",
    summary=(
        "Reading the blockchain itself: exchange flows, holder distribution, cost-basis metrics "
        "and stablecoin liquidity — plus the limits of every one of them."
    ),
    level=CourseLevel.ADVANCED,
    phase=CoursePhase.ANALYSIS,
    lessons=[
        LessonSpec(
            title="What on-chain data is and why it exists",
            minutes=8,
            body=(
                "Crypto is the only asset class where the settlement layer is public. Every "
                "transfer, every balance and every contract interaction is visible to anyone, "
                "permanently. In equities you would need regulatory filings and a delay of weeks "
                "to see a fraction of this; here it is available in real time and free.\n\n"
                "That is genuinely a structural edge, and it is underused because reading it takes "
                "effort. What it lets you observe:\n\n"
                "- Supply distribution: how concentrated ownership is, and how that is changing.\n"
                "- Flows: assets moving to exchanges (often preceding selling) or away from them "
                "(often accumulation into custody).\n"
                "- Holder behaviour: how long coins have been held, and whether long-term holders "
                "are distributing.\n"
                "- Cost basis: what the market as a whole paid, which allows a rough read on "
                "whether holders are in profit or loss.\n"
                "- Protocol activity: users, fees, and whether a chain is actually being used.\n\n"
                "The limits deserve equal weight. On-chain data shows movement, not intent — a "
                "transfer to an exchange may be a sale, a loan, a custody change or an internal "
                "reshuffle. Exchange address labelling is inferred and imperfect. Activity "
                "increasingly happens on Layer 2s and inside exchanges, where it is invisible to "
                "base-layer analysis. And derivatives positioning, which drives much short-term "
                "price action, is largely off-chain.\n\n"
                "Treat on-chain as a slow, structural signal rather than a timing tool. It is "
                "excellent at answering 'what is the state of holder behaviour over months' and "
                "poor at answering 'what happens this week'. Used with that expectation it is one "
                "of the more valuable inputs available; used as a trade trigger it disappoints "
                "consistently."
            ),
        ),
        LessonSpec(
            title="Block explorers and reading a transaction",
            minutes=8,
            body=(
                "A block explorer is a search engine for a blockchain. Learning to use one is the "
                "foundation of every other skill in this module, and it takes about twenty "
                "minutes.\n\n"
                "What you can look up:\n\n"
                "- A transaction hash: sender, recipient, amount, fee, status and the exact "
                "contract calls it made. This is how you verify that a transfer you made actually "
                "arrived, and it is the first thing to check before contacting any support desk.\n"
                "- An address: full balance, complete transaction history, and every token held. "
                "There is no privacy here by default.\n"
                "- A token contract: total supply, holder count, the distribution across the top "
                "holders, and whether the source code is verified.\n\n"
                "Three practical uses that pay for themselves immediately.\n\n"
                "First, verifying a token before you buy it. Anyone can deploy a token with any "
                "name. Always reach the contract address through the project's own documentation "
                "or a reputable aggregator, then confirm on the explorer that the contract matches "
                "and the holder distribution is not absurd.\n\n"
                "Second, checking holder concentration. The explorer's holders tab shows the "
                "largest addresses and their share. If ten addresses hold 70% of supply and are "
                "not identifiable as exchanges or locked contracts, you have found something "
                "important in about thirty seconds.\n\n"
                "Third, reading contract permissions. Verified contracts show their source. You do "
                "not need to be a developer to search for functions like mint, pause or blacklist, "
                "and finding an owner-only mint function on a token you were about to buy is worth "
                "the effort of looking.\n\n"
                "Get comfortable enough that checking an explorer is reflexive rather than an "
                "occasion. Most of the value is in the routine checks, not the deep dives."
            ),
        ),
        LessonSpec(
            title="Exchange flows and balances",
            minutes=9,
            body=(
                "Assets held on exchange addresses are the portion of supply positioned to be "
                "sold quickly. Tracking that aggregate, and the flows into and out of it, is the "
                "most widely used on-chain signal.\n\n"
                "The standard interpretation: sustained outflows from exchanges suggest holders "
                "are moving assets into self-custody, which usually indicates intent to hold. "
                "Sustained inflows suggest positioning to sell. Large single inflows from dormant "
                "addresses have historically preceded selling often enough to be worth "
                "watching.\n\n"
                "Where this reading breaks down, and it does regularly:\n\n"
                "- Exchange address labelling is inferred. Venues rotate addresses and consolidate "
                "internally, producing apparent flows that are purely operational.\n"
                "- The rise of custody solutions and Layer 2s means coins leaving an exchange are "
                "not necessarily going into long-term storage.\n"
                "- Deposits can be collateral for a loan or a derivatives position rather than a "
                "sale, which is a different signal entirely.\n"
                "- Structural changes — a large venue changing custody providers, or a "
                "jurisdiction forcing migration — can produce enormous flows with no market "
                "meaning at all.\n\n"
                "So use it as a trend rather than an event. A multi-month decline in exchange "
                "balances during a price consolidation is a genuinely useful piece of context; a "
                "single day's inflow is noise, and the accounts that post about individual large "
                "transfers are usually generating engagement rather than insight.\n\n"
                "Pair it with stablecoin balances on exchanges, which is the other half of the "
                "picture. Rising stablecoin reserves alongside falling asset reserves suggests "
                "buying power accumulating against shrinking sellable supply — a combination that "
                "has historically been constructive. Neither number alone tells you much."
            ),
        ),
        LessonSpec(
            title="Holder distribution and cohort behaviour",
            minutes=9,
            body=(
                "Who holds an asset, and for how long, is one of the more durable pieces of "
                "information available — and unlike price, it changes slowly enough to be "
                "actionable.\n\n"
                "Concentration is the first read. Group holders by balance size and look at what "
                "share the largest addresses control. High concentration means a small number of "
                "participants can move the price and that your liquidity depends on their "
                "patience. Watch the trend as much as the level: large holders accumulating during "
                "weakness reads very differently from large holders distributing into strength.\n\n"
                "Age of supply is the second and more interesting one. Coins can be grouped by how "
                "long since they last moved. Supply that has not moved in years belongs to holders "
                "who have survived at least one full drawdown, and it behaves very differently "
                "from recently acquired supply. When long-dormant coins begin moving after a large "
                "advance, that is historically a meaningful distribution signal — patient holders "
                "selling to newer, more excitable ones.\n\n"
                "This produces the long-term / short-term holder framework used across on-chain "
                "analysis. Long-term holders tend to accumulate through declines and distribute "
                "into strength. Short-term holders do the opposite, and their cost basis often "
                "acts as a support or resistance level, because that is the price at which recent "
                "buyers break even.\n\n"
                "Cautions. Exchange and custodial addresses hold coins on behalf of many people, "
                "so a single enormous address may represent a million users. Wrapped assets and "
                "bridges distort counts. And a whale who splits holdings across a hundred "
                "addresses looks like a hundred small holders.\n\n"
                "The practical use is regime identification rather than timing: knowing whether "
                "patient or impatient money currently owns the asset tells you a great deal about "
                "how it will behave under stress."
            ),
        ),
        LessonSpec(
            title="Cost-basis metrics: realised cap, MVRV and SOPR",
            minutes=10,
            body=(
                "The most sophisticated on-chain metrics attempt to estimate what the market "
                "actually paid, which allows something close to a valuation read on assets that "
                "have no cash flows.\n\n"
                "Realised capitalisation values every coin at the price when it last moved, rather "
                "than at the current price. It approximates the aggregate cost basis of all "
                "holders — roughly, the capital genuinely committed. It is far more stable than "
                "market cap, and it rises only when coins change hands at higher prices.\n\n"
                "MVRV is market cap divided by realised cap: how far the market price sits above "
                "or below the average holder's cost. High readings mean holders are sitting on "
                "large unrealised gains, which historically correlates with cycle tops because "
                "large paper profits eventually get taken. Readings below one mean the average "
                "holder is underwater — historically, the region where major bottoms have "
                "formed.\n\n"
                "SOPR — spent output profit ratio — measures whether coins moving today are being "
                "sold at a profit or a loss. Above one, holders are realising gains. Below one, "
                "they are realising losses, which happens in capitulation. A useful nuance: in "
                "bull markets, SOPR dipping to one and bouncing indicates holders refusing to sell "
                "at a loss; in bear markets, failing to reclaim one indicates persistent "
                "distribution.\n\n"
                "Three cautions that matter. These metrics were developed on Bitcoin, where the "
                "supply is old, widely distributed and mostly on the base layer; they translate "
                "poorly to newer assets with concentrated supply. Every 'movement' is inferred, so "
                "internal transfers create noise. And every historical threshold is derived from a "
                "small number of cycles — three or four — which is nowhere near enough to "
                "establish a reliable level.\n\n"
                "Use them as regime indicators: are holders broadly in profit or in pain, and is "
                "that changing? That question is answerable and useful. 'MVRV of 3.7 means sell' "
                "is false precision dressed in a chart."
            ),
        ),
        LessonSpec(
            title="Stablecoins and the liquidity backdrop",
            minutes=8,
            body=(
                "Stablecoins are the dollar plumbing of crypto, and their aggregate supply is one "
                "of the cleanest available proxies for how much purchasing power is sitting inside "
                "the system.\n\n"
                "The logic is straightforward. To buy crypto with dollars, that value generally "
                "has to enter as a stablecoin first. Growing aggregate stablecoin supply means "
                "capital is arriving; shrinking supply means it is leaving, as holders redeem back "
                "to bank dollars. Sustained expansion has historically accompanied constructive "
                "conditions, and sustained contraction the opposite.\n\n"
                "Refinements worth tracking:\n\n"
                "- Stablecoin balances held on exchanges, which is buying power positioned to act "
                "rather than sitting idle in DeFi or in wallets.\n"
                "- The ratio of stablecoin supply to total crypto market cap, sometimes called a "
                "dry-powder ratio. High values mean a lot of sidelined capital relative to market "
                "size.\n"
                "- Issuance versus redemption, which shows the direction of net flows more quickly "
                "than the supply level.\n"
                "- Which stablecoins are growing, since it reveals which jurisdictions and venues "
                "capital is arriving through.\n\n"
                "The risks belong here too. Stablecoins are not equivalent to each other. Some are "
                "backed by reserves held at regulated institutions and attested regularly. Some "
                "are backed by crypto collateral, which is reflexive — the collateral falls in "
                "value precisely when redemptions spike. Algorithmic designs with no meaningful "
                "backing have failed catastrophically, most notably in 2022, taking a large "
                "portion of the market down with them.\n\n"
                "For a holder, two practical rules: understand what backs any stablecoin you hold "
                "in size, and remember that a depeg during stress will happen exactly when you "
                "most need the value to be stable."
            ),
        ),
        LessonSpec(
            title="Wallet tracking, labels and their limits",
            minutes=8,
            body=(
                "Because addresses are public, it is possible to follow specific participants — "
                "and an entire industry of 'smart money' dashboards has grown around doing so. It "
                "is genuinely useful and routinely over-interpreted.\n\n"
                "What works. Following addresses associated with entities that have to be public — "
                "protocol treasuries, foundations, exchanges, publicly listed holders — gives you "
                "real information about flows that matter. Watching newly deployed contracts and "
                "unusual accumulation can surface things early. Tracking addresses that "
                "consistently entered before major moves has some value, particularly for "
                "identifying where informed participants are looking.\n\n"
                "What does not. Labels are inferred, not verified — an address tagged as a "
                "particular fund may be a hot wallet, a custodian, or simply wrong. Sophisticated "
                "participants split activity across many addresses precisely because they know "
                "they are watched. Copy-trading a wallet without knowing its overall size, hedges "
                "or holding period means you see one leg of a position and none of the context: "
                "the buy you are copying may be a hedge against a short elsewhere.\n\n"
                "There is also an adversarial dimension worth naming. Once a strategy of following "
                "known wallets becomes popular, it becomes profitable to feed it — buying visibly, "
                "letting followers push the price, then selling into them. Any signal watched by "
                "enough people eventually gets farmed.\n\n"
                "Used well, wallet analysis answers structural questions: is treasury supply "
                "moving, are early investors distributing after an unlock, is a large holder "
                "accumulating over months. Used badly, it is a slower, more confident way to "
                "follow strangers. The difference is whether you are reading flows or copying "
                "trades."
            ),
        ),
        LessonSpec(
            title="Assembling a research dashboard",
            minutes=8,
            body=(
                "The failure mode of on-chain analysis is drowning: hundreds of metrics, all "
                "interesting, none decision-relevant. The fix is deciding in advance which "
                "questions you are asking and tracking only what answers them.\n\n"
                "A workable dashboard covers four questions with one or two metrics each.\n\n"
                "Is capital entering or leaving the system? Aggregate stablecoin supply and its "
                "direction over ninety days.\n\n"
                "Is sellable supply growing or shrinking? Exchange balances for the assets you "
                "hold, again as a multi-month trend.\n\n"
                "Are holders in profit or pain? A cost-basis metric such as MVRV for the major "
                "assets, read as a regime rather than a level.\n\n"
                "Is the thing I own actually used? Fees paid and active addresses for your "
                "specific holdings, compared against their own six-month history and against "
                "competitors.\n\n"
                "Practical construction:\n\n"
                "- Review weekly, not continuously. These metrics move slowly and checking them "
                "daily creates noise-driven decisions.\n"
                "- Always view trends over months, never single readings.\n"
                "- Write one sentence per review recording what you observed. Over a year this "
                "becomes a record of how metrics actually behaved around real moves, which is far "
                "more instructive than any article about them.\n"
                "- Use free tiers first. Most public dashboards cover everything above; paid data "
                "is worth considering only once you know which metrics you actually use.\n\n"
                "Finally, keep the causality straight. On-chain data describes the state of "
                "holders. It does not predict price, and every historically 'reliable' threshold "
                "is drawn from a handful of cycles. It belongs in your process as context that "
                "makes other evidence interpretable — never as a trigger on its own."
            ),
        ),
        homework(
            title="Week 10 homework — read the chain yourself",
            minutes=12,
            body=(
                "1. Explorer practice.\n\n"
                "Find one of your own transactions on a block explorer. Identify the hash, the "
                "fee, the block, and confirm the destination matches what you intended. Then look "
                "up the contract address of a token you hold and check the holders tab: what share "
                "do the top ten addresses control, and can you identify any of them?\n\n"
                "2. Verify a token properly.\n\n"
                "Take any token outside the top fifty. Reach its contract address through the "
                "project's own documentation. On the explorer, check whether the source is "
                "verified and search it for mint, pause or blacklist functions. Write down what "
                "you found.\n\n"
                "3. Build the dashboard.\n\n"
                "Using free tools, assemble views for the four questions in the last lesson. "
                "Bookmark them together. Record today's reading for each in one line.\n\n"
                "4. Historical check.\n\n"
                "Pick one metric — exchange balances or MVRV — and look at how it behaved around "
                "the last major low and the last major high. Write two sentences on whether it "
                "would have been useful in real time, honestly. Include the false signals.\n\n"
                "5. Set the routine.\n\n"
                "Put a weekly fifteen-minute slot in your calendar for this review, with a note "
                "template: four readings, one sentence of interpretation, no trades taken on the "
                "day of the review."
            ),
        ),
    ],
)
